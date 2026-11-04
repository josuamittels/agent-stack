#!/usr/bin/env python3
"""Build, export, and validate a CV using bundled skill assets."""

from __future__ import annotations

import argparse
import html
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path
from typing import Any
from xml.etree import ElementTree as ET

from docx import Document
from docx.enum.style import WD_STYLE_TYPE
from docx.enum.table import WD_CELL_VERTICAL_ALIGNMENT, WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_TAB_ALIGNMENT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt, RGBColor
from pypdf import PdfReader
import pypdfium2 as pdfium

SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

from cv_support import (
    FONT_DIR,
    BULLET_SIZE_HALF_POINTS,
    SECTION_RULE_EIGHTH_POINTS,
    SEPARATOR_RAISE_HALF_POINTS,
    file_hash,
    read_json,
    validate_inputs,
)


FONT_FAMILY = "EB Garamond"
BLACK = RGBColor(0, 0, 0)
GREY = RGBColor(110, 110, 110)
BLUE = RGBColor(25, 110, 230)
CONTENT_WIDTH_CM = 17.3
CV_STEM = "CV"
PDF_FONT_PREFIX = "EBGaramond-"
BULLET_GLYPH = "."


def set_run_font(
    run,
    size: float,
    color=BLACK,
    *,
    bold: bool = False,
    italic: bool = False,
) -> None:
    run.font.name = FONT_FAMILY
    run.font.size = Pt(size)
    run.font.color.rgb = color
    run.font.bold = bold
    run.font.italic = italic
    fonts = run._element.get_or_add_rPr().get_or_add_rFonts()
    for key in ("ascii", "hAnsi", "eastAsia", "cs"):
        fonts.set(qn(f"w:{key}"), FONT_FAMILY)


def set_keep(paragraph, *, keep_next: bool = False, keep_lines: bool = True) -> None:
    properties = paragraph._p.get_or_add_pPr()
    if keep_next:
        properties.append(OxmlElement("w:keepNext"))
    if keep_lines:
        properties.append(OxmlElement("w:keepLines"))
    properties.append(OxmlElement("w:widowControl"))


def add_bottom_border(
    paragraph,
    size_eighth_points: int = SECTION_RULE_EIGHTH_POINTS,
    space: int = 3,
) -> None:
    properties = paragraph._p.get_or_add_pPr()
    borders = OxmlElement("w:pBdr")
    bottom = OxmlElement("w:bottom")
    bottom.set(qn("w:val"), "single")
    bottom.set(qn("w:sz"), str(size_eighth_points))
    bottom.set(qn("w:space"), str(space))
    bottom.set(qn("w:color"), "000000")
    borders.append(bottom)
    properties.append(borders)


def add_hyperlink(paragraph, text: str, url: str) -> None:
    relation_id = paragraph.part.relate_to(
        url,
        "http://schemas.openxmlformats.org/officeDocument/2006/relationships/hyperlink",
        is_external=True,
    )
    hyperlink = OxmlElement("w:hyperlink")
    hyperlink.set(qn("r:id"), relation_id)
    run = OxmlElement("w:r")
    run_properties = OxmlElement("w:rPr")
    fonts = OxmlElement("w:rFonts")
    for key in ("ascii", "hAnsi", "eastAsia", "cs"):
        fonts.set(qn(f"w:{key}"), FONT_FAMILY)
    run_properties.append(fonts)
    color = OxmlElement("w:color")
    color.set(qn("w:val"), "196EE6")
    run_properties.append(color)
    for element_name in ("w:sz", "w:szCs"):
        size = OxmlElement(element_name)
        size.set(qn("w:val"), "21")
        run_properties.append(size)
    run.append(run_properties)
    text_element = OxmlElement("w:t")
    text_element.text = text
    run.append(text_element)
    hyperlink.append(run)
    paragraph._p.append(hyperlink)


def add_contact_separator(paragraph) -> None:
    run = paragraph.add_run(" | ")
    set_run_font(run, 10.5)


