# Refactor audit and master plan

## Contract and coverage

Record requested mode, outcomes, repositories, bases, versions, instruction paths, supported consumers, baseline commands/results, and inspected/sampled/excluded/unavailable areas.

## Rules and decisions

| Rule or conflict | Authority and path | Consequence | User decision | Markdown amendment |
| --- | --- | --- | --- | --- |

## Architecture

Describe current and target ownership, package graph, import direction, state/schema ownership, runtime boundaries, package consumption, and release ordering. Justify each proposed structural change.

## Findings

| ID | Severity | Location and evidence | Concrete consequence | Confidence | Proposed action |
| --- | --- | --- | --- | --- | --- |

## Component families

| Family | Implementations and consumers | Purpose/semantics/state | Differences and variants | Decision and rationale | Canonical owner and API mapping | Checks |
| --- | --- | --- | --- | --- | --- | --- |

## Design direction and UI consistency

Record supplied design authorities, observed patterns, relevant Git evolution and supersession evidence, inferred direction, confidence, competing directions, and unavailable history or renders. Record the selected aesthetics/coding guidance and resolved decisions. Without a supplied system, define the minimum maintained visual-role, token, component, and page-composition contract needed for this product.

| Role or repeated task | Routes/products and rendered evidence | Inconsistent typography, space, container, composition, or behavior | Intended rule and canonical owner | Migration task and justified exceptions | Before/after and runtime checks |
| --- | --- | --- | --- | --- | --- |

Classify implementations as canonical, contextual alternatives, transitions, experiments, obsolete, or unresolved. Link obsolete components, tokens, styles, and overrides to replacements and removal tasks. Include all affected consumers and supported states; distinguish intentional visual changes from behavior-preserving refactoring.

Include a component-family outlier pass: compare equivalent roles and states, record unexplained deviations from shared design foundations, trace their causes and possible legacy origins, and resolve each through consolidation or an evidenced exception. For form fields include labels/help/errors, text roles, density, padding, borders, surfaces, icons, focus, and disabled/read-only presentation across actual forms.

## Removal ledger

| Item | Obsolescence evidence | Indirect/public consumers checked | Replacement or retention | Task | Verification and recovery |
| --- | --- | --- | --- | --- | --- |

## Translation and naming consistency

Record authoritative naming rules, supported locales, source locales and fallbacks, namespace/file/key organization, shared versus product ownership, loaders and extraction tools, locale parity exceptions, placeholder and plural/select contracts, hardcoded strings, and unresolved coverage. Distinguish structural migration from changes to translated meaning.

## Rename and reference ledger

| Old name, path, or key | Replacement and rationale | Affected products, locales, and consumers | Task and migration order | Compatibility or historical exceptions | Reference and runtime verification |
| --- | --- | --- | --- | --- | --- |

## Migration tasks

Assign unique IDs. For each task record dependencies, repositories/paths, proposed change, caller mapping, compatibility window, execution steps, acceptance checks, rollback, themed commit, and status. Document graph and execution order in machine-readable evidence as well.

## Agent coordination

Record the coordinator, audit questions and read-only coverage per agent, implementation domains, task IDs, exclusive writable paths, shared-file owners, contract prerequisites, integration order, and reviewer independence. Explain where fewer than three implementation agents or sequential execution better fits the dependency graph. Record scope transfers, returned evidence, and integrated results.

## Delivery and verification

Record per-repository branch/base/result SHAs, linked themed commits, compatible versions, release order, partial-delivery recovery, actual check results, runtime evidence, comment-scan scope, independent review findings/resolutions, and objective result with limits.

## Remaining work

Reconcile every finding and task as complete, justified retention, user-agreed deferral, or blocked. Include unknown consumers, unavailable verification, resolved conflicts, and adapter removal triggers. Do not silently omit items.
