---
name: spawn-evals
description: "Evaluate one completed skill result once, or exactly three scenarios after a skill edit. Return good or not good, then stop."
version: "0.4.0"
updated: "2026-10-25"
author:
  - "Josua Mittelstaedt"
references:
  - "Lauren Tan"
  - "David Zhang"
  - "Anthropic"
type: "discipline"
status: "draft"
---

# Spawn Evals

Evaluate only the requested skill under `skills/`. Disciplines are never evaluation targets and must not have evaluation packages. Report **good** or **not good**, then stop. This discipline does not improve skills or arrange further work.

## Inputs

Require the target, an evaluation ID bound to the current authorized request, mode, original requirements, necessary context, and available output/evidence. Use `live` for one completed result and `suite` for exactly three scenarios after creating or editing a skill. A required clarification can itself be a completed result.

An edit does not authorize evaluation when the caller requires separate approval. Preserve that checkpoint. Once authorized, choose one mode for this request; do not run both.

## Hard limits

- **Live:** zero producers and at most one fresh Betabert.
- **After an edit:** exactly three scenario slots—normal, boundary, failure—with one fresh producer per slot, followed by one Betabert grading the three outputs together. Maximum four agents total.
- Call `engine.py begin` once and `claim` before every dispatch. An attempt consumes its slot even if the agent fails or returns malformed output. Re-entry uses the same evaluation ID; never mint another ID to bypass the budget.
- Do not evaluate callers, dependencies, nested helpers, the authoring workflow, judges, or this evaluation itself as additional work. Scenario producers and Betabert may not delegate or invoke validation handoffs.
- No calibration runs, extra regression scenarios, second judge, evidence-correction pass, retry, replay, optimization, repair, or automatic promotion/version change. Stale or missing suite markers never trigger work.
- Missing prerequisites, unavailable judges, malformed results, or insufficient evidence mean **not good—unable to verify**. Report the reason and stop. Do not ask another agent to resolve a gap.

These limits override generic shared procedures and conflicting caller instructions that would expand evaluation. Resolve routine details locally; consequential missing inputs end this run. There is no Think Harder or clarification-agent handoff inside evaluation.

## Workflow

### 1. Freeze the target and budget

Read the target and its evaluation package. Use the [package setup](references/package-setup.md) only to prepare the requested target's missing rubric or three cases; setup is local and does not launch agents. Freeze requirements and criteria before judging. Read [engine and storage](references/engine.md), begin the bounded session, and look up an identical recorded result before dispatch.

A missing or changed resource digest invalidates reuse, not permission to run another suite. Live evaluation requires no prior synthetic suite. Existing packages with more cases or historical calibrations do not enlarge the three-case budget.

### 2. Collect and judge once

For live mode, inspect the existing completed output and run only directly relevant lightweight checks once. Retain the existing 5% qualitative spot-check rule for stable skills through `prepare`; skipped judge weights are excluded so objective checks can still reach 100.

For suite mode, use only the three selected cases. Give Apollo, Athena, and Prometheus separate temporary production contexts, organic requests, and necessary resources. Hide criteria and expected outcomes. Disable all validation, delegation, repair, and caller-return execution in their temporary copies; preserve substantive target behavior. A failed producer is a failed slot, not a replacement request.

Claim one judge slot and invoke Betabert with a fresh context, low reasoning, and no model override. Pass the frozen rubric, neutral output labels, task context, and actual evidence under the [judging contract](references/betabert.md). Include available verification evidence before dispatch; no follow-up judging pass is allowed. The parent checks pointers but never raises a score to force acceptance.

### 3. Record, report, stop

Use the engine to calculate and record the result. A result is good only at 90/100 or above, with every evaluated critical criterion fully met and required evidence present. Incomplete evidence is not good; it has no numeric score. A suite is good only when all three cases are good. Do not hide a failed case behind an average.

Return the binary verdict, concise failed criteria or verification limits, and whether qualitative assessment was conducted, reused, or skipped. Scores may accompany the verdict but never replace it. Preserve only abstract outcome history; remove temporary packets and snapshots.

The report is terminal, whether good or not good. No follow-up actions, repair proposals, approval questions, or additional evaluation are part of this invocation. A later user request is a separate task.