def configure_styles(document: Document) -> None:
    styles = document.styles
    normal = styles["Normal"]
    normal.font.name = FONT_FAMILY
    normal.font.size = Pt(10.7)
    for key in ("ascii", "hAnsi", "eastAsia", "cs"):
        normal._element.rPr.rFonts.set(qn(f"w:{key}"), FONT_FAMILY)
    normal.paragraph_format.space_before = Pt(0)
    normal.paragraph_format.space_after = Pt(0)
    normal.paragraph_format.line_spacing = 1.08

    section = styles.add_style("CV Section", WD_STYLE_TYPE.PARAGRAPH)
    section.font.name = FONT_FAMILY
    section.font.size = Pt(11.5)
    section.font.bold = True
    for key in ("ascii", "hAnsi", "eastAsia", "cs"):
        section._element.rPr.rFonts.set(qn(f"w:{key}"), FONT_FAMILY)
    section.paragraph_format.space_before = Pt(7)
    section.paragraph_format.space_after = Pt(6)
    section.paragraph_format.line_spacing = 1.0

    entry = styles.add_style("CV Entry", WD_STYLE_TYPE.PARAGRAPH)
    entry.paragraph_format.space_before = Pt(2.5)
    entry.paragraph_format.space_after = Pt(0)
    entry.paragraph_format.line_spacing = 1.0

    secondary = styles.add_style("CV Secondary", WD_STYLE_TYPE.PARAGRAPH)
    secondary.paragraph_format.space_before = Pt(0)
    secondary.paragraph_format.space_after = Pt(1.2)
    secondary.paragraph_format.line_spacing = 1.0

    descriptor = styles.add_style("CV Descriptor", WD_STYLE_TYPE.PARAGRAPH)
    descriptor.paragraph_format.space_before = Pt(0)
    descriptor.paragraph_format.space_after = Pt(1.5)
    descriptor.paragraph_format.line_spacing = 1.0

    bullet = styles.add_style("CV Bullet", WD_STYLE_TYPE.PARAGRAPH)
    bullet.base_style = normal
    bullet.paragraph_format.left_indent = Cm(0.52)
    bullet.paragraph_format.first_line_indent = Cm(-0.30)
    bullet.paragraph_format.right_indent = Cm(0)
    bullet.paragraph_format.space_before = Pt(0)
    bullet.paragraph_format.space_after = Pt(1.15)
    bullet.paragraph_format.line_spacing = 1.08
    bullet.font.name = FONT_FAMILY
    bullet.font.size = Pt(10.6)
    for key in ("ascii", "hAnsi", "eastAsia", "cs"):
        bullet._element.rPr.rFonts.set(qn(f"w:{key}"), FONT_FAMILY)


def create_bullet_numbering(document: Document) -> int:
    numbering = document.part.numbering_part.element
    abstract_ids = [
        int(element.get(qn("w:abstractNumId")))
        for element in numbering.findall(qn("w:abstractNum"))
    ]
    num_ids = [
        int(element.get(qn("w:numId")))
        for element in numbering.findall(qn("w:num"))
    ]
    abstract_id = max(abstract_ids, default=0) + 1
    num_id = max(num_ids, default=0) + 1

    abstract = OxmlElement("w:abstractNum")
    abstract.set(qn("w:abstractNumId"), str(abstract_id))
    multi = OxmlElement("w:multiLevelType")
    multi.set(qn("w:val"), "singleLevel")
    abstract.append(multi)

    level = OxmlElement("w:lvl")
    level.set(qn("w:ilvl"), "0")
    for name, value in (
        ("w:start", "1"),
        ("w:numFmt", "bullet"),
        ("w:lvlText", BULLET_GLYPH),
        ("w:lvlJc", "left"),
    ):
        element = OxmlElement(name)
        element.set(qn("w:val"), value)
        level.append(element)

    paragraph_properties = OxmlElement("w:pPr")
    tabs = OxmlElement("w:tabs")
    tab = OxmlElement("w:tab")
    tab.set(qn("w:val"), "num")
    tab.set(qn("w:pos"), "295")
    tabs.append(tab)
    paragraph_properties.append(tabs)
    indent = OxmlElement("w:ind")
    indent.set(qn("w:left"), "295")
    indent.set(qn("w:hanging"), "170")
    paragraph_properties.append(indent)
    level.append(paragraph_properties)

    run_properties = OxmlElement("w:rPr")
    fonts = OxmlElement("w:rFonts")
    for key in ("ascii", "hAnsi", "eastAsia", "cs"):
        fonts.set(qn(f"w:{key}"), FONT_FAMILY)
    run_properties.append(fonts)
    bold = OxmlElement("w:b")
    bold.set(qn("w:val"), "1")
    run_properties.append(bold)
    for element_name in ("w:sz", "w:szCs"):
        size = OxmlElement(element_name)
        size.set(qn("w:val"), str(BULLET_SIZE_HALF_POINTS))
        run_properties.append(size)
    position = OxmlElement("w:position")
    position.set(qn("w:val"), str(SEPARATOR_RAISE_HALF_POINTS))
    run_properties.append(position)
    level.append(run_properties)
    abstract.append(level)
    numbering.append(abstract)

    num = OxmlElement("w:num")
    num.set(qn("w:numId"), str(num_id))
    reference = OxmlElement("w:abstractNumId")
    reference.set(qn("w:val"), str(abstract_id))
    num.append(reference)
    numbering.append(num)
    return num_id


