from __future__ import annotations

import argparse
import re
from pathlib import Path

from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt, RGBColor

CHAPTER_RE = re.compile(r"^Kapitel\s+(\d+)(?:\s*[:\-–—].*)?$")

CHAPTER_TITLES = {
    1: "Komisch reicht nicht",
    2: "Die harmlose Erklärung",
    3: "Drei Türen",
    4: "Ein Millimeter",
    5: "Lagerhaus C",
    6: "Hamburg",
    7: "Der gelbe Streifen",
    8: "Privat",
    9: "Nur Wahrheit",
    10: "Zwei Risiken",
    11: "Richtig genug",
    12: "Die Uhr",
    13: "Parkebene 3",
    14: "Noch nicht",
    15: "Unabhängig",
    16: "Der Zugriff",
    17: "Vor der Suche",
    18: "Was die Quelle will",
    19: "Nicht größer",
    20: "Drei Treffer",
    21: "Der Sonderweg",
    22: "Dienstag",
    23: "Zu oft",
    24: "Die bessere Frage",
    25: "Vor dem Fall",
    26: "Zurückhalten",
    27: "Außerhalb des Falls",
    28: "Eigene Entscheidung",
    29: "Die Regel bleibt",
    30: "Gefährlich vernünftig",
    31: "Leerlauf",
    32: "Die alte Version",
    33: "Die alte Grenze",
    34: "Ohne Heller",
    35: "Der blaue Transporter",
    36: "Die einfache Geschichte",
    37: "Die Uhr läuft",
    38: "Drei Anker",
    39: "Verworfene Namen",
    40: "Der Schuss",
    41: "Was habt ihr selbst?",
    42: "Nicht weil er es sagte",
    43: "5.18 Uhr",
    44: "Verbundprüfung",
    45: "So ist es jetzt",
    46: "Schlechtes Bauchgefühl",
    47: "Die Gegenhypothese",
}


def style_by_name(doc: Document, name: str):
    return next(style for style in doc.styles if style.name == name)


def set_run_font(run, *, name: str, size: float, color: RGBColor | None = None) -> None:
    run.font.name = name
    run.font.size = Pt(size)
    if color is not None:
        run.font.color.rgb = color
    rpr = run._element.get_or_add_rPr()
    rfonts = rpr.rFonts
    if rfonts is None:
        rfonts = OxmlElement("w:rFonts")
        rpr.insert(0, rfonts)
    for attr in ("ascii", "hAnsi", "eastAsia", "cs"):
        rfonts.set(qn(f"w:{attr}"), name)
    lang = rpr.find(qn("w:lang"))
    if lang is None:
        lang = OxmlElement("w:lang")
        rpr.append(lang)
    lang.set(qn("w:val"), "de-DE")
    lang.set(qn("w:eastAsia"), "de-DE")
    lang.set(qn("w:bidi"), "de-DE")


def configure_style_font(style, *, name: str, size: float, color: RGBColor | None = None) -> None:
    style.font.name = name
    style.font.size = Pt(size)
    if color is not None:
        style.font.color.rgb = color
    rpr = style.element.get_or_add_rPr()
    rfonts = rpr.rFonts
    if rfonts is None:
        rfonts = OxmlElement("w:rFonts")
        rpr.insert(0, rfonts)
    for attr in ("ascii", "hAnsi", "eastAsia", "cs"):
        rfonts.set(qn(f"w:{attr}"), name)
    lang = rpr.find(qn("w:lang"))
    if lang is None:
        lang = OxmlElement("w:lang")
        rpr.append(lang)
    lang.set(qn("w:val"), "de-DE")
    lang.set(qn("w:eastAsia"), "de-DE")
    lang.set(qn("w:bidi"), "de-DE")


def validate_titles() -> None:
    expected = set(range(1, 48))
    actual = set(CHAPTER_TITLES)
    if actual != expected:
        missing = sorted(expected - actual)
        extra = sorted(actual - expected)
        raise SystemExit(f"Chapter title map mismatch; missing={missing}, extra={extra}")


def polish_docx(path: Path) -> None:
    validate_titles()
    doc = Document(path)

    normal = style_by_name(doc, "Normal")
    heading1 = style_by_name(doc, "Heading 1")

    # Readable test-reader/manuscript layout. Full justification creates large
    # word gaps in the many short thriller paragraphs, especially in Word.
    configure_style_font(normal, name="Times New Roman", size=11.5)
    normal.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.LEFT
    normal.paragraph_format.line_spacing = 1.15
    normal.paragraph_format.space_before = Pt(0)
    normal.paragraph_format.space_after = Pt(0)
    normal.paragraph_format.first_line_indent = Cm(0.4)
    normal.paragraph_format.widow_control = True

    configure_style_font(heading1, name="Times New Roman", size=15, color=RGBColor(0, 0, 0))
    heading1.font.bold = True
    heading1.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
    heading1.paragraph_format.first_line_indent = Cm(0)
    heading1.paragraph_format.space_before = Pt(0)
    heading1.paragraph_format.space_after = Pt(20)
    heading1.paragraph_format.keep_with_next = True
    heading1.paragraph_format.keep_together = True

    seen: list[int] = []
    first_body_after_heading = False

    for paragraph in doc.paragraphs:
        style_name = paragraph.style.name if paragraph.style is not None else ""

        if style_name == "Heading 1":
            text = paragraph.text.strip()
            if text == "Prolog":
                display = "Prolog"
            else:
                match = CHAPTER_RE.match(text)
                if not match:
                    raise SystemExit(f"Unexpected Heading 1 text: {text!r}")
                number = int(match.group(1))
                if number not in CHAPTER_TITLES:
                    raise SystemExit(f"Missing title for chapter {number}")
                seen.append(number)
                display = f"Kapitel {number} - {CHAPTER_TITLES[number]}"

            paragraph.clear()
            run = paragraph.add_run(display)
            run.bold = True
            set_run_font(run, name="Times New Roman", size=15, color=RGBColor(0, 0, 0))
            paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
            paragraph.paragraph_format.first_line_indent = Cm(0)
            paragraph.paragraph_format.space_after = Pt(20)
            first_body_after_heading = True
            continue

        if style_name == "Normal" and paragraph.text.strip():
            paragraph.alignment = WD_ALIGN_PARAGRAPH.LEFT
            paragraph.paragraph_format.line_spacing = 1.15
            paragraph.paragraph_format.space_before = Pt(0)
            paragraph.paragraph_format.space_after = Pt(0)
            paragraph.paragraph_format.widow_control = True
            paragraph.paragraph_format.first_line_indent = Cm(0 if first_body_after_heading else 0.4)
            for run in paragraph.runs:
                set_run_font(run, name="Times New Roman", size=11.5)
            first_body_after_heading = False

    if seen != list(range(1, 48)):
        raise SystemExit(f"Chapter headings mismatch after polish: {seen}")

    doc.save(path)
    print(f"Polished {path} with {len(seen)} chapter titles")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("docx", nargs="?", default="AUSNAHMEZUSTAND.docx")
    args = parser.parse_args()
    polish_docx(Path(args.docx))


if __name__ == "__main__":
    main()
