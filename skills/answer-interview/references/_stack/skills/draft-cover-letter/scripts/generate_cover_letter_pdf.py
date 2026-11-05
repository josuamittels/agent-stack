#!/usr/bin/env python3
"""Generate a cover-letter PDF using the bundled EB Garamond layout."""

from __future__ import annotations

import argparse
import json
import os
import shutil
import sys
import tempfile
from pathlib import Path
from xml.sax.saxutils import escape


def require_working_directory(path):
    scripts = Path(__file__).resolve().parents[2] / "compose-career-profile" / "scripts"
    if str(scripts) not in sys.path:
        sys.path.insert(0, str(scripts))
    from career_workspace import require_working_directory as check
    return check(path)


REQUIRED_FIELDS = (
    "greeting",
    "opening",
    "high_level_content",
    "experience",
    "motivation",
    "call_to_action",
    "sign_off",
    "name",
)


class PageLimitError(RuntimeError):
    """Raised when the PDF needs more than the configured page limit."""


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate an A4 cover-letter PDF in the bundled EB Garamond layout."
    )
    parser.add_argument("input_json", type=Path, help="UTF-8 JSON with the required letter fields")
    parser.add_argument("output_pdf", type=Path, help="Destination PDF path")
    parser.add_argument(
        "--font",
        type=Path,
        help="TrueType font file; defaults to the skill's bundled EB Garamond Regular font",
    )
    parser.add_argument(
        "--max-pages",
        type=int,
        default=1,
        help="Maximum number of pages (default: 1)",
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Replace an existing destination PDF",
    )
    return parser.parse_args()


def read_letter(path: Path) -> dict[str, str | list[str]]:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        raise ValueError(f"Cannot read UTF-8 JSON input {path}: {exc}") from exc
    if not isinstance(data, dict):
        raise ValueError("Input JSON must be an object containing the letter fields.")

    fields = ("greeting", "sign_off", "name") if "paragraphs" in data else REQUIRED_FIELDS
    missing = [field for field in fields if field not in data]
    if missing:
        raise ValueError("Missing required field(s): " + ", ".join(missing))

    letter: dict[str, str | list[str]] = {}
    for field in fields:
        value = data[field]
        if not isinstance(value, str) or not value.strip():
            raise ValueError(f"Field '{field}' must be a non-empty string.")
        letter[field] = value.strip()
    if "paragraphs" in data:
        paragraphs = data["paragraphs"]
        if not isinstance(paragraphs, list) or not paragraphs or not all(isinstance(x, str) and x.strip() for x in paragraphs):
            raise ValueError("paragraphs must be a non-empty string list")
        letter["paragraphs"] = [x.strip() for x in paragraphs]
    return letter


def paragraph_markup(text: str) -> str:
    """Escape user text for ReportLab Paragraph XML and preserve line breaks."""
    return "<br/>".join(escape(line) for line in text.splitlines())


def make_canvas_class(max_pages: int):
    from reportlab.pdfgen.canvas import Canvas

    class PageLimitedCanvas(Canvas):
        def __init__(self, *args, **kwargs):
            self.page_limit = max_pages
            self.pages_written = 0
            kwargs.setdefault("initialFontName", "EBGaramond")
            super().__init__(*args, **kwargs)

        def showPage(self):
            self.pages_written += 1
            if self.pages_written > self.page_limit:
                raise PageLimitError(
                    f"The letter exceeds the {self.page_limit}-page limit. "
                    "Shorten the content or set a higher --max-pages value."
                )
            super().showPage()

    return PageLimitedCanvas


def create_pdf(letter: dict[str, str | list[str]], output_path: Path, font_path: Path, max_pages: int) -> None:
    require_working_directory(output_path.parent)
    try:
        from reportlab.lib.colors import black
        from reportlab.lib.enums import TA_JUSTIFY, TA_LEFT
        from reportlab.lib.pagesizes import A4
        from reportlab.lib.styles import ParagraphStyle
        from reportlab.lib.units import mm
        from reportlab.pdfbase import pdfmetrics
        from reportlab.pdfbase.ttfonts import TTFont
        from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer
    except ImportError as exc:
        raise RuntimeError(
            "ReportLab is required. Install the skill's dependency from requirements.txt."
        ) from exc

    if not font_path.is_file():
        raise FileNotFoundError(f"Font file not found: {font_path}")

    font_name = "EBGaramond"
    try:
        pdfmetrics.registerFont(TTFont(font_name, str(font_path)))
    except Exception as exc:
        raise ValueError(f"Cannot load TrueType font {font_path}: {exc}") from exc

    body = ParagraphStyle(
        "LetterBody",
        fontName=font_name,
        fontSize=12,
        leading=19.2,
        alignment=TA_JUSTIFY,
        textColor=black,
        spaceAfter=8,
        splitLongWords=1,
    )
    left = ParagraphStyle(body.name + "Left", parent=body, alignment=TA_LEFT)

    document = SimpleDocTemplate(
        str(output_path),
        pagesize=A4,
        leftMargin=25 * mm,
        rightMargin=25 * mm,
        topMargin=75,
        bottomMargin=25 * mm,
        title="Cover Letter",
        author=letter["name"],
        allowSplitting=1,
    )
    paragraphs = letter.get("paragraphs") or [letter[key] for key in ("opening", "high_level_content", "experience", "motivation", "call_to_action")]
    story = [Paragraph(paragraph_markup(letter["greeting"]), left), Spacer(1, 8)]
    story.extend(Paragraph(paragraph_markup(text), body) for text in paragraphs)
    story.extend([Spacer(1, 4), Paragraph(paragraph_markup(letter["sign_off"]), left), Paragraph(paragraph_markup(letter["name"]), left)])

    canvas_class = make_canvas_class(max_pages)
    document.build(story, canvasmaker=canvas_class)


def main() -> int:
    args = parse_args()
    if args.max_pages < 1:
        print("Error: --max-pages must be at least 1.", file=sys.stderr)
        return 2

    skill_root = Path(__file__).resolve().parents[1]
    font_path = args.font or skill_root / "references" / "fonts" / "EBGaramond-Regular.ttf"
    output_path = args.output_pdf.expanduser().resolve()

    if output_path.suffix.lower() != ".pdf":
        print("Error: output path must end in .pdf.", file=sys.stderr)
        return 2
    if output_path.exists() and not args.overwrite:
        print(
            f"Error: output already exists: {output_path}. Choose another path or pass --overwrite.",
            file=sys.stderr,
        )
        return 2

    try:
        require_working_directory(args.output_pdf.expanduser().absolute().parent)
        letter = read_letter(args.input_json.expanduser())
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with tempfile.NamedTemporaryFile(
            prefix=f".{output_path.stem}.",
            suffix=".partial.pdf",
            dir=output_path.parent,
            delete=False,
        ) as temp_file:
            temp_path = Path(temp_file.name)
        try:
            create_pdf(letter, temp_path, font_path.expanduser(), args.max_pages)
            if args.overwrite:
                os.replace(temp_path, output_path)
            else:
                # Exclusive creation prevents replacing a destination that appeared
                # while generation was in progress, including on cloud-backed folders.
                created_destination = False
                try:
                    with output_path.open("xb") as destination:
                        created_destination = True
                        with temp_path.open("rb") as source:
                            shutil.copyfileobj(source, destination)
                except Exception:
                    if created_destination:
                        output_path.unlink(missing_ok=True)
                    raise
                temp_path.unlink()
        except Exception:
            temp_path.unlink(missing_ok=True)
            raise
    except (OSError, ValueError, RuntimeError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1

    print(output_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
