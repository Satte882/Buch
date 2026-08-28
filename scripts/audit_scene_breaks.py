from __future__ import annotations

import argparse
import re
from collections import defaultdict
from pathlib import Path

CHAPTER_RE = re.compile(r"^##\s+(Prolog|\d+)\s*$")


def next_meaningful(lines: list[str], start: int) -> str | None:
    for idx in range(start, len(lines)):
        value = lines[idx].strip()
        if value:
            return value
    return None


def audit(path: Path) -> dict[str, int]:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    current: str | None = None
    breaks: dict[str, int] = defaultdict(int)

    for idx, raw in enumerate(lines):
        line = raw.strip()
        match = CHAPTER_RE.match(line)
        if match:
            current = match.group(1)
            continue

        if current is None or line != "---":
            continue

        following = next_meaningful(lines, idx + 1)
        if following and CHAPTER_RE.match(following):
            continue

        breaks[current] += 1

    total = sum(breaks.values())
    print(f"Explicit semantic scene breaks: {total}")
    if total:
        for chapter in ["Prolog"] + [str(i) for i in range(1, 48)]:
            if breaks.get(chapter):
                print(f"  {chapter}: {breaks[chapter]}")
    else:
        print("  none currently encoded inside chapters")

    em_dash_count = text.count("—")
    print(f"Em dashes in source before normalization: {em_dash_count}")
    return dict(breaks)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("source", nargs="?", default="AUSNAHMEZUSTAND_FINAL.md")
    args = parser.parse_args()
    audit(Path(args.source))


if __name__ == "__main__":
    main()
