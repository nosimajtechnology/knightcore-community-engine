# Style Adapter Router

Use a style adapter only when the user selects it, names an alias, supplies an
approved style-specific project image, or clearly requests its visual target.
Otherwise retain the flagship PS2 build.

## Registered adapters

| Adapter | Aliases and cues | Reference |
| --- | --- | --- |
| `late-z-battle-cel-v1` | Late-Z Battle Cel, Buu-saga-inspired, mid-1990s DBZ-esque battle anime | [late-z-battle-cel.md](style-adapters/late-z-battle-cel.md) |

## Style selection menu

Present style choices only after the user selects a mode or the Engine infers
one from the idea. List `FLAGSHIP PS2 (DEFAULT)` first, then every registered
adapter using its display signifier and one short plain-language description.

`FLAGSHIP PS2` routes to [rendering-grounding.md](rendering-grounding.md) and
[bloom-and-glow.md](bloom-and-glow.md). It remains the default when the user
says `default`, `PS2`, `flagship`, or simply asks to continue after seeing the
chooser. A named adapter routes to its registered reference. Skip the menu when
the user already chose a registered style or supplied an approved
style-specific project image.

## Selection rules

When an adapter is selected:

1. record its exact ID and version in project state
2. read only that adapter reference
3. keep the bundled Anchor Knight reference as archetype, silhouette, armor
   arrangement, and complexity authority
4. let the adapter replace the flagship PS2 rendering and bloom layers unless
   the user explicitly requests a hybrid
5. preserve the adapter through Genesis Frame, storyboard, animation brief,
   model packaging, and repair
6. after a project frame is approved, use it as the strongest project-specific
   visual authority while retaining the adapter and Anchor Knight locks
7. assign supplied videos or mixed-era references a declared role before use;
   a motion reference must not override identity, rendering, palette, or audio

Style adapters control rendering, palette behavior, camera grammar, motion
grammar, and style-local surface treatment. Archetype identity remains under
`canon.md`. Platform syntax remains under `model-adapters.md`.

## Visible title signifier

After style selection, append the selected style signifier to every
creator-facing stage title. Use `FLAGSHIP PS2` for the default build or the
adapter's display signifier for a registered adapter.

Use:

```text
KNIGHTCORE COMMUNITY ENGINE · [STYLE SIGNIFIER]
GENESIS FRAME · [STYLE SIGNIFIER]
STORYBOARD · [STYLE SIGNIFIER]
ANIMATION PROMPT · [STYLE SIGNIFIER]
REPAIR · [STYLE SIGNIFIER]
```

Do not place a motion profile in the title; retain it in the project lock.
