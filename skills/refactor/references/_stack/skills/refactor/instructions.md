---
name: "refactor"
description: "Audit and refactor codebases and interacting component libraries. Plan architecture, component consolidation, variants, conventions, and legacy removal; implement in themed commits on refactor branches when requested."
version: "0.1.1"
created: "2026-11-15"
updated: "2026-11-15"
author:
  - "Josua Mittelstaedt"
references:
  - "Martin Fowler"
  - "React"
  - "GOV.UK Design System"
  - "TypeScript"
  - "npm"
type: "skill"
status: "experimental"
---

# Refactor

Turn inconsistent codebases into a coherent system through an evidence-backed audit, a dependency-ordered master plan, and verified incremental changes. Coordinate applications and shared libraries as one migration while preserving each repository's contracts.

## Scope

Use for comprehensive cleanup, standardization, architectural consolidation, component-library alignment, and obsolete-code removal. Support audit-only, plan-only, and implementation requests. For a bounded feature or defect use [Build](../build/instructions.md). Refactor owns the audit and migration plan; Build owns implementation quality and review; [Ship](../ship/instructions.md) owns authorized Git delivery.

### Boundaries

An audit request authorizes investigation and reporting. Implement when the user requests implementation or complete cleanup; present the concrete master plan first and continue within that authorization. Resolve consequential unknowns before dependent changes. Preserve observable behavior by default; explicitly identify intentional design, API, data, and behavior changes in the plan.

Honor applicable AGENTS.md files, architecture decisions, contracts, and user requirements. For conflicting requirements, quote the rules and paths, explain the practical consequences, and obtain a decision through Ask User Question. Also raise material conflicts between proposed engineering practices and established repository rules. Continue independent work while the affected action waits. After resolution, amend the authoritative Markdown instructions within the authorized repositories with the agreed rule. Preserve unrelated instructions. Never rewrite standards silently to justify a preferred implementation.

## Inputs

Use repository paths and relationships, requested mode, desired outcome, supported consumers and releases, constraints, design system, and delivery authorization. Recover these from context and accessible code. Require both sides before claiming a complete cross-repository audit; record unavailable packages, repositories, consumers, and runtimes as coverage gaps.

### Default Procedures

When task input is needed from the user, route the question through [ask-user-question](../ask-user-question/instructions.md) for preparation, delivery, and interpretation. First invoke [think-harder](../think-harder/instructions.md) when ambiguity, missing information, or competing interpretations may be resolved from context, relevant guidance, evidence, or a reasonable default. Skip Think Harder for direct permission or approval gates, explicitly requested interviews, and facts or preferences only the user can supply. Ask only about consequential unresolved items. Continue independent work and preserve approval requirements.

If any discipline is unavailable, perform it directly and report the fallback. Carry unresolved constraints forward and do not invent answers or pretend the dependency ran.

## Workflow

### Coordination across domains

Keep one coordinator responsible for the combined audit, master plan, shared contracts, integration, verification, and delivery. For substantial implementation, default to about three domain agents when the dependency graph offers independently editable work. Choose boundaries from the actual codebase; a useful allocation is shared components and library APIs, application consumers and domain compositions, and repository tooling, structure, and legacy cleanup. These are examples, not fixed roles. Use fewer agents or sequential work when edits share files, contracts remain unsettled, or coordination would cost more than it saves. Respect host concurrency limits.

Before spawning implementation agents, settle shared API shapes, tokens, ownership, compatibility rules, and migration order in the master plan. Give each agent task IDs, exclusive writable paths, read-only dependencies, baseline SHA, applicable instructions, acceptance checks, and required return evidence. Explicitly assign shared files such as manifests, lockfiles, exports, and global styles to one owner. Agents must request scope transfers through the coordinator rather than editing another agent's files. Block dependent tasks until their prerequisite contracts and implementation are available; parallel work does not override migration order.

Audit work may also use parallel read-only agents for architecture and package consumption, component families and design consistency, and legacy/tooling/conventions. Give them distinct questions and require locations, evidence, coverage limits, concrete consequences, and conflicting interpretations. The coordinator traces findings across domains, deduplicates them, investigates disagreement, and produces one master plan. Separate reports alone do not establish complete coverage.

Each implementation agent applies Build as a helper and returns its exact diff or commit range, checks and results, removed paths, contract changes, and remaining risks. Keep commit creation coordinated through Ship; agents must not independently push, merge, or release. In a shared checkout, serialize Git index and commit operations and stage only the owning task's paths. With isolated worktrees, agree integration order and rerun checks on the combined result. Update the ledger after each integrated wave.