def apply_numbering(paragraph, num_id: int) -> None:
    properties = paragraph._p.get_or_add_pPr()
    numbering = OxmlElement("w:numPr")
    level = OxmlElement("w:ilvl")
    level.set(qn("w:val"), "0")
    identifier = OxmlElement("w:numId")
    identifier.set(qn("w:val"), str(num_id))
    numbering.append(level)
    numbering.append(identifier)
    properties.insert(0, numbering)


def add_section(container, title: str) -> None:
    paragraph = container.add_paragraph(style="CV Section")
    run = paragraph.add_run(title.upper())
    set_run_font(run, 11.5, bold=True)
    add_bottom_border(paragraph)
    set_keep(paragraph, keep_next=True)


def add_entry_heading(
    container, title: str, dates: str, location: str | None = None,
    role: str | None = None,
) -> None:
    paragraph = container.add_paragraph(style="CV Entry")
    paragraph.paragraph_format.tab_stops.add_tab_stop(
        Cm(CONTENT_WIDTH_CM), WD_TAB_ALIGNMENT.RIGHT
    )
    title_run = paragraph.add_run(title)
    set_run_font(title_run, 11.2, bold=True)
    if location:
        location_run = paragraph.add_run(f", {location}")
        set_run_font(location_run, 11.0, GREY)
    if role:
        separator_run = paragraph.add_run(", ")
        set_run_font(separator_run, 10.5)
        role_run = paragraph.add_run(role)
        set_run_font(role_run, 10.9, italic=True)
    tab_run = paragraph.add_run("\t")
    set_run_font(tab_run, 11.0)
    date_run = paragraph.add_run(dates)
    set_run_font(date_run, 11.0, italic=True)
    set_keep(paragraph, keep_next=True)


def add_secondary(container, primary: str, location: str | None = None) -> None:
    paragraph = container.add_paragraph(style="CV Secondary")
    primary_run = paragraph.add_run(primary)
    set_run_font(primary_run, 10.9, italic=True)
    if location:
        separator = paragraph.add_run(" | ")
        set_run_font(separator, 10.8, GREY, italic=True)
        location_run = paragraph.add_run(location)
        set_run_font(location_run, 10.8, GREY, italic=True)
    set_keep(paragraph, keep_next=True)


def add_descriptor(container, text: str) -> None:
    paragraph = container.add_paragraph(style="CV Descriptor")
    run = paragraph.add_run(text)
    set_run_font(run, 10.2, GREY, italic=True)
    set_keep(paragraph, keep_next=True)


def add_bullet(container, text: str, num_id: int, *, keep_next: bool = False) -> None:
    paragraph = container.add_paragraph(style="CV Bullet")
    apply_numbering(paragraph, num_id)
    run = paragraph.add_run(text)
    set_run_font(run, 10.6)
    set_keep(paragraph, keep_next=keep_next)


def add_skill_bullet(container, label: str, details: str, num_id: int) -> None:
    paragraph = container.add_paragraph(style="CV Bullet")
    apply_numbering(paragraph, num_id)
    label_run = paragraph.add_run(f"{label}:")
    set_run_font(label_run, 10.6, bold=True)
    detail_run = paragraph.add_run(f" {details}")
    set_run_font(detail_run, 10.6)
    set_keep(paragraph)


