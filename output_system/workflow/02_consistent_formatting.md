# WORKFLOW: Consistent Formatting

## Identity
Consistent formatting means every output looks the same. Same window structure, same ordering, same headers, same separator style. Formatting is not a stylistic choice — it is a production requirement. Consistent formatting makes outputs scannable, copy-able, and predictable across every session.

## The Formatting Spec

### Window Structure

Each window has two parts:

**1. Label** — displayed above the copy block. Never copied.
```
[VARIATION LEVEL IN CAPS] — [Style Pack Name in Title Case]
Subject: [Subject line]
```

**2. Prompt block** — the copy target. Contains only the image prompt.
```
[Prompt text only — no headers, no subject line, no labels]
```

### Full Three-Window Block

**REALISTIC — [Style Pack Name]**
Subject: [Subject]

```
[Prompt text]
```

**STYLIZED — [Style Pack Name]**
Subject: [Subject]

```
[Prompt text]
```

**FULL CRAZY — [Style Pack Name]**
Subject: [Subject]

```
[Prompt text]
```

### Default Text Addition
When text has not been opted out, append to the label:
```
Text: [Caption text] | [Style] | [Texture] | [Placement]
```

Full example:

**REALISTIC — Meme Lord**
Subject: Tired office worker at a desk
Text: "WHEN IT'S ONLY TUESDAY" | Bold Meme Block | Clean | Split

```
[Prompt text with text instructions embedded]
```

## Formatting Rules

| Rule | Requirement |
|------|-------------|
| **Ordering** | Always Realistic → Stylized → Full Crazy |
| **Label caps** | Variation level is ALWAYS ALL CAPS |
| **Style pack name** | Always Title Case in label |
| **Subject line** | Always present in label, always matches user input verbatim |
| **Prompt block** | Contains image prompt text only — no headers, no subject, no labels |
| **Nothing in the block but the prompt** | Variation name, style pack, and subject are NEVER inside the copy block |

## Why Formatting Consistency Matters

On a phone, users scroll through PDFs and select text by tapping. Consistent formatting creates predictable tap targets — the prompt always starts in the same position relative to the header. If formatting varies, selection becomes unreliable.

In an AI tool, consistent formatting means prompts can be scanned visually in under two seconds. The user does not need to read to find the prompt — they see the structure and know where to look.

## Formatting Drift Prevention
See [No Drift](../structure/04_no_drift.md) — formatting drift is a specific category of drift and is explicitly prohibited. The formatting spec above is fixed. It does not change across sessions, style packs, or user moods.
