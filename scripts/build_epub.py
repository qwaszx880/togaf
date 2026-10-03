#!/usr/bin/env python3
"""Build the repository's Markdown course as a self-contained EPUB 3 book."""

from __future__ import annotations

import argparse
import html
import re
import zipfile
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = ROOT / "epub" / "togaf-hands-on-guide.epub"
BOOK_ID = "urn:uuid:778622a2-a0c5-5f90-a05a-a8691cb49fd5"

SECTIONS = (
    ("Course Overview", ".", ("README.md",)),
    ("Start Here", "00-start-here", ("README.md", "diagnostic.md", "progress-tracker.md", "study-plans.md")),
    ("Foundation", "01-foundation", ("README.md", "01-concepts.md", "02-adm-fundamentals.md", "03-adm-techniques.md", "04-applying-adm.md", "05-governance.md", "06-architecture-content.md", "07-review-and-mock.md")),
    ("Worked Examples Overview", "examples", ("README.md",)),
    ("Foundation Worked Examples", "examples/foundation", ("01-concepts-coffee-shop.md", "02-adm-walkthrough.md", "03-technique-chain.md", "04-tailoring.md", "05-governance-and-content.md")),
    ("Practitioner", "02-practitioner", ("README.md", "01-ea-context.md", "02-stakeholders.md", "03-phase-a.md", "04-development.md", "05-implementation.md", "06-change.md", "07-requirements.md", "08-supporting-work.md", "09-scenario-workshop.md")),
    ("Practitioner Worked Examples", "examples/practitioner", ("01-context-and-stakeholders.md", "02-phase-a-vision.md", "03-domain-development.md", "04-roadmap-and-governance.md", "05-change-and-requirements.md", "06-supporting-techniques.md", "07-scenario-reasoning.md")),
    ("Northstar Outfitters Case Study", "case-study", ("README.md", "01-vision-and-scope.md", "02-architecture-and-roadmap.md")),
    ("Reusable Templates", "case-study/templates", ("architecture-vision-canvas.md", "gap-analysis.md", "requirements-register.md", "roadmap.md")),
    ("Reference", "reference", ("glossary.md", "quick-reference.md", "exam-facts.md", "further-reading.md")),
)


@dataclass(frozen=True)
class Chapter:
    section: str
    source: Path
    href: str
    title: str


def slugify(value: str) -> str:
    """Return a stable, EPUB-safe identifier."""
    plain = re.sub(r"[*_`]+", "", value).lower()
    slug = re.sub(r"[^a-z0-9]+", "-", plain).strip("-")
    return slug or "section"


def book_chapters() -> list[Chapter]:
    """Return source documents in the intended reading order."""
    chapters: list[Chapter] = []
    for section, directory, names in SECTIONS:
        for name in names:
            source = ROOT / directory / name
            first_heading = next(
                (line[2:].strip() for line in source.read_text(encoding="utf-8").splitlines() if line.startswith("# ")),
                source.stem.replace("-", " ").title(),
            )
            relative = source.relative_to(ROOT)
            href = f"text/{slugify(str(relative.with_suffix('')))}.xhtml"
            chapters.append(Chapter(section, source, href, first_heading))
    return chapters


def resolve_link(raw: str, source: Path, hrefs: dict[Path, str]) -> str:
    """Translate a repository-relative Markdown link into an EPUB link."""
    if raw.startswith(("http://", "https://", "mailto:")):
        return raw
    path_text, marker, fragment = raw.partition("#")
    if not path_text:
        return f"#{slugify(unquote(fragment))}" if marker else raw
    target = (source.parent / unquote(path_text)).resolve()
    if target.is_dir():
        target /= "README.md"
    target = target.with_suffix(".md") if not target.suffix else target
    if target not in hrefs:
        return raw
    suffix = f"#{slugify(unquote(fragment))}" if marker and fragment else ""
    current_href = hrefs[source]
    # Every chapter lives in the same EPUB directory, so only the basename is needed.
    if hrefs[target] == current_href:
        return suffix or "#"
    return f"{Path(hrefs[target]).name}{suffix}"


