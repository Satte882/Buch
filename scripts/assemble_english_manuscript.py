from __future__ import annotations

import argparse
import re
from pathlib import Path

CHAPTER_HEADING_RE = re.compile(r"^#{1,2}\s+(\d+)\s*$", re.M)
STORY_HEADING_RE = re.compile(r"^##\s+(Prologue|\d+)\s*$", re.M)
EXPECTED = ["Prologue"] + [str(i) for i in range(1, 48)]
EXPECTED_ENDING = '"How strong is your counterhypothesis?"'


def read_chapter(path: Path, number: int) -> str:
    text = path.read_text(encoding="utf-8").strip()
    match = CHAPTER_HEADING_RE.search(text)
    if not match or int(match.group(1)) != number:
        raise SystemExit(f"Unexpected chapter heading in {path}: expected {number}")
    body = text[match.end():].strip()
    if not body:
        raise SystemExit(f"Empty chapter body: {path}")
    return f"## {number}\n\n{body}"


def assemble(source_dir: Path) -> str:
    prologue_path = source_dir / "00_PROLOGUE.md"
    prologue = prologue_path.read_text(encoding="utf-8").strip()
    marker = "## Prologue"
    idx = prologue.find(marker)
    if idx < 0:
        raise SystemExit(f"Missing '{marker}' in {prologue_path}")

    front_matter = prologue[:idx].rstrip()
    prologue_story = prologue[idx:].strip()
    if not front_matter.startswith("# NORMALFALL"):
        raise SystemExit("Unexpected English front matter title; update assembler intentionally if title source changes")

    parts = [front_matter, prologue_story]
    for number in range(1, 48):
        parts.append(read_chapter(source_dir / f"{number:02d}.md", number))

    text = "\n\n".join(parts).rstrip() + "\n"
    headings = STORY_HEADING_RE.findall(text)
    if headings != EXPECTED:
        raise SystemExit(f"Story heading mismatch: expected {EXPECTED}, got {headings}")
    if not text.rstrip().endswith(EXPECTED_ENDING):
        raise SystemExit("English manuscript ending does not match the approved chapter-47 ending")
    return text


def main() -> None:
    parser = argparse.ArgumentParser(description="Assemble the approved English chapter files into one generated master manuscript.")
    parser.add_argument("source_dir", nargs="?", type=Path, default=Path("ENGLISH/manuscript"))
    parser.add_argument("output", nargs="?", type=Path, default=Path("ENGLISH/NORMALFALL_ENGLISH.md"))
    args = parser.parse_args()

    text = assemble(args.source_dir)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(text, encoding="utf-8")
    print(f"Assembled {args.output}: {len(text):,} characters, 48 story units")


if __name__ == "__main__":
    main()
