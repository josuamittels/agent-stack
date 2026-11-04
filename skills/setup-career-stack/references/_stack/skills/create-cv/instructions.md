---
name: "create-cv"
description: "Create evidence-backed, role-tailored CV content and a PDF in a defined EB Garamond layout from a professional career profile and target."
version: "1.0.0"
created: "2026-11-04"
updated: "2026-11-04"
author:
  - "Josua Mittelstaedt"
references: []
type: "skill"
status: "stable"
---

# Create CV

Create a role-relevant, evidence-backed CV from a supplied professional career profile and target. Deliver a content draft and a correctly formatted PDF in the defined EB Garamond layout. The skill carries its own templates, references, fonts, and PDF generator.

## Scope

Use for a new or revised, tailored CV when the user supplies a professional career profile context file (or its contents) and a target. A target can be a job description, vacancy, company and role, role family, or explicit positioning brief. The job description is useful but not required when another target gives enough direction. In a project with a root `AGENTS.md` and `staples/`, follow its career-workspace routing and compare approved staples before creating new content. For a request that only selects or reuses an existing CV without drafting new content, use that existing CV workflow instead.

### Boundaries

- Treat the supplied profile context as an input artifact. Do not name or invoke the workflow that produced it.
- Do not invent facts, dates, metrics, ownership, skills, or credentials. Preserve qualifiers and source status. Exclude unresolved conflicting claims; ask only when resolving one is necessary to produce a useful CV.
- Populate a task-specific CV profile from the supplied career context. Treat the bundled profile JSON as a mock template only; never use its placeholders in an exported CV.
- Do not create an opening profile or summary, a separate competencies section, or a recommendation appendix. Follow the section order below.
- A request to draft a CV authorizes local draft artifacts. Copy a delivery version only to a user-approved destination after approval of the exact content. Do not submit or send the CV to an employer.
- Keep the bundled font files within this private skill package. Do not publish or redistribute them without confirming their licences.

## Inputs

Require a professional career profile context file or supplied profile text, and a target. First check task attachments and conversation context for the profile file; accept a local path or pasted content as well. When working in a career application project, read its root `AGENTS.md` and prefer `references/career-context.md` as the profile. Ask for a missing required input only after checking available context. Preserve any requested language, page limit, role title, or output path; otherwise use the defaults below.

When the project has approved CVs under `staples/`, read their `MATCH.md` files and inspect any plausible staple against the target's requirements and the CV's actual evidence. Reuse a staple only when its match criteria and evidence fit the target without a material positioning or content change. If it fits, return it as the selected CV; when a final application copy is requested, follow the project's `AGENTS.md` naming and approval rules. If no staple fits or a material change is needed, continue with this skill to create a new target-specific CV. Do not use company name or industry alone as proof of fit, and do not silently edit a staple.

The package is self-contained. Its templates, fonts, references, and scripts are listed below with their purpose. Use only these bundled resources at runtime.

**Templates**

- `templates/cv-profile.example.json` is a mock schema for candidate identity/contact, education, languages, interests, and blocked terms. Copy it to the task output folder, populate it from verified profile context, and replace every bracket/example value before generation.
- `templates/cv-content.example.json` is the role-specific JSON structure for company/role metadata, experience entries, and grouped hard skills. Copy it to the task output folder and fill it for the target.

**Font assets**

- `assets/fonts/EBGaramond-Regular.ttf` supplies normal text.
- `assets/fonts/EBGaramond-Bold.ttf` supplies the name, section headings, entry titles, and bullet marker.
- `assets/fonts/EBGaramond-RegularItalic.ttf` supplies dates, degree lines, and descriptors.
- `assets/fonts/EBGaramond-BoldItalic.ttf` supplies bold italic emphasis.
- `assets/fonts/OFL-1.1.txt` carries the font software's redistribution license and attribution.

**References**

- `references/source-of-truth.md` defines evidence precedence, conflict handling, and claim limits.
- `references/cv-guidelines.md` defines bullet construction, tense, ownership verbs, chronology, and evidence density.
- `references/role-relevance.md` provides the optional evidence scoring model and role-family prompts. Use it when the evidence set needs prioritization.
- `references/ats-guidelines.md` covers selectable text, simple reading order, supported keywords, and extraction checks.
- `references/cv-layout.md` is the authoritative section order and visual specification.
- `references/font-usage.md` identifies the font faces and the package's redistribution boundary.
- `references/export-and-qa.md` explains rendered-page inspection and PDF checks.

