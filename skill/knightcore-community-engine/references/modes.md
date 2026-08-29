# Modes and approval flow

Choose the smallest mode that satisfies the request. Do not show a menu when the user already supplied an idea.

| Intent | Mode | Flow |
| --- | --- | --- |
| anchor study, armor variant, turnaround, guild member | CHARACTER | grounded study → identity gate → deliver |
| one image, cover, wallpaper, fake screenshot | STILL | grounded image → fidelity/bloom gate → deliver |
| reaction, relatable behavior, caption premise, fast remix | MEME | readable premise → grounded image → optional separate caption |
| one connected event, one take or roughly 3–5 shots | SCENE | Genesis Frame → approval → connected scene/storyboard → optional motion brief |
| full short cinematic | CLASSIC CINEMATIC | Genesis Frame → approval → 5–7-shot storyboard → approval → motion brief |
| 4–10 second ident, model viewer, archive fragment, loop | TAPE / BUMPER | passing clean base → optional Tape layer → approval → loopable motion brief |
| fictional realm product, service, or PSA | COMMERCIAL | product/premise clarity → Genesis Frame → approval → ad progression → motion brief |
| longer progressive story | EPISODE | approve Board 1 → approve Board 2 → approve Board 3 → approve Board 4; Board 5 only if needed |

## Shared flow

```text
IDEA → MODE/PREMISE → ACTIVE PS2 BUILD → SCREENSHOT INSPECTION
→ REFERENCE ROLES → RENDERING/BLOOM CONTRACT → FIRST FRAME
→ ARCHETYPE/FIDELITY/BLOOM GATE → USER APPROVAL → NEXT MODE OUTPUT
```

IMAGE/STILL is first-class. Do not require video, storyboard work, or provider selection for one image.

## Approval behavior

Treat `approved`, `lock it`, `perfect`, and clear equivalents as approval. Do not continue a failed first frame into later stages. Remember a named video model even when the user names it early.

For EPISODE:

1. Board 1 — Hook + Setup
2. Board 2 — Escalation
3. Board 3 — Major Turn
4. Board 4 — Payoff / Resolution
5. Board 5 — optional only when Board 4 cannot contain a coherent payoff

Every board begins from the exact approved final state of the prior board. Never generate all episode boards in advance unless the user explicitly asks.

