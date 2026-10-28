---
name: "show-me-your-work"
description: "Keep an evidence-linked decision log for long-running, multi-phase, or unattended work, then audit it before handoff."
version: "0.1.0"
created: "2026-10-27"
updated: "2026-10-28"
author:
  - "Josua Mittelstaedt"
references:
  - "Lauren Tan"
type: "discipline"
status: "experimental"
---

# Show Me Your Work

Keep one concise, reviewable record of consequential decisions and checkpoints. Record observable work, reasons, evidence, and results. Do not expose private chain-of-thought or turn the log into a transcript of every action.

## Scope

Use when the user asks for an audit trail, or when work is long-running, multi-phase, or unattended and a later reviewer needs to understand what changed and why. Also use when another skill or workflow hands off its decision log to this skill.

For routine, short tasks with no meaningful decisions to revisit, work normally without creating a log. For delivery-specific records such as a release checklist, use the skill that owns that delivery and invoke this skill only for the shared decision trail.

### Boundaries

Keep the log local by default. Commit or publish it only when the user requests that or the intended reviewer needs the trail to assess the result. Follow the caller's authorization and the repository's data-handling rules.

Do not record hidden reasoning, credentials, private data that is not needed to substantiate a decision, or unverified claims. Do not rewrite or remove earlier rows to make the run look cleaner. The current run may append a correction that identifies the row it supersedes.

## Inputs

Use the requested outcome, task work directory, current log if one exists, decisions and checkpoints made so far, evidence artifacts, and the host's available conversation or transcript access. Do not assume a transcript path or scan unrelated conversation histories. If a prior run's identity or timestamp range cannot be established, mark that gap instead of inventing it.

Use the [decision-log template](templates/decision-log-template.tsv) to start a new log. Keep this format authoritative when another skill delegates a decision trail here.

### Default Procedures

If you miss relevant information, first invoke [think-harder](../think-harder/SKILL.md), passing all unresolved constraints and all available context, including references and guidelines, over. If `think-harder` leaves one or more constraints unresolved, use [ask-user-question](../ask-user-question/SKILL.md) to inquire the missing information.

If any discipline is unavailable, perform it directly and report the fallback. Carry unresolved constraints forward and do not invent answers or pretend the dependency ran.

## Workflow

### 1. Decide whether a log will help

Create or continue a log when the user explicitly requests one, or when the work has multiple phases, meaningful branches, unattended execution, consequential pivots, blockers, or verification gates that a reviewer may need to reconstruct.

Log decisions and checkpoints, not routine tool calls or self-evident steps. For repeated loops, add one row per iteration only when the iteration changes a decision, result, or next action.

### 2. Choose the canonical log

Use `decisions.tsv` in the task work directory for one effort. When several efforts share a directory, use `.audit/<task-slug>.tsv`. Reuse the existing log for this effort rather than creating competing copies.

Keep it uncommitted by default. Commit it only when its evidence helps the intended reviewer trust or assess the delivered work. Do not create a public or shared copy without authorization.

### 3. Start or resume the run

Start a new log with the header from `templates/decision-log-template.tsv`. Use these six tab-separated columns in order: `ts`, `phase`, `decision`, `why`, `evidence`, and `result`.

Use a UTC timestamp in ISO 8601 form, such as `2026-10-27T15:04:05Z`. Keep each cell on one line. Write the decision in plain words, the reason briefly, the evidence as a resolvable path or link, and the result as an observed outcome or a clear state such as `open` or `INCONCLUSIVE`.

When resuming an existing log, read its latest rows before writing. If another run wrote since this run's last entry, begin this run's entries with a `start` row that identifies the prior timestamp range this run did not write and points to the current run using a host-provided identifier when available. Use `start` only for this purpose. If the range or identifier is unavailable, state that in the row rather than guessing.

### 4. Record meaningful checkpoints

Append one row when a decision, pivot, completed work unit, verification gate, blocker, or revert changes what the reviewer should understand. Include:

- **Decision:** what was chosen, changed, or stopped.
- **Reason:** why that action fit the task or what triggered it.
- **Evidence:** a concise pointer to the relevant commit, pull request, file and line, test output, screenshot, trace, or other artifact.
- **Result:** what the evidence showed, or what remains unresolved.

Use `open` or `INCONCLUSIVE` when work is pending or evidence does not settle the claim. Do not describe a planned check as a completed result. Keep cells on one line; if content contains tabs or line breaks, replace them with spaces. If a cell begins with `=`, `+`, `-`, or `@`, prefix it with a single quote so spreadsheet software does not treat it as a formula.

If an earlier row is wrong or incomplete, append a new row that names the superseded row and records the corrected facts. Preserve the original row as history.

### 5. Audit before handoff

Compare this run's rows with the conversation or transcript the host exposes and with the linked evidence. Check that:

1. Each row corresponds to a real decision, action, or checkpoint.
2. Each evidence pointer resolves and supports the claim in its row.
3. Important pivots, reversals, blockers, and verification outcomes are represented.
4. Pending work remains marked open or inconclusive.

If an entry is unsupported, inaccurate, or missing a key event, append a correcting or additional row. Do not edit earlier history. If the host does not expose the needed transcript or evidence, audit what is available and state the gap; do not search global histories or unrelated private conversations.

### 6. Review an existing trail

When the user asks to review or catch them up on an existing log, read it top to bottom and follow its evidence pointers where accessible. Summarize the decisions, outcomes, and unresolved items. Flag rows with missing or mismatched evidence and point to their timestamps. Do not alter the log unless the user also asks you to update it or the active work requires appending a correction.

If the host supports an authorized independent reviewer from a different model family, request a focused review of the log and accessible run record for weak evidence, unsupported verification claims, risky choices, and important omissions. Otherwise skip this optional review and report that it was unavailable or not run. Never claim a review, reviewer identity, or agreement that did not occur.

## Output

For a logging run, return the log path, the main decisions and outcomes it captures, unresolved items, and the evidence audit result. For a review-only request, return the summary and specific evidence gaps. State whether independent review occurred; when it did, include the reviewer's model if known and list actionable flags with the relevant row timestamps. Keep the handoff concise and do not include private chain-of-thought.