**Scripts and runtime**

- `scripts/generate_cv_pdf.py` preflights the package and runs the bundled build script; it can copy a validated PDF only to a supplied, non-existing destination.
- `scripts/build_cv.py` builds the DOCX/PDF, extracts PDF text, renders pages, and writes machine-readable validation.
- `scripts/cv_support.py` supplies bundled asset paths, JSON loading, hashing, and schema checks.
- `scripts/requirements.txt` lists Python libraries. PDF export also requires LibreOffice/soffice, which the wrapper checks before writing output.

Do not call an external generator or copy assets from another system.
### Default Procedures

When task input is needed from the user, route the question through [ask-user-question](../ask-user-question/instructions.md) for preparation, delivery, and interpretation. First invoke [think-harder](../think-harder/instructions.md) when ambiguity, missing information, or competing interpretations may be resolved from context, relevant guidance, evidence, or a reasonable default. Skip Think Harder for direct permission or approval gates, explicitly requested interviews, and facts or preferences only the user can supply. Ask only about consequential unresolved items. Continue independent work and preserve approval requirements.

If any discipline is unavailable, perform it directly and report the fallback. Carry unresolved constraints forward and do not invent answers or pretend the dependency ran.

## Workflow

### 1. Establish the target and source of truth

Read the supplied career profile and target. If the workspace `AGENTS.md` applies, follow its application workflow. Identify the role, company (if known), output language, target audience, and explicit constraints. Use the profile as the source for career evidence and fixed CV fields. Create a task-specific `cv-profile.json` from `templates/cv-profile.example.json`, filling only verified identity, contact, education, language, and interest data. Leave the mock template unchanged. If a required fixed field is missing or conflicted, ask or omit it; do not export placeholders. Do not resolve a factual conflict by choosing the more impressive version.

Before drafting, compare relevant staples with the target when available. Record why a staple does or does not fit based on its match notes and evidence in the CV. Reuse a fitting staple without regenerating near-duplicate content. Continue the full generation workflow only when a new tailored CV is needed.

If no full job description is supplied, derive fit only from the stated target. Label assumptions and limit the job-fit assessment to evidence available in that target.

### 2. Rank criteria and map evidence

Derive and rank five to eight meaningful selection criteria from the target where possible. Map each criterion to specific experiences, projects, achievements, and skills in the profile. Separate proven evidence from partial evidence and gaps. Use exact target terminology only where the profile supports it.

Use the five-dimension role-relevance framework and its score bands when the evidence set is large; favor coverage across distinct criteria over repeated proof of one strength. Select evidence for a coherent role-specific CV. Order dated entries in reverse chronological order within Education, Professional Experience, and Personal Experience; do not reorder entries by relevance. Put strongest relevant proof early through bullet selection and density. Keep no more than four bullets per experience entry, with fewer where the evidence warrants. Do not add filler to reach a page count.

### 3. Draft strict CV content

Create `cv-content.json` from `templates/cv-content.example.json` and `cv-profile.json` from `templates/cv-profile.example.json`. Keep role-specific content in the content file; the populated CV profile supplies identity, contact, education, interests, and languages. Never export the profile template itself.

Apply [Write](../write/instructions.md) to the CV prose, including experience bullets and skill descriptions. Follow the user's requested language and keep the evidence and structure rules below authoritative for CV content.

Use this section order without additions:

1. Education
2. Professional Experience
3. Personal Experience
4. Hard Skills
5. Personal Interests
6. Language Proficiency

Keep the defined CV structure strict:

- Do not add an opening profile, summary, objective, or competencies section.
- Keep Professional Experience and Personal Experience separate. Use official employer and role titles. Do not add location metadata to experience headings. Use a short company descriptor only when the employer is unfamiliar and the descriptor aids comprehension.
- Use one functional title per Personal Experience entry. Do not expose individual project names; describe independent work and products generically, with one bullet per distinct project where grouped.
- Group Hard Skills by related tool family and state the purpose or output supported by each family. Do not use a flat keyword list.
- Keep canonical interests and languages unchanged from the selected CV profile. Use only the allowed language proficiency labels in `references/cv-layout.md`.
- Use a concise evidence bullet structure: action + object/problem + method/scope + result, including only supported elements. Use one principal action per bullet, concrete opening verbs, accurate ownership, and numbers with their original qualifiers. Default to British English unless the requested/target language indicates otherwise. Target 18–28 words and no more than two rendered lines where the meaning remains intact.
- Use `GPA` without modifiers. Keep education entries, exchange study, country metadata, dates, and supporting bullets as defined in `references/cv-layout.md`. Format date ranges with spaced en dashes.