Require explicit coordinator authorization for further delegation and reuse agents when practical. For final independent review, use an agent that did not author the reviewed implementation; an implementer reviewing its own domain is self-review. Run review after implementation slots become available when necessary. If subagents are unavailable, perform the work sequentially and report the limitation. Never describe parallel audits, implementation, or independent review as completed unless they actually ran.

### 1. Establish authority, baseline, and coverage

Read instructions at each root and affected subtree. Record Git roots, branches, HEADs, worktree status, remotes, pinned languages and frameworks, manifests, lockfiles, generators, workspace relationships, release policies, and required checks. Preserve unrelated edits; never stash, reset, or commit them implicitly.

Load [TypeScript conventions](../../guidelines/coding/typescript.md) for TS/TSX and [Python conventions](../../guidelines/coding/python.md) for Python. For other languages use repository guidance and verified official version-appropriate documentation. Treat formatter and lint configuration as evidence of established practice. Record contradictions instead of choosing a convenient rule.

Use [Think Deeper](../think-deeper/instructions.md) to select professional audit methods and falsifiable checks. For substantial multi-phase work use [Show Me Your Work](../show-me-your-work/instructions.md) for evidence and decisions. Start [the audit and master-plan template](templates/audit-plan.md) in the repository's documentation convention or agreed working location. Keep private code out of public research queries.

Inventory packages, entrypoints, routes, domains, exports, components, tokens, styles, assets, tests, tooling, and generated sources. Mark inspected, sampled, excluded, and inaccessible areas. Investigate every in-scope component family and package boundary; disclose sampling limits on repetitive callers. Run available baseline checks and representative journeys. Separate existing failures from new regressions.

### 2. Trace architecture and consumption

Map actual dependencies and ownership across entrypoints, domain rules, state, transport, persistence, UI, and packages. Inspect imports and runtime registration. Find cycles, deep imports, duplicate schemas and state owners, framework leakage, catch-all utilities, needless layers, misplaced domain logic, and unstable public APIs. Explain concrete consequences; file size alone is not a defect.

For each app-library edge inspect development and production resolution, workspace links versus published artifacts, export maps, declarations, module formats, peer dependencies, duplicated framework runtimes, CSS side effects, token/theme delivery, assets, SSR/client boundaries, packaging, and release order. A development alias that masks a broken package export is a finding. Verify how consumers actually receive updates.

Propose consistent ownership, naming, imports, and layout from the established architecture. Keep cohesive features together and dependencies directed toward stable contracts. Do not prescribe a monorepo, framework, component library, atomic-design hierarchy, or extra layers solely for neatness. Justify shared infrastructure with actual consumers and maintenance benefits.

### 3. Audit component families

For UI work read [component decisions](references/component-decisions.md) before classifying families. Inspect source, stories, tests, tokens, documentation, and rendered app uses together. Load Build's applicable accessibility and interaction guidance; use Audit Design only for a requested broader design audit.

Inventory every implementation, alias, wrapper, primitive, app-local copy, and style override by purpose, consumers, semantic element, interactions, state ownership, visual differences, variants, and owner. Naming and similar JSX alone cannot establish equivalence.

Classify each difference as a defect to standardize, legitimate variant, compositional slot, domain wrapper, distinct component, or temporary adapter. Record evidence and rejected alternatives. Choose a canonical implementation and map old APIs, imports, styles, defaults, and supported states to destinations. Resolve unexplained design divergence against the established design direction before choosing a winner.

### 4. Audit legacy, artifacts, and comments

Investigate dead exports, dependencies, assets, flags, routes, stale configuration, duplicate tooling, backups, abandoned tests, and accidentally committed generated artifacts. Static unused-code reports supply candidates. Before deletion inspect dynamic imports, reflection, registries, template/CSS references, generators, CLIs, external consumers, deployment scripts, and retention obligations.

Maintain a removal ledger with item, evidence of obsolescence, consumers checked, replacement, wave, verification, and recovery. Preserve deployed migration history, required records, vendor sources, and source-of-truth relationships. Regenerate outputs through their owner. Empty text search alone cannot justify deleting public APIs or resources.

Require comment-free handwritten code throughout the agreed cleanup scope: production, tests, scripts, markup, styles, examples, and comment-capable configuration. Inventory explanatory comments, docstrings, TODOs, suppressions, regions, and disabled code. Encode intent through names, types, structure, validation, and meaningful tests; move necessary rationale to external documentation. Fix suppressed diagnostics at their cause. Never substitute inert strings. Preserve required legal notices and executable or machine-interpreted metadata; raise conflicts that prevent compliance. Use language-aware tooling plus manual inspection and report unsupported languages and excluded sources.

### 5. Produce the master plan

