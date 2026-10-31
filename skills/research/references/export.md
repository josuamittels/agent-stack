---
name: "research-export"
description: "Deterministic Research export commands, portable content requirements, dependencies, and Word/PDF visual verification."
version: "0.1.0"
created: "2026-10-30"
updated: "2026-10-30"
author:
  - "Josua Mittelstaedt"
references:
  - "Pandoc"
  - "The Document Foundation"
type: "reference"
status: "experimental"
---

# Research export requirements

Read for requested files. Use compiled report.md as the canonical export input. Chat displays that compiled text without another drafting pass. These conversions use existing local executables and never call a model or download a style, font, asset or converter.

## Explicit conversion commands

These paths are illustrative. Run from the repository root with the actual project/output locations:

```sh
python skills/research/scripts/research.py export --input /private/tmp/research-project/report.md --format md --output /private/tmp/research-project/output/report.md --project /private/tmp/research-project
python skills/research/scripts/research.py export --input /private/tmp/research-project/report.md --format latex --output /private/tmp/research-project/output/report.tex --project /private/tmp/research-project
python skills/research/scripts/research.py export --input /private/tmp/research-project/report.md --format docx --output /private/tmp/research-project/output/report.docx --project /private/tmp/research-project
```

For PDF, first use the host's dependency lookup to resolve its bundled LibreOffice executable. Pass that actual absolute path with `--soffice`:

```text
python skills/research/scripts/research.py export --input <project>/report.md --format pdf --output <project>/output/report.pdf --project <project> --soffice <absolute-bundled-soffice-path>
```

PDF always follows Pandoc → temporary DOCX → bundled LibreOffice → PDF, with an isolated temporary LibreOffice profile. Temporary conversion files are cleaned up. No standalone TeX engine is needed. LaTeX export emits standalone editable .tex with already rendered citations and references; it does not promise PDF compilation or require BibTeX. Optional `--reference-doc /absolute/path/reference.docx` controls Word styling for both DOCX and PDF. Retain the same styling document for consistent Word/PDF layout.

For a standalone Markdown document still containing citation keys, pass `--bibliography /absolute/path/csl.json` and `--style apa` or a local CSL path. Already compiled report.md needs neither option. The CLI rejects a supplied bibliography with no unresolved citation keys to avoid accidental duplicate reference generation.

## Supported content and failure behavior

Use Markdown headings, ordinary text, lists, links, footnotes, Pandoc tables, math and local PNG/JPEG images. Retain image captions/alt text. Refer to local images relative to the input Markdown; their existence is checked before conversion. Markdown/LaTeX exports copy image bytes into a companion asset folder and rewrite references. Word/PDF embed assets. Keep that asset folder with a text export when moving it.

Raw HTML/TeX, remote/data/file-URL images, unfilled placeholders, missing images and unsupported image types fail explicitly. Convert required vector/other assets separately through an authorized tool before export; do not silently drop them. Mathematical Markdown is supported even though raw TeX blocks are not. Ordinary HTTPS reference links remain links; they are not downloaded.

The helper asks Pandoc to fail on warnings, checks output signatures and verifies that generated Word content retains table/math structures and image media. These checks cannot establish perfect layout, mathematical equivalence or preservation of every semantic detail. Re-render and inspect the actual outputs before delivery.

## Visual and content verification

For every requested Word/PDF file, use available host document/PDF rendering tools to render all pages to images and inspect them. Verify headings, Unicode glyphs, equations, table borders/wrapping, image visibility, citation locators and references. Compare section order and distinctive content against report.md. Check clipping, overlap and missing content. This review is separate from offline conversion and can require model-assisted inspection.

On a desktop host, use its bundled runtime and LibreOffice paths rather than hard-coding this machine's paths into the skill. If rendering is unavailable, report visual verification as pending/unverified; do not silently claim the format is delivery-ready.

After actual inspection, update the matching exports.json entry with `visual_review: "complete"` and a nonempty `visual_review_evidence` list describing page images inspected and observed results. Keep the generated input/output hashes unchanged. If the file is regenerated, its new receipt resets visual review to pending. Standalone exports without a project keep the same review annotation in the `.receipt.json` companion.

## Provenance and limits

Every export receipt records source/output hashes, backend, tool version, detected tables/math/images, asset paths and review status. Re-export after report changes. Missing tools return unavailable; the caller reports the missing prerequisite and still delivers any other requested format that completed honestly. Preserve Markdown and LaTeX sources when PDF/Word cannot be produced. Do not install tools or change backends automatically.

The [Pandoc manual](https://pandoc.org/MANUAL.html) is the primary fallback for unsupported syntax or changed converter behavior. The local CLI reference owns routine commands, so ordinary exports should not require rediscovering the conversion procedure.
