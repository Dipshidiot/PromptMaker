# Text System Index — Prompt Maker v2.0

Full reference for Pillar 2 of the [Core Rules Document](../CORE_RULES.md). Covers every text styling option, texture option, and placement option with detailed rules and compatibility guidance.

---

## Text Styles

Define the *personality* and *visual character* of the text.

| # | Style | Identity |
|---|-------|----------|
| 01 | [Bold Meme Block](styles/01_bold_meme_block.md) | All-caps Impact, white fill, black outline — the internet's native tongue |
| 02 | [Soft Wholesome](styles/02_soft_wholesome.md) | Rounded, warm, gentle — feels handwritten and kind |
| 03 | [Chaotic Burst](styles/03_chaotic_burst.md) | Mixed fonts, sizes, and angles — zine energy, maximum personality |
| 04 | [Vintage Noir](styles/04_vintage_noir.md) | Condensed serifs, wide tracking, melancholy elegance |
| 05 | [Corporate Parody](styles/05_corporate_parody.md) | Clean sans-serif professional precision applied to absurd subjects |

---

## Text Textures

Define the *surface material* of the text itself.

| # | Texture | Identity |
|---|---------|----------|
| 01 | [Clean](textures/01_clean.md) | Perfectly flat, no noise — pure digital type |
| 02 | [Grainy](textures/02_grainy.md) | Film grain and analog noise — warm, organic, imperfect |
| 03 | [Neon Glow](textures/03_neon_glow.md) | Colored bloom and light emission — the text is a light source |
| 04 | [Chalky](textures/04_chalky.md) | Chalk-on-board texture — soft, dusty, handmade |
| 05 | [Glossy](textures/05_glossy.md) | Lacquered specular finish — polished, premium, confident |
| 06 | [Comic Halftone](textures/06_comic_halftone.md) | Ben-Day dot pattern fill — print culture, graphic, retro |

---

## Text Placements

Define *where* the text lives in the image.

| # | Placement | Identity |
|---|-----------|----------|
| 01 | [Top](placements/01_top.md) | Anchored to upper edge — context, setup, title |
| 02 | [Center](placements/02_center.md) | Optical center — dominant, unavoidable, statement-making |
| 03 | [Bottom](placements/03_bottom.md) | Anchored to lower edge — caption, punchline, closing word |
| 04 | [Split](placements/04_split.md) | Top + Bottom simultaneously — the classic meme format |
| 05 | [Floating](placements/05_floating.md) | Compositionally placed — style-dependent, in-world, discovered |

---

## Compatibility Matrix

### Style × Texture

| | Clean | Grainy | Neon Glow | Chalky | Glossy | Comic Halftone |
|---|:---:|:---:|:---:|:---:|:---:|:---:|
| **Bold Meme Block** | ✅ | ✅ | ⚠️ | ✅ | ✅ | ✅ |
| **Soft Wholesome** | ✅ | ✅ | ❌ | ✅ | ⚠️ | ❌ |
| **Chaotic Burst** | ❌ | ✅ | ✅ | ⚠️ | ❌ | ✅ |
| **Vintage Noir** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Corporate Parody** | ✅ | ❌ | ⚠️ | ❌ | ✅ | ✅ |

> ✅ Recommended &nbsp;&nbsp; ⚠️ Use with intention &nbsp;&nbsp; ❌ Avoid

---

### Style × Placement

| | Top | Center | Bottom | Split | Floating |
|---|:---:|:---:|:---:|:---:|:---:|
| **Bold Meme Block** | ✅ | ⚠️ | ✅ | ✅ | ❌ |
| **Soft Wholesome** | ✅ | ✅ | ✅ | ⚠️ | ✅ |
| **Chaotic Burst** | ⚠️ | ✅ | ⚠️ | ✅ | ✅ |
| **Vintage Noir** | ✅ | ✅ | ✅ | ⚠️ | ✅ |
| **Corporate Parody** | ✅ | ✅ | ✅ | ✅ | ❌ |

---

### Style Pack × Recommended Text Style

| Style Pack | Primary Text Style | Secondary Option |
|------------|--------------------|-----------------|
| Meme Lord | Bold Meme Block | Chaotic Burst |
| Neon Noir | Vintage Noir | — |
| Cottagecore | Soft Wholesome | Vintage Noir |
| Cyberpunk Chrome | Corporate Parody | Chaotic Burst |
| Ghibli Soft | Soft Wholesome | — |
| Retro Vintage | Vintage Noir | Corporate Parody |
| Dark Academia | Vintage Noir | Soft Wholesome |
| Vaporwave Dream | Chaotic Burst | Corporate Parody |
| Toy Box | Soft Wholesome | Chaotic Burst |
| Grunge Street | Chaotic Burst | Bold Meme Block |
| Luxury Brand | Vintage Noir | Corporate Parody |
| Cosmic Horror | Vintage Noir | Chaotic Burst |
| Kawaii Pop | Soft Wholesome | Chaotic Burst |
| Cinematic Epic | Vintage Noir | Corporate Parody |
| Propaganda Parody | Corporate Parody | Bold Meme Block |

---

## Text Rule (from Core Rules)

When **Image + Text** mode is selected, ALL of the following must be true:

1. **Text must match style tone** — use the compatibility matrix.
2. **Text must fit subject** — the caption should be relevant to the image.
3. **Text must follow placement rules** — use the placement docs for margin and legibility rules.
4. **No drift** — once a style/texture/placement combination is chosen, it does not change mid-generation.

---

## How to Build a Text Combination

1. Choose your **Style Pack** (see [Style Packs Index](../style_packs/INDEX.md))
2. Look up the **Recommended Text Style** in the table above
3. Choose a **Texture** compatible with that style (compatibility matrix)
4. Choose a **Placement** appropriate to your caption type
5. Write your caption following the **Caption Tone** guidelines in the style pack
6. Apply across all three variation levels: Realistic → Stylized → Full Crazy
