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

## Removal ledger

| Item | Obsolescence evidence | Indirect/public consumers checked | Replacement or retention | Task | Verification and recovery |
| --- | --- | --- | --- | --- | --- |

## Migration tasks

Assign unique IDs. For each task record dependencies, repositories/paths, proposed change, caller mapping, compatibility window, execution steps, acceptance checks, rollback, themed commit, and status. Document graph and execution order in machine-readable evidence as well.

## Agent coordination

Record the coordinator, audit questions and read-only coverage per agent, implementation domains, task IDs, exclusive writable paths, shared-file owners, contract prerequisites, integration order, and reviewer independence. Explain where fewer than three implementation agents or sequential execution better fits the dependency graph. Record scope transfers, returned evidence, and integrated results.

## Delivery and verification

Record per-repository branch/base/result SHAs, linked themed commits, compatible versions, release order, partial-delivery recovery, actual check results, runtime evidence, comment-scan scope, independent review findings/resolutions, and objective result with limits.

## Remaining work

Reconcile every finding and task as complete, justified retention, user-agreed deferral, or blocked. Include unknown consumers, unavailable verification, resolved conflicts, and adapter removal triggers. Do not silently omit items.
