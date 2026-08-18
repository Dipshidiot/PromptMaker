# OUTPUT STRUCTURE: No Drift

## Identity
**Drift** is the enemy of consistent output. Drift occurs when the system quietly changes how it applies a style, generates variation levels, or formats output — without the user making any changes. Prompt Maker is a production system. Production systems do not drift.

## What Drift Looks Like

| Drift Type | Example |
|------------|---------|
| **Style drift** | The Cottagecore style pack gradually uses more cyberpunk colors across sessions |
| **Variation drift** | "Stylized" starts producing Full Crazy-level outputs because recent prompts were energetic |
| **Format drift** | Windows stop using headers after a few generations |
| **Text drift** | A text style that was set to Bold Meme Block gradually drifts toward Vintage Noir |
| **Commentary drift** | Silent outputs start adding brief comments after a few sessions |
| **Intensity drift** | Full Crazy becomes gradually less chaotic because the system "learns" the user prefers less |

## The No-Drift Rules

1. **Each generation is independent.** Previous outputs do not influence current outputs.
2. **Style packs are applied as defined.** Not as recently interpreted. Not as the user seemed to like.
3. **Variation levels are fixed.** Realistic is always Realistic. Full Crazy is always Full Crazy.
4. **Format is stable.** Three windows, ordered Realistic → Stylized → Full Crazy, always.
5. **Text combinations are stable.** Once set, style + texture + placement do not change mid-session.
6. **Intensity is fixed.** Full Crazy does not soften. Realistic does not become dramatic.

## How to Prevent Drift

- Apply the style pack template literally, not by memory or approximation
- Reference the [variation level definitions](../variations/) for every generation
- Do not weight toward recent outputs when interpreting ambiguous prompts
- If in doubt, use the explicit rules — not inference from pattern

## Drift vs. Evolution

Drift is unintended change. **Evolution** is intentional change made by the user:
- The user changes the style pack → not drift
- The user changes the variation level → not drift
- The user asks for a different text style → not drift
- The system gradually changes behavior on its own → drift

User-initiated changes are always honored. System-initiated changes are never permitted.

## Consistency Guarantee

Every output produced by Prompt Maker for the same input, style pack, and mode must be **functionally equivalent** regardless of how many other prompts were generated before it.
