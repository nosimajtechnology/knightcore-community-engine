# Late-Z Battle Cel Adapter v1.2

## Purpose and activation

Adapter ID: `late-z-battle-cel-v1`

Adapter version: `1.2`

Display signifier: `LATE-Z BATTLE CEL`

Use for Knightcore images and cinematics that request Late-Z Battle Cel,
Buu-saga-inspired, mid-1990s DBZ-esque battle anime, or an approved project
image in that treatment. This is a render-and-motion adapter. It replaces the
flagship PS2 build and bloom doctrine while active; do not mix cel animation
with 3D game rendering unless the user explicitly requests a hybrid.

Borrow period visual grammar only. Do not add franchise characters, costumes,
symbols, attacks, locations, logos, or story canon unless the user separately
requests them.

## Reference assignments

- `../../assets/knightcore-anchor-reference.jpeg` remains the immutable
  authority for the faceless great helm, silhouette, adult proportions,
  armor-part arrangement, painted-chainmail placement, restrained complexity,
  and recognizable Anchor Knight construction.
- `../../assets/knightcore-late-z-character-sheet.jpeg` is the bundled Late-Z
  translation reference for the Anchor Knight's cool gray-blue cel palette,
  charcoal cape, helmet treatment, simplified armor planes, orthographic
  appearance, line economy, and equipment design. Its SHA-256 is
  `e914869b79eecbd8504fcf6970526e714754e0c74a58e859adf3548f736553c4`.
- A user-approved project image controls current rendering, wardrobe,
  environment, lighting, pose, and continuity.
- Target-era cel references control line, paint, camera, and motion grammar
  only. They may not import protected character or franchise content.

When image tooling accepts references, assign the original Anchor Knight sheet
to underlying identity and construction, and assign the bundled Late-Z sheet to
the adapter-specific character translation. Assign any approved cel project
image to project continuity. A user-approved project frame remains stronger for
current wardrobe, pose, setting, light, and action state.

## Reference-role firewall

Assign every supplied reference a primary role before generation:

- **IDENTITY:** locked Anchor Knight or an approved project variant
- **STYLE:** bundled Late-Z character sheet, approved project image, or
  target-era cel reference
- **PROJECT:** approved frame or storyboard controlling current continuity
- **MOTION:** clips controlling only timing, cuts, camera rhythm, pose cadence,
  or effects behavior

A mixed-era or off-target motion clip may guide cadence without becoming style
authority. Do not inherit its character designs, armor, anatomy, palette,
effects colors, locations, logos, crop, letterboxing, watermark, captions, or
audio. Reference audio is non-authoritative unless the user assigns it an audio
role.

## Rendering lock

- original 4:3 mid-1990s television-cel presentation
- confident dark ink contours, thicker on the outer silhouette and thinner on
  sparse interior armor marks
- simplified armor planes with two opaque cel values and an occasional third
  highlight; hard-edged shadows and no soft character gradients
- preserve the enclosed faceless great helm, narrow black visor slit, broad
  breastplate, compact pauldrons, block gauntlets, simple greaves, angular feet,
  and dark painted-chainmail regions
- silver armor becomes restrained cool gray-blue or neutral silver paint planes
  with one coherent highlight family; never mirror chrome
- cap detail at the locked Anchor Knight's simplicity; no ornate filigree,
  dense rivets, modeled chainmail rings, or articulated detailed fingers
- hand-painted backgrounds use broad opaque shapes, sparse terrain marks, and
  atmospheric color recession rather than dense digital detail
- very light fine cel-photography grain, restrained broadcast softness, and
  minute color bleed; no obvious aging effect
- in animation, grain remains a stable finishing texture instead of crawling,
  boiling, or redrawing independently

## Camera and composition

Favor tense close-ups, low three-quarter confrontation views, selective dutch
angles, wide aftermath frames, strong asymmetry, foreground terrain, clear
silhouettes, practical pans, short push-ins, snap reframes, and decisive cuts.

