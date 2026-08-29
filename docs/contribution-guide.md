# Contribution guide

## Before opening a change

- Preserve `skill/knightcore-community-engine/SKILL.md` as the sole behavioral source.
- Keep the root `SKILL.md` a short compatibility pointer.
- Never edit, optimize, crop, or re-encode `knightcore-anchor-reference.jpeg`.
- Put conditional detail in the appropriate reference rather than duplicating it across files.
- Keep creator-facing copy plain, compact, and usable on mobile.
- Do not bundle gameplay screenshots, extracted models, token art, or third-party assets.

## Validate

```bash
python3 scripts/build_release.py --check
python3 scripts/validate_acceptance.py
python3 scripts/build_release.py
sha256sum -c dist/SHA256SUMS
```

Inspect the ZIP and confirm it has one top-level `knightcore-community-engine/` folder and one `SKILL.md`.

## Release boundary

Ordinary pull requests and merges never publish a release. Only an explicitly approved `v*` tag triggers release automation. The first intended release tag is `v1.0.0`.