def add_unbreakable_block(document: Document):
    table = document.add_table(rows=1, cols=1)
    table.alignment = WD_TABLE_ALIGNMENT.LEFT
    table.autofit = False
    table.columns[0].width = Cm(CONTENT_WIDTH_CM)
    properties = table._tbl.tblPr
    layout = OxmlElement("w:tblLayout")
    layout.set(qn("w:type"), "fixed")
    properties.append(layout)
    indent = OxmlElement("w:tblInd")
    indent.set(qn("w:w"), "0")
    indent.set(qn("w:type"), "dxa")
    properties.append(indent)
    borders = OxmlElement("w:tblBorders")
    for edge_name in ("top", "left", "bottom", "right", "insideH", "insideV"):
        edge = OxmlElement(f"w:{edge_name}")
        edge.set(qn("w:val"), "nil")
        borders.append(edge)
    properties.append(borders)

    row = table.rows[0]
    row._tr.get_or_add_trPr().append(OxmlElement("w:cantSplit"))
    cell = row.cells[0]
    cell.vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.TOP
    cell.width = Cm(CONTENT_WIDTH_CM)
    cell_properties = cell._tc.get_or_add_tcPr()
    margins = OxmlElement("w:tcMar")
    for side_name in ("top", "left", "bottom", "right"):
        side = OxmlElement(f"w:{side_name}")
        side.set(qn("w:w"), "0")
        side.set(qn("w:type"), "dxa")
        margins.append(side)
    cell_properties.append(margins)
    return cell


def finish_block(cell) -> None:
    if len(cell.paragraphs) > 1 and not cell.paragraphs[0].text:
        element = cell.paragraphs[0]._element
        element.getparent().remove(element)


def add_block_separator(document: Document) -> None:
    paragraph = document.add_paragraph()
    paragraph.paragraph_format.space_before = Pt(0)
    paragraph.paragraph_format.space_after = Pt(0)
    paragraph.paragraph_format.line_spacing = Pt(1)


def build_docx(profile: dict[str, Any], content: dict[str, Any], output: Path) -> None:
    document = Document()
    section = document.sections[0]
    section.page_width = Cm(21.0)
    section.page_height = Cm(29.7)
    section.top_margin = Cm(1.75)
    section.bottom_margin = Cm(1.45)
    section.left_margin = Cm(1.85)
    section.right_margin = Cm(1.85)
    section.header_distance = Cm(0)
    section.footer_distance = Cm(0)
    configure_styles(document)

    identity = profile["identity"]
    metadata = content["document"]
    document.core_properties.title = (
        f"{identity['name']} - CV - {metadata['company']} {metadata['role']}"
    )
    document.core_properties.author = identity["name"]
    document.core_properties.subject = "Curriculum Vitae"

    name = document.add_paragraph()
    name.alignment = WD_ALIGN_PARAGRAPH.CENTER
    name.paragraph_format.space_after = Pt(5)
    name.paragraph_format.line_spacing = 1.0
    name_run = name.add_run(identity["name"])
    set_run_font(name_run, 18, bold=True)
    set_keep(name, keep_next=True)

    contact = document.add_paragraph()
    contact.alignment = WD_ALIGN_PARAGRAPH.CENTER
    contact.paragraph_format.space_after = Pt(9)
    contact.paragraph_format.line_spacing = 1.0
    location = contact.add_run(identity["location"])
    set_run_font(location, 10.5)
    for key in ("portfolio", "linkedin", "phone", "email"):
        add_contact_separator(contact)
        item = identity[key]
        add_hyperlink(contact, item["label"], item["url"])
    set_keep(contact, keep_next=True)

    bullet_num_id = create_bullet_numbering(document)

    for index, education in enumerate(profile["education"]):
        block = add_unbreakable_block(document)
        if index == 0:
            add_section(block, "Education")
        add_entry_heading(
            block,
            education["institution"],
            education["dates"],
            education["location"],
        )
        add_secondary(block, education["degree"])
        details = education["details"]
        for detail_index, detail in enumerate(details):
            add_bullet(
                block,
                detail,
                bullet_num_id,
                keep_next=detail_index < len(details) - 1,
            )
        finish_block(block)
        add_block_separator(document)

    for index, entry in enumerate(content["professional_experience"]):
        block = add_unbreakable_block(document)
        if index == 0:
            add_section(block, "Professional Experience")
        add_entry_heading(block, entry["employer"], entry["dates"], role=entry["role"])
        if entry.get("descriptor"):
            add_descriptor(block, entry["descriptor"])
        bullets = entry["bullets"]
        for bullet_index, bullet in enumerate(bullets):
            add_bullet(
                block,
                bullet,
                bullet_num_id,
                keep_next=bullet_index < len(bullets) - 1,
            )
        finish_block(block)
        add_block_separator(document)

    for index, entry in enumerate(content["personal_experience"]):
        block = add_unbreakable_block(document)
        if index == 0:
            add_section(block, "Personal Experience")
        add_entry_heading(block, entry["title"], entry["dates"])
        bullets = entry["bullets"]
        for bullet_index, bullet in enumerate(bullets):
            add_bullet(
                block,
                bullet,
                bullet_num_id,
                keep_next=bullet_index < len(bullets) - 1,
            )
        finish_block(block)
        add_block_separator(document)

    add_section(document, "Hard Skills")
    for skill in content["hard_skills"]:
        add_skill_bullet(document, skill["label"], skill["details"], bullet_num_id)

    add_section(document, "Personal Interests")
    add_bullet(document, ", ".join(profile["interests"]), bullet_num_id)

    add_section(document, "Language Proficiency")
    languages = [
        f"{item['name']} ({item['level']})"
        for item in profile["language_policy"]["languages"]
    ]
    add_bullet(document, ", ".join(languages), bullet_num_id)

    output.parent.mkdir(parents=True, exist_ok=True)
    document.save(output)


