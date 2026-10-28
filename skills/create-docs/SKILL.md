---
name: create-docs
description: "Create evidence-grounded documentation in root/docs for people who use a repository's product or resources. Explain its structure, components, and supported use; do not default to contributor or maintainer manuals."
version: "0.5.0"
created: "2026-10-28"
updated: "2026-10-28"
author:
  - "Josua Mittelstaedt"
references:
  - "The Nextra Project"
  - "Garrick Aden-Buie"
  - "Nuxt Content"
  - "Anthropic"
  - "Google"
type: "skill"
status: "experimental"
---

# Create docs

Inspect a repository and create documentation for people who use what the repository provides. Explain its structure, components, how they work, and how readers use them. Follow the documentation standard strictly in either output mode.

## Scope

Own repository investigation, end-user and page planning, documentation authoring, mode-specific setup, and verification. Document the repository's actual deliverable: its user-visible components, capabilities, interfaces, supported workflows, relationships, and limits. This applies to applications, libraries, command-line tools, agent stacks, and monorepos.

The default audience is the people or systems that use the repository's product, library, commands, services, capabilities, or reference resources. Derive their outcomes from public interfaces, entry points, route instructions, and repository guidance. Maintainers are not the default audience. Do not fill the docs with contribution, release, deployment, or docs-site maintenance procedures unless they are part of a user-facing product or the user explicitly requests contributor documentation.

Write every published page for the person using the repository's deliverable. Address that reader directly. Prefer “Use [capability] to …” or “Use this guide to …”; do not describe a hypothetical user's intent with phrases such as “Use when the user wants to …”. Do not expose agent-authoring or docs-maintenance procedure as product documentation unless the repository's users need that procedure or the user asks for it.

For repositories that organize reusable capabilities or reference resources, document every available, substantive user-facing component in scope. Explain its type, purpose, activation or use, main behavior, inputs and outputs, dependencies or references, current version and lifecycle status where defined, and recorded changes. Treat a skill, discipline, router, guideline, reference, and playbook according to its actual source contract. Link the canonical instruction or resource instead of copying it wholesale.

For reusable documentation standards, use [Create Guidelines](../create-guidelines/SKILL.md). For a small prose edit, use [Natural Writing](../natural-writing/SKILL.md) directly.

### Boundaries

Write documentation under `<repository-root>/docs/`. Here, `root` means the target repository root, not the filesystem root or this skill's repository. Preserve existing authored material, stable URLs, and unrelated changes. Do not rewrite application behavior or silently migrate an incompatible docs stack.

Interactive selection authorizes a local Nextra docs package and its necessary dependencies within repository policy. It does not authorize deployment, publication, paid services, or upgrading the target application's toolchain. Basic selection creates Markdown documentation without a site framework. Inspect configuration names and loaders without exposing secrets or copying private data into public docs.

## Inputs

Require an accessible target repository and an explicit output mode, `basic` or `interactive`. Resolve a supplied path or repository reference first. Use the current checkout when it is clearly the target. Ask for the target if multiple repositories remain plausible. Clone a supplied remote only through available, authorized access.

If the mode is absent, ask through Ask User Question before format-dependent authoring:

> Which version should I generate? Basic creates interlinked Markdown files in `docs/`, readable directly in the repository. Interactive creates a Nextra documentation site in `docs/`, with navigation, search, and MDX components, and requires a Node.js build setup.

Offer Basic and Interactive as the choices. Do not infer consent from existing tooling or choose a mode after a timeout. Continue independent read-only investigation while awaiting the answer. An already supplied choice satisfies this requirement.

Use optional audience, language, version, scope, visibility, and existing docs constraints when supplied. Otherwise infer the end-user audience and coverage from repository evidence, state the assumptions, and use English technical prose. Treat format choice separately from content depth. Ask only if the repository's deliverable or intended users cannot be established from available evidence and materially affect the docs.

### Default Procedures