Show the user the content draft or a compact, complete text preview and retain `cv-content.json` before final layout. A request for a PDF draft authorizes a local first-draft PDF. For a final/delivered CV, wait for the user to approve the exact content before final export and copy it only to the approved destination.

### 4. Generate the CV PDF with the bundled script

Use a user-selected output folder and set `document.max_pages` to `null` unless the user explicitly sets a limit. The generator names the files `CV.docx` and `CV.pdf`. Keep `cv-profile.json`, `cv-content.json`, and generated files together. Check the selected output folder before generation; do not overwrite an existing CV artifact.

Run the bundled entrypoint; it preflights bundled fonts, references, templates, scripts, Python modules, and the PDF export tool, then invokes the bundled build script. That script is the layout authority. Do not hand-build or restyle the PDF.

For a local draft, run:

```bash
python /path/to/create-cv/scripts/generate_cv_pdf.py --content "/path/to/cv-output/cv-content.json" --profile "/path/to/cv-output/cv-profile.json" --output-root "/path/to/cv-output"
```

The script requires the populated CV profile explicitly and does not copy a delivery version by default. It creates `CV.docx`, `CV.pdf`, and QA artifacts in `qa/` under the output root. It rejects the bundled mock profile while any placeholders remain.

After the user approves the exact content and requests a delivery copy, specify a new destination file with `--copy-to`, for example:

```bash
python /path/to/create-cv/scripts/generate_cv_pdf.py --content "/path/to/cv-output/cv-content.json" --profile "/path/to/cv-output/cv-profile.json" --output-root "/path/to/cv-output" --copy-to "/path/to/delivery/CV.pdf"
```

The script refuses to overwrite an existing delivery file. If a dependency or bundled asset is missing, report it; do not bypass preflight or silently substitute fonts.

### 5. Verify and assess fit

Read `qa/validation.json` and require `ok: true`, `layout: "cv"`, PDF fonts limited to embedded `EBGaramond-*` faces, `all_pdf_fonts_embedded: true`, and `experience_blocks_intact: true`. Read `qa/extracted.txt`, inspect every current page render at 100%, and confirm A4 portrait, exact section order, intact entries, readable bullets, no clipping or accidental blank pages, and text extraction beginning with the candidate's name and contact details.

If any check fails, repair the content or generator issue and regenerate. Do not present an unverified or malformed file as correctly formatted. If visual inspection or PDF validation is unavailable, report that limitation clearly.

After validation, compare the final rendered CV with the target. Save `qa/job-fit-evaluation.md` with each ranked criterion rated `Strong`, `Partial`, or `Gap`, the actual CV evidence, an overall fit verdict, material limitations, and the likely hiring-manager concern. Do not infer fit from keyword presence alone.

### 6. Validate implementation

When invoked as a helper, return to the owning workflow without separate evaluation. For a skill with meaningful, deterministic, task-specific checks, invoke [Spawn Evals](../spawn-evals/instructions.md) once with a structured invocation record containing the original request, resolved constraints and their source, complete UTF-8 outputs, and machine-readable evidence. Its objective package in `src/evals/create-cv/` defines only those checks. Report PASS, FAIL, or NOT PASSED — UNVERIFIED with the failing or unavailable verification steps. Do not use model judges, sub-agents, qualitative assessments, weighted scores, or synthetic scenarios. If no package exists for an objectively checkable skill, report NOT PASSED — UNVERIFIED; do not create one during an ordinary skill invocation. If no meaningful objective check is possible for this skill, omit this entire validation section and all Spawn Evals references from the skill.

## Output

Return the content draft and links to `cv-profile.json`, `cv-content.json`, `CV.docx`, and `CV.pdf`. If you reused a staple, link the selected staple and its `MATCH.md` instead, state why its existing evidence fits, and do not imply that you generated new files. When a delivery copy was approved, also link that file. Include the job-fit assessment, a concise strengths/gaps summary, unresolved facts or verification limits, page count, and whether PDF validation and visual inspection completed. Do not expose internal evidence tags in the CV.
