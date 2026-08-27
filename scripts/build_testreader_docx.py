from __future__ import annotations

import argparse
import re
from pathlib import Path

from docx import Document
from docx.enum.section import WD_SECTION
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt

CHAPTER_RE = re.compile(r"^##\s+(Prolog|\d+)\s*$")
INLINE_RE = re.compile(r"(\*\*\*.+?\*\*\*|\*\*.+?\*\*|(?<!\*)\*[^*]+?\*(?!\*))")


def set_run_font(run, name: str = "Times New Roman", size: float = 12.0) -> None:
    run.font.name = name
    run.font.size = Pt(size)
    rpr = run._element.get_or_add_rPr()
    rfonts = rpr.rFonts
    if rfonts is None:
        rfonts = OxmlElement("w:rFonts")
        rpr.insert(0, rfonts)
    for attr in ("ascii", "hAnsi", "eastAsia", "cs"):
        rfonts.set(qn(f"w:{attr}"), name)


def add_page_number(paragraph) -> None:
    paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = paragraph.add_run()
    set_run_font(run, size=10)
    fld_char1 = OxmlElement("w:fldChar")
    fld_char1.set(qn("w:fldCharType"), "begin")
    instr = OxmlElement("w:instrText")
    instr.set(qn("xml:space"), "preserve")
    instr.text = " PAGE "
    fld_char2 = OxmlElement("w:fldChar")
    fld_char2.set(qn("w:fldCharType"), "end")
    run._r.append(fld_char1)
    run._r.append(instr)
    run._r.append(fld_char2)


def set_page_number_start(section, start: int = 1) -> None:
    sect_pr = section._sectPr
    pg_num_type = sect_pr.find(qn("w:pgNumType"))
    if pg_num_type is None:
        pg_num_type = OxmlElement("w:pgNumType")
        sect_pr.append(pg_num_type)
    pg_num_type.set(qn("w:start"), str(start))


def configure_section(section) -> None:
    section.page_width = Cm(21.0)
    section.page_height = Cm(29.7)
    section.top_margin = Cm(2.5)
    section.bottom_margin = Cm(2.5)
    section.left_margin = Cm(2.5)
    section.right_margin = Cm(2.5)
    section.header_distance = Cm(1.2)
    section.footer_distance = Cm(1.25)


def parse_manuscript(text: str):
    chapters: list[tuple[str, list[tuple[str, str]]]] = []
    current_title: str | None = None
    current_blocks: list[tuple[str, str]] = []
    paragraph_lines: list[str] = []

    def flush_paragraph() -> None:
        nonlocal paragraph_lines
        if paragraph_lines and current_title is not None:
            value = " ".join(line.strip() for line in paragraph_lines if line.strip()).strip()
            if value:
                current_blocks.append(("paragraph", value))
        paragraph_lines = []

    def flush_chapter() -> None:
        nonlocal current_title, current_blocks
        flush_paragraph()
        if current_title is not None:
            chapters.append((current_title, current_blocks))
        current_blocks = []

    for raw_line in text.splitlines():
        line = raw_line.rstrip()
        match = CHAPTER_RE.match(line.strip())
        if match:
            flush_chapter()
            current_title = match.group(1)
            continue

        if current_title is None:
            continue

        if not line.strip():
            flush_paragraph()
            continue

        if line.strip() == "---":
            flush_paragraph()
            continue

        if line.lstrip().startswith("#"):
            flush_paragraph()
            continue

        paragraph_lines.append(line)

    flush_chapter()

    expected = ["Prolog"] + [str(i) for i in range(1, 48)]
    actual = [title for title, _ in chapters]
    if actual != expected:
        raise SystemExit(f"Chapter structure mismatch: expected {expected}, got {actual}")

    return chapters


