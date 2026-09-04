#!/usr/bin/env python3
"""Validate and deterministically build the Knightcore Community Engine Skill."""

from __future__ import annotations

import argparse
import hashlib
import io
import re
import sys
import zipfile
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parent.parent
SKILL_NAME = "knightcore-community-engine"
VERSION = "1.2.1"
SKILL_DIR = ROOT / "skill" / SKILL_NAME
CANONICAL_MANIFEST = SKILL_DIR / "SKILL.md"
ROOT_ENTRYPOINT = ROOT / "SKILL.md"
ASSET = SKILL_DIR / "assets" / "knightcore-anchor-reference.jpeg"
ASSET_SHA256 = "321195c5886547227c5d2618bdcb6da8409f82157d49f908dd270a908938a3db"
DIST = ROOT / "dist"
ZIP_NAME = f"{SKILL_NAME}.zip"
FIXED_TIME = (2026, 1, 1, 0, 0, 0)
MAX_FILES = 500
MAX_FILE_BYTES = 25 * 1024 * 1024
MAX_TOTAL_BYTES = 25 * 1024 * 1024
MAX_ZIP_BYTES = 50 * 1024 * 1024
MAX_ROOT_ENTRYPOINT_BYTES = 2 * 1024
MARKDOWN_LINK = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")

REQUIRED_REPOSITORY_FILES = (
    "README.md",
    "SKILL.md",
    "LICENSE",
    "CHANGELOG.md",
    ".github/workflows/validate.yml",
    ".github/workflows/release.yml",
    "community/quickstart/quickstart.md",
    "community/remix-templates/starter-templates.md",
    "community/guidelines/community-guide.md",
    "examples/still.md",
    "examples/meme.md",
    "examples/scene.md",
    "examples/tape.md",
    "examples/commercial.md",
    "examples/episode.md",
    "docs/architecture.md",
    "docs/canon-policy.md",
    "docs/contribution-guide.md",
    "docs/acceptance-matrix.md",
    "scripts/build_release.py",
    "scripts/validate_acceptance.py",
)

REQUIRED_PACKAGE_FILES = (
    "SKILL.md",
    "agents/openai.yaml",
    "assets/knightcore-anchor-reference.jpeg",
    "references/canon.md",
    "references/community-tone.md",
    "references/transformations.md",
    "references/rendering-grounding.md",
    "references/bloom-and-glow.md",
    "references/modes.md",
    "references/continuity.md",
    "references/model-adapters.md",
    "references/community-boundaries.md",
)


def fail(message: str) -> None:
    print(f"FAIL {message}", file=sys.stderr)
    raise SystemExit(1)


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def parse_frontmatter(text: str) -> dict[str, str]:
    match = re.match(r"^---\n(.*?)\n---(?:\n|$)", text, re.DOTALL)
    if not match:
        fail("canonical SKILL.md has no valid YAML front matter")
    fields: dict[str, str] = {}
    for raw_line in match.group(1).splitlines():
        if not raw_line.strip() or raw_line.lstrip().startswith("#"):
            continue
        if ":" not in raw_line:
            fail(f"malformed front matter line: {raw_line!r}")
        key, value = raw_line.split(":", 1)
        fields[key.strip()] = value.strip().strip('"\'')
    return fields


def validate_markdown_links(markdown: Path, allowed_root: Path) -> None:
    for raw_target in MARKDOWN_LINK.findall(markdown.read_text(encoding="utf-8")):
        target = raw_target.strip()
        if target.startswith("<") and target.endswith(">"):
            target = target[1:-1]
        parsed = urlsplit(target)
        if parsed.scheme or target.startswith("#"):
            continue
        path_part = unquote(parsed.path)
        if not path_part:
            continue
        resolved = (markdown.parent / path_part).resolve()
        try:
            resolved.relative_to(allowed_root.resolve())
        except ValueError:
            fail(f"{markdown.relative_to(ROOT)} links outside allowed root: {raw_target!r}")
        if not resolved.exists():
            fail(f"{markdown.relative_to(ROOT)} links to missing file {raw_target!r}")


def validate_repository() -> None:
    missing = [path for path in REQUIRED_REPOSITORY_FILES if not (ROOT / path).is_file()]
    if missing:
        fail(f"missing repository files: {missing}")

    if ROOT_ENTRYPOINT.stat().st_size > MAX_ROOT_ENTRYPOINT_BYTES:
        fail("root SKILL.md is too large to be a compatibility pointer")
    root_text = ROOT_ENTRYPOINT.read_text(encoding="utf-8")
    canonical_link = f"skill/{SKILL_NAME}/SKILL.md"
    if canonical_link not in root_text or "compatibility" not in root_text.casefold():
        fail("root SKILL.md must delegate to the canonical nested manifest")

    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    expected_download = f"releases/latest/download/{ZIP_NAME}"
    if expected_download not in readme:
        fail("README direct release ZIP link is missing or stale")
    for phrase in ("Do not unzip", "default archetype", "not a named mascot", "approved and locked"):
        if phrase.casefold() not in readme.casefold():
            fail(f"README is missing required beginner/canon language: {phrase!r}")

    changelog = (ROOT / "CHANGELOG.md").read_text(encoding="utf-8")
    if f"## {VERSION}" not in changelog:
        fail(f"CHANGELOG does not contain version {VERSION}")

    for path in ROOT.rglob("*.md"):
        if ".git" in path.parts or "dist" in path.parts:
            continue
        allowed_root = SKILL_DIR if path.is_relative_to(SKILL_DIR) else ROOT
        validate_markdown_links(path, allowed_root)

    print(f"OK   repository structure and copy, version={VERSION}")


