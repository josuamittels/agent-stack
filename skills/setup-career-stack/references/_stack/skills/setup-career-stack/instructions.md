---
name: "setup-career-stack"
description: "Initialize a project workspace for managing job applications, career context, reusable CVs, and application materials. Use when setting up a fresh career application system or organizing a new job-search project."
version: "2.0.1"
created: "2026-11-04"
updated: "2026-11-05"
author:
  - "Josua J. Mittelstaedt"
references: []
type: "skill"
status: "stable"
---

# Setup Career Stack

Create a durable, agent-coordinated workspace for career applications. Prepare its folders and root `AGENTS.md`, build a reusable career context, gather the user's target role families, and create one staple CV per materially distinct family.

## Scope

Use when the user wants a fresh project or folder for managing job applications, career context, reusable CVs, motivation letters, and application answers. This skill initializes the project and starts the first-time profile and staple-CV workflow.

For an individual career profile, use [Compose Career Profile](../compose-career-profile/instructions.md). For a new or revised CV, use [Create CV](../create-cv/instructions.md). For a motivation or cover letter, use [Draft Cover Letter](../draft-cover-letter/instructions.md). For application-form or interview questions, use [Answer Interview](../answer-interview/instructions.md). The generated project `AGENTS.md` directs later requests to these workflows even when the user does not name a skill.

### Boundaries

- Work only in the fresh folder or project selected by the user. If the destination already contains meaningful files or an existing `AGENTS.md`, inspect them and preserve them; do not overwrite or restructure without an explicit request.
- Use the stack's career skills through the host's supported invocation when available. If no separate invocation mechanism is available, read and apply their instructions directly; do not claim a separate skill ran.
- Do not submit applications, send messages, or upload application materials.
- Keep each application folder limited to `job.md`, the approved final CV PDF, and an optional approved final motivation-letter PDF. Keep editable source and QA files in the corresponding staple folder or durable application working directory, not in the application folder.
- Never copy a staple or generated CV into an application folder as a final deliverable until the user approves that CV's exact content. Preserve the Create CV approval and delivery rules.
- Do not fabricate career facts, role preferences, or evidence. Keep the career context as the source of truth.

## Inputs

Require a user-selected project folder. Use the user's supplied career materials, previous profile, target roles, and preferences when available. Ask only for a destination if none can be inferred safely. Before modifying a non-empty folder, check whether it is already a career workspace and preserve existing content.

Create this structure at the project root:

```text
AGENTS.md
applications/
references/
staples/
work/
```

Store career context at `references/career-context.md`. Both letter and answer skills share optional personalized guidance at `references/professional-voice-profile.md`, created from reusable feedback. Store persistent application identity and numbering in `references/applications.json`. Keep tailored working revisions under `work/<application-folder>/`; each staple keeps its own source and QA files beside its approved `CV.pdf` and `MATCH.md`.

Read [workspace operations](../compose-career-profile/references/workspace.md) before creating folders or application artifacts. It owns the helper commands and their behavior. Read the [shared professional voice](../compose-voice-profile/references/professional-voice-profile.md) for feedback persistence and migration from older split profiles. Do not create a personalized profile without evidence.

### Default Procedures

When task input is needed from the user, route the question through [ask-user-question](../ask-user-question/instructions.md) for preparation, delivery, and interpretation. First invoke [think-harder](../think-harder/instructions.md) when ambiguity, missing information, or competing interpretations may be resolved from context, relevant guidance, evidence, or a reasonable default. Skip Think Harder for direct permission or approval gates, explicitly requested interviews, and facts or preferences only the user can supply. Ask only about consequential unresolved items. Continue independent work and preserve approval requirements.

If any discipline is unavailable, perform it directly and report the fallback. Carry unresolved constraints forward and do not invent answers or pretend the dependency ran.

## Workflow

### 1. Select and prepare the project root

Use the folder or project the user selected. If no destination is explicit, use the current fresh project folder only when it is clearly the intended destination. Use the shared workspace helper’s `init` command with the selected root and this skill’s [`AGENTS.md` template](templates/AGENTS.md). It creates `applications/`, `references/`, `staples/`, and `work/`, preserving existing files. If the project has a known name, use it in the heading; preserve the routing rules.

