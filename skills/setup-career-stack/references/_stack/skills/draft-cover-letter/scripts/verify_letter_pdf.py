#!/usr/bin/env python3
"""Compare a letter PDF to its input, inspect fonts, and render every page."""
import argparse
import hashlib
import json
from pathlib import Path
from generate_cover_letter_pdf import read_letter, require_working_directory


def verify(pdf, source, output, max_pages=1):
    require_working_directory(output)
    from pypdf import PdfReader
    from pypdf.generic import ContentStream
    import pypdfium2 as pdfium
    if pdf.resolve().parent != source.resolve().parent:
        raise ValueError("Keep the letter input JSON beside the PDF for reproducible QA and delivery")
    letter = read_letter(source)
    body = letter.get("paragraphs") or [letter[key] for key in ("opening", "high_level_content", "experience", "motivation", "call_to_action")]
    expected = "\n".join([letter["greeting"], *body, letter["sign_off"], letter["name"]])
    reader = PdfReader(str(pdf))
    text = "\n".join(page.extract_text() or "" for page in reader.pages)
    output.mkdir(parents=True, exist_ok=False)
    (output / "extracted.txt").write_text(text, encoding="utf-8")
    fonts, unembedded = set(), set()
    a4 = True
    for page in reader.pages:
        a4 = a4 and abs(float(page.mediabox.width) - 595.276) < 1 and abs(float(page.mediabox.height) - 841.89) < 1
        resources = page.get("/Resources", {})
        current, stack, used = None, [], set()
        for operands, operation in ContentStream(page.get_contents(), reader).operations:
            if operation == b"q":
                stack.append(current)
            elif operation == b"Q":
                current = stack.pop() if stack else None
            elif operation == b"Tf":
                current = operands[0]
            elif operation in (b"Tj", b"TJ", b"'", b'"') and current is not None:
                used.add(current)
        for key in used:
            font = resources["/Font"][key].get_object()
            name = str(font.get("/BaseFont", "")).lstrip("/").split("+", 1)[-1]
            fonts.add(name)
            descriptors = [font["/FontDescriptor"].get_object()] if font.get("/FontDescriptor") else []
            for ref in font.get("/DescendantFonts", []):
                descendant = ref.get_object()
                if descendant.get("/FontDescriptor"):
                    descriptors.append(descendant["/FontDescriptor"].get_object())
            if not any(d.get(k) for d in descriptors for k in ("/FontFile", "/FontFile2", "/FontFile3")):
                unembedded.add(name)
    errors = []
    if " ".join(text.split()) != " ".join(expected.split()):
        errors.append("Extracted text differs from input")
    if not 1 <= len(reader.pages) <= max_pages:
        errors.append("Page limit violated")
    if not a4:
        errors.append("PDF is not A4 portrait")
    if not fonts or any(not x.startswith("EBGaramond") for x in fonts) or unembedded:
        errors.append("Unexpected or unembedded fonts")
    document = pdfium.PdfDocument(str(pdf))
    for index, page in enumerate(document):
        page.render(scale=2.5).to_pil().save(output / f"page-{index+1}.png")
    report = {"ok": not errors, "page_count": len(reader.pages), "pdf_sha256": hashlib.sha256(pdf.read_bytes()).hexdigest(),
              "input": source.name, "input_sha256": hashlib.sha256(source.read_bytes()).hexdigest(), "fonts": sorted(fonts), "all_fonts_embedded": not unembedded,
              "text_matches": " ".join(text.split()) == " ".join(expected.split()), "a4_portrait": a4, "errors": errors}
    (output / "validation.json").write_text(json.dumps(report, indent=2) + "\n")
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("pdf", type=Path)
    parser.add_argument("input_json", type=Path)
    parser.add_argument("qa_directory", type=Path)
    parser.add_argument("--max-pages", type=int, default=1)
    args = parser.parse_args()
    try:
        if args.max_pages < 1:
            raise ValueError("--max-pages must be positive")
        result = verify(args.pdf, args.input_json, args.qa_directory, args.max_pages)
        print(json.dumps(result))
        return 0 if result["ok"] else 1
    except (ImportError, OSError, ValueError) as exc:
        parser.exit(2, f"Letter QA unavailable: {exc}\n")


if __name__ == "__main__":
    raise SystemExit(main())
