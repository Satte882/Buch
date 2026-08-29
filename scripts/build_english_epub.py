from __future__ import annotations

import argparse
import ast
import html
import json
import re
import uuid
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET

STORY_HEADING_RE = re.compile(r"^##\s+(Prologue|\d+)\s*$", re.M)
INLINE_RE = re.compile(r"(\*\*\*.+?\*\*\*|\*\*.+?\*\*|(?<!\*)\*[^*]+?\*(?!\*))")
EXPECTED = ["Prologue"] + [str(i) for i in range(1, 48)]
EXPECTED_ENDING = '"How strong is your counterhypothesis?"'
EPUB_MIMETYPE = "application/epub+zip"
EDITION_MODIFIED = "2026-08-30T00:00:00Z"


def load_config(path: Path) -> dict:
    data = json.loads(path.read_text(encoding="utf-8"))
    if data.get("market_title_status") != "approved":
        raise SystemExit("English market title must be approved before EPUB production")
    title = data.get("market_title")
    if not isinstance(title, str) or not title.strip():
        raise SystemExit("Approved market title is missing")
    if data.get("language") != "en-US":
        raise SystemExit("English EPUB pipeline expects en-US")
    return data


def load_chapter_titles(script_path: Path) -> dict[int, str]:
    tree = ast.parse(script_path.read_text(encoding="utf-8"))
    for node in tree.body:
        if not isinstance(node, ast.Assign):
            continue
        for target in node.targets:
            if isinstance(target, ast.Name) and target.id == "CHAPTER_TITLES":
                value = ast.literal_eval(node.value)
                if not isinstance(value, dict) or set(value) != set(range(1, 48)):
                    raise SystemExit("Unexpected CHAPTER_TITLES mapping in print builder")
                return {int(k): str(v) for k, v in value.items()}
    raise SystemExit("CHAPTER_TITLES not found in print builder")


def split_story(text: str) -> tuple[str, list[tuple[str, str]]]:
    matches = list(STORY_HEADING_RE.finditer(text))
    headings = [m.group(1) for m in matches]
    if headings != EXPECTED:
        raise SystemExit(f"Story heading mismatch: expected {EXPECTED}, got {headings}")
    if not text.rstrip().endswith(EXPECTED_ENDING):
        raise SystemExit("English manuscript ending does not match approved chapter 47 ending")

    front = text[: matches[0].start()].strip()
    chapters: list[tuple[str, str]] = []
    for idx, match in enumerate(matches):
        end = matches[idx + 1].start() if idx + 1 < len(matches) else len(text)
        body = text[match.end() : end].strip()
        if not body:
            raise SystemExit(f"Empty story unit: {match.group(1)}")
        chapters.append((match.group(1), body))
    return front, chapters


def inline_html(text: str) -> str:
    out: list[str] = []
    cursor = 0
    for match in INLINE_RE.finditer(text):
        out.append(html.escape(text[cursor : match.start()], quote=False))
        token = match.group(0)
        if token.startswith("***") and token.endswith("***"):
            out.append(f"<strong><em>{html.escape(token[3:-3], quote=False)}</em></strong>")
        elif token.startswith("**") and token.endswith("**"):
            out.append(f"<strong>{html.escape(token[2:-2], quote=False)}</strong>")
        else:
            out.append(f"<em>{html.escape(token[1:-1], quote=False)}</em>")
        cursor = match.end()
    out.append(html.escape(text[cursor:], quote=False))
    return "".join(out)


def body_to_html(body: str) -> str:
    parts: list[str] = []
    for raw in re.split(r"\n\s*\n", body.strip()):
        block = " ".join(line.strip() for line in raw.splitlines() if line.strip()).strip()
        if not block:
            continue
        if block == "---":
            parts.append('<p class="scene-break" aria-hidden="true">*</p>')
            continue
        if block.startswith("#"):
            continue
        parts.append(f"<p>{inline_html(block)}</p>")
    return "\n".join(parts)


def xhtml_document(title: str, body: str, css_href: str = "styles.css") -> str:
    return f'''<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" lang="en-US" xml:lang="en-US">
<head>
  <meta charset="utf-8"/>
  <title>{html.escape(title)}</title>
  <link rel="stylesheet" type="text/css" href="{css_href}"/>
</head>
<body>
{body}
</body>
</html>
'''


