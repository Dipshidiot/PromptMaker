# Core Rules Document — Prompt Maker v2.0

A stable, universal rule system that governs how every prompt is generated, regardless of style, subject, or text mode.

---

## Pillar 1 — Core Image Structure

Defines the universal physics of the system. These rules never change.

### 1. Subject Rules

- Subject must be clear and concrete.
- Optional setting may be included.
- Optional mood may be included.
- Subject must not contain style instructions.

### 2. Scene Composition Rules

- Foreground subject is always the focus.
- Background environment must support the subject.
- Props may be included if relevant.
- Action or pose must be clearly described.

### 3. Lighting Rules

- Neutral baseline lighting.
- Style packs may override lighting behavior.
- No random lighting drift.

### 4. Color Rules

- Neutral baseline palette.
- Style packs define palette behavior.
- No uncontrolled saturation or hue shifts.

### 5. Variation Levels (Mandatory)

Every prompt must generate three variations:

| Variation | Description |
|-----------|-------------|
| **Realistic** | Grounded, photographic, natural. |
| **Stylized** | Enhanced, expressive, artistic. |
| **Full Crazy** | Exaggerated, viral, chaotic. |

These three levels are required for every output.

---

## Pillar 2 — Text Styling & Placement

Defines how text behaves across all styles.

### Text Styling Options

- Bold Meme Block
- Soft Wholesome
- Chaotic Burst
- Vintage Noir
- Corporate Parody

### Text Texture Options

- Clean
- Grainy
- Neon Glow
- Chalky
- Glossy
- Comic Halftone

### Text Placement Options

- Top
- Center
- Bottom
- Split (top + bottom)
- Floating (style‑dependent)

### Text Rule

If **Image + Text** is selected:

- Text must match style tone.
- Text must fit subject.
- Text must follow placement rules.
- No drift.

→ **Full reference:** [Text System Index](text_system/INDEX.md) — all text styles, textures, placements, and compatibility matrices.

---

## Pillar 3 — Style Pack System

Style packs are modular and define how a style behaves.

### Style Pack Template

```
# STYLE PACK: [Name]

## Core Aesthetic
Describe the visual identity.

## Lighting Behavior
How light behaves in this style.

## Color Behavior
Palette, saturation, contrast.

## Texture Behavior
Smooth, grainy, neon, plush, clay, etc.

## Motion Behavior
Streaks, blur, chaos, stillness.

## Caption Tone
How text should sound.

## Transformation Rules
### Realistic
How realism behaves.

### Stylized
How stylization behaves.

### Full Crazy
How chaos behaves.

## Example Outputs
- Realistic:
- Stylized:
- Full Crazy:
```

→ **Full reference:** [Style Packs Index](style_packs/INDEX.md) — all 15 style packs ready to use.

---

## Pillar 4 — Output Formatting

Defines how final content is structured.

### Output Structure

Each generation produces:

- Three windows:
  - Realistic
  - Stylized
  - Full Crazy
- Copy‑ready text
- No commentary
- No drift
- Consistent formatting

### PDF Workflow

1. Write prompt in Markdown.
2. Export to PDF.
3. Use on phone.

→ **Full reference:** [Output System Index](output_system/INDEX.md) — variation levels, output structure rules, and production workflows.

---

## Purpose of Core Rules

- Ensure consistency.
- Prevent drift.
- Maintain predictable outputs.
- Support unlimited style expansion.
- Keep system modular and stable.

---

## Future Expansion

- Additional style packs.
- Text tone library.
- Favorites system.
- Super Randomizer Mode.
- Advanced caption behaviors.

---

*This Core Rules Document defines the stable foundation of Prompt Maker v2.0 and supports all future style packs, text systems, and output formats.*
