#!/usr/bin/env python3
"""Validate the documented Knightcore v1 acceptance dry runs and controls."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MATRIX = ROOT / "docs" / "acceptance-matrix.md"
SKILL = ROOT / "skill" / "knightcore-community-engine" / "SKILL.md"
REFS = ROOT / "skill" / "knightcore-community-engine" / "references"


def fail(message: str) -> None:
    print(f"FAIL {message}", file=sys.stderr)
    raise SystemExit(1)


def require(text: str, terms: tuple[str, ...], label: str) -> None:
    missing = [term for term in terms if term.casefold() not in text.casefold()]
    if missing:
        fail(f"{label} missing controls: {missing}")


def main() -> None:
    matrix = MATRIX.read_text(encoding="utf-8")
    cases = [int(value) for value in re.findall(r"^## (\d+)\. ", matrix, re.MULTILINE)]
    if cases != list(range(1, 18)):
        fail(f"acceptance cases must be numbered 1..17 exactly, found {cases}")
    if matrix.count("**Result: PASS**") != 17:
        fail("all 17 acceptance cases must record PASS")

    skill = SKILL.read_text(encoding="utf-8")
    grounding = (REFS / "rendering-grounding.md").read_text(encoding="utf-8")
    bloom = (REFS / "bloom-and-glow.md").read_text(encoding="utf-8")
    tone = (REFS / "community-tone.md").read_text(encoding="utf-8")
    transformations = (REFS / "transformations.md").read_text(encoding="utf-8")
    modes = (REFS / "modes.md").read_text(encoding="utf-8")
    boundaries = (REFS / "community-boundaries.md").read_text(encoding="utf-8")
    continuity = (REFS / "continuity.md").read_text(encoding="utf-8")

    require(skill, ("Anchor Knight", "at most one question", "generate", "prompt only"), "Skill UX")
    require(
        grounding,
        ("Summoner", "Warriors of Might and Magic", "painted chainmail", "block", "original-platform", "three to five"),
        "grounding",
    )
    require(bloom, ("source-bound", "silhouette", "Tape layer"), "bloom")
    require(
        skill,
        ("luminous medieval dreamcore", "Do not infer dark fantasy", "approved project/reference authority"),
        "dreamcore routing",
    )
    require(
        tone,
        ("Default tonal center", "wonder over dread", "Dark-fantasy spectacle — opt-in", "reroute it to the dreamcore default"),
        "dreamcore tone",
    )
    require(
        grounding,
        ("Default environmental bias", "whimsical travel", "does not grant its grim narrative tone", "Gothic corridor, undead, cursed castle — opt-in"),
        "dreamcore grounding",
    )
    require(
        bloom,
        ("Cosmic gradients are rare accents", "not a full-screen rainbow grade", "modern HDR"),
        "dreamcore bloom",
    )
    require(
        transformations,
        ("ordinary goal or object", "one impossible deviation", "quietly wondrous consequence"),
        "dreamcore transformation",
    )
    require(modes, ("CHARACTER", "STILL", "MEME", "SCENE", "CLASSIC CINEMATIC", "TAPE / BUMPER", "COMMERCIAL", "EPISODE"), "modes")
    require(continuity, ("LOCK:", "CHANGE ONLY:", "DO NOT CHANGE:"), "repair")
    require(boundaries, ("not a trading tool", "financial advice", "unofficial"), "community boundary")

    print("OK   17/17 acceptance dry runs recorded PASS")
    print("OK   UX, dreamcore routing, grounding, bloom, mode, continuity, and boundary controls discovered")


if __name__ == "__main__":
    main()