def title_page(title: str) -> str:
    body = f'''<section epub:type="titlepage" class="title-page">
  <h1>{html.escape(title)}</h1>
  <div class="epigraph">
    <p><em>A rule withstands<br/>everything,</em></p>
    <p><em>except proof</em></p>
    <p><em>that things work<br/>better without it.</em></p>
  </div>
</section>'''
    return xhtml_document(title, body)


def definition_page() -> str:
    body = '''<section epub:type="preface" class="definition-page">
  <p><strong>Normalfall (German noun):</strong></p>
  <p>A case handled according to the usual rules.</p>
  <div class="epigraph compact">
    <p><em>A rule withstands everything,</em></p>
    <p><em>except proof</em></p>
    <p><em>that things work better without it.</em></p>
  </div>
</section>'''
    return xhtml_document("Normalfall", body)


def chapter_page(label: str, display: str, body: str) -> str:
    epub_type = "prologue" if label == "Prologue" else "chapter"
    content = f'''<section epub:type="{epub_type}">
  <h1>{html.escape(display)}</h1>
  {body_to_html(body)}
</section>'''
    return xhtml_document(display, content)


def nav_page(items: list[tuple[str, str]]) -> str:
    lis = "\n".join(
        f'      <li><a href="{html.escape(href)}">{html.escape(label)}</a></li>'
        for href, label in items
    )
    body = f'''<nav epub:type="toc" id="toc">
  <h1>Contents</h1>
  <ol>
{lis}
  </ol>
</nav>'''
    return xhtml_document("Contents", body)


def content_opf(title: str, language: str, identifier: str, chapter_files: list[str], author: str | None) -> str:
    creator = f"\n    <dc:creator>{html.escape(author)}</dc:creator>" if author else ""
    manifest = [
        '    <item id="nav" href="nav.xhtml" media-type="application/xhtml+xml" properties="nav"/>',
        '    <item id="css" href="styles.css" media-type="text/css"/>',
        '    <item id="title" href="title.xhtml" media-type="application/xhtml+xml"/>',
        '    <item id="definition" href="definition.xhtml" media-type="application/xhtml+xml"/>',
    ]
    spine = ['    <itemref idref="title"/>', '    <itemref idref="definition"/>']
    for idx, filename in enumerate(chapter_files):
        item_id = f"story-{idx:02d}"
        manifest.append(f'    <item id="{item_id}" href="{filename}" media-type="application/xhtml+xml"/>')
        spine.append(f'    <itemref idref="{item_id}"/>')
    return f'''<?xml version="1.0" encoding="utf-8"?>
<package xmlns="http://www.idpf.org/2007/opf" version="3.0" unique-identifier="bookid" xml:lang="en-US">
  <metadata xmlns:dc="http://purl.org/dc/elements/1.1/">
    <dc:identifier id="bookid">{identifier}</dc:identifier>
    <dc:title>{html.escape(title)}</dc:title>
    <dc:language>{html.escape(language)}</dc:language>{creator}
    <meta property="dcterms:modified">{EDITION_MODIFIED}</meta>
  </metadata>
  <manifest>
{chr(10).join(manifest)}
  </manifest>
  <spine>
{chr(10).join(spine)}
  </spine>
</package>
'''


CSS = '''html { -webkit-text-size-adjust: 100%; }
body { font-family: serif; line-height: 1.4; margin: 0 5%; }
h1 { text-align: center; font-size: 1.45em; margin: 2.5em 0 2em; page-break-before: always; }
p { margin: 0; text-indent: 1.2em; }
h1 + p, .title-page p, .definition-page p, .epigraph p, .scene-break { text-indent: 0; }
.title-page, .definition-page { text-align: center; }
.title-page h1 { font-size: 2em; margin-top: 25%; page-break-before: auto; }
.epigraph { margin-top: 3em; }
.epigraph p { margin: 0.8em 0; }
.compact { margin-top: 2.5em; }
.scene-break { text-align: center; margin: 1em 0; }
nav ol { list-style-type: none; padding-left: 0; }
nav li { margin: 0.35em 0; }
a { text-decoration: none; color: inherit; }
'''