def inline(text: str, source: Path, hrefs: dict[Path, str]) -> str:
    """Convert the small inline-Markdown subset used by this course."""
    tokens: list[str] = []

    def stash(value: str) -> str:
        tokens.append(value)
        return f"\x00{len(tokens) - 1}\x00"

    text = re.sub(r"`([^`]+)`", lambda m: stash(f"<code>{html.escape(m.group(1))}</code>"), text)

    def link(match: re.Match[str]) -> str:
        label, target = match.group(1), match.group(2)
        href = html.escape(resolve_link(target, source, hrefs), quote=True)
        return stash(f'<a href="{href}">{html.escape(label)}</a>')

    text = re.sub(r"\[([^]]+)]\(([^)]+)\)", link, text)
    text = html.escape(text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"(?<!\*)\*([^*]+)\*", r"<em>\1</em>", text)
    text = re.sub(r"~~([^~]+)~~", r"<del>\1</del>", text)
    for index, token in enumerate(tokens):
        text = text.replace(f"\x00{index}\x00", token)
    return text


def markdown_to_xhtml(markdown: str, source: Path, hrefs: dict[Path, str]) -> tuple[str, str]:
    """Render the repository's intentionally simple Markdown without dependencies."""
    lines = markdown.splitlines()
    output: list[str] = []
    paragraph: list[str] = []
    list_stack: list[tuple[int, str]] = []
    title = source.stem.replace("-", " ").title()
    in_code = False
    code_lines: list[str] = []
    in_table = False
    heading_counts: dict[str, int] = {}

    def flush_paragraph() -> None:
        if paragraph:
            output.append(f"<p>{inline(' '.join(part.strip() for part in paragraph), source, hrefs)}</p>")
            paragraph.clear()

    def close_lists(level: int = -1) -> None:
        while list_stack and list_stack[-1][0] >= level:
            _, tag = list_stack.pop()
            output.append(f"</{tag}>")

    index = 0
    while index < len(lines):
        line = lines[index]
        stripped = line.strip()
        if stripped.startswith("```"):
            flush_paragraph()
            close_lists()
            if in_code:
                output.append(f"<pre><code>{html.escape(chr(10).join(code_lines))}</code></pre>")
                code_lines.clear()
            in_code = not in_code
            index += 1
            continue
        if in_code:
            code_lines.append(line)
            index += 1
            continue

        heading = re.match(r"^(#{1,6})\s+(.+)$", stripped)
        if heading:
            flush_paragraph()
            close_lists()
            level = len(heading.group(1))
            heading_text = heading.group(2).strip()
            if level == 1:
                title = re.sub(r"[*_`]", "", heading_text)
            base_id = slugify(heading_text)
            heading_counts[base_id] = heading_counts.get(base_id, 0) + 1
            identifier = base_id if heading_counts[base_id] == 1 else f"{base_id}-{heading_counts[base_id]}"
            output.append(f'<h{level} id="{identifier}">{inline(heading_text, source, hrefs)}</h{level}>')
            index += 1
            continue

        # GitHub-style tables always have a delimiter row immediately after the header.
        if "|" in line and index + 1 < len(lines) and re.match(r"^\s*\|?\s*:?-{3,}", lines[index + 1]):
            flush_paragraph()
            close_lists()
            headers = [cell.strip() for cell in line.strip().strip("|").split("|")]
            output.append("<table><thead><tr>" + "".join(f"<th>{inline(cell, source, hrefs)}</th>" for cell in headers) + "</tr></thead><tbody>")
            in_table = True
            index += 2
            continue
        if in_table:
            if "|" in line and stripped:
                cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
                output.append("<tr>" + "".join(f"<td>{inline(cell, source, hrefs)}</td>" for cell in cells) + "</tr>")
                index += 1
                continue
            output.append("</tbody></table>")
            in_table = False

        item = re.match(r"^(\s*)([-+*]|\d+[.)])\s+(.*)$", line)
        if item:
            flush_paragraph()
            indent = len(item.group(1).replace("\t", "    ")) // 2
            tag = "ol" if item.group(2)[0].isdigit() else "ul"
            while list_stack and list_stack[-1][0] > indent:
                _, old_tag = list_stack.pop()
                output.append(f"</{old_tag}>")
            if not list_stack or list_stack[-1] != (indent, tag):
                if list_stack and list_stack[-1][0] == indent:
                    _, old_tag = list_stack.pop()
                    output.append(f"</{old_tag}>")
                output.append(f"<{tag}>")
                list_stack.append((indent, tag))
            item_text = item.group(3)
            task = re.match(r"\[([ xX])]\s+(.*)", item_text)
            if task:
                mark = "☑" if task.group(1).strip() else "☐"
                item_text = f'<span class="task">{mark}</span> {inline(task.group(2), source, hrefs)}'
            else:
                item_text = inline(item_text, source, hrefs)
            output.append(f"<li>{item_text}</li>")
            index += 1
            continue

        if stripped.startswith(">"):
            flush_paragraph()
            close_lists()
            quote_lines = []
            while index < len(lines) and lines[index].strip().startswith(">"):
                quote_lines.append(lines[index].strip()[1:].strip())
                index += 1
            output.append(f"<blockquote><p>{inline(' '.join(quote_lines), source, hrefs)}</p></blockquote>")
            continue
        if re.match(r"^([-*_])\1\1+$", stripped):
            flush_paragraph()
            close_lists()
            output.append("<hr/>")
            index += 1
            continue
        if not stripped:
            flush_paragraph()
            close_lists()
        else:
            paragraph.append(stripped)
        index += 1

    flush_paragraph()
    close_lists()
    if in_table:
        output.append("</tbody></table>")
    return title, "\n".join(output)


