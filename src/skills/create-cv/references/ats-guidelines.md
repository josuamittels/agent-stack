# ATS Guidelines

## Structure

- Use a single reading column.
- Use clear headings: `Education`, `Professional Experience`, `Personal Experience`, `Hard Skills`, `Personal Interests`, and `Language Proficiency`. Do not add a standalone `Competencies` section; surface those terms in experience bullets where evidence supports them.
- Put dates, employers, and titles in selectable text. Omit countries and other location metadata from position headers. Personal Experience entries intentionally use one functional title plus selectable grey date metadata, without a secondary title.
- Avoid text boxes, tables used for layout, icons, charts, ratings, photos, and decorative sidebars.
- Use simple bullet characters and consistent indentation.
- Keep contact links visible as text, not icon-only.

## Keywords

Mirror exact job-description terminology only when supported by evidence. Use both common and specific terms when helpful, for example `business intelligence (Looker)` or `product discovery (stakeholder interviews, behavioural data)`.

Do not:

- copy whole requirement phrases;
- add a skill because it appears in the JD;
- repeat a keyword unnaturally;
- hide keywords in white text or metadata.

## Parsing checks

After PDF export:

1. Extract text from the PDF.
2. Confirm name, titles, employers, dates, bullets, skills, and links appear in the intended order.
3. Search for missing glyphs and broken ligatures.
4. Confirm no line is reordered because of multiple columns or floating objects.
5. Confirm the file is not image-only.

## File and metadata

- PDF is default unless the portal requests DOCX.
- If delivery is requested, save the file as `CV.pdf` in the user-approved destination.
- Set a sensible document title and remove stale template metadata.
- Do not password-protect the CV.

## Fixed consistency rules

- Use `GPA` for every academic average, without modifiers.
- Use only `native`, `fluent`, `prof. working`, `lim. working`, `A1`, `A2`, `B1`, `B2`, `C1`, `C2`, or `basic` for language proficiency.
- Keep the canonical language and interest lines identical to the populated task-specific CV profile.
- Generate DOCX/PDF through the bundled build script so layout, fonts, and reading-order validation stay consistent.

## Content checks ATS cannot perform

Passing extraction is necessary but not sufficient. Human reviewers still need a clear top-third story, credible scope, readable density, and visible fit. Never sacrifice credibility or readability for keyword count.
