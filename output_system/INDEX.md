# Output System Index — Prompt Maker v2.0

Full reference for Pillar 4 of the [Core Rules Document](../CORE_RULES.md). Covers every variation level, output structure rule, and production workflow in detail.

---

## Variation Levels

Every generation produces exactly three variations. These are non-negotiable and always ordered Realistic → Stylized → Full Crazy.

| # | Variation | Identity |
|---|-----------|----------|
| 01 | [Realistic](variations/01_realistic.md) | Grounded, photographic, natural — the style pack's most plausible interpretation |
| 02 | [Stylized](variations/02_stylized.md) | Enhanced, expressive, artistic — the style pack at full intentional voice |
| 03 | [Full Crazy](variations/03_full_crazy.md) | Exaggerated, viral, chaotic — maximum energy, subject still identifiable |

---

## Output Structure

Defines how every generation is assembled and presented.

| # | Rule | Identity |
|---|------|----------|
| 01 | [Three Windows](structure/01_three_windows.md) | Every generation produces exactly three self-contained prompt blocks |
| 02 | [Copy-Ready Text](structure/02_copy_ready_text.md) | Every window is paste-and-go — no placeholders, no editing required |
| 03 | [No Commentary](structure/03_no_commentary.md) | Output is prompts only — no preamble, explanation, or suggestions |
| 04 | [No Drift](structure/04_no_drift.md) | Style, variation level, and format stay consistent across every session |

---

## Workflows

Production paths for using Prompt Maker output in the real world.

| # | Workflow | Identity |
|---|----------|----------|
| 01 | [PDF Workflow](workflow/01_pdf_workflow.md) | Write in Markdown → export to PDF → use on phone |
| 02 | [Consistent Formatting](workflow/02_consistent_formatting.md) | The exact window format spec — headers, separators, ordering |

---

## The Three-Window Format (Quick Reference)

```
---
REALISTIC — [Style Pack Name]
Subject: [Subject]

[Prompt text]
---

---
STYLIZED — [Style Pack Name]
Subject: [Subject]

[Prompt text]
---

---
FULL CRAZY — [Style Pack Name]
Subject: [Subject]

[Prompt text]
---
```

---

## Output Rule (from Core Rules)

Every generation must satisfy ALL of the following:

1. **Three windows** — Realistic, Stylized, Full Crazy. Always all three.
2. **Copy-ready** — every window is immediately usable with no editing.
3. **No commentary** — output is prompts only. Nothing else.
4. **No drift** — style, format, and variation behavior are stable across sessions.
5. **Consistent formatting** — window structure, headers, and ordering never vary.

---

## How to Read an Output

1. Identify the **variation level** from the window header
2. Identify the **style pack** from the window header
3. Find the **subject line** to confirm the prompt matches your input
4. **Select and copy** the prompt body
5. **Paste** into your AI image generation tool
6. Generate

That's it. No interpretation required.