CSS = """
@page { margin: 5%; }
body { color: #17212b; font-family: sans-serif; line-height: 1.55; margin: 0 auto; max-width: 44em; }
h1, h2, h3, h4 { color: #123c5a; font-family: serif; line-height: 1.2; page-break-after: avoid; }
h1 { border-bottom: .18em solid #e3a72f; font-size: 2em; padding-bottom: .25em; }
h2 { border-bottom: .06em solid #8ca9b8; margin-top: 1.8em; padding-bottom: .15em; }
a { color: #075f83; }
blockquote { background: #eef5f7; border-left: .3em solid #21758f; margin: 1.2em 0; padding: .45em 1em; }
code { background: #eef0f2; font-family: monospace; padding: .08em .25em; }
pre { background: #17212b; color: #f6f7f8; overflow-wrap: break-word; padding: 1em; white-space: pre-wrap; }
table { border-collapse: collapse; font-size: .9em; margin: 1.2em 0; width: 100%; }
th { background: #123c5a; color: white; text-align: left; }
th, td { border: 1px solid #9caab2; padding: .45em; vertical-align: top; }
tr:nth-child(even) td { background: #f2f6f7; }
li { margin: .25em 0; }
.task { color: #b06d00; font-weight: bold; }
.cover { padding-top: 18%; text-align: center; }
.cover h1 { border: 0; font-size: 2.6em; }
.cover .rule { background: #e3a72f; height: .35em; margin: 2em auto; width: 7em; }
.subtitle { color: #3f5f6f; font-size: 1.25em; }
.fine-print { font-size: .82em; margin-top: 5em; }
nav ol { list-style-type: none; padding-left: 1em; }
nav > ol { padding-left: 0; }
nav li { margin: .55em 0; }
""".strip()


def xhtml_page(title: str, body: str, body_class: str = "") -> str:
    return f'''<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" lang="en" xml:lang="en">
<head><meta charset="utf-8"/><title>{html.escape(title)}</title><link rel="stylesheet" href="../styles/book.css"/></head>
<body class="{body_class}">{body}</body></html>'''


