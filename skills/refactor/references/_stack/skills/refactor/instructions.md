---
name: "refactor"
description: "Audit and refactor codebases and interacting component libraries. Plan architecture, component consolidation, variants, conventions, and legacy removal; implement in themed commits on refactor branches when requested."
version: "0.2.0"
created: "2026-11-15"
updated: "2026-11-17"
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

Use for comprehensive cleanup, standardization, architectural consolidation, design-system consistency, component-library alignment, and obsolete-code removal, including scattered applications without a supplied design system or library. Support audit-only, plan-only, and implementation requests. For a bounded feature or defect use [Build](../build/instructions.md). Refactor owns the audit and migration plan; Build owns implementation quality and review; [Ship](../ship/instructions.md) owns authorized Git delivery.

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

For UI consolidation, give every domain agent the same resolved design direction, visual roles and tokens, canonical components, composition patterns, and documented exceptions. Assign shared tokens, typography, containers, and global styles to explicit owners. Reconcile cross-domain visual decisions before parallel edits so separate agents do not create competing standards.

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

Audit naming conventions across files, directories, packages, exports, component props, types, functions, routes, configuration, and translation keys. Establish the authoritative convention for each concern from project rules and actual contracts. Identify accidental casing, terminology, abbreviations, aliases, and singular/plural drift while preserving meaningful domain and language differences. Treat externally consumed names, URLs, persisted identifiers, and configuration keys as compatibility contracts; a rename needs a consumer migration or an explicit transition policy.

For localized products, inventory locale files, namespaces, resource loaders, source locales, fallback chains, extraction/generation tools, and translation ownership across all connected products and libraries. Compare directory and file organization, nesting versus flat keys, key naming, namespace boundaries, and how shared and product-specific messages are owned. Audit missing and extra keys, duplicate JSON keys, conflicting copies, hardcoded user-facing strings, unused-key candidates, interpolation names and types, plural/select branches, rich-text placeholders, and framework-specific message syntax. Check parity against the framework's rules: locales can legitimately require different plural categories or grammar. Do not flatten namespaces, merge equal-looking messages, or impose identical language structure without establishing semantic equivalence and translator context. Preserve translated values, fallback behavior, and locale-specific formatting during structural changes; use [Translate](../translate/instructions.md) for actual translation or localization work, passing the affected messages, locales, terminology, and placeholder constraints and returning the localized values to this migration.

### 3. Audit component families

Establish the design direction before choosing canonical UI implementations. Use supplied design-system files, brand guidance, component libraries, and approved decisions when available, then compare them with the actual product. Without those inputs, reconstruct the working system from rendered screens, recurring patterns, tokens, styles, stories, accessibility behavior, and repository history. A missing design-system file does not block the audit or justify inventing a new identity. State what is supplied, observed, inferred, or unresolved, with evidence paths and confidence.

Use relevant Git history, diffs, renames, deprecations, and migration notes to distinguish active design evolution from older implementations. Correlate recent changes with approved direction, repeated adoption, completeness across states, and runtime quality. A recent timestamp or majority usage alone does not make a pattern authoritative: a recent experiment can be wrong, while a mature component can remain canonical. File modification times are insufficient evidence. When history is unavailable, state the limit and use observable consistency without claiming chronology. Extrapolate routine missing cases from the best-supported direction; raise materially competing directions through the conflict procedure and resolve substantial new design decisions through [Design](../design/instructions.md), passing the evidence, affected surfaces, constraints, and open decisions and returning its implementable handoff to the master plan.

Read the [aesthetics framework](../../guidelines/aesthetics/reference.md) and apply its precedence and relevant domain guidance. For every UI consistency audit load [Interaction](../../guidelines/aesthetics/interaction.md), [Accessibility](../../guidelines/aesthetics/accessibility.md), [Composition](../../guidelines/aesthetics/composition.md), and [Typography](../../guidelines/aesthetics/typography.md). Load Colour, Iconography, and Motion through the framework when those decisions are affected, and platform references for native work. Keep numerical and domain standards in those authoritative guides. Apply coding conventions alongside aesthetics; visual cleanup must preserve semantics, supported behavior, and maintainable ownership.

