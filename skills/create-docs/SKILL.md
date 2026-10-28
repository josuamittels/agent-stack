---
name: create-docs
description: "Scan a repository and create evidence-grounded project documentation under root/docs, as interlinked Markdown or an interactive Nextra site. Use for generating or substantially rebuilding repository documentation, rather than authoring reusable documentation standards."
version: "0.1.0"
created: "2026-10-28"
updated: "2026-10-28"
author:
  - "Josua Mittelstaedt"
references:
  - "The Nextra Project"
  - "Garrick Aden-Buie"
  - "Nuxt Content"
  - "Anthropic"
type: "skill"
status: "experimental"
---

# Create docs

Inspect a repository's implementation and generate documentation that helps its readers use, integrate with, operate, and maintain it. Follow the documentation standard strictly in either output mode.

## Scope

Own repository investigation, reader and page planning, documentation authoring, mode-specific setup, and verification. Cover components, code structure, interfaces, workflows, states, and data lifecycle according to the actual project and readers, including non-application repositories and monorepos.

For reusable documentation standards, use [Create Guidelines](../create-guidelines/SKILL.md). For a small prose edit, use [Natural Writing](../natural-writing/SKILL.md) directly.

### Boundaries

Write documentation under `<repository-root>/docs/`. Here, `root` means the target repository root, not the filesystem root or this skill's repository. Preserve existing authored material, stable URLs, and unrelated changes. Do not rewrite application behavior or silently migrate an incompatible docs stack.

Interactive selection authorizes a local Nextra docs package and its necessary dependencies within repository policy. It does not authorize deployment, publication, paid services, or upgrading the target application's toolchain. Basic selection creates Markdown documentation without a site framework. Inspect configuration names and loaders without exposing secrets or copying private data into public docs.

## Inputs

Require an accessible target repository and an explicit output mode, `basic` or `interactive`. Resolve a supplied path or repository reference first. Use the current checkout when it is clearly the target. Ask for the target if multiple repositories remain plausible. Clone a supplied remote only through available, authorized access.

If the mode is absent, ask through Ask User Question before format-dependent authoring:

> Which version should I generate? Basic creates interlinked Markdown files in `docs/`, readable directly in the repository. Interactive creates a Nextra documentation site in `docs/`, with navigation, search, and MDX components, and requires a Node.js build setup.

Offer Basic and Interactive as the choices. Do not infer consent from existing tooling or choose a mode after a timeout. Continue independent read-only investigation while awaiting the answer. An already supplied choice satisfies this requirement.

Use optional audience, language, version, scope, visibility, and existing docs constraints when supplied. Otherwise infer a bounded audience and coverage from evidence, state the assumptions, and use English technical prose. Treat format choice separately from content depth.

### Default Procedures

When task input is needed from the user, route the question through [ask-user-question](../ask-user-question/SKILL.md) for preparation, delivery, and interpretation. First invoke [think-harder](../think-harder/SKILL.md) when ambiguity, missing information, or competing interpretations may be resolved from context, relevant guidance, evidence, or a reasonable default. Skip Think Harder for direct permission or approval gates, explicitly requested interviews, and facts or preferences only the user can supply. Ask only about consequential unresolved items. Continue independent work and preserve approval requirements.

If any discipline is unavailable, perform it directly and report the fallback. Carry unresolved constraints forward and do not invent answers or pretend the dependency ran.

## Workflow

### 1. Read the standards and establish the baseline

Read [the documentation guideline](../../guidelines/docs/reference.md) in full before assessing coverage or drafting. Apply it as the content and readiness standard, including its basic Markdown organization. Preserve its separation of tutorial, how-to, reference, and explanation. Apply its evidence, commands, accessibility, maintenance, and verification rules in both modes.

