# OUTPUT STRUCTURE: Three Windows

## Identity
Every generation produces exactly three outputs — one per variation level. These are called **windows**: discrete, self-contained prompt blocks. Each window is complete on its own — it can be used independently or as part of a set.

## Window Format

Each window has two parts: a **label** (not for copying) and a **prompt block** (copy this).

The label identifies the variation and subject. The prompt block contains only the image prompt — nothing else.

```
[VARIATION LEVEL] — [Style Pack Name]
Subject: [Subject from prompt]

```
[Full prompt text — copy this]
```
```

The label sits above the code block. The code block contains the prompt and nothing else.

### Example

**REALISTIC — Meme Lord**
Subject: Tired office worker at a desk

```
Photograph of an exhausted office worker slumped at a cluttered desk, flat fluorescent overhead lighting, slightly washed-out whites, neutral grey background. Natural tired expression, standard office props. Wide-angle lens slightly below eye level. No color grading.
```

**STYLIZED — Meme Lord**
Subject: Tired office worker at a desk

```
Cartoonishly wide eyes with loading-icon pupils, saturated yellow-white color wash, JPEG grain aesthetic. Desk buried in chaos. Coffee mug overflowing. Monitor shows the spinning wheel of death. Exaggerated tired expression, bold composition. Compression artifacts visible on edges.
```

**FULL CRAZY — Meme Lord**
Subject: Tired office worker at a desk

```
The worker has become the desk. Skull emojis orbit them. Lens flares everywhere. Three overlapping captions: "MONDAY" "STILL MONDAY" "ALWAYS MONDAY." Deep-fried color. The office is on fire but also underwater. The fluorescent lights are screaming. Scale is gone.
```

## Rules

- **Always three windows.** Never fewer. Never more per generation.
- **Windows are ordered:** Realistic → Stylized → Full Crazy. Always.
- **All three are always generated.** The user does not select a variation level as an input — they pick which output to use after seeing all three.
- **Each window is independent.** It must work without the others.
- **Label is not part of the prompt.** Variation level, style pack name, and subject line are display labels only — they sit above the copy block and are never inside it.
- **The copy block contains only the image prompt.** Nothing else — no headers, no subject line, no commentary.
- **Labels are mandatory.** Variation level and style pack name always present above each block.

## Copy-Ready Requirement
See [Copy-Ready Text](02_copy_ready_text.md) — each prompt block must be usable immediately without editing.