Check that the root instructions and all four directories exist. Treat the template as a reusable scaffold: the delivered project file must not contain unresolved square-bracket placeholders.

### 2. Create the career context

Invoke [Compose Career Profile](../compose-career-profile/instructions.md). Pass relevant supplied material and instruct it to save the completed profile to `references/career-context.md`. Follow its evidence handling and interview stages. If there is an existing current profile the user has identified, use it and update only when requested; do not needlessly interview or replace it.

Continue when `references/career-context.md` exists and contains a usable profile, or when the user chooses to proceed with documented gaps. Never replace an unavailable profile with invented content.

### 3. Elicit the target role families

Review the user's request and career context for roles they intend to pursue. When role targets are not already clear, ask what kinds of roles they want and invite them to share as many relevant job links and full job descriptions as they can, ideally across different titles and companies. Ask for company profile links or notes too when available. The examples help distinguish roles that can share a staple CV from those that need separate positioning. If the user cannot provide links, accept role titles or descriptions in their own words; do not make link collection a blocker.

Cluster roles by the evidence, positioning, and content they require. Merge examples into one family when the same CV structure and evidence selection would credibly serve them. Keep families distinct when they call for materially different professional positioning, experience emphasis, or skills. Explain the proposed families briefly and ask the user to correct material grouping errors before creating the staples.

### 4. Build staple CVs

For each confirmed role family, invoke [Create CV](../create-cv/instructions.md) with `references/career-context.md` and a representative role-family brief. Save that family's working files and QA artifacts in a uniquely named folder under `staples/`. Use the Create CV workflow to produce the tailored `CV.pdf`, verify its layout, and assess its fit against the family brief.

Create one staple only when its evidence selection and positioning are meaningfully reusable across the family. Do not create near-duplicate staples for titles that use the same evidence and emphasis. If one family needs materially different CV variants, split it into separate families and record their match criteria. The user reviews and approves each staple's exact content before it becomes a reusable final PDF. Keep a concise `MATCH.md` next to each PDF listing the family it serves, positive match signals, limitations, and cases that require a fresh CV.

If needed details or approval are pending for a family, record that family as pending and continue with independent families. Do not mark a pending family as having a completed staple.

### 5. Confirm the workspace and operating rules

Verify the project root contains `AGENTS.md`, `applications/`, `references/`, `staples/`, and `work/`; confirm the career context path; and list each created or pending staple with its match-note path. Confirm the root instructions route every candidate-written employer question in application forms, screening questionnaires, and interviews to Answer Interview, including questions bundled with broader application requests. Also confirm each specific application folder can hold the plain-Markdown `job.md` alongside approved final files, and that the instructions explain application numbering, staple selection, fresh CVs, optional letters, and persistent writing feedback.

Do not make a test application or invent a sample CV. Do not create a starter voice profile from no evidence; the shared professional voice remains the fallback until the user gives reusable feedback.

### 6. Validate implementation

When invoked as a helper, return to the owning workflow without separate evaluation. For a skill with meaningful, deterministic, task-specific checks, invoke [Spawn Evals](../spawn-evals/instructions.md) once with a structured invocation record containing the original request, resolved constraints and their source, complete UTF-8 outputs, and machine-readable evidence. Its objective package in `src/evals/setup-career-stack/` defines only those checks. Report PASS, FAIL, or NOT PASSED — UNVERIFIED with the failing or unavailable verification steps. Do not use model judges, sub-agents, qualitative assessments, weighted scores, or synthetic scenarios. If no package exists for an objectively checkable skill, report NOT PASSED — UNVERIFIED; do not create one during an ordinary skill invocation. If no meaningful objective check is possible for this skill, omit this entire validation section and all Spawn Evals references from the skill.

## Output

Return the project path and links to its root `AGENTS.md`, `references/career-context.md`, the four directories, and each completed staple CV and `MATCH.md`. State which role families were merged or split, identify any pending profile or staple work, and confirm the application-folder naming and letter-feedback rules. Clearly distinguish a generated draft from a user-approved staple. Do not claim an approval that was not given.