def add_inline_markdown(paragraph, text: str) -> None:
    cursor = 0
    for match in INLINE_RE.finditer(text):
        if match.start() > cursor:
            run = paragraph.add_run(text[cursor:match.start()])
            set_run_font(run)
        token = match.group(0)
        run = paragraph.add_run()
        if token.startswith("***") and token.endswith("***"):
            run.text = token[3:-3]
            run.bold = True
            run.italic = True
        elif token.startswith("**") and token.endswith("**"):
            run.text = token[2:-2]
            run.bold = True
        else:
            run.text = token[1:-1]
            run.italic = True
        set_run_font(run)
        cursor = match.end()
    if cursor < len(text):
        run = paragraph.add_run(text[cursor:])
        set_run_font(run)


def build_docx(source: Path, output: Path) -> None:
    chapters = parse_manuscript(source.read_text(encoding="utf-8"))

    doc = Document()
    doc.core_properties.title = "Ausnahmezustand"
    doc.core_properties.subject = "Romanmanuskript – Testleserfassung"
    doc.core_properties.author = ""
    doc.core_properties.keywords = ""
    doc.core_properties.comments = ""

    first_section = doc.sections[0]
    configure_section(first_section)
    first_section.different_first_page_header_footer = True

    normal = doc.styles["Normal"]
    normal.font.name = "Times New Roman"
    normal.font.size = Pt(12)
    normal.paragraph_format.line_spacing = 1.15
    normal.paragraph_format.space_before = Pt(0)
    normal.paragraph_format.space_after = Pt(0)
    normal.paragraph_format.first_line_indent = Cm(0.65)

    for _ in range(6):
        doc.add_paragraph()
    title = doc.add_paragraph()
    title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    title.paragraph_format.first_line_indent = Cm(0)
    title.paragraph_format.space_after = Pt(10)
    run = title.add_run("AUSNAHMEZUSTAND")
    run.bold = True
    set_run_font(run, size=24)

    subtitle = doc.add_paragraph()
    subtitle.alignment = WD_ALIGN_PARAGRAPH.CENTER
    subtitle.paragraph_format.first_line_indent = Cm(0)
    run = subtitle.add_run("Roman")
    run.italic = True
    set_run_font(run, size=12)

    manuscript_section = doc.add_section(WD_SECTION.NEW_PAGE)
    configure_section(manuscript_section)
    manuscript_section.different_first_page_header_footer = False
    manuscript_section.footer.is_linked_to_previous = False
    set_page_number_start(manuscript_section, 1)
    footer_p = manuscript_section.footer.paragraphs[0]
    add_page_number(footer_p)

    for chapter_index, (chapter_title, blocks) in enumerate(chapters):
        if chapter_index > 0:
            doc.add_page_break()

        heading = doc.add_paragraph()
        heading.alignment = WD_ALIGN_PARAGRAPH.CENTER
        heading.paragraph_format.first_line_indent = Cm(0)
        heading.paragraph_format.space_before = Pt(0)
        heading.paragraph_format.space_after = Pt(18)
        heading.paragraph_format.keep_with_next = True
        heading.paragraph_format.keep_together = True
        display = "Prolog" if chapter_title == "Prolog" else f"Kapitel {chapter_title}"
        run = heading.add_run(display)
        run.bold = True
        set_run_font(run, size=16)

        first_body = True
        for block_type, value in blocks:
            if block_type != "paragraph":
                continue
            p = doc.add_paragraph()
            p.paragraph_format.line_spacing = 1.15
            p.paragraph_format.space_before = Pt(0)
            p.paragraph_format.space_after = Pt(0)
            p.paragraph_format.widow_control = True
            p.paragraph_format.first_line_indent = Cm(0 if first_body else 0.65)
            add_inline_markdown(p, value)
            first_body = False

    output.parent.mkdir(parents=True, exist_ok=True)
    doc.save(output)
    if output.stat().st_size < 100_000:
        raise SystemExit(f"DOCX unexpectedly small: {output.stat().st_size} bytes")
    print(f"Built {output} ({output.stat().st_size} bytes, {len(chapters)} story units)")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("source", nargs="?", default="AUSNAHMEZUSTAND_FINAL.md")
    parser.add_argument("output", nargs="?", default="AUSNAHMEZUSTAND.docx")
    args = parser.parse_args()
    build_docx(Path(args.source), Path(args.output))


if __name__ == "__main__":
    main()
