from __future__ import annotations

import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
CORE_RULES = REPO_ROOT / "CORE_RULES.md"
STYLE_PACKS_DIR = REPO_ROOT / "style_packs"
CHAOS_FILE = "00_chaos_agent.md"
CORE_RULES_START_MARKER = "## Pillar 1"
STRIP_BLOCK_START = "<!-- build:strip-start -->"
STRIP_BLOCK_END = "<!-- build:strip-end -->"
OUTPUT = REPO_ROOT / "PROMPT_MAKER.md"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8").strip() + "\n"


def extract_style_pack_name(text: str) -> str:
    match = re.search(r"^# STYLE PACK: (.+)$", text, re.MULTILINE)
    if not match:
        raise ValueError("Missing style pack title")
    return match.group(1).strip()


def extract_pack_number(path: Path) -> int:
    match = re.match(r"(\d+)_", path.name)
    if not match:
        raise ValueError(f"Missing numeric prefix in {path}")
    return int(match.group(1))


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
    start = next((i for i, line in enumerate(lines) if line.startswith(CORE_RULES_START_MARKER)), None)
    if start is None:
        raise ValueError(f"Could not find {CORE_RULES_START_MARKER!r} in {CORE_RULES}")

    selected = "\n".join(lines[start:])
    selected = re.sub(
        rf"\n?{re.escape(STRIP_BLOCK_START)}.*?{re.escape(STRIP_BLOCK_END)}\n?",
        "\n",
        selected,
        flags=re.DOTALL,
    )
    selected = re.sub(
        r"(\*\*Special mode:\*\* )\[([^\]]+)\]\([^)]+\)",
        r"\1\2",
        selected,
    )
    return "\n".join(["# CORE RULES", "", selected.strip()])


def build_pack_section(pack_number: int, name: str, text: str) -> str:
    body = re.sub(r"^# STYLE PACK: .+\n?", "", text, count=1, flags=re.MULTILINE).strip()
    body = shift_heading_levels(body)
    return f"## PACK {pack_number} — {name}\n\n{body}"


def build_chaos_section(path: Path) -> str:
    text = trim_example_outputs(read(path))
    body = re.sub(r"^# STYLE PACK: .+\n?", "", text, count=1, flags=re.MULTILINE).strip()
    return f"# CHAOS AGENT MODE\n\n{body}"


def main() -> None:
    pack_entries: list[tuple[int, str, str]] = []
    for path in sorted(STYLE_PACKS_DIR.glob("*.md")):
        if path.name == CHAOS_FILE:
            continue
        text = trim_example_outputs(read(path))
        pack_entries.append((extract_pack_number(path), extract_style_pack_name(text), text))

    chaos_path = STYLE_PACKS_DIR / CHAOS_FILE
    if not chaos_path.exists():
        raise FileNotFoundError(chaos_path)

    pack_entries.sort(key=lambda entry: entry[0])
    sections = [build_intro([name for _, name, _ in pack_entries]), build_core_rules(), "# STYLE PACKS"]
    sections.extend(build_pack_section(pack_number, name, text) for pack_number, name, text in pack_entries)
    sections.append(build_chaos_section(chaos_path))

    output = "\n\n---\n\n".join(section.strip() for section in sections if section.strip()) + "\n"
    OUTPUT.write_text(output, encoding="utf-8")


if __name__ == "__main__":
    main()