Apply [Natural Writing](../natural-writing/SKILL.md) before composing. For English, read the general guidance and [Technical style](../../guidelines/languages/english.md#technical). For another requested language, use its language reference and transferable technical-writing principles. Do not substitute promotional text or generated API dumps for practical documentation.

Read target repository instructions and existing docs. Identify the revision or release, dirty working-tree changes, project type, workspace boundaries, supported tooling, docs generator, and existing entry points. Describe the working tree when uncommitted behavior is included. Keep a lightweight authoring record outside published pages, using the host's task workspace or a temporary directory unless the project has a convention.

### 2. Investigate the system and its states

Start with a broad file inventory using `rg --files` and targeted searches. Exclude dependencies, build outputs, caches, generated artifacts, and vendored copies unless they establish a relevant contract. Inspect manifests and lockfiles, entry points, routes, public exports, schemas, configuration loaders, tests, CI, deployment definitions, and decision records. Read the implementations behind names before making claims.

Trace primary reader journeys from their entry points through component interactions to observable results. Investigate these subjects where the repository implements them:

| Subject | Evidence to capture |
| --- | --- |
| Components and structure | Responsibilities, boundaries, ownership, important dependencies, public/internal distinction, and useful paths or symbols. |
| Interfaces and configuration | Inputs, outputs, validation, defaults, precedence, permissions, errors, compatibility, and restart or reload behavior. |
| UI and workflows | Exact labels, route access, actions, guards, loading, empty, success, validation, error, and recovery states that exist. |
| Runtime and background work | Startup/shutdown, jobs, events, retries, cancellation, timeouts, concurrency, and failure behavior where implemented. |
| Data and transitions | State owner, initial state, trigger, guard, transition, side effects, persistence, reset, migration, deletion, and recovery where applicable. |
| Development and operations | Supported setup, test/build commands, external services, health signals, deployment assumptions, and established recovery procedures. |

Record consequential relationships and transitions with source paths and symbols. Distinguish observed behavior, test evidence, intended contracts, and unresolved discrepancies. A missing state is not permission to invent it. Omit inapplicable subjects with a short rationale in the authoring record.

Continue when the main path can be explained end to end, relevant failure and recovery branches are accounted for, and consequential claims have identifiable evidence. For a large repository, track inspected and uninspected areas explicitly. Do not claim whole-repository coverage from a sample.

### 3. Map evidence to reader outcomes and pages

Identify actual readers and important outcomes. Build a coverage map in the authoring record: reader outcome, component or state, source evidence, destination page, and verification performed or needed. Choose useful pages from the guideline's component inventory. Create directories only when they contain substantive pages.

Give each page one dominant documentation mode and a canonical subject. Order navigation around orientation, first success, common tasks, reference, and explanation. Include troubleshooting, security boundaries, and upgrade or recovery help where evidence and reader needs justify them. Explain architecture and state behavior in the pages they support rather than generating one page per file.

Reuse accurate existing content and repair stale statements against the inspected revision. Resolve conflicting evidence or name the precise limitation. Explain mechanisms without inventing historical design intent. Plan redirects or link repairs before moving established pages. Ask about a material collision requiring destructive migration, then continue unaffected work.

### 4. Generate the selected format

**Basic.** Create `docs/index.md` and substantive `.md` pages under `docs/`, adapting the guideline's file organization to the project. Link every page into navigation, provide a route back to the index or parent, and use descriptive relative links between pages. Link assets and code references with paths that resolve from their page. Include a useful landing page rather than a directory listing. Keep the result readable without MDX, React, or a framework. Use an existing compatible Markdown renderer for preview checks when available.

**Interactive.** Read [the Nextra operational reference](references/nextra-docs.md) before setup. Use its bundled [starter files](templates/nextra/) for a new docs package. Generate the Nextra application and substantive MDX pages under `docs/`, keeping the docs application root distinct from its URL. Follow the reference for App Router pages, theme layout, navigation, search, components, design, and build checks. Preserve a compatible existing Nextra layout. Consult official sources only for an uncovered behavior, a version conflict, or observed behavior that differs. Do not silently substitute another framework.

For both modes, write complete instructions with working directories, prerequisites, exact names, observable results, and relevant recovery steps. Use synthetic example data. Link canonical facts instead of duplicating them. Use diagrams when they clarify relationships or transitions. Before authoring Mermaid, read [the Mermaid guideline](../../guidelines/coding/mermaid.md). Include a text explanation of essential relationships.

### 5. Verify readiness and capture evidence

Review the guideline's readiness conditions. Compare consequential interface, configuration, permission, and state claims with source evidence. Exercise a representative supported task from its stated starting conditions when safe and available. Identify untested services, platforms, credentials, and destructive operations precisely. Never report a build as proof of accuracy or reader success.

Check navigation, links and anchors, assets, examples, code fences, headings, and rendering. For interactive output, install with the selected package manager under repository policy, build the docs, verify Pagefind output, and inspect rendered pages, mobile navigation, keyboard use, theme behavior, and a real search result. Repair in-scope failures. Report unavailable checks without claiming they ran.

Prepare the invocation evidence described in [verification evidence](references/verification-evidence.md). Capture complete rendered HTML for each documentation page when a renderer is available. This supports deterministic page reachability and fragment checks. If rendering is unavailable, preserve the authored files and report the gap. Do not fabricate HTML evidence. Keep temporary previews and evaluation records out of published docs.

### 6. Validate implementation


When invoked as a helper, return to the owning workflow without separate evaluation. For a skill with meaningful, deterministic, task-specific checks, invoke [Spawn Evals](../spawn-evals/SKILL.md) once with a structured invocation record containing the original request, resolved constraints and their source, complete UTF-8 outputs, and machine-readable evidence. Its objective package in `evals/create-docs/` defines only those checks. Report PASS, FAIL, or NOT PASSED — UNVERIFIED with the failing or unavailable verification steps. Do not use model judges, sub-agents, qualitative assessments, weighted scores, or synthetic scenarios. If no package exists for an objectively checkable skill, report NOT PASSED — UNVERIFIED; do not create one during an ordinary skill invocation. If no meaningful objective check is possible for this skill, omit this entire validation section and all Spawn Evals references from the skill.

## Output

Return the docs location and landing page, selected mode, covered readers and subjects, target revision, and verification results with precise limits. For interactive output, include the working directory, resolved package versions or lockfile, and exact install, development, build, and start commands. Name remaining coverage or evidence gaps and the nonpublished authoring record. State whether reader validation occurred. Do not publish unless requested.