def build(output: Path) -> None:
    chapters = book_chapters()
    hrefs = {chapter.source.resolve(): chapter.href for chapter in chapters}
    rendered = []
    for chapter in chapters:
        markdown = chapter.source.read_text(encoding="utf-8")
        # A download link to the book is useful on GitHub but circular inside the book.
        if chapter.source == ROOT / "README.md":
            markdown = re.sub(r"^- \[Download the complete, reader-ready EPUB].*\n", "", markdown, flags=re.MULTILINE)
        title, body = markdown_to_xhtml(markdown, chapter.source.resolve(), hrefs)
        rendered.append((chapter, title, xhtml_page(title, body)))

    grouped_nav: list[str] = []
    for section, _, _ in SECTIONS:
        entries = [(chapter, title) for chapter, title, _ in rendered if chapter.section == section]
        links = "".join(f'<li><a href="{Path(chapter.href).name}">{html.escape(title)}</a></li>' for chapter, title in entries)
        grouped_nav.append(f"<li><span>{html.escape(section)}</span><ol>{links}</ol></li>")
    nav = xhtml_page("Contents", f'<nav epub:type="toc" id="toc"><h1>Contents</h1><ol>{"".join(grouped_nav)}</ol></nav>')

    cover_body = '''<section class="cover" epub:type="cover">
<p>INDEPENDENT STUDY EDITION</p><h1>TOGAF Enterprise Architecture</h1>
<div class="rule"></div><p class="subtitle">A Hands-On Certification Preparation Guide</p>
<p>Foundation • Practitioner • Northstar Outfitters case study</p>
<p class="fine-print">Original learning material. TOGAF is a registered trademark of The Open Group.<br/>Not an official or accredited Open Group course.</p></section>'''
    cover = xhtml_page("Cover", cover_body, "cover-page")

    manifest = ['<item id="cover" href="text/cover.xhtml" media-type="application/xhtml+xml"/>',
                '<item id="nav" href="text/nav.xhtml" media-type="application/xhtml+xml" properties="nav"/>',
                '<item id="css" href="styles/book.css" media-type="text/css"/>']
    spine = ['<itemref idref="cover"/>', '<itemref idref="nav"/>']
    for number, (chapter, _, _) in enumerate(rendered, 1):
        manifest.append(f'<item id="chapter-{number}" href="{chapter.href}" media-type="application/xhtml+xml"/>')
        spine.append(f'<itemref idref="chapter-{number}"/>')
    package = f'''<?xml version="1.0" encoding="utf-8"?>
<package xmlns="http://www.idpf.org/2007/opf" version="3.0" unique-identifier="book-id" xml:lang="en">
<metadata xmlns:dc="http://purl.org/dc/elements/1.1/">
<dc:identifier id="book-id">{BOOK_ID}</dc:identifier><dc:title>TOGAF Enterprise Architecture: A Hands-On Certification Preparation Guide</dc:title>
<dc:language>en</dc:language><dc:creator>TOGAF Learning Guide Contributors</dc:creator><dc:subject>Enterprise architecture</dc:subject>
<dc:description>An original course for TOGAF Enterprise Architecture Foundation and Practitioner certification preparation.</dc:description>
<meta property="dcterms:modified">2026-10-03T00:00:00Z</meta></metadata>
<manifest>{''.join(manifest)}</manifest><spine>{''.join(spine)}</spine></package>'''
    container = '''<?xml version="1.0" encoding="UTF-8"?>
<container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container"><rootfiles>
<rootfile full-path="EPUB/package.opf" media-type="application/oebps-package+xml"/>
</rootfiles></container>'''

    output.parent.mkdir(parents=True, exist_ok=True)
    def write_file(archive: zipfile.ZipFile, name: str, content: str, compress: bool = True) -> None:
        """Write deterministic entries so unchanged source produces an unchanged book."""
        info = zipfile.ZipInfo(name, date_time=(2026, 10, 3, 0, 0, 0))
        info.compress_type = zipfile.ZIP_DEFLATED if compress else zipfile.ZIP_STORED
        info.external_attr = 0o644 << 16
        archive.writestr(info, content)

    with zipfile.ZipFile(output, "w") as archive:
        # The EPUB specification requires this to be the first, uncompressed entry.
        write_file(archive, "mimetype", "application/epub+zip", compress=False)
        write_file(archive, "META-INF/container.xml", container)
        write_file(archive, "EPUB/package.opf", package)
        write_file(archive, "EPUB/styles/book.css", CSS)
        write_file(archive, "EPUB/text/cover.xhtml", cover)
        write_file(archive, "EPUB/text/nav.xhtml", nav)
        for chapter, _, document in rendered:
            write_file(archive, f"EPUB/{chapter.href}", document)
    print(f"Built {output.relative_to(ROOT)} with {len(chapters)} chapters.")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("output", nargs="?", type=Path, default=DEFAULT_OUTPUT, help="output EPUB path")
    args = parser.parse_args()
    build(args.output.resolve())


if __name__ == "__main__":
    main()