Produce a durable audit and plan using the template. Include current and target ownership maps, evidence-linked findings, component decisions, explicit removals, conflicts, and coverage limits. Each finding needs severity, location, concrete consequence, evidence, and confidence. Distinguish defects, hypotheses, and deliberate tradeoffs; avoid invented quality scores and unsupported universal rules.

Assign stable task IDs and dependencies. Each task names repositories and paths, destination API or structure, migration steps and callers, compatibility policy, acceptance checks, rollback, and themed commit. Prioritize broken contracts and verification prerequisites before consolidation, consumer migration, removal, and enforcement. Separate mechanical moves and formatting from semantic changes when independently viable. Keep each committed wave usable.

Across repositories specify compatible producer-consumer versions, release order, adapters and removal conditions, lockfile updates, and recovery if only one side ships. Use incremental abstraction where it enables a supported transition. Record retained exceptions with owners and removal triggers.

Use [Pre-Mortem](../pre-mortem/instructions.md) against completion of this migration. Probe unknown consumers, false component equivalence, changed focus or state behavior, destructive deletion, production resolution, rule conflicts, and partial delivery. Amend checks and sequence accordingly. Present the audit and concrete plan before edits; ask only about unresolved consequential choices or genuinely missing authorization.

### 6. Implement on refactor branches

Before code edits create a dedicated branch in every affected Git repository, normally `codex/refactor-<topic>` in Codex, following host and project naming rules. Record bases and branch names. Use isolated worktrees when existing edits require isolation. Resolve policy conflicts with the requested branch workflow through the conflict procedure before proceeding.

Invoke [Build](../build/instructions.md) as a helper for each coherent wave. Pass task IDs, resolved decisions, affected consumers, authoritative rules, baseline failures, target boundaries, acceptance checks, comment-removal scope, and compatibility constraints. Expect code, verification evidence, and review findings; integrate and update the master plan before continuing. Build returns without separate objective evaluation.

Use [Ship](../ship/instructions.md) for themed commits on the refactor branches. Pass the commit-only delivery boundary, repository rules, exact task scope, related branches, and check results. Group by coherent outcome and explain the affected contract. Link related cross-repository SHAs in the ledger. The implementation request authorizes these commits; pushing, merging, releases, and deployment follow explicit user and repository authority. Preserve the branch route unless resolved project instructions override it.

### 7. Verify the integrated result

Run applicable project checks and Build's risk-based checks on the final dependency graph. Add characterization tests before risky changes to untested behavior, compatibility tests for migrations, and regression tests for defects. Avoid tests that mirror implementation. Exercise consumers using the built or packed library artifact, including declarations, exports, styles, themes, and runtime identity.

Exercise affected journeys in the actual runtime. For UI consolidation inspect relevant wide/narrow layouts, keyboard focus, semantics, loading/error/empty/disabled states, controlled/uncontrolled behavior, forms, persistence, SSR/hydration, and variant interactions. Select from actual risk and state which combinations ran; representative coverage does not establish all combinations.

Repeat duplicate, obsolete-reference, import-boundary, and language-aware comment checks. Reconcile each task and removal as complete, justified retention, user-agreed deferral, or blocked. Obtain Build's independent review over the integrated diff and both sides of package boundaries. Resolve substantiated findings and rerun affected checks. Report unavailable evidence.

### 8. Validate implementation

When invoked as a helper, return to the owning workflow without separate evaluation. For a skill with meaningful, deterministic, task-specific checks, invoke [Spawn Evals](../spawn-evals/instructions.md) once with a structured invocation record containing the original request, resolved constraints and their source, complete UTF-8 outputs, and machine-readable evidence. Its objective package in `src/evals/refactor/` defines only those checks. Report PASS, FAIL, or NOT PASSED — UNVERIFIED with the failing or unavailable verification steps. Do not use model judges, sub-agents, qualitative assessments, weighted scores, or synthetic scenarios. If no package exists for an objectively checkable skill, report NOT PASSED — UNVERIFIED; do not create one during an ordinary skill invocation. If no meaningful objective check is possible for this skill, omit this entire validation section and all Spawn Evals references from the skill.

Read [verification evidence](references/verification.md) when assembling the record. This package checks migration task references and dependency order only; engineering judgment and software correctness require the checks above.

## Output

Return the audit, master plan, component decisions, removal ledger, resolved rule changes, coverage, verification evidence, and remaining gaps. For implementation include branches, bases and resulting SHAs, themed commits, release ordering, rollback, and review status. State the objective result with its limits. Link durable artifacts. Claim completion only for the inspected and verified scope, with no silently skipped tasks or unresolved blocking findings.