def build_epub(source: Path, output: Path, config_path: Path, print_builder: Path) -> None:
    config = load_config(config_path)
    title = config["market_title"].strip()
    language = config["language"]
    author = config.get("author")
    if author is not None and not isinstance(author, str):
        raise SystemExit("author must be a string or null")

    text = source.read_text(encoding="utf-8")
    front, chapters = split_story(text)
    if not front.startswith(f"# {title}"):
        raise SystemExit("Generated English master front-matter title does not match publishing config")

    chapter_titles = load_chapter_titles(print_builder)
    book_uuid = uuid.uuid5(uuid.NAMESPACE_URL, f"Satte882/Buch:{title}:{language}")
    identifier = f"urn:uuid:{book_uuid}"

    files: dict[str, str] = {
        "META-INF/container.xml": '''<?xml version="1.0" encoding="UTF-8"?>
<container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container">
  <rootfiles>
    <rootfile full-path="OEBPS/content.opf" media-type="application/oebps-package+xml"/>
  </rootfiles>
</container>
''',
        "OEBPS/styles.css": CSS,
        "OEBPS/title.xhtml": title_page(title),
        "OEBPS/definition.xhtml": definition_page(),
    }

    nav_items: list[tuple[str, str]] = []
    chapter_files: list[str] = []
    for label, body in chapters:
        if label == "Prologue":
            filename = "prologue.xhtml"
            display = "Prologue"
        else:
            number = int(label)
            filename = f"chapter-{number:02d}.xhtml"
            display = f"Chapter {number} – {chapter_titles[number]}"
        files[f"OEBPS/{filename}"] = chapter_page(label, display, body)
        nav_items.append((filename, display))
        chapter_files.append(filename)

    files["OEBPS/nav.xhtml"] = nav_page(nav_items)
    files["OEBPS/content.opf"] = content_opf(title, language, identifier, chapter_files, author.strip() if isinstance(author, str) and author.strip() else None)

    output.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(output, "w") as zf:
        zf.writestr("mimetype", EPUB_MIMETYPE, compress_type=zipfile.ZIP_STORED)
        for path, content in files.items():
            zf.writestr(path, content.encode("utf-8"), compress_type=zipfile.ZIP_DEFLATED)

    validate_epub(output, title)
    print(f"Built {output} ({output.stat().st_size} bytes, {len(chapters)} story units, title={title!r})")


def validate_epub(path: Path, expected_title: str) -> None:
    with zipfile.ZipFile(path, "r") as zf:
        names = zf.namelist()
        if not names or names[0] != "mimetype":
            raise SystemExit("EPUB mimetype must be first ZIP entry")
        if zf.read("mimetype").decode("ascii") != EPUB_MIMETYPE:
            raise SystemExit("Invalid EPUB mimetype")
        info = zf.getinfo("mimetype")
        if info.compress_type != zipfile.ZIP_STORED:
            raise SystemExit("EPUB mimetype must be uncompressed")
        required = {"META-INF/container.xml", "OEBPS/content.opf", "OEBPS/nav.xhtml", "OEBPS/title.xhtml", "OEBPS/prologue.xhtml", "OEBPS/chapter-47.xhtml"}
        missing = required.difference(names)
        if missing:
            raise SystemExit(f"Missing EPUB entries: {sorted(missing)}")
        for name in names:
            if name.endswith((".xml", ".opf", ".xhtml")):
                ET.fromstring(zf.read(name))
        if expected_title not in zf.read("OEBPS/title.xhtml").decode("utf-8"):
            raise SystemExit("EPUB title page does not contain approved market title")
        if EXPECTED_ENDING not in zf.read("OEBPS/chapter-47.xhtml").decode("utf-8"):
            raise SystemExit("EPUB chapter 47 ending does not match approved manuscript")


def main() -> None:
    parser = argparse.ArgumentParser(description="Build reflowable EPUB 3 for the English edition.")
    parser.add_argument("source", nargs="?", type=Path, default=Path("ENGLISH/NORMALFALL_ENGLISH.md"))
    parser.add_argument("output", nargs="?", type=Path, default=Path("ENGLISH/REASONABLE_MEASURES.epub"))
    parser.add_argument("--config", type=Path, default=Path("ENGLISH/PUBLISHING_CONFIG.json"))
    parser.add_argument("--print-builder", type=Path, default=Path("scripts/build_english_book_docx.py"))
    args = parser.parse_args()
    build_epub(args.source, args.output, args.config, args.print_builder)


if __name__ == "__main__":
    main()
