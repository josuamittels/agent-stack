# Repair ownership and handoffs

Read when create-skill or create-guidelines investigates evaluation feedback, routes a defect, or updates a consumer as part of a guideline change. This protocol owns coordination; each skill owns its authoring procedure.

## Diagnose from evidence

Inspect the failing output, the requirement it violates, the guideline and skill passages in force, and evidence that the consumer loaded the relevant guide. Classify each demonstrated cause before proposing changes.

| Cause | Owner | Example |
| --- | --- | --- |
| Incorrect, inconsistent, ambiguous, or missing domain rules; tool or language usage; quality conventions | create-guidelines | The guide teaches invalid Mermaid syntax, or omits the condition for a valid TypeScript pattern. |
| Guide selection or loading; general workflow order; handoff or validation procedures | create-skill | The skill loads the wrong language guide, consults a guide after producing output, or skips validation. |
| Both layers contribute | Both, in one coordinated proposal | A guide needs an exception and its consumer needs an instruction to consult that section before drafting. |
| Correct instructions were available and properly loaded, but not followed | Report the execution failure first | One output ignores an explicit rule; the evidence does not yet establish an instruction defect. |
| Incorrect evaluation criterion, fixture, or scoring expectation | Evaluation package | A case rejects a valid convention permitted by the actual requirements. Revise the measuring instrument explicitly; keep that separate from production repairs. |

Use the smallest correction that addresses the cause. Domain quality belongs in the guide even when discovered through a skill evaluation. General orchestration belongs in the skill even when the failure appears in domain output. Do not copy domain rules into each caller as a workaround for a shared guide defect. Ask when evidence cannot establish the cause; avoid assigning every low score to a document defect.

## Carry one repair context

The initiating skill coordinates the repair and records, in active task context:

- Original request and invocation identity, demonstrated failure, and relevant evidence.
- Affected guideline and consumer paths, proposed changes by owner, and exact approved scope or pending approval.
- Return destination, pending consumer work, completed changes and evaluation identities, and active handoffs keyed by target and repair issue.

Present related changes together. Existing approval covers that specific proposal; obtain approval only for a new or materially expanded change. A request to investigate or propose leaves production files unchanged until implementation is approved. Read-only investigation and research records may proceed.

## Route and resume

When create-skill diagnoses a guideline defect, invoke create-guidelines with the repair context. Create-guidelines returns the guideline result, evidence, affected callers, and any required consumer work to the coordinating create-skill invocation. The coordinator resumes its pending skill edits and evaluations; create-guidelines does not open another create-skill call for that same work.

When create-guidelines starts the task and the user requests consumer integration, author the guideline and invoke create-skill for the approved consumer changes. Pass the completed guideline change and return context. Create-skill treats that completed repair as an input and returns its consumer result rather than reopening it.

If a handoff reaches an already active target for the same issue, return to the existing coordinator with the finding instead of nesting another invocation. A newly discovered material issue becomes a proposal for additional scope, not an automatic mutual-call loop. Keep real original requirements in active context for replay; abstract evaluation logs cannot reconstruct them.

## Completion and evaluation

Each owner reports actual files changed, preserved behavior, compatibility concerns for other callers, completed evidence, and unresolved work. The coordinator aggregates nested results without claiming a child result validates the whole repair. Follow each owner's validation instructions. Create-guidelines uses its direct task-completion check without subagents or evaluation packages. Where another owner's workflow calls for spawn-evals, use it once per completed invocation and reuse its identity for repeated requests. An unacceptable evaluation result requires user confirmation before another repair round; prior approval is not an unlimited retry authorization.
