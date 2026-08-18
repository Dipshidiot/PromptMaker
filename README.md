# PromptMaker

A prompt creator for creators.

## Quick Start — Load One File

**[PROMPT_MAKER.md](PROMPT_MAKER.md)** — load this single file into your AI tool. Everything is inside: core rules, all 5 style packs, Chaos Agent. Switch packs at any time mid-conversation by saying the pack name.

## Style Packs (all embedded in PROMPT_MAKER.md)

| Pack | Vibe |
|---|---|
| Meme Lord | Internet chaos, bold, degenerate, funny |
| Neon Noir | Dark, cinematic, glowing edges, rain-soaked |
| Ghibli Soft | Warm, painterly, wonder-soaked, emotional |
| Cyberpunk Chrome | Machine-future, chrome, electric, hard-edged |
| Cosmic Horror | Reality-bending, eldritch, beautiful dread |
| Chaos Agent | All rules suspended. Everything random. |

## For Developers

Source of truth lives in the modular files:

- Core rules: [CORE_RULES.md](CORE_RULES.md)
- Individual pack files: [`style_packs/`](style_packs/)
- Blank template: [STYLE_PACK_TEMPLATE.md](STYLE_PACK_TEMPLATE.md)
- Generator: [`/home/runner/work/PromptMaker/PromptMaker/scripts/build_prompt_maker.py`](/home/runner/work/PromptMaker/PromptMaker/scripts/build_prompt_maker.py)

Regenerate the shipping file with:

```bash
python /home/runner/work/PromptMaker/PromptMaker/scripts/build_prompt_maker.py
```

`PROMPT_MAKER.md` is generated from those source files and should not be hand-edited.
