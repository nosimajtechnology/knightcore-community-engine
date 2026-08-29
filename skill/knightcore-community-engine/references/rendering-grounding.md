# Original-PS2 rendering grounding

Read this before every PS2 image, Genesis Frame, storyboard, Tape base frame, commercial, episode board, or fidelity repair.

## Non-negotiable workflow

1. Resolve one primary original-PS2 scene build and at most two secondary titles.
2. Search for and visually inspect three to five authentic original-platform gameplay or real-time in-engine screenshots.
3. Prefer: action/gameplay camera; environment/architecture; armor/material/light; optional creature/NPC/prop; optional user-named game.
4. Reject remasters, remakes, HD collections, later ports, enhanced backward compatibility, emulator texture packs, widescreen hacks, mods, ReShade, box art, promotional renders, pre-rendered cinematics, fan art, and platform-ambiguous captures.
5. Assign every accepted source one narrow role. Never instruct a model to “blend all references.”
6. Derive a rendering contract and keep the Anchor Knight as the geometry/material ceiling.
7. Run the gate before showing the result.

Use identifiable original-PS2 gameplay first; then original in-engine captures, contemporary platform-labeled reviews/manuals, or credible screenshot databases. An extracted asset archive may supplement construction evidence only after confirming it is a low-poly gameplay model, not a cinematic/high-detail variant. Never bundle or redistribute source screenshots or extracted models.

## Default construction hierarchy

1. **Locked Anchor Knight:** silhouette, sparse polygons, armor planes, material simplicity, painted chainmail, block hands, and raw model-rip ceiling.
2. **Summoner (PS2 launch build, 2000):** primitive rooms/exteriors, tiny tiled textures, simple light, crude shadows, sparse early-PS2 scene construction. Example gallery: <https://www.mobygames.com/game/3501/summoner/screenshots/>
3. **Warriors of Might and Magic (PS2, 2001):** early-PS2 humanoid density, angular body segments, simple equipment, repeated enemies, close-range readability. Example gallery: <https://gamesdb.launchbox-app.com/games/images/600-warriors-of-might-and-magic>
4. **Final Fantasy X extracted low-poly PS2 asset archives:** supplementary geometry/texture-allocation evidence only. Example archive: <https://models.spriters-resource.com/playstation_2/finalfantasyx/>
5. **Knights of the Temple: Infernal Crusade (PS2, 2004):** armor-part arrangement and melee-camera staging only.
6. **Shadow of the Colossus (PS2, 2005):** restrained highlight/bloom, haze, scale, and sky exposure only.

Later titles cannot raise polygon count, armor segmentation, material quality, or prop density.

## Scene router

| Need | Primary grounding | Narrow role |
| --- | --- | --- |
| Test room, courtyard, village, neutral reference | *Summoner* | tiled textures, primitive massing, crude shadows, sparse scene |
| Early dark-fantasy character/enemy | *Warriors of Might and Magic* | angular foreground density and repeated NPC assets |
| Sunlit ruins, reflective travel, quiet realm | *Shadow of the Colossus* + *Ico* | bloom, haze, stone, negative space, quiet camera |
| Knight action, fortress, crusade, melee | *Knights of the Temple* | armor arrangement, combat scale, camera only |
| Tavern, guild hall, practical dungeon | *Baldur's Gate: Dark Alliance II* or *Champions of Norrath* | warm light, prop density, reusable NPCs |
| Gothic corridor, undead, cursed castle | *Castlevania: Curse of Darkness* or *Lament of Innocence* | gothic massing, monster silhouettes, cool-dark light |
| Dragon flight, bestiary travel, wide fantasy landscape | *Drakan: The Ancients' Gates* | dragon scale, aerial camera, fog-managed vista |
| Spectral realm/supernatural castle | *Legacy of Kain: Defiance* | gothic silhouette, spectral glow, dramatic camera |
| Grocery, gym, street, airport-like modern collision | *Grand Theft Auto: San Andreas* original PS2 | environment/NPC construction only |

## Role assignment

Keep an internal assignment such as:

```text
ANCHOR KNIGHT — identity and base asset construction
APPROVED PROJECT IMAGE — current project state
KNIGHTCORE SOURCE — tone and iconography only
GAMEPLAY A — camera, subject scale, spacing
GAMEPLAY B — environment massing, density, draw distance
EARLY-PS2 CONSTRUCTION — geometry and texture ceiling
GAMEPLAY C — scene light, shadows, bloom, and effects only
SECONDARY CHARACTER — that character's identity only
USER MOOD REFERENCE — mood/composition only unless reassigned
```

## Baseline contract

- raw 2000–2002 PS2 gameplay/model-rip target; native-looking 4:3, roughly 480i/640×480-era capture
- sparse polygon counts, large planar breaks, chunky helmet/chest/shoulder/arm/hand/leg/foot blocks
- tiny diffuse textures with blur, compression, repetition, mild UV stretch, and visible tiling
- painted chainmail tile; no modeled rings
- simple environment map or baked low-resolution highlight; flat/vertex/Gouraud-like lighting and crude normals
- baked/blob/projected/hard shadow; floor/wall planes and sparse reusable props
- short or fog-managed draw distance; reusable low-variation NPCs/creatures
- sparse alpha smoke, sparks, magic sprites, and visible era aliasing/filtering
- readable third-person or in-engine cinematic framing; no HUD unless requested

Reject PBR, ray tracing, true mirrors, smooth subdivision, dense armor parts, modeled chainmail, detailed fingers, volumetric fog, global illumination, bokeh/DOF, modern cloth/skin, dense particles, micro-scratches, modern concept-art cameras, Unreal-style grading, remaster sharpness, or retro noise concealing modern assets.

## Presentation gate

A single major archetype failure fails. A single modern base-construction upgrade fails. Two other fidelity failures fail. A single major bloom failure fails.

On failure: do not present; lock the correct premise/composition/identity/geography/action; repair one isolated layer automatically; regenerate when broadly modern; rerun the gate. After two failed grounded attempts, report the limitation and ask before a third.

