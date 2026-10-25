---
name: ask-user-question
description: "Ask clear decision questions with context, recommendations, tradeoffs, and effort estimates. Use for consequential gaps left unresolved by context and Think Harder, or questions required by the caller."
version: "0.1.0"
updated: "2026-10-25"
author:
  - "Josua Mittelstaedt"
references:
  - "Garry Tan"
type: "discipline"
status: "draft"
---

# Ask User Question

Give the user enough information to choose without reconstructing the task. Keep questions compact, explain consequences, and make your recommendation explicit.

## Scope

Use within the owning workflow for unresolved user decisions, missing facts, or required interview questions. The caller owns execution and approval requirements. Preserve established answers and authorizations; do not create approval checkpoints for routine implementation choices.

## Inputs

Use the original outcome, caller and current stage, unresolved gaps, evidence, prior answers, permissions, alternatives, and host question-tool limits. Reuse the caller's Think Harder findings; inspect accessible context before asking for facts it already contains.

The shared procedure below describes the caller's sequence. Inside this discipline, apply the method directly; do not invoke yourself or send the same gap back through Think Harder. Reconstruct missing context where possible, then ask only what remains necessary.

### Default Procedures

If you miss relevant information, first invoke [think-harder](../think-harder/SKILL.md), passing all unresolved constraints and all available context, including references and guidelines, over. If `think-harder` leaves one or more constraints unresolved, use [ask-user-question](SKILL.md) to inquire the missing information.

If any discipline is unavailable, perform it directly and report the fallback. Carry unresolved constraints forward and do not invent answers or pretend the dependency ran.

## Workflow

### 1. Isolate the decision

Ask when the answer changes the next useful action or satisfies the caller's required question. Defer unrelated gaps until they matter. Ask one decision at a time; resolve prerequisites first. Separate commitments the user could independently accept or reject. Keep the code, tests, and documentation needed for one behavior together.

Offer meaningful alternatives for the same decision, including deferral or keeping the current state when viable. Ask an open question when the user must supply facts or describe an experience; do not invent alternatives to fit a selector.

### 2. Compose the brief

Use this format for discrete choices. Continue `D<N>` numbering throughout the owning task, including across handoffs and stages. Repeat the option fields for every alternative.

```text
D<N> — <one-line question>
Context: <task grounding, plain-language situation, and stakes>
Recommendation: <option> because <concrete reason>

A) <option label> (recommended)
✅ <concrete advantage>
✅ <second meaningful advantage>
❌ <honest disadvantage>
Estimate: <human effort range / agent-assisted effort range; assumptions>

B) <alternative label>
<same option fields>

Tradeoff: <what choosing between these options changes>
```

- **Context:** Use one or two sentences a non-specialist can understand. Name what changes for the user, what could break, or what would be lost.
- **Recommendation:** Mark exactly one option `(recommended)` and explain why it best serves the outcome. For a taste call, identify a neutral default and say there is no strong preference. A recommendation does not authorize the choice.
- **Pros and cons:** Give each option two meaningful pros and one honest con using the markers above, without character-count targets. Do not invent benefits or pad repeated points. If fewer distinct benefits exist, give those available; for a required hard stop with no real downside, state that directly.
- **Estimates:** For effort-bearing options, give approximate, comparable ranges for human effort and agent-assisted effort, with assumptions and uncertainty. Distinguish active effort from waiting when material. Write `unknown` for unsupported estimates; do not invent speedups. Omit this line for choices involving no effort.
- **Coverage:** When alternatives differ in coverage, add `Completeness: X/10 — <included and omitted coverage>` to each option. Anchor 10 to the complete stated outcome, 7 to the happy path, and 3 to a shortcut. These are explained judgments, not measurements. Omit scores for differences in kind; never hide a scope cut behind a score.

For an open question, use `Q<N> — <question>` followed by `Why I'm asking: <how the answer changes the work>` and invite a reply in the user's own words. Request concrete examples or necessary details without coaching a preferred answer.

### 3. Deliver through the host

Prefer an available question tool, following its actual schema and limits. Put the brief in supported question and option-description fields. Keep selectors short while preserving context, recommendation, pros, cons, and applicable estimates. Use literal Unicode for non-ASCII text instead of manually transcribing codepoints. If the tool cannot carry the required information, use prose.

Preserve every meaningful alternative when the tool's option limit is exceeded:

- **Mutually exclusive alternatives:** Show the full set and use clearly labeled pages or groups with a way to reach every choice. A first-page answer is provisional until the user has seen the remaining alternatives. Do not silently drop, merge, or defer options to fit.
- **Independent scope candidates:** Ask sequential `D<N>.k` questions using Include / Defer / Cut / Hold. Explain dependencies and conflicts before affected choices. Use prose if the tool cannot fit all four actions. Above six candidates, first ask whether to continue individually, narrow the set, or use coherent groups. Stop immediately on Hold and resume only when requested. Preserve prior answers, revisit affected choices to reconcile conflicts, then confirm the assembled scope after checking dependencies. This confirms the selected set, not permission for unrelated actions.

If no suitable tool exists or a call clearly fails before delivery, present the same brief in prose with explicit reply selectors, then wait. Retry at most once, only when the call certainly did not reach the user. If delivery is uncertain, preserve the pending question and avoid duplicate prompts. Never substitute a guessed answer for tool failure.

Before a prose question, finish independent tool work, then send the complete question as the turn's final message. Do not follow it with tools or another waiting message. With an asynchronous question tool, independent work may continue while the answer is pending. If human interaction is unavailable, return the unresolved decision to the caller; a subagent or unattended run does not acquire consent by choosing the recommendation.

### 4. Interpret and return

Wait for an answer before dependent work. A preselected option, silence, timeout, or recommendation is not an answer or approval. Apply a bare selector only when it identifies one unambiguous pending question; otherwise clarify its target. Accept clear free-text choices and corrections without forcing the user to repeat menu wording.

For an existing approval gate involving irreversible or destructive action, state the consequence and require an explicit, unambiguous choice. Clarify vague assent; reuse prior authorization that already covers the action.

## Output

Return answered question IDs, selected options or supplied facts, resulting constraints, and pending questions to the owning workflow. Preserve accepted scope cuts and their consequences in task state. Create a separate decision record only when the caller requires one. Check that each returned answer maps to the question actually asked; leave unresolved items explicit.

## Boundaries

Own question preparation, delivery, and interpretation. Do not restart routing, execute selected work, install question tools, or add gstack runtime dependencies. The caller retains execution, lifecycle, and validation responsibilities.
