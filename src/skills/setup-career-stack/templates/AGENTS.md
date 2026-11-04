# Career Application Workspace

This project organizes career context, reusable CVs, and job applications. Follow these instructions whenever work in this project relates to a job search or application, even when the user does not name a skill.

## Workspace map

- `applications/`: one folder per application, named `<company>_<job>_<runningnumber>`; store `job.md`, the approved final `CV.pdf`, and optional approved `Motivation_Letter.pdf` here.
- `references/career-context.md`: durable career profile and source of truth for experience, skills, motivation, and preferences.
- `references/professional-voice-profile.md`: optional personalized letter voice profile. When present, it takes priority over the bundled profile in Draft Cover Letter.
- `references/application-answer-voice-profile.md`: optional personalized answer voice profile. When present, it takes priority over the bundled profile in Answer Interview.
- `staples/`: pre-generated, approved CVs grouped by materially distinct role family. Each staple folder contains `CV.pdf`, `MATCH.md`, Create CV source files, and QA evidence.

Do not treat a generated draft as an approved final. Do not submit, email, or upload applications. Never invent career facts or claims.

## Route career requests automatically

Read the relevant skill instructions from the available Agent Stack career skills. Use the host's supported skill invocation when available; otherwise read and apply the instructions directly. Do not claim a skill ran when it was not separately invoked.

**Route every employer question that needs a candidate-written answer to `answer-interview`.** This includes free-text questions in application forms, screening questionnaires, and interview prompts, whether the user supplies one question or a full set. Apply this rule even when the questions arrive as part of a broader new-application or CV request; route CV and letter work to their own skills separately. Pass the exact question text, target job description, relevant career context, language, and any word or character limits.

1. **Career profile missing or needs substantial update:** use `compose-career-profile`. Save the resulting profile as `references/career-context.md`.
2. **New application or request for a CV:** read the career context and target job description or company/role profile. For a specific application with a full job description, create or reuse its numbered folder and archive the complete posting as `job.md` in plain Markdown before preparing or selecting a CV. Compare the target with every relevant staple's `MATCH.md` and actual CV. Ask for a missing target only when necessary. If a staple fits its stated scope and its evidence covers the target, use that approved PDF. Otherwise use `create-cv` to make a role-specific CV and assess it against the target. Get approval of exact CV content before placing a final PDF in `applications/`.
3. **Cover or motivation letter requested:** use `draft-cover-letter`, with the career context, target details, and any user-provided employer context. For a specific application with a full job description, archive the complete posting as `job.md` in the matching numbered application folder. A letter is optional; do not create one unless requested. Save an approved PDF as `Motivation_Letter.pdf` in that folder.
4. **Feedback after a letter:** revise the letter. Apply immediate, application-specific feedback to that letter. Preserve reusable writing preferences in `references/professional-voice-profile.md`, scoped as narrowly as the feedback requires. Create the file from the available bundled profile through `compose-voice-profile` when needed. Once the project profile exists, it takes priority over the Draft Cover Letter skill's bundled voice reference. Do not store career facts in a voice profile.
5. **Application-form, screening, or interview question:** use `answer-interview` for each employer question requiring a candidate response. Return direct, copy-ready answers in chat and include exact word or character counts when limits apply.
6. **Feedback after an answer:** revise the answer. Apply immediate, application-specific feedback to it. Preserve reusable answer-writing preferences in `references/application-answer-voice-profile.md`, scoped as narrowly as the feedback requires. Create or update it through `compose-voice-profile` when needed. Once it exists, it takes priority over Answer Interview's bundled voice reference. Do not store career facts in a voice profile.

If the user gives a broad career request, first establish whether the career context exists, then route to the next required workflow above. Do not ask the user to name these skills.

## Application folders and files

- Assign a monotonically increasing running number to each new application. Never reuse a number, including after an application is withdrawn. Determine the next number from existing folders; use `001`, `002`, `003`, and so on.
- Create `applications/<company>_<job>_<runningnumber>/` with filesystem-safe company and job names. Keep the number as the final segment.
- Save a supplied or accessible full job description as `job.md` in plain Markdown, preserving its content and order. Format source headings, lists, and paragraphs cleanly. Add no application analysis, fit notes, retrieval metadata, or other content; omit webpage navigation. If the description came from a URL, read the supplied posting and archive the posting text, not the surrounding website. If the URL is inaccessible, ask the user to paste the full posting before claiming the archive is complete. If only a role summary is available, do not invent or create a partial `job.md`.
- Place the approved, final `CV.pdf` and, if requested and approved, `Motivation_Letter.pdf` in that folder. Do not overwrite existing files. Reuse `job.md` when it matches the same posting; ask before replacing a different existing description. For a revision, preserve existing final files until the user approves the replacement.
- Keep source JSON, DOCX, drafts, match assessments, and QA artifacts with the relevant staple or in a temporary working location. Do not clutter application folders with working files.

## Choosing and maintaining staple CVs

- Match from the actual role requirements, responsibilities, seniority, domain, and employer context when supplied. A company name alone is not enough to establish fit.
- Reuse a staple only when its `MATCH.md` criteria and actual evidence in the CV fit the target. Record material gaps or target-specific differences. If any important criterion requires different evidence, positioning, or content, use `create-cv` to make a new tailored version.
- Do not silently edit the staple during an application. Keep a new target-specific CV with its application's working material, and promote it to a staple only after the user approves that reusable change.
- When the career context changes, review affected staples for stale facts before using them.

## Skill locations

These names identify the Agent Stack capabilities; resolve them using the current host's skill catalog or installed package paths rather than assuming a filesystem path:

- `setup-career-stack`
- `compose-career-profile`
- `create-cv`
- `draft-cover-letter`
- `answer-interview`
- `compose-voice-profile`