def validate_package() -> list[Path]:
    if not SKILL_DIR.is_dir():
        fail(f"missing {SKILL_DIR.relative_to(ROOT)}")

    missing = [path for path in REQUIRED_PACKAGE_FILES if not (SKILL_DIR / path).is_file()]
    if missing:
        fail(f"missing package files: {missing}")

    files = sorted(
        (path for path in SKILL_DIR.rglob("*") if path.is_file()),
        key=lambda path: path.relative_to(SKILL_DIR).as_posix(),
    )
    if len(files) > MAX_FILES:
        fail(f"{len(files)} package files exceeds guardrail {MAX_FILES}")

    manifests = [path for path in files if path.name.casefold() == "skill.md"]
    if manifests != [CANONICAL_MANIFEST]:
        fail(f"package must contain exactly one top-level SKILL.md, found {manifests}")

    fields = parse_frontmatter(CANONICAL_MANIFEST.read_text(encoding="utf-8"))
    if set(fields) != {"name", "description"}:
        fail("canonical front matter must contain only name and description")
    if fields["name"] != SKILL_NAME or not fields["description"]:
        fail("canonical front matter name/description is invalid")
    if f"v{VERSION}" not in CANONICAL_MANIFEST.read_text(encoding="utf-8"):
        fail("canonical SKILL.md version is not synchronized")

    actual_asset_hash = digest(ASSET)
    if actual_asset_hash != ASSET_SHA256:
        fail(f"locked Anchor Knight SHA-256 changed: {actual_asset_hash}")

    total = 0
    for path in files:
        size = path.stat().st_size
        total += size
        if size > MAX_FILE_BYTES:
            fail(f"{path.relative_to(ROOT)} exceeds {MAX_FILE_BYTES} bytes")
    if total > MAX_TOTAL_BYTES:
        fail(f"{total} package bytes exceeds guardrail {MAX_TOTAL_BYTES}")

    print(f"OK   locked Anchor Knight sha256 {actual_asset_hash}")
    print(f"OK   canonical package: {len(files)} files, {total} bytes")
    return files


def archive_bytes(files: list[Path]) -> bytes:
    buffer = io.BytesIO()
    with zipfile.ZipFile(buffer, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for path in files:
            relative = path.relative_to(SKILL_DIR).as_posix()
            info = zipfile.ZipInfo(f"{SKILL_NAME}/{relative}", date_time=FIXED_TIME)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.create_system = 3
            info.external_attr = 0o644 << 16
            archive.writestr(
                info,
                path.read_bytes(),
                compress_type=zipfile.ZIP_DEFLATED,
                compresslevel=9,
            )
    return buffer.getvalue()


def validate_archive(payload: bytes) -> None:
    if len(payload) > MAX_ZIP_BYTES:
        fail(f"ZIP exceeds {MAX_ZIP_BYTES} bytes")
    with zipfile.ZipFile(io.BytesIO(payload)) as archive:
        names = archive.namelist()
        roots = {name.split("/", 1)[0] for name in names}
        if roots != {SKILL_NAME}:
            fail(f"ZIP must contain exactly one top-level folder, found {sorted(roots)}")
        manifests = [name for name in names if name.casefold().endswith("/skill.md")]
        if manifests != [f"{SKILL_NAME}/SKILL.md"]:
            fail(f"ZIP must contain one canonical manifest, found {manifests}")
        packaged_asset = archive.read(f"{SKILL_NAME}/assets/{ASSET.name}")
        if hashlib.sha256(packaged_asset).hexdigest() != ASSET_SHA256:
            fail("packaged Anchor Knight is not byte-identical")
        corrupt = archive.testzip()
        if corrupt is not None:
            fail(f"ZIP integrity failed at {corrupt}")


def build(files: list[Path]) -> tuple[Path, str]:
    first = archive_bytes(files)
    second = archive_bytes(files)
    if first != second:
        fail("two independent builds are not byte-identical")
    validate_archive(first)

    DIST.mkdir(exist_ok=True)
    output = DIST / ZIP_NAME
    output.write_bytes(first)
    archive_hash = hashlib.sha256(first).hexdigest()
    (DIST / "SHA256SUMS").write_text(
        f"{archive_hash}  {ZIP_NAME}\n", encoding="utf-8", newline="\n"
    )
    print("OK   two independent builds are byte-identical")
    print(f"OK   {output.relative_to(ROOT)} ({len(first)} bytes)")
    print(f"OK   sha256 {archive_hash}")
    return output, archive_hash


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="validate without writing dist")
    args = parser.parse_args()
    validate_repository()
    files = validate_package()
    if not args.check:
        build(files)


if __name__ == "__main__":
    main()