def verify_docx_fonts(docx_path: Path) -> dict[str, Any]:
    namespace = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}
    attributes = tuple(
        f"{{{namespace['w']}}}{name}" for name in ("ascii", "hAnsi", "eastAsia", "cs")
    )
    errors: list[str] = []
    used_fonts: set[str] = set()
    with zipfile.ZipFile(docx_path) as archive:
        document_root = ET.fromstring(archive.read("word/document.xml"))
        numbering_root = ET.fromstring(archive.read("word/numbering.xml"))

    for run in document_root.findall(".//w:r", namespace):
        visible = "".join((node.text or "") for node in run.findall("w:t", namespace))
        if not visible:
            continue
        properties = run.find("w:rPr", namespace)
        fonts = properties.find("w:rFonts", namespace) if properties is not None else None
        assigned = {
            fonts.get(attribute)
            for attribute in attributes
            if fonts is not None and fonts.get(attribute)
        }
        if not assigned:
            errors.append(f"Visible DOCX text lacks an explicit font: `{visible}`")
        used_fonts.update(assigned)

    marker_fonts = None
    for level in numbering_root.findall(".//w:lvl", namespace):
        level_text = level.find("w:lvlText", namespace)
        if level_text is not None and level_text.get(f"{{{namespace['w']}}}val") == BULLET_GLYPH:
            marker_fonts = level.find("w:rPr/w:rFonts", namespace)
            break
    marker_assignment = {
        marker_fonts.get(attribute)
        for attribute in attributes
        if marker_fonts is not None and marker_fonts.get(attribute)
    }
    if marker_assignment != {FONT_FAMILY}:
        errors.append("CV bullet marker lacks an explicit EB Garamond assignment")
    used_fonts.update(marker_assignment)

    unexpected = sorted(used_fonts - {FONT_FAMILY})
    if unexpected:
        errors.append("Unexpected DOCX fonts: " + ", ".join(unexpected))
    if errors:
        raise ValueError("CV DOCX font validation failed:\n- " + "\n- ".join(errors))
    return {"fonts": sorted(used_fonts), "errors": []}


def export_pdf(docx_path: Path, pdf_path: Path) -> None:
    soffice = shutil.which("soffice") or shutil.which("libreoffice")
    if not soffice:
        raise RuntimeError("LibreOffice/soffice is required for PDF export")
    required_fonts = (
        "EBGaramond-Regular.ttf",
        "EBGaramond-Bold.ttf",
        "EBGaramond-RegularItalic.ttf",
        "EBGaramond-BoldItalic.ttf",
    )
    missing = [name for name in required_fonts if not (FONT_DIR / name).is_file()]
    if missing:
        raise RuntimeError("Missing bundled EB Garamond fonts: " + ", ".join(missing))

    with tempfile.TemporaryDirectory(prefix="cv-export-") as temp_name:
        temp = Path(temp_name)
        export_dir = temp / "export"
        home_dir = temp / "home"
        profile_dir = temp / "profile"
        cache_dir = temp / "font-cache"
        for directory in (export_dir, home_dir, profile_dir, cache_dir):
            directory.mkdir(parents=True, exist_ok=True)
        fontconfig = temp / "fonts.conf"
        fontconfig.write_text(
            "<?xml version=\"1.0\"?>\n"
            "<!DOCTYPE fontconfig SYSTEM \"fonts.dtd\">\n"
            "<fontconfig>\n"
            f"  <dir>{html.escape(str(FONT_DIR))}</dir>\n"
            f"  <cachedir>{html.escape(str(cache_dir))}</cachedir>\n"
            "</fontconfig>\n",
            encoding="utf-8",
        )
        environment = os.environ.copy()
        environment["FONTCONFIG_FILE"] = str(fontconfig)
        environment["HOME"] = str(home_dir)
        result = subprocess.run(
            [
                soffice,
                "--headless",
                f"-env:UserInstallation={profile_dir.as_uri()}",
                "--convert-to",
                "pdf",
                "--outdir",
                str(export_dir),
                str(docx_path),
            ],
            env=environment,
            capture_output=True,
            text=True,
            timeout=60,
        )
        generated = export_dir / f"{docx_path.stem}.pdf"
        if result.returncode != 0 or not generated.is_file():
            raise RuntimeError(
                "CV PDF export failed\n"
                f"stdout: {result.stdout.strip()}\n"
                f"stderr: {result.stderr.strip()}"
            )
        pdf_path.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(generated, pdf_path)


