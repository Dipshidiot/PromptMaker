from __future__ import annotations

import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
CORE_RULES = REPO_ROOT / "CORE_RULES.md"
STYLE_PACKS_DIR = REPO_ROOT / "style_packs"
CHAOS_FILE = "00_chaos_agent.md"
OUTPUT = REPO_ROOT / "PROMPT_MAKER.md"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8").strip() + "\n"


def extract_style_pack_name(text: str) -> str:
    match = re.search(r"^# STYLE PACK: (.+)$", text, re.MULTILINE)
    if not match:
        raise ValueError("Missing style pack title")
    return match.group(1).strip()


def trim_example_outputs(text: str) -> str:
    marker = "\n## Example Outputs\n"
    if marker in text:
        text = text.split(marker, 1)[0].rstrip()
    return text


def shift_heading_levels(text: str) -> str:
    def replace(match: re.Match[str]) -> str:
        hashes, title = match.groups()
        return f"{hashes}# {title}"

    return re.sub(r"^(###|##) (.+)$", replace, text, flags=re.MULTILINE)


def build_intro(pack_names: list[str]) -> str:
    packs_display = " · ".join(pack_names + ["Chaos Agent"])
    return "\n".join(
        [
            "# PROMPT MAKER — Complete System",
            "",
            "> Generated from `CORE_RULES.md` and `style_packs/*.md` by `scripts/build_prompt_maker.py`.",
            "",
            "Load this single file into your AI tool. Everything is here. You can switch style packs at any time by saying the pack name.",
            "",
            "## How to Use",
            "",
            "1. Load this file into your AI tool as the system prompt.",
            '2. Say a style pack name + your subject. Example: **"Neon Noir — a soap character in a tree"**',
            "3. Get three copy-ready prompts: Realistic, Stylized, Full Crazy.",
            "4. Copy the one you want. Paste. Generate.",
            "5. Switch packs any time: just say the new pack name.",
            "",
            f"**Available packs:** {packs_display}",
        ]
    )


def build_core_rules() -> str:
    if not CORE_RULES.exists():
        raise FileNotFoundError(CORE_RULES)

    text = read(CORE_RULES)
    lines = text.splitlines()
    start = next((i for i, line in enumerate(lines) if line.startswith("## Pillar 1")), None)
    if start is None:
        raise ValueError(f"Could not find '## Pillar 1' in {CORE_RULES}")
    selected = "\n".join(lines[start:])
    selected = re.sub(
        r"\nTo add a new pack:.*?(?=\n---\n)",
        "\n",
        selected,
        flags=re.DOTALL,
    )
    selected = selected.replace(
        "**Special mode:** [Chaos Agent](style_packs/00_chaos_agent.md) — suspends all rules, randomizes everything.",
        "**Special mode:** Chaos Agent — suspends all rules, randomizes everything.",
    )
    return "\n".join(["# CORE RULES", "", selected.strip()])


def build_pack_section(index: int, path: Path) -> str:
    text = trim_example_outputs(read(path))
    name = extract_style_pack_name(text)
    body = re.sub(r"^# STYLE PACK: .+\n?", "", text, count=1, flags=re.MULTILINE).strip()
    body = shift_heading_levels(body)
    return f"## PACK {index} — {name}\n\n{body}"


def build_chaos_section(path: Path) -> str:
    text = trim_example_outputs(read(path))
    body = re.sub(r"^# STYLE PACK: .+\n?", "", text, count=1, flags=re.MULTILINE).strip()
    return f"# CHAOS AGENT MODE\n\n{body}"


def main() -> None:
    pack_paths = sorted(STYLE_PACKS_DIR.glob("*.md"))
    normal_paths = [path for path in pack_paths if path.name != CHAOS_FILE]
    chaos_path = STYLE_PACKS_DIR / CHAOS_FILE
    if not chaos_path.exists():
        raise FileNotFoundError(chaos_path)

    pack_names = [extract_style_pack_name(read(path)) for path in normal_paths]
    sections = [build_intro(pack_names), build_core_rules(), "# STYLE PACKS"]
    sections.extend(build_pack_section(index, path) for index, path in enumerate(normal_paths, start=1))
    sections.append(build_chaos_section(chaos_path))

    output = "\n\n---\n\n".join(section.strip() for section in sections if section.strip()) + "\n"
    OUTPUT.write_text(output, encoding="utf-8")


if __name__ == "__main__":
    main()