Compare equivalent roles and tasks across routes, products, themes, viewports, and states. Audit text roles, actual font loading, size, weight, line height, tracking/letter spacing and kerning settings, measure, wrapping, hierarchy, and localized text. Inspect spacing rhythm, gaps, padding, alignment, grids, container widths, gutters, nesting, responsive breakpoints, density, surfaces, borders, radii, elevation, icons, and control sizing. Check computed styles and rendered results where possible: identical tokens can produce different output through inheritance, overrides, fallback fonts, or nested containers. Record the intended role and concrete inconsistency before changing a value; meaningful hierarchy and task-specific density need not be uniform.

Inventory repeated page-level solutions such as headers and actions, filter/toolbars, form sections, settings groups, list/detail layouts, cards, empty states, loading states, errors, and feedback. Where related tasks solve the same problem differently, compare their information hierarchy, interaction and accessibility contracts, content, and responsive behavior. Choose a canonical approach, compose reusable page sections or layouts, and reuse it across related cases when the contract holds. Keep domain compositions with their domain and product-independent primitives in their appropriate shared owner. Prefer stable slots and composition over copied markup or page-name flags; do not turn every page into one configurable mega-component.

For UI work read [component decisions](references/component-decisions.md) before classifying families. Inspect source, stories, tests, tokens, documentation, and rendered app uses together. Load Build's applicable accessibility and interaction guidance; use Audit Design only for a requested broader design audit.

Inventory every implementation, alias, wrapper, primitive, app-local copy, and style override by purpose, consumers, semantic element, interactions, state ownership, visual differences, variants, and owner. Naming and similar JSX alone cannot establish equivalence.

Actively detect outliers within component families, including implementations with different names or no shared import. For example, compare text inputs, textareas, search fields, selects, and date controls against the supported field design: label and help placement, text roles, height/density, padding, border/radius, surface, icons, focus treatment, error presentation, and disabled/read-only states. Compare equivalent roles and states at matching viewports and themes. Flag unexplained deviations even when each implementation works in isolation, then trace whether they come from an older component, copied markup, hardcoded values, stale CSS, an override, or an intentional requirement. Use source and history to substantiate possible legacy status; appearance alone establishes an outlier, not its age.

Apply the same comparison to buttons, cards, dialogs, navigation, tables, and repeated page sections. Record each outlier's location, rendered evidence, expected family contract, cause, confidence, and proposed consolidation or justified exception. For related field controls, reuse common field structure, tokens, and accessible state presentation where their contracts align while retaining appropriate control-specific semantics and interactions. Verify the resulting family together across real forms and journeys so consumers receive a consistent experience rather than isolated cosmetic fixes.

Classify each difference as a defect to standardize, legitimate variant, compositional slot, domain wrapper, distinct component, or temporary adapter. Record evidence and rejected alternatives. Choose a canonical implementation and map old APIs, imports, styles, defaults, and supported states to destinations. Resolve unexplained design divergence against the established design direction before choosing a winner.

Classify each implementation as canonical, a justified contextual alternative, an active transition, an experiment, obsolete, or unresolved. Support legacy/obsolete labels with supersession and consumer evidence, rather than visual age alone. Map each superseded component, composition, token, stylesheet, and local override to its replacement and removal task. Migrate consumers and supported states before deleting the old path, and remove overrides and aliases that would otherwise keep the previous design alive. Where no formal system exists, record the smallest useful role/token/component and composition contract in the project's maintained Markdown or existing documentation convention; do not require a new library package merely to establish consistency.

### 4. Audit legacy, artifacts, and comments

Investigate dead exports, dependencies, assets, flags, routes, stale configuration, duplicate tooling, backups, abandoned tests, and accidentally committed generated artifacts. Static unused-code reports supply candidates. Before deletion inspect dynamic imports, reflection, registries, template/CSS references, generators, CLIs, external consumers, deployment scripts, and retention obligations.

