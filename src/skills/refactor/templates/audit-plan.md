# Refactor audit and master plan

## Contract and coverage

Record requested mode, outcomes, project purpose and domain terminology, implemented users/roles and primary flows, repositories, bases, versions, instruction paths, supported consumers, preservation baseline, baseline commands/results, and inspected/sampled/excluded/unavailable areas.

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

## Established UI contracts and consolidation

Record authoritative component/token/style sources, code owners, consumer and supersession evidence, migration history, justified alternatives, and unresolved authority. Describe which implementations diverge from the same established contract and how consolidation preserves behavior and meaning. Do not propose a new design direction here.

| Existing pattern and contract | Duplicate/divergent implementations and consumers | Canonical source and evidence | Preserved differences | Migration/removal task | Regression verification |
| --- | --- | --- | --- | --- | --- |

## Removal ledger

| Item | Obsolescence evidence | Indirect/public consumers checked | Replacement or retention | Task | Verification and recovery |
| --- | --- | --- | --- | --- | --- |

## Translation and naming consistency

Record authoritative naming rules, supported locales, source locales and fallbacks, namespace/file/key organization, shared versus product ownership, loaders and extraction tools, locale parity exceptions, placeholder and plural/select contracts, hardcoded strings, and unresolved coverage. Distinguish structural migration from changes to translated meaning.

## Rename and reference ledger

| Old name, path, or key | Replacement and rationale | Affected products, locales, and consumers | Task and migration order | Compatibility or historical exceptions | Reference and runtime verification |
| --- | --- | --- | --- | --- | --- |

## Supplied decisions and out-of-scope observations

Reference existing approved decisions or supplied findings only where they establish a migration target or preservation constraint. Record optional product/design/content concerns separately without initiating audits or making improvements prerequisites for cleanup.

## Migration tasks

Assign unique IDs. For each task record dependencies, repositories/paths, proposed change, caller mapping, compatibility window, execution steps, acceptance checks, rollback, themed commit, and status. Document graph and execution order in machine-readable evidence as well.

## Agent coordination

Record the coordinator, audit questions and read-only coverage per agent, implementation domains, task IDs, exclusive writable paths, shared-file owners, contract prerequisites, integration order, and reviewer independence. Explain where fewer than three implementation agents or sequential execution better fits the dependency graph. Record scope transfers, returned evidence, and integrated results.

## Delivery and verification

Record per-repository branch/base/result SHAs, linked themed commits, compatible versions, release order, partial-delivery recovery, actual check results, runtime evidence, comment-scan scope, independent review findings/resolutions, and objective result with limits.

## Remaining work

Reconcile every finding and task as complete, justified retention, user-agreed deferral, or blocked. Include unknown consumers, unavailable verification, resolved conflicts, and adapter removal triggers. Do not silently omit items.
