# Architecture

## Single source of behavior

`skill/knightcore-community-engine/SKILL.md` is the only behavioral manifest. The root `SKILL.md` is a compatibility pointer and is excluded from the install ZIP.

The canonical Skill routes to focused references only when needed:

- identity and construction: `canon.md`
- original-PS2 inspection and quality gate: `rendering-grounding.md`
- source-bound highlight behavior: `bloom-and-glow.md`
- routing and approval stages: `modes.md`
- project state and narrow repair: `continuity.md`
- premise/community grammar: `community-tone.md` and `transformations.md`
- animation output: `model-adapters.md`
- lore, rights, attribution, and finance: `community-boundaries.md`

The exact locked JPEG lives inside the installable package. The build refuses a changed byte.

## Release shape

The release ZIP contains exactly:

```text
knightcore-community-engine/
  SKILL.md
  agents/openai.yaml
  assets/knightcore-anchor-reference.jpeg
  references/*.md
```

Repository docs, examples, tests, scripts, the compatibility pointer, and third-party reference screenshots are not included in the install ZIP.

## Validation

`scripts/build_release.py --check` validates repository invariants without writing artifacts. Running without `--check` performs the same validation, builds the archive twice with fixed metadata, confirms byte-identical output, checks ZIP integrity/topology, and writes `dist/SHA256SUMS`.

`scripts/validate_acceptance.py` verifies that all 17 acceptance cases are represented and that construction/bloom/community/packaging controls are discoverable in the canonical sources.

