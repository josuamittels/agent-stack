# CV Layout Specification

This document defines the CV page design and content presentation used by the `create-cv` skill.

## Page and hierarchy

- A4 portrait, one column, approximately 18-19 mm side margins.
- Centred name and contact line on page 1 only.
- Section order remains Education, Professional Experience, Personal Experience, Hard Skills, Personal Interests, Language Proficiency.
- Section headings are uppercase EB Garamond Bold with the same 1.75 pt black underline throughout this layout.
- Institution/employer/title is bold on the left; education countries follow institution names in grey after a comma; do not add city metadata unless it is part of the official institution name; the date range is italic and right-aligned on the same line.
- Degree appears in italic on the following line. Professional roles sit beside the employer, separated by a comma with no preceding space, on the dated title line and must not wrap.
- Optional company descriptors appear as a restrained grey italic line.
- Every entry and its bullets must remain on one page.

## Typography

- Family: EB Garamond, using the four bundled faces described in `font-usage.md`.
- Name: Bold, 18 pt.
- Contact: Regular, approximately 10.5 pt; links retain the established blue.
- Section heading: Bold, 11.5 pt.
- Institution/employer/title: Bold, approximately 11.2 pt.
- Date and degree line: Italic, approximately 10.8-11 pt.
- Position entries omit countries and other location metadata. Professional headings keep employer, role, and date on one line. Personal Experience entries use the dated heading without a secondary location line.
- Descriptor: Regular Italic, approximately 10.2 pt, grey.
- Bullet text: Regular, approximately 10.6 pt with compact but readable leading.
- Bullet marker: a small raised period in 10 pt EB Garamond Bold, positioned consistently with the bullet text.

## ATS and consistency

- Use real numbering and explicit tab stops; no text boxes, icons, ratings, columns, or layout-only floating objects.
- Use `GPA` without modifiers.
- Render home degrees and exchange semesters as separate education entries. Each entry places its grey country directly after the institution name with a comma and receives its own degree/exchange label, dates, `GPA: …` bullet, and `Notable Courses: …` bullet; add `Activities: …` after courses where supplied. Honours stay on the applicable GPA line.
- Keep canonical language and interest lines unchanged from the populated CV profile.
- Use one `cv-content.json`; formatting must not create a second content source.
- The standalone PDF may contain only embedded EB Garamond faces.

## Outputs

- Editable source: `CV.docx` in the selected output folder.
- PDF: `CV.pdf` in the selected output folder.
- Optional delivery file: `CV.pdf` at the user-approved destination.
- QA: `qa/`.
- Deliver the CV only; do not append recommendations.
