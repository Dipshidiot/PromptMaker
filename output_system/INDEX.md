# Output System Index — Prompt Maker v2.0

Full reference for Pillar 4 of the [Core Rules Document](../CORE_RULES.md). Covers every variation level, output structure rule, and production workflow in detail.

---

## Variation Levels

Every generation always produces all three variations. The user does not pick a variation upfront — the system generates all three automatically, and the user selects the one they want after seeing them.

| # | Variation | Identity |
|---|-----------|----------|
| 01 | [Realistic](variations/01_realistic.md) | Camera-first, photographic — the style pack's most grounded interpretation |
| 02 | [Stylized](variations/02_stylized.md) | Artist's interpretation — the style pack at full intentional voice |
| 03 | [Full Crazy](variations/03_full_crazy.md) | Reality broken — physics gone, subject still identifiable, everything else is chaos |

**The user inputs:** style pack + subject → **The system outputs:** all three → **The user picks:** whichever prompt they want to copy.

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

Labels are displayed above each block. The copy block contains the prompt only.

**REALISTIC — [Style Pack Name]**
Subject: [Subject]

```
[Prompt text — copy this]
```

**STYLIZED — [Style Pack Name]**
Subject: [Subject]

```
[Prompt text — copy this]
```

**FULL CRAZY — [Style Pack Name]**
Subject: [Subject]

```
[Prompt text — copy this]
```

---

## Output Rule (from Core Rules)

Every generation must satisfy ALL of the following:

1. **Three windows** — Realistic, Stylized, Full Crazy. Always all three.
2. **450-character limit** — every prompt body is 450 characters or fewer. No exceptions.
3. **Copy-ready** — every window is immediately usable with no editing.
4. **No commentary** — output is prompts only. Nothing else.
5. **No drift** — style, format, and variation behavior are stable across sessions.
6. **Consistent formatting** — window structure, headers, and ordering never vary.
7. **Visible distinction** — Realistic, Stylized, and Full Crazy must be immediately distinguishable from each other. If they could be confused, push harder.

> **Chaos Agent Exception:** When [Chaos Agent mode](../style_packs/00_chaos_agent.md) is active, rules 1 (ordering), 5 (no drift), and 6 (consistent style/variation) are suspended. Three windows are still produced, every window is still copy-ready, and the 450-character limit still applies.

---

## How to Use an Output

1. Read all three prompt blocks — Realistic, Stylized, Full Crazy
2. Decide which energy level matches what you want
3. Tap/select the prompt text in that block
4. Copy
5. Paste into your AI image generation tool
6. Generate
