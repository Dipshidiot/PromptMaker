# WORKFLOW: Consistent Formatting

## Identity
Consistent formatting means every output looks the same. Same window structure, same ordering, same headers, same separator style. Formatting is not a stylistic choice — it is a production requirement. Consistent formatting makes outputs scannable, copy-able, and predictable across every session.

## The Formatting Spec

### Window Separators
Each window is bounded by triple dashes:
```
---
[window content]
---
```

### Window Header Format
```
[VARIATION LEVEL IN CAPS] — [Style Pack Name in Title Case]
Subject: [Subject line]
```

### Full Three-Window Block
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

### Text Mode Addition (Image + Text)
When Image + Text mode is active, append to each window header:
```
Text: [Caption text] | [Style] | [Texture] | [Placement]
```

Full example:
```
---
REALISTIC — Meme Lord
Subject: Tired office worker at a desk
Text: "WHEN IT'S ONLY TUESDAY" | Bold Meme Block | Clean | Split

[Prompt text with text instructions embedded]
---
```

## Formatting Rules

| Rule | Requirement |
|------|-------------|
| **Ordering** | Always Realistic → Stylized → Full Crazy |
| **Separators** | Triple dashes (`---`) before and after each window |
| **Header caps** | Variation level is ALWAYS ALL CAPS |
| **Style pack name** | Always Title Case |
| **Subject line** | Always present, always matches user input verbatim |
| **Blank line** | One blank line between header block and prompt body |
| **No trailing text** | Nothing after the final `---` |

## Why Formatting Consistency Matters

On a phone, users scroll through PDFs and select text by tapping. Consistent formatting creates predictable tap targets — the prompt always starts in the same position relative to the header. If formatting varies, selection becomes unreliable.

In an AI tool, consistent formatting means prompts can be scanned visually in under two seconds. The user does not need to read to find the prompt — they see the structure and know where to look.

## Formatting Drift Prevention
See [No Drift](../structure/04_no_drift.md) — formatting drift is a specific category of drift and is explicitly prohibited. The formatting spec above is fixed. It does not change across sessions, style packs, or user moods.
