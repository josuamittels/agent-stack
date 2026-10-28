---
name: "pre-mortem"
description: "Find concrete failure paths in an adjustable, consequential plan before commitment by imagining it has failed and working backward."
version: "0.1.0"
created: "2026-10-25"
updated: "2026-10-28"
author:
  - "Josua Mittelstaedt"
references:
  - "Gary Klein"
  - "Deborah J. Mitchell"
  - "J. Edward Russo"
  - "Nancy Pennington"
  - "Beth Veinott"
  - "Sterling Wiggins"
type: "discipline"
status: "experimental"
---

# Pre-Mortem

Find plausible ways a consequential plan could fail while its owner can still change it. Turn the strongest causes into checks or plan changes. A pre-mortem surfaces risks; it does not predict which outcome will occur.

## Scope

Use when the user asks for a pre-mortem, failure paths, or blind spots in a concrete plan before commitment. The plan needs a clear outcome and enough detail to analyze. Use another route for a vague idea, a factual question, editing feedback, or a decision whose relevant actions are already irreversible.

Use [Think Harder](../think-harder/SKILL.md) to resolve ambiguity about the intended plan or constraints. Use [Ask User Question](../ask-user-question/SKILL.md) for consequential missing facts that context cannot resolve.

An AI pass can surface candidate risks. It cannot supply private team knowledge, tacit experience, or the candor and coordination benefits of a live session. When those affect the plan, treat this analysis as preparation for the people who know the work.

### Boundaries

Do not present imagined causes as facts, forecasts, calibrated probabilities, or proof that the plan should stop. Do not invent private context or claim a simulated discussion represents a real team. Keep the decision and approval authority with the plan's owner. Do not add implementation, publication, spending, or other commitments beyond the user's request.

## Inputs

Use the plan, its owner, intended outcome, success condition, relevant time horizon, constraints, available records, and prior decisions. Recover details from the conversation and accessible files before asking for them. Distinguish known facts from assumptions.

### Default Procedures

If you miss relevant information, first invoke [think-harder](../think-harder/SKILL.md), passing all unresolved constraints and all available context, including references and guidelines, over. If `think-harder` leaves one or more constraints unresolved, use [ask-user-question](../ask-user-question/SKILL.md) to inquire the missing information.

If any discipline is unavailable, perform it directly and report the fallback. Carry unresolved constraints forward and do not invent answers or pretend the dependency ran.

## Workflow

### 1. Confirm the plan can be examined

Summarize the proposed action, desired result, and the point at which success or failure will be judged. Continue when the plan is concrete and a consequential part remains adjustable. Ask only for missing details that could change the failure analysis.

If no useful time horizon is available, ask for one. Do not invent a date and present it as the user's plan.

### 2. Set the failure premise

Name the horizon and outcome. State that the plan has failed, then ask what caused the failure. Treat failure as certain for the exercise; do not treat the premise as a forecast or assign probabilities without evidence.

### 3. Generate causes before evaluating them

Identify several distinct, specific causal paths anchored in the plan. Consider relevant execution steps, dependencies, resources, user or customer response, assumptions, external conditions, and ownership. Do not fill a quota with generic risks.

For a group exercise, have participants write causes independently before discussion. For solo analysis, make one pass across relevant angles and label it as model-generated. Do not claim human input, independent review, parallel agents, or team consensus unless it happened.

### 4. Consolidate and strengthen the candidates

Merge duplicate explanations without losing distinct causes. For each retained cause, give:

- **Failure path:** how the plan's details could lead to the stated outcome.
- **Basis:** the supporting fact or the assumption that still needs evidence.
- **Warning sign:** an observable signal that could appear before failure.
- **Response:** one practical prevention or damage-limiting action.

Rank by consequence and how directly the plan supports the cause. Keep the short list focused on risks that could change a decision. Do not imply a ranking is a measured likelihood.

### 5. Revisit the decision

State which plan changes or checks address the leading causes. If the analysis favors delaying, reducing, or dropping the plan, optionally examine the failure path of not acting. Keep the two cases separate and leave the decision with its owner.

For a plan involving a team, identify questions only its members can answer, such as workload, coordination, incentives, or reluctance to raise concerns. Recommend a live discussion when those answers materially affect the plan.

## Output

Return:

1. The failure premise and horizon.
2. A short, ranked list of specific failure paths, each with its basis, warning sign, and response.
3. The changes or checks that would most improve the plan, plus unresolved questions for its owner.
4. The limits of the analysis, including assumptions and any team knowledge it could not access.

Keep the result proportionate to the plan. Do not create a persistent record unless requested.
