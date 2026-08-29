# Bloom and glow doctrine

Read this with rendering grounding. Bloom is a Knightcore material/light rule, not a full-screen retro filter.

## Required behavior

- bright plate edges and silver highlights may clip into soft low-resolution halos
- sword tips, stars, magic sprites, moonlight, windows, torches, and reflective edges may create era-appropriate glints
- use simple additive sprites, low-resolution flare cards, exposure bleed, or star-shaped highlight sprites only where the selected PS2 build supports them
- preserve dark values, faceted armor planes, helmet read, and silhouette
- keep one shared highlight color family per scene

| Scene | Behavior |
| --- | --- |
| Daylight | Cool white/pale cyan plate-edge bloom, sun haze, restrained star glints |
| Dawn/dusk | Warm gold sky bleed with cooler silver reflections |
| Night/starlight | Blue-violet halos and sparse stars while preserving black levels |
| Tavern/interior | Local amber torch/candle halos with cool silver response |
| Magic/gothic | One source-bound accent hue; no rainbow/neon spill |

Reject modern anamorphic flares, mirror armor, cyberpunk rim light, glow around every object, source-less accents, overexposure that erases the knight, chromatic aberration, or analog noise used to conceal modern construction.

## Optional Tape layer

Add composite softness, scanlines, tracking noise, timecode, or REC overlays only when the user requests a Tape/archive/analog treatment. First confirm that the clean base scene already passes PS2 construction and bloom fidelity. The Tape layer cannot rescue or disguise a modern render.

