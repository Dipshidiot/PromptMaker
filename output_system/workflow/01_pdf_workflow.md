# WORKFLOW: PDF Workflow

## Identity
The PDF Workflow is the production path for phone-ready output. Write in Markdown, export to PDF, use on your phone. Simple, fast, durable.

## Steps

### Step 1 — Write Prompt in Markdown

Write your subject and configuration in any Markdown editor. Use the following template:

```markdown
# Prompt Generation Request

**Style Pack:** [Style Pack Name]
**Text:** On by default / say No Text to opt out
**Text Style:** [optional override]
**Text Texture:** [optional override]
**Text Placement:** [optional override]

## Subject
[Your subject here]

## Optional Details
- Setting: [optional]
- Mood: [optional]
- Props: [optional]
```

> Do not specify a variation level. The system always generates all three — Realistic, Stylized, and Full Crazy — from your input. You choose which one to use after seeing them.
>
> Caption wording is generated from the subject and style pack rules unless you explicitly ask for **No Text**.

### Step 2 — Generate Output

Paste the Markdown into your preferred AI tool with the Prompt Maker system loaded. The system produces three copy-ready prompt blocks. No editing required.

### Step 3 — Export to PDF

Export the generated output to PDF from your Markdown editor or browser. Recommended tools:

| Tool | Method |
|------|--------|
| **VS Code** | Markdown PDF extension → Export |
| **Typora** | File → Export → PDF |
| **Obsidian** | Export to PDF via print |
| **Browser** | Open Markdown preview → Print → Save as PDF |
| **Any editor** | Copy output → Paste into Google Docs → Download as PDF |

### Step 4 — Use on Phone

Load the PDF into your phone's Files app, Google Drive, or iCloud. When generating images on your phone:

1. Open the PDF
2. Read all three outputs — Realistic, Stylized, Full Crazy
3. Decide which one you want
4. Long-press to select that prompt text
5. Copy
6. Paste into your AI image generation app

## Format Recommendations for Phone Use

| Setting | Recommendation |
|---------|----------------|
| **Page size** | A4 or Letter (standard) |
| **Font size** | 11–13pt for body text |
| **Line spacing** | 1.4–1.6 for readability |
| **Margins** | Standard (2–2.5cm) |
| **Orientation** | Portrait |

## Keeping Your PDF Library Organized

Use a consistent file naming convention:

```
YYYYMMDD_[StylePack]_[Subject].pdf
```

Examples:
- `20250818_Meme_Lord_Office_Worker.pdf`
- `20250818_Neon_Noir_Rainy_Street.pdf`
- `20250818_Cottagecore_Cat_Garden.pdf`

## Updating Prompts

If you want to modify an existing prompt:
1. Return to the original Markdown source
2. Update the subject, style pack, or configuration
3. Re-generate
4. Export a new PDF
5. Archive the old PDF or overwrite

Never manually edit the generated prompt text in the PDF — return to Markdown and re-generate to maintain consistency.