Create dynamism through composition contrast: wide establish, tight visor or
gauntlet insert, release, reaction, and aftermath. Do not solve a static
sequence with constant camera movement.

Keep 4:3 unless the user requests another format. Avoid modern shallow depth of
field, glossy lens effects, floating drone movement, or continuous orbiting.

## Temporal rhythm

For animated work:

- use held key poses with limited secondary motion, then brief decisive bursts
- let principal shots breathe; do not assign every storyboard panel equal time
- tag each beat `HOLD`, `BURST`, `INSERT`, or `REVEAL`
- use visibly stepped pose changes and repeated drawings instead of perfectly
  smooth interpolation; effects may update faster than the knight
- give each shot one dominant motion channel: subject, camera, or effects
- during a hold, allow restrained cape/environment motion or one short optical
  push-in, not both aggressively
- favor hard cuts and use a very brief impact cel only when contact or a state
  change needs punctuation
- keep helmet, armor contours, cel-shadow geometry, visor slit, and grain stable;
  no line boil, plate morphing, elastic zoom, or exposed face

## Motion profiles

### POWER_UP_TRANSFORM

Build from discrete states: intact pre-state; held strain pose with escalating
weather, dust, aura, or magic; progressively tighter hard cuts or one restrained
push-in; one brief silhouette/impact insert; hard cut to completed post-state;
held reveal and reaction or aftermath.

Record:

```text
PRE-STATE:
CHANGE ONLY:
POST-STATE:
```

The delta controls only named changes. Preserve helmet closure, anatomy,
proportions, armor construction, equipment count, position, and environment
unless named. Never continuously morph the face area, body, plate geometry, or
weapons between states.

### IMPACT_MELEE

Use a readable chain: launch or approach, one strike, very brief contact insert,
follow-through, opponent reaction, aftermath. Use one attack path per principal
shot. Do not ask for an extended exchange, simultaneous attacks, or prolonged
overlapping limbs and weapons. Keep exactly one body, two arms, two legs, and
the approved weapon count per character.

For 8–15 seconds, prefer four or five principal shots plus no more than two
brief inserts. Written durations guide rhythm rather than guaranteeing
frame-accurate control.

## Exclusions

- no glossy modern digital-anime finish, remaster coloring, airbrushed
  gradients, volumetric light, lens flare, or cinematic depth of field
- no 3D, CGI, PS2 render, photoreal metal, true mirror armor, or modern PBR
- no heavy grain, VHS noise, scanlines, scratches, film burns, chromatic
  aberration, sepia cast, vignette, CRT border, or compression blocks
- no ornate Soulslike redesign, sci-fi power armor, visible face, dense armor
  segmentation, modeled chainmail, franchise traits, logos, subtitles, HUD, or
  watermark by default
- no constant camera motion, equal-duration montage rhythm, smooth
  transformation morph, crawling grain, line boil, or fluid modern interpolation

## Repair checks

- **too clean:** add only very light fine cel-photography grain and restrained
  broadcast softness
- **too painterly:** remove soft blends; restore opaque planes, hard shadows,
  and economical interior lines
- **identity drifts:** restore the locked faceless helm, proportions, armor-part
  arrangement, painted-chainmail placement, and restrained complexity
- **too ornate:** simplify plate divisions, fingers, trim, rivets, and chainmail
  to the Anchor Knight ceiling
- **camera feels stiff:** add shot-scale contrast, one restrained push-in, or a
  decisive cut; never constant orbiting or random handheld movement
- **transformation morphs:** restore locked pre- and post-states and bridge them
  only with effects plus one brief impact insert
- **held drawing crawls:** stabilize armor contours, visor, cel shadows, and
  grain; animate only the declared dominant motion channel
- **melee duplicates anatomy or weapons:** reduce to one readable strike and
  attack path; restore exact limb and equipment counts before adding effects