Maintain a removal ledger with item, evidence of obsolescence, consumers checked, replacement, wave, verification, and recovery. Preserve deployed migration history, required records, vendor sources, and source-of-truth relationships. Regenerate outputs through their owner. Empty text search alone cannot justify deleting public APIs or resources.

Require comment-free handwritten code throughout the agreed cleanup scope: production, tests, scripts, markup, styles, examples, and comment-capable configuration. Inventory explanatory comments, docstrings, TODOs, suppressions, regions, and disabled code. Encode intent through names, types, structure, validation, and meaningful tests; move necessary rationale to external documentation. Fix suppressed diagnostics at their cause. Never substitute inert strings. Preserve required legal notices and executable or machine-interpreted metadata; raise conflicts that prevent compliance. Use language-aware tooling plus manual inspection and report unsupported languages and excluded sources.

### 5. Produce the master plan

Produce a durable audit and plan using the template. Include current and target ownership maps, evidence-linked findings, component decisions, explicit removals, conflicts, and coverage limits. Each finding needs severity, location, concrete consequence, evidence, and confidence. Distinguish defects, hypotheses, and deliberate tradeoffs; avoid invented quality scores and unsupported universal rules.

For UI work include the evidenced design direction, chronology and inference limits, role/token mappings, canonical page compositions, justified exceptions, and a route-by-route migration matrix. Pair each visual inconsistency with its intended rule, replacement owner, affected consumers, and before/after acceptance evidence. Preserve distinct product identities where required; consistency applies within the appropriate system and role. Distinguish behavior-preserving cleanup from intentional visual or interaction changes and resolve consequential choices before implementation.

Assign stable task IDs and dependencies. Each task names repositories and paths, destination API or structure, migration steps and callers, compatibility policy, acceptance checks, rollback, and themed commit. Prioritize broken contracts and verification prerequisites before consolidation, consumer migration, removal, and enforcement. Separate mechanical moves and formatting from semantic changes when independently viable. Keep each committed wave usable.

Maintain an explicit rename and reference ledger for changed names, paths, string keys, namespaces, and public contracts. Map every old identifier to its replacement, affected locales and products, direct and indirect consumers, migration task, compatibility/removal condition, and verification. Trace references through code, templates, dynamic key construction, route builders, tests, stories, documentation, examples, fixtures, configuration, extraction manifests, and translation-platform mappings when accessible. Resolve dynamic references through framework-aware analysis and runtime evidence; a global text replacement is insufficient. Mark inaccessible products or external consumers as unresolved coverage rather than claiming all mentions are fixed.

Across repositories specify compatible producer-consumer versions, release order, adapters and removal conditions, lockfile updates, and recovery if only one side ships. Use incremental abstraction where it enables a supported transition. Record retained exceptions with owners and removal triggers.

Use [Pre-Mortem](../pre-mortem/instructions.md) against completion of this migration. Probe unknown consumers, false component equivalence, changed focus or state behavior, destructive deletion, production resolution, rule conflicts, and partial delivery. Amend checks and sequence accordingly. Present the audit and concrete plan before edits; ask only about unresolved consequential choices or genuinely missing authorization.

### 6. Implement on refactor branches

Before code edits create a dedicated branch in every affected Git repository, normally `codex/refactor-<topic>` in Codex, following host and project naming rules. Record bases and branch names. Use isolated worktrees when existing edits require isolation. Resolve policy conflicts with the requested branch workflow through the conflict procedure before proceeding.

Invoke [Build](../build/instructions.md) as a helper for each coherent wave. Pass task IDs, resolved decisions, affected consumers, authoritative rules, baseline failures, target boundaries, acceptance checks, comment-removal scope, and compatibility constraints. Expect code, verification evidence, and review findings; integrate and update the master plan before continuing. Build returns without separate objective evaluation.

When changing a name or resource structure, migrate every affected in-scope product and its references in the same coherent wave or the planned compatible sequence. Update translation lookups and resources for all supported locales, imports, exports, loaders, extraction configuration, generated outputs through their generators, tests, stories, examples, and documentation together. Preserve string meaning and placeholder contracts. Assign shared translation catalogs and naming maps to one agent owner. Retain old references only for documented supported compatibility or historical records that must remain accurate; identify them in the ledger rather than silently leaving stale mentions.

