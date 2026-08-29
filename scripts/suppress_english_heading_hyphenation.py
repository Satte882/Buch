from __future__ import annotations

import argparse
from pathlib import Path

from docx import Document
from docx.oxml import OxmlElement
from docx.oxml.ns import qn


def suppress_auto_hyphenation(paragraph) -> None:
    ppr = paragraph._p.get_or_add_pPr()
    node = ppr.find(qn("w:suppressAutoHyphens"))
    if node is None:
        node = OxmlElement("w:suppressAutoHyphens")
        ppr.append(node)
    node.set(qn("w:val"), "true")


def apply(path: Path) -> None:
    doc = Document(path)
    story_started = False
    protected = 0

    for paragraph in doc.paragraphs:
        style_name = paragraph.style.name if paragraph.style is not None else ""
        text = paragraph.text.strip()

        # Front matter and the materialized TOC should never be auto-hyphenated.
        if not story_started:
            suppress_auto_hyphenation(paragraph)
            protected += 1

        if style_name == "Heading 1":
            story_started = True
            suppress_auto_hyphenation(paragraph)
            protected += 1

    if protected < 50:
        raise SystemExit(f"Unexpectedly few paragraphs protected from auto-hyphenation: {protected}")

    doc.save(path)
    print(f"Suppressed automatic hyphenation in front matter/TOC and chapter headings: {protected} paragraphs")


def main() -> None:
    parser = argparse.ArgumentParser(description="Prevent automatic hyphenation in English KDP front matter, TOC, and chapter headings.")
    parser.add_argument("document", type=Path)
    args = parser.parse_args()
    if not args.document.exists():
        raise SystemExit(f"File not found: {args.document}")
    apply(args.document)


if __name__ == "__main__":
    main()
