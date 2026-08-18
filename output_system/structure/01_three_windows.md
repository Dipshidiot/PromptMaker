# OUTPUT STRUCTURE: Three Windows

## Identity
Every generation produces exactly three outputs — one per variation level. These are called **windows**: discrete, self-contained prompt blocks. Each window is complete on its own — it can be used independently or as part of a set.

## Window Format

Each window follows this structure:

```
---
[VARIATION LEVEL] — [Style Pack Name]
Subject: [Subject from prompt]

[Full prompt text]
---
```

### Example

```
---
REALISTIC — Meme Lord
Subject: Tired office worker at a desk

Photograph of an exhausted office worker slumped at a cluttered desk, 
flat fluorescent overhead lighting, slightly washed-out whites, neutral 
grey background. Natural tired expression. Standard office props: coffee 
mug, stacked papers, glowing monitor. Shot as if with a wide-angle lens 
slightly below eye level. No color grading.
---

---
STYLIZED — Meme Lord
Subject: Tired office worker at a desk

Cartoonishly wide eyes with loading-icon pupils, saturated yellow-white 
color wash, slight JPEG grain aesthetic. The desk is buried in chaos. 
Coffee mug overflowing. Monitor shows the spinning wheel of death. 
Exaggerated tired expression, bold composition. Compression artifacts 
visible on edges.
---

---
FULL CRAZY — Meme Lord
Subject: Tired office worker at a desk

Pixelated chaos entity. The worker has become the desk. Surrounded by 
orbiting spinning skull emojis, lens flares, red alert overlays. Three 
overlapping captions at different angles: "MONDAY", "STILL MONDAY", 
"ALWAYS MONDAY". Deep-fried color. Scale meaningless. The fluorescent 
lights are screaming.
---
```

## Rules

- **Always three windows.** Never fewer. Never more per generation.
- **Windows are ordered:** Realistic → Stylized → Full Crazy. Always.
- **Each window is independent.** It must work without the others.
- **No shared text between windows** (except subject reference which is identical).
- **Window headers are mandatory.** Variation level and style pack name always present.

## Copy-Ready Requirement
See [Copy-Ready Text](02_copy_ready_text.md) — each window must be usable immediately without editing.