Use [Ship](../ship/instructions.md) for themed commits on the refactor branches. Pass the commit-only delivery boundary, repository rules, exact task scope, related branches, and check results. Group by coherent outcome and explain the affected contract. Link related cross-repository SHAs in the ledger. The implementation request authorizes these commits; pushing, merging, releases, and deployment follow explicit user and repository authority. Preserve the branch route unless resolved project instructions override it.

### 7. Verify the integrated result

Run applicable project checks and Build's risk-based checks on the final dependency graph. Add characterization tests before risky changes to untested behavior, compatibility tests for migrations, and regression tests for defects. Avoid tests that mirror implementation. Exercise consumers using the built or packed library artifact, including declarations, exports, styles, themes, and runtime identity.

Exercise affected journeys in the actual runtime. For UI consolidation inspect relevant wide/narrow layouts, keyboard focus, semantics, loading/error/empty/disabled states, controlled/uncontrolled behavior, forms, persistence, SSR/hydration, and variant interactions. Select from actual risk and state which combinations ran; representative coverage does not establish all combinations.

Review related screens together against the same resolved direction and aesthetics guidance. Compare before/after renders and computed styles for typography, space, containers, shared sections, and states; check that global token changes and removed overrides have not regressed other consumers. Exercise the full affected journey for consistent interaction and feedback, focus continuity, layout stability, responsive transitions, and motion/reduced-motion behavior where applicable. Smoothness needs runtime evidence, not a screenshot alone. Investigate new visual baselines before accepting snapshots. Reconcile each obsolete UI implementation and residual override against the migration matrix, including cases deliberately retained.

Repeat duplicate, obsolete-reference, import-boundary, and language-aware comment checks. Reconcile each task and removal as complete, justified retention, user-agreed deferral, or blocked. Obtain Build's independent review over the integrated diff and both sides of package boundaries. Resolve substantiated findings and rerun affected checks. Report unavailable evidence.

For translation changes, run the project's resource parser, duplicate-key and schema checks, message compiler or extractor, and locale/key/placeholder checks where available. Exercise changed lookups and interpolation in the actual products, including supported plural/select cases, fallback and missing-key behavior, lazy-loaded namespaces, and representative long-text and RTL layouts when supported and affected. Search every affected repository for old names and paths, inspect remaining matches, and reconcile them against the rename ledger. Verify dynamic callers and built artifacts separately. Completion requires that each affected product and locale is migrated and verified, or explicitly reported as blocked or user-agreed deferred; clean search output alone does not prove reference completeness.

### 8. Validate implementation

When invoked as a helper, return to the owning workflow without separate evaluation. For a skill with meaningful, deterministic, task-specific checks, invoke [Spawn Evals](../spawn-evals/instructions.md) once with a structured invocation record containing the original request, resolved constraints and their source, complete UTF-8 outputs, and machine-readable evidence. Its objective package in `src/evals/refactor/` defines only those checks. Report PASS, FAIL, or NOT PASSED — UNVERIFIED with the failing or unavailable verification steps. Do not use model judges, sub-agents, qualitative assessments, weighted scores, or synthetic scenarios. If no package exists for an objectively checkable skill, report NOT PASSED — UNVERIFIED; do not create one during an ordinary skill invocation. If no meaningful objective check is possible for this skill, omit this entire validation section and all Spawn Evals references from the skill.

Read [verification evidence](references/verification.md) when assembling the record. This package checks migration task references and dependency order only; engineering judgment and software correctness require the checks above.

## Output

Return the audit, master plan, component decisions, removal ledger, resolved rule changes, coverage, verification evidence, and remaining gaps. For implementation include branches, bases and resulting SHAs, themed commits, release ordering, rollback, and review status. State the objective result with its limits. Link durable artifacts. Claim completion only for the inspected and verified scope, with no silently skipped tasks or unresolved blocking findings.