When task input is needed from the user, route the question through [ask-user-question](../ask-user-question/SKILL.md) for preparation, delivery, and interpretation. First invoke [think-harder](../think-harder/SKILL.md) when ambiguity, missing information, or competing interpretations may be resolved from context, relevant guidance, evidence, or a reasonable default. Skip Think Harder for direct permission or approval gates, explicitly requested interviews, and facts or preferences only the user can supply. Ask only about consequential unresolved items. Continue independent work and preserve approval requirements.

If any discipline is unavailable, perform it directly and report the fallback. Carry unresolved constraints forward and do not invent answers or pretend the dependency ran.

## Workflow

### 1. Read the standards and establish the baseline

Read [the documentation guideline](../../guidelines/docs/reference.md) in full before assessing coverage or drafting. Apply it as the content and readiness standard, including its basic Markdown organization. Preserve its separation of tutorial, how-to, reference, and explanation. Apply its evidence, commands, accessibility, maintenance, and verification rules in both modes.

Apply [Natural Writing](../natural-writing/SKILL.md) before composing. For English, read the general guidance and [Technical style](../../guidelines/languages/english.md#technical). For another requested language, use its language reference and transferable technical-writing principles. Do not substitute promotional text or generated API dumps for practical documentation.

Read target repository instructions and existing docs. Identify the revision or release, dirty working-tree changes, project type, workspace boundaries, supported tooling, docs generator, and existing entry points. Describe the working tree when uncommitted behavior is included. Keep a lightweight authoring record outside published pages, using the host's task workspace or a temporary directory unless the project has a convention.

### 2. Investigate the system and its states

Start with a broad file inventory using `rg --files` and targeted searches. Exclude dependencies, build outputs, caches, generated artifacts, and vendored copies unless they establish a user-facing contract. Inspect manifests and lockfiles, product entry points, routes, public exports, schemas, configuration loaders, examples, tests, and source material that explains the delivered product. Read the implementations behind names before making claims. Inspect CI, deployment, and release material only when users operate those systems or the requested docs explicitly cover maintainers.

Trace primary reader journeys from their entry points through component interactions to observable results. Investigate these subjects where the repository implements them:

| Subject | Evidence to capture |
| --- | --- |
| Components and structure | Responsibilities, boundaries, ownership, important dependencies, public/internal distinction, and useful paths or symbols. |
| Interfaces and configuration | Inputs, outputs, validation, defaults, precedence, permissions, errors, compatibility, and restart or reload behavior. |
| UI and workflows | Exact labels, route access, actions, guards, loading, empty, success, validation, error, and recovery states that exist. |
| Runtime and background work | Startup/shutdown, jobs, events, retries, cancellation, timeouts, concurrency, and failure behavior where implemented. |
| Data and transitions | State owner, initial state, trigger, guard, transition, side effects, persistence, reset, migration, deletion, and recovery where applicable. |
| User setup and operation | Supported installation or access, configuration, task flows, external services, observable results, and established recovery procedures that repository users need. |
| Capability and resource catalog | Actual type, purpose, trigger or consumer, workflow or method, inputs and outputs, dependencies, version/status, and recorded changes for each available user-facing component. |

Record consequential relationships and transitions with source paths and symbols. Distinguish observed behavior, test evidence, intended contracts, and unresolved discrepancies. A missing state is not permission to invent it. Omit inapplicable subjects with a short rationale in the authoring record.

Continue when the main user path can be explained end to end, relevant failure and recovery branches are accounted for, and consequential claims have identifiable evidence. For capability repositories, build an inventory from substantive source files, not map nodes or directory names. Reconcile the documented set against the available in-scope skills, disciplines, routers, guidelines, references, and playbooks. Record excluded planned, empty, generated, vendored, or maintainer-only material in the authoring record. Do not claim whole-repository coverage from a sample.

### 3. Map evidence to reader outcomes and pages

Identify actual end users and their important outcomes. Build a coverage map in the authoring record: reader outcome, product component or resource, source evidence, destination page, and verification performed or needed. For a capability stack, map every available in-scope capability and reference resource to a page or a clearly labeled catalog entry. A type listing alone is not coverage; explain what each item is for and how a reader or calling capability uses it. Create directories only when they contain substantive pages.

Give each page one dominant documentation mode and a canonical subject. Order navigation around orientation, a supported first success when one exists, user tasks, reference, and explanation. For a repository with distinct component types, use top-level groups that help users distinguish them, such as capabilities, guidelines and references, and playbooks. Group items by their actual resource taxonomy; do not mirror the directory tree blindly.

Create individual entries for available components when users need to find them directly. Each capability entry should state its type, purpose, route or usage, main workflow, required inputs and outputs, important handoffs or dependencies, version and lifecycle status when defined, and a link to the canonical source. Each guideline or reference entry should state its subject, scope, when consumers use it, related resources or callers, version and status when defined, and a link to its source. For playbooks, describe the supported sequence and identify draft outlines as drafts; a filename alone does not establish an executable workflow.

Write every page for its reader in direct language. Describe the outcome with wording such as “Use this to…” or “Use [capability] to…”. Avoid meta phrasing such as “Use when the user wants…”. Read the source workflow and explain the actions that produce the outcome; do not copy activation metadata as a user guide. On skill, discipline, and router pages, put the process under a `## Workflow` heading and use an actual ordered list. Start each item with a concrete action and briefly explain its purpose or result. Combine routine setup, omit evaluator or authoring mechanics that do not help repository users, and keep the list to the essential sequence. Never put step numbers inside unordered-list bullets. For guidelines and references, explain how to apply the resource; do not invent a sequential workflow for material that is organized as a reference.

Use canonical templates as working artifacts: link the template where the reader needs it and tell them what to fill in. Do not merely tell them to read the template. Link each important handoff to that capability's documentation page and say what it contributes. For example, a voice-profile workflow should tell readers to fill in the voice-profile template and use the Think Deeper documentation page to synthesize the voice strategy. Prefer a few contextual links embedded in the relevant explanation over long lists of isolated or one-word link labels. On individual component pages, put a compact `## References` section last. List the canonical source and relevant supporting references directly; do not discuss metadata fields or explain that the names came from front matter. Keep version and history information before References.

Derive current component versions and status from each component's authoritative metadata. Use inventory files such as `VERSIONS.md` as snapshots, not as a substitute for component metadata. Describe changes only from an available changelog or source history. Link to those records and state when there is no component-level change history. Do not invent rationale, compatibility guarantees, or history.

Include tutorials or getting-started pages only when repository evidence supports a complete end-user path. Do not create an empty section, placeholder page, or promised future guide for a planned feature; leave unsupported future content out of the published navigation. Include contributor, release, deployment, and documentation-maintenance pages only when the user requests them or when those procedures are part of the repository's user-facing product. Explain architecture and behavior in the pages they support rather than generating one page per implementation file.

For an interactive Nextra site, make each major navigation destination open its overview directly. Put meaningful sections on that page with descriptive headings and linked cards or similarly scannable content. Nextra renders each `Cards.Card` body before its title by default. Apply a shared stylesheet to every card: add `padding: 1rem` to `.nextra-card`, then set `order: -1` and `padding: 0` on `.nextra-card > span:last-child` so the title leads the description and both align within the same padding. Keep each card's title in the `title` prop and its concise, reader-facing description in the body; do not repeat the title or put version and lifecycle metadata in the description when the component page already presents it. Do not add page-specific card markup. Treat taxonomy labels such as Skills, Disciplines, and Router as sidebar group headings when they only organize individual entries; do not add an index page that repeats the group's label and list. Use a folder index page only when it has a distinct purpose readers need. Align `_meta.js` with the route hierarchy so a reader does not see the same page once as a folder and again as its first child. Where a folder has a useful landing page, use Nextra's index-page convention so its folder label opens the page instead of adding a duplicate child link. Keep page headings, sidebar groups, and cards in agreement, and point cards to actual user-facing pages.

Reuse accurate existing content and repair stale statements against the inspected revision. Resolve conflicting evidence or name the precise limitation. Explain mechanisms without inventing historical design intent. Plan redirects or link repairs before moving established pages. Ask about a material collision requiring destructive migration, then continue unaffected work.

### 4. Generate the selected format

**Basic.** Create `docs/index.md` and substantive `.md` pages under `docs/`, adapting the guideline's file organization to the project. Link every page into navigation, provide a route back to the index or parent, and use descriptive relative links between pages. Link assets and code references with paths that resolve from their page. Include a useful landing page rather than a directory listing. Keep the result readable without MDX, React, or a framework. Use an existing compatible Markdown renderer for preview checks when available.

**Interactive.** Read [the Nextra operational reference](references/nextra-docs.md) before setup. Use its bundled [starter files](templates/nextra/) for a new docs package. Generate the Nextra application and substantive MDX pages under `docs/`, keeping the docs application root distinct from its URL. Follow the reference for App Router pages, theme layout, navigation, search, components, design, and build checks. Give each major destination a direct overview page with headings and descriptive cards. Use sidebar groups for categories that only organize pages, and remove redundant index pages that repeat the group's label. Use Nextra's folder index convention when a folder also needs useful landing content. Preserve a compatible existing Nextra layout. Consult official sources only for an uncovered behavior, a version conflict, or observed behavior that differs. Do not silently substitute another framework.

For both modes, write complete instructions with working directories, prerequisites, exact names, observable results, and relevant recovery steps. Use synthetic example data. Link canonical facts instead of duplicating them. Use diagrams when they clarify relationships or transitions. Before authoring Mermaid, read [the Mermaid guideline](../../guidelines/coding/mermaid.md). Include a text explanation of essential relationships.

### 5. Verify readiness and capture evidence

Review the guideline's readiness conditions. Compare consequential interface, configuration, permission, component metadata, routing, version, change-history, and state claims with their canonical sources. Exercise a representative end-user task from its stated starting conditions when safe and available. Identify untested services, platforms, credentials, and destructive operations precisely. Never report a build as proof of accuracy or reader success.

Check navigation, links and anchors, assets, examples, code fences, headings, and rendering. For interactive output, install with the selected package manager under repository policy, build the docs, verify Pagefind output, and inspect rendered pages, mobile navigation, keyboard use, theme behavior, and a real search result. Repair in-scope failures. Report unavailable checks without claiming they ran.

Prepare the invocation evidence described in [verification evidence](references/verification-evidence.md). Capture complete rendered HTML for each documentation page when a renderer is available. This supports deterministic page reachability and fragment checks. If rendering is unavailable, preserve the authored files and report the gap. Do not fabricate HTML evidence. Keep temporary previews and evaluation records out of published docs.

### 6. Validate implementation


When invoked as a helper, return to the owning workflow without separate evaluation. For a skill with meaningful, deterministic, task-specific checks, invoke [Spawn Evals](../spawn-evals/SKILL.md) once with a structured invocation record containing the original request, resolved constraints and their source, complete UTF-8 outputs, and machine-readable evidence. Its objective package in `evals/create-docs/` defines only those checks. Report PASS, FAIL, or NOT PASSED — UNVERIFIED with the failing or unavailable verification steps. Do not use model judges, sub-agents, qualitative assessments, weighted scores, or synthetic scenarios. If no package exists for an objectively checkable skill, report NOT PASSED — UNVERIFIED; do not create one during an ordinary skill invocation. If no meaningful objective check is possible for this skill, omit this entire validation section and all Spawn Evals references from the skill.

## Output

Return the docs location and landing page, selected mode, end-user audience, covered components and outcomes, target revision, and verification results with precise limits. For capability repositories, report inventory coverage and distinguish available components from planned or excluded resources. For interactive output, include the working directory, resolved package versions or lockfile, and exact install, development, build, and start commands. Name remaining evidence gaps and the nonpublished authoring record. State whether reader validation occurred. Do not publish unless requested.
