# PDF export and quality checks

Keep approved content unchanged while applying the CV layout. Use the bundled script entry point and fonts rather than manually rebuilding the design.

## Build and inspect

Keep `qa/`, JSON, DOCX, and draft PDFs outside final application folders. Use the career workspace’s `work/<application-folder>/<revision>/` or a staple working folder. Temporary QA is also allowed outside application folders. The generator rejects paths in `applications/` and paths below a folder containing `job.md`. Deliver only the reviewed final PDF.

1. Run `scripts/generate_cv_pdf.py` to build the editable DOCX, export the PDF, extract text, validate fonts and structure, and render every page.
2. Read `qa/validation.json` and `qa/extracted.txt`.
3. Inspect every rendered `qa/page-*.png` at 100%.
4. Confirm the PDF is A4 portrait, has no accidental blank pages, starts in extraction order with the candidate's name and any supplied, externally permitted contact details, embeds EB Garamond faces, and has clickable visible links.
5. Check for clipped text, missing glyphs, awkward breaks, widows/orphans, split experience entries, and inconsistent spacing. Fix content selection or layout through the generator; do not shrink below the cv specification to force a page limit.
6. Retain `cv-content.json`, `CV.docx`, `CV.pdf`, and `qa/` together.

## Fidelity priorities

1. Page geometry and margins.
2. Font family and weight.
3. Reading order and hierarchy.
4. Line and paragraph rhythm.
5. Rules, colours, alignment, and link treatment.
6. Exact line breaks only when they preserve content and ATS parsing.
