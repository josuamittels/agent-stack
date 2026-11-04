# Cover Letter PDF Layout

Use this reference when the user requests PDF output. It records the Application System's letter design tokens and the bundled font asset.

## Page and type

- Page: A4, 595.3 × 841.9 pt.
- Left and right margins: 70.9 pt (25 mm).
- Top text position: 75 pt.
- Bottom margin: 70.9 pt.
- Font: bundled `fonts/EBGaramond-Regular.ttf`, EB Garamond Regular.
- Font size: 12 pt.
- Line leading: 19.2 pt.
- Paragraph spacing: 8 pt after each unit.
- Text colour: black.
- Body alignment: justified.
- Greeting, sign-off, and name: left aligned.
- Header, footer, page number, and contact block: none.

Do not reduce the font size to force overflow. The generator stops when a letter exceeds its configured page limit. Edit the content or increase the limit only when the user asks for a longer document.

## Typeface

The regular font is included under `fonts/` with the SIL Open Font License 1.1 in the same folder. The font's embedded metadata identifies the copyright as 2017 The EB Garamond Project Authors and the license as OFL 1.1. Preserve `OFL-1.1.txt` with the font when redistributing the skill. Do not modify the font file.

## Review

After generation, confirm the expected page count, extract the PDF text to check reading order and exact content, render every page at 150–200 dpi, and inspect each rendered page for clipping, missing glyphs, awkward breaks, or accidental blank pages. Report any inspection step that was unavailable.
