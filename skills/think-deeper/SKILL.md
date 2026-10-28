---
name: "think-deeper"
description: "Deepen a substantive, well-scoped task with professional methods, primary inputs, suitable tools, and an independent check without enlarging its goal."
version: "0.1.0"
created: "2026-10-25"
updated: "2026-10-28"
author:
  - "Josua Mittelstaedt"
references:
  - "Felix Rieseberg"
  - "SirRobinBlibs"
type: "discipline"
status: "experimental"
---

# Think Deeper

Improve how the work is done. Keep the user's goal and deliverable the same; deepen the evidence, methods, tools, or verification only where they can change the result.

## Scope

Use when the user asks to go deeper or when a substantive task would benefit materially from professional methods and stronger evidence. Start after the intended outcome and constraints are sufficiently clear. Use [Think Harder](../think-harder/SKILL.md) to resolve ambiguity about what the user wants. Skip trivial lookups, quick answers, and pure formatting when deeper methods cannot change the result.

This discipline can prepare a prompt or guide authorized work. A request to rewrite a prompt ends with the rewritten prompt. A request to perform the task continues through the caller's workflow and authorization.

### Boundaries

Do not enlarge the goal, add deliverables, change acceptance criteria, or extend access, spending, installation, publication, communication, or persistent side effects without the authorization required by the caller. Ambition changes the quality of the approach, not the user's permissions. Do not invent methods, materials, or verification results.

## Inputs

Use the user's goal, requested deliverable, constraints, known assumptions, available source material, tools, access, and any acceptance criteria. Identify which details are established and which are assumptions. Do not assume that raw data, software installation, external services, or additional permissions are available.

### Default Procedures

If you miss relevant information, first invoke [think-harder](../think-harder/SKILL.md), passing all unresolved constraints and all available context, including references and guidelines, over. If `think-harder` leaves one or more constraints unresolved, use [ask-user-question](../ask-user-question/SKILL.md) to inquire the missing information.

If any discipline is unavailable, perform it directly and report the fallback. Carry unresolved constraints forward and do not invent answers or pretend the dependency ran.

## Workflow

### 1. Fix the goal and scope

State the requested outcome and deliverable in one sentence. Keep their size and boundaries fixed. If the prompt leaves a choice that could change the field or result, resolve it through the caller's clarification process before proceeding.

### 2. Identify professional work that would change the result

Name the relevant field or practitioner and the concrete steps they would take that the surface approach misses. Prefer actions over claims such as “be rigorous” or “use best practices.” Keep a step only if a capable non-expert might skip it and doing it could improve correctness, usefulness, or evidence. Describe the method, not an expert persona.

### 3. Find the primary material

Identify the most direct source that can answer the task: original records, data, code, logs, research papers, recordings, or other source artifacts. Inspect the material when it is available and relevant. If it is not available, name the access needed and the nearest usable proxy, including what the proxy cannot establish. Never claim to have accessed material you could not inspect.

### 4. Choose specific methods and tools

Select only methods and tools that fit the field, source material, and requested outcome. Name each method or tool and what it will establish. Confirm that it is available and authorized before relying on it. Drop tools that add process without improving the result.

### 5. Define an outside check

Before work begins, choose the strongest practical check that can disagree with the result. Prefer a runnable test, benchmark, reproduction, reconciliation, held-out data, or comparison with an authoritative source. An independent qualified reviewer can be useful when a tool-based check does not fit. State a pass condition precise enough to fail.

Do not use the producing model's confidence or self-review as the outside check. If no independent check fits, state that limit and identify the best available evidence without calling it independent validation. Use a challenging target only when it is measurable and compatible with the user's constraints; report feasibility and results honestly.

### 6. Rewrite the prompt or do the work

For a prompt rewrite, produce a concise, copyable prompt that keeps the original goal and deliverable size. Include the selected material, methods, tools, outside check, pass condition, and what to do if required access is missing. State what extra scope you deliberately left out when that guards against bloat. Stop after the rewrite unless the user also asked you to perform the task.

For an authorized task, briefly communicate material method choices, then continue through the caller's workflow. Treat the depth brief as execution guidance, not a separate approval checkpoint. If an action requires access or authority the caller does not have, stop that action and report the exact dependency.

### 7. Report observed evidence

Distinguish the proposed method and planned check from work actually completed. Report the check's observed result, any unmet pass condition, inaccessible inputs, and material limits. Do not claim success from a plan, a plausible explanation, or agreement between models.

## Output

For a prompt rewrite, return the unchanged goal, the chosen source material and methods, the outside check and pass condition, any missing access, and a copyable prompt. For task execution, report the work completed, evidence and check results, and remaining limits. Keep the explanation proportionate; do not make the response longer merely to display every step.
