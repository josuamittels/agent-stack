# Career Application Workspace

This project organizes career context, reusable CVs, and job applications. Follow these instructions whenever work in this project relates to a job search or application, even when the user does not name a skill.

## Workspace map

- `applications/`: one folder per application, named `<company>_<job>_<runningnumber>`; store `job.md`, the approved final `CV.pdf`, and optional approved `Motivation_Letter.pdf` here.
- `references/career-context.md`: durable career profile and source of truth for experience, skills, motivation, and preferences.
- `references/professional-voice-profile.md`: optional shared letter and answer voice profile. When present, it takes priority over the bundled profile for both skills; channel-specific preferences remain scoped.
- `references/applications.json`: persistent application identity and monotonically increasing numbering. Preserve withdrawn and deleted application records.
- `work/`: durable tailored source files and QA, grouped by application and revision.
- `staples/`: pre-generated, approved CVs grouped by materially distinct role family. Each staple folder contains `CV.pdf`, `MATCH.md`, Create CV source files, and QA evidence.

Do not treat a generated draft as an approved final. Do not submit, email, or upload applications. Never invent career facts or claims.

## Route career requests automatically

Read the relevant skill instructions from the available Agent Stack career skills. Use the host's supported skill invocation when available; otherwise read and apply the instructions directly. Do not claim a skill ran when it was not separately invoked.

**Route every employer question that needs a candidate-written answer to `answer-interview`.** This includes free-text questions in application forms, screening questionnaires, and interview prompts, whether the user supplies one question or a full set. Apply this rule even when the questions arrive as part of a broader new-application or CV request; route CV and letter work to their own skills separately. Pass the exact question text, target job description, relevant career context, language, and any word or character limits.

1. **Career profile missing or needs substantial update:** use `compose-career-profile`. Save the resulting profile as `references/career-context.md`.
2. **New application or request for a CV:** read the career context and target job description or company/role profile. For a specific application with a full job description, create or reuse its numbered folder and archive the complete posting as `job.md` in plain Markdown before preparing or selecting a CV. Compare the target with every relevant staple's `MATCH.md` and actual CV. Ask for a missing target only when necessary. If a staple fits its stated scope and its evidence covers the target, use that approved PDF. Otherwise use `create-cv` to make a role-specific CV and assess it against the target. Get approval of exact CV content before placing a final PDF in `applications/`.
3. **Cover or motivation letter requested:** use `draft-cover-letter`, with the career context, target details, and any user-provided employer context. For a specific application with a full job description, archive the complete posting as `job.md` in the matching numbered application folder. A letter is optional; do not create one unless requested. Save an approved PDF as `Motivation_Letter.pdf` in that folder.
4. **Feedback after a letter:** revise the letter. Apply immediate, application-specific feedback to that letter. Preserve reusable writing preferences in `references/professional-voice-profile.md`, scoped as narrowly as the feedback requires. Create the file from the available bundled profile through `compose-voice-profile` when needed. Both writing skills read this profile. Keep letter-only guidance scoped to letters. Do not store career facts in a voice profile.
5. **Application-form, screening, or interview question:** use `answer-interview` for each employer question requiring a candidate response. Use the shared workspace helper for application identity and full-posting archiving even for answer-only applications. Return direct, copy-ready answers in chat and include exact word or character counts when limits apply.
6. **Feedback after an answer:** revise the answer. Apply immediate, application-specific feedback to it. Preserve reusable answer-writing preferences in `references/professional-voice-profile.md`, scoped as narrowly as the feedback requires. Create or update it through `compose-voice-profile` when needed. Both writing skills read this profile. Keep answer-only guidance scoped to answers. Do not store career facts in a voice profile.

If the user gives a broad career request, first establish whether the career context exists, then route to the next required workflow above. Do not ask the user to name these skills.

## Application folders and files

- Read the workspace-operations reference bundled with `compose-career-profile` and use its helper for initialization, application identity, numbering, archive paths, and delivery. Do not calculate these independently in each skill.
- Identify an application by requisition id or canonical vacancy URL; reuse that identity for the same posting, and distinguish intentional reapplications. Resolve ambiguous duplicates before allocation.
- The helper returns `applications/<company>_<job>_<runningnumber>/` and `work/<application-folder>/`. Preserve `references/applications.json` so deleted or withdrawn applications never recycle their numbers.
- Archive the complete posting as canonical plain Markdown `job.md`, with no navigation, analysis, or retrieval notes. If only a summary or inaccessible link is available, document the gap and continue supported work without inventing a partial archive.
- Place only the approved final `CV.pdf` and optional approved `Motivation_Letter.pdf` beside `job.md`. Deliver the reviewed bytes with their approved hash. Preserve an existing final until the replacement is approved; move the old version to `work/` before replacement.
- Keep source JSON, DOCX, drafts, assessments, and QA under durable working revision directories or the relevant staple. Do not use temporary storage as their only retained location.
- Keep installed defaults immutable. Outside this workspace, use conversation feedback or an explicitly chosen user-owned profile. Merge older split voice profiles into the shared workspace profile with channel scopes while preserving the originals.
- Honor the career context's sharing restrictions for every outward-facing artifact. Factual support alone does not authorize disclosure.

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