def normalize_text(value: str) -> str:
    normalized = re.sub(r"\s+", " ", value).strip()
    return re.sub(r"-\s+", "-", normalized)


def verify_pdf(
    pdf_path: Path,
    docx_path: Path,
    profile: dict[str, Any],
    content: dict[str, Any],
    qa_dir: Path,
    content_path: Path,
    profile_path: Path,
) -> dict[str, Any]:
    qa_dir.mkdir(parents=True, exist_ok=True)
    for stale in qa_dir.glob("page-*.png"):
        stale.unlink()

    reader = PdfReader(str(pdf_path))
    page_texts = [page.extract_text() or "" for page in reader.pages]
    extracted = "\n".join(page_texts)
    (qa_dir / "extracted.txt").write_text(extracted, encoding="utf-8")
    errors: list[str] = []
    docx_fonts = verify_docx_fonts(docx_path)

    max_pages = content["document"].get("max_pages")
    if max_pages is not None and len(reader.pages) > max_pages:
        errors.append(
            f"CV has {len(reader.pages)} pages; maximum is {max_pages}"
        )

    pdf_fonts: set[str] = set()
    unembedded: set[str] = set()
    for page in reader.pages:
        resources = page.get("/Resources", {})
        for reference in (resources.get("/Font", {}) if resources else {}).values():
            font = reference.get_object()
            base_font = str(font.get("/BaseFont", "")).lstrip("/")
            normalized_font = base_font.split("+", 1)[-1]
            if normalized_font:
                pdf_fonts.add(normalized_font)
            descriptors = []
            if font.get("/FontDescriptor"):
                descriptors.append(font["/FontDescriptor"].get_object())
            for descendant_reference in font.get("/DescendantFonts", []):
                descendant = descendant_reference.get_object()
                if descendant.get("/FontDescriptor"):
                    descriptors.append(descendant["/FontDescriptor"].get_object())
            if not descriptors or not any(
                descriptor.get(key) is not None
                for descriptor in descriptors
                for key in ("/FontFile", "/FontFile2", "/FontFile3")
            ):
                unembedded.add(normalized_font or base_font or "unknown")

    unexpected = sorted(font for font in pdf_fonts if not font.startswith(PDF_FONT_PREFIX))
    if unexpected:
        errors.append("Unexpected CV PDF fonts: " + ", ".join(unexpected))
    if unembedded:
        errors.append("Unembedded CV PDF fonts: " + ", ".join(sorted(unembedded)))

    required_text = [profile["identity"]["name"]]
    for education in profile["education"]:
        required_text.extend(education["details"])
    normalized_extracted = normalize_text(extracted)
    for required in required_text:
        if normalize_text(required) not in normalized_extracted:
            errors.append(f"Required text missing from CV PDF: `{required}`")
    for interest in profile["interests"]:
        if interest not in extracted:
            errors.append(f"Canonical interest missing from CV PDF: `{interest}`")
    for language in profile["language_policy"]["languages"]:
        label = f"{language['name']} ({language['level']})"
        if label not in extracted:
            errors.append(f"Canonical language missing from CV PDF: `{label}`")

    headings = (
        "EDUCATION",
        "PROFESSIONAL EXPERIENCE",
        "PERSONAL EXPERIENCE",
        "HARD SKILLS",
        "PERSONAL INTERESTS",
        "LANGUAGE PROFICIENCY",
    )
    positions = [extracted.find(heading) for heading in headings]
    if any(position < 0 for position in positions) or positions != sorted(positions):
        errors.append("CV PDF headings are missing or out of ATS reading order")

    normalized_pages = [normalize_text(text) for text in page_texts]
    entry_pages: dict[str, list[int]] = {}
    for section_name, entries in (
        ("PROFESSIONAL EXPERIENCE", content["professional_experience"]),
        ("PERSONAL EXPERIENCE", content["personal_experience"]),
    ):
        for index, entry in enumerate(entries):
            required_text = [
                entry.get("employer", ""),
                entry.get("role", ""),
                entry.get("title", ""),
                entry["dates"],
                entry.get("descriptor", ""),
                *entry["bullets"],
            ]
            required = [normalize_text(text) for text in required_text if text]
            matches = [
                page_index
                for page_index, page_text in enumerate(normalized_pages)
                if all(text in page_text for text in required)
            ]
            entry_pages[f"{section_name}:{index}"] = matches
            if not matches:
                errors.append(
                    f"CV experience entry is split across pages: `{required_text[0]}`"
                )
        first_pages = entry_pages.get(f"{section_name}:0", [])
        heading_pages = [
            index for index, page_text in enumerate(normalized_pages) if section_name in page_text
        ]
        if first_pages and not set(first_pages).intersection(heading_pages):
            errors.append(f"CV section heading is separated from `{section_name}`")

    document = pdfium.PdfDocument(str(pdf_path))
    for index, page in enumerate(document):
        page.render(scale=1.7).to_pil().save(qa_dir / f"page-{index + 1}.png")

    report = {
        "ok": not errors,
        "layout": "cv",
        "page_count": len(reader.pages),
        "max_pages": max_pages,
        "pdf": pdf_path.name,
        "pdf_sha256": file_hash(pdf_path),
        "docx": docx_path.name,
        "docx_sha256": file_hash(docx_path),
        "content": content_path.name,
        "content_sha256": file_hash(content_path),
        "profile": profile_path.name,
        "profile_sha256": file_hash(profile_path),
        "docx_fonts": docx_fonts["fonts"],
        "pdf_fonts": sorted(pdf_fonts),
        "all_pdf_fonts_embedded": not unembedded,
        "section_rule_eighth_points": SECTION_RULE_EIGHTH_POINTS,
        "bullet_size_half_points": BULLET_SIZE_HALF_POINTS,
        "bullet_raise_half_points": SEPARATOR_RAISE_HALF_POINTS,
        "experience_blocks_intact": not any("split across" in error for error in errors),
        "errors": errors,
    }
    (qa_dir / "validation.json").write_text(
        json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    if errors:
        raise ValueError("CV validation failed:\n- " + "\n- ".join(errors))
    return report



def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Build the EB Garamond CV from role-specific content and a candidate CV profile"
    )
    parser.add_argument("content", type=Path)
    parser.add_argument("--profile", type=Path, required=True, help="Candidate-specific CV profile JSON")
    parser.add_argument("--output-root", type=Path)
    parser.add_argument("--docx-only", action="store_true")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    content_path = args.content.resolve()
    profile_path = args.profile.resolve()
    output_root = (args.output_root or content_path.parent).resolve()
    profile = read_json(profile_path)
    content = read_json(content_path)
    validate_inputs(profile, content)

    docx_path = output_root / f"{CV_STEM}.docx"
    pdf_path = output_root / f"{CV_STEM}.pdf"
    qa_dir = output_root / "qa"

    with tempfile.TemporaryDirectory(prefix="cv-build-") as temp_name:
        temp_docx = Path(temp_name) / f"{CV_STEM}.docx"
        build_docx(profile, content, temp_docx)
        verify_docx_fonts(temp_docx)
        docx_path.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(temp_docx, docx_path)
        if not args.docx_only:
            export_pdf(temp_docx, pdf_path)

    print("DOCX: CV.docx")
    if args.docx_only:
        return

    report = verify_pdf(
        pdf_path,
        docx_path,
        profile,
        content,
        qa_dir,
        content_path,
        profile_path,
    )
    print("PDF: CV.pdf")
    print("QA: qa/")
    print(f"Validated: {report['page_count']} page(s)")


if __name__ == "__main__":
    main()
