---
name: create-skill
description: "Create new skills and disciplines, or propose and implement approved improvements to existing ones in the agent stack. Prepare objective checks only when a skill has meaningful script-verifiable criteria."
version: "0.8.1"
updated: "2026-10-26"
author:
  - "Josua Mittelstaedt"
references:
  - "OpenAI"
  - "Matt Pocock"
  - "Anthropic"
  - "Jesse Vincent"
  - "Daniel Miessler"
  - "Microsoft"
  - "Lauren Tan"
  - "Affaan Mustafa"
type: "skill"
status: "experimental"
---

# Create Skill

Turn a user's description into a researched, reusable skill with clear decisions, useful handoffs, and evidence of completion. Improve existing skills through a researched proposal followed by approved implementation.

## Scope

Own creation and improvement of `skills/<skill-name>/SKILL.md` and `disciplines/<discipline-name>/SKILL.md`, their capabilities, ownership and scopes, necessary supporting resources, research records, and relationships.

Create skills under `skills/` with type `skill`. Skills are reusable workflows that produce a specific outcome.
Create disciplines under `disciplines/` with type `discipline`. Disciplines are reusable methods that guide how work is approached across different tasks, meant to be used directly or through skills.

Route guideline creation to [create-guidelines](../create-guidelines/SKILL.md).

## Inputs

For a new skill, require the intended capability and a precise name for a new skill.

If the name was not supplied, ask thoughtfully: "What shall we name this one? A skill deserves a name you've chosen." Reasoning cannot choose the name on the user's behalf. Use [ask-user-question](../../disciplines/ask-user-question/SKILL.md) to resolve a missing, invalid, or colliding name; do not silently rename or overwrite an existing skill. You may include suggestions to resolve the conflict in the request. From the name, derive a lowercase slug of letters, digits, and single hyphens, at most 64 characters, without leading or trailing hyphens.

For a skill modification, require an identifiable existing skill and the desired change or observed problem.

Before composing or revising skill or discipline instruction prose, apply [natural-writing](../natural-writing/SKILL.md) as an authoring helper. Read the [English guidelines](../../guidelines/languages/english.md), including the general guidance and specifically the [Technical style](../../guidelines/languages/english.md#technical). Use them to write the instructions in English. Return to this workflow without a separate writing evaluation.

This requirement governs the authored instructions. The resulting skill's task and user requirements determine the language and style of its output artifacts. Keep language rules in the English guideline and skill-specific workflow conventions in [authoring conventions](references/authoring.md).

### Default Procedures

If you miss relevant information, first invoke [think-harder](../../disciplines/think-harder/SKILL.md), passing all unresolved constraints and all available context, including references and guidelines, over. If `think-harder` leaves one or more constraints unresolved, use [ask-user-question](../../disciplines/ask-user-question/SKILL.md) to inquire the missing information.

If any discipline is unavailable, perform it directly and report the fallback. Carry unresolved constraints forward and do not invent answers or pretend the dependency ran.

## Workflow

For new creation of skills, follow steps 1A, 2, 3A, 4A, 5, 6, 7.
For modification of existing skills, follow steps 1B, 2, 3B, 4B, 5, 6, 7.

### 1A. Establish the contract

Read the target or neighboring skills, the [shared template](../../templates/SKILL.md), and [authoring conventions](references/authoring.md).

Establish what should select the skill, its nearest competing capability, required and optional inputs, expected artifacts, relevant tools, boundaries, and observable completion criteria. Reuse supplied requirements rather than interviewing the user again. Continue when consequential gaps are resolved and the new name or existing target is settled.

### 1B. Understand the contract

Inspect supporting files, callers, existing metadata, and evidence of the reported failure. Treat unrelated local changes as work to preserve.

For evaluation-driven improvements, or changes involving a guideline you consulted, first read [repair ownership and handoffs](../create-guidelines/references/repair-handoffs.md). Trace the failure to the instructions that were actually used, then identify where the fix belongs:
- **Guideline:** domain rules, quality standards, and instructions for using tools or languages.
- **Skill:** selecting and loading guidelines, ordering workflow steps, managing handoffs, and validating results.

Before changing instructions, check whether the failure came from incorrect execution or flawed evaluation criteria.

If the evidence shows a guideline defect, invoke [create-guidelines](../create-guidelines/SKILL.md). Include the evidence, affected callers, approved scope, and the context needed to identify the coordinator and return the result. Resume any pending skill work when the result comes back. Do not start another handoff for the same issue if one is already active or completed.

### 2. Research comparable skills

Establish the research questions from the contract: which comparable workflows, decision rules, tools, handoffs, and failure-handling approaches could improve this capability?

For an edit, include the reported domain and failure mechanism as well as the overall capability. Keep the intended outcome and constraints authoritative when assessing inspiration.

1. Invoke [browse-skills](../../disciplines/browse-skills/SKILL.md) for related-skill discovery and inspection. Pass the contract, chosen name, relevant context and references, constraints, research questions, useful search terms, supplied sources or prior findings, and `sources/research_<skill-name>.md` as the record path.

2. Use `disciplines/research-web` to research domain facts, standards, or tool behavior beyond the skill sources. Keep that evidence in the same research record. Do not duplicate browse-skills' discovery procedure here or treat a listing as an inspected source.

Use the returned findings to choose what to incorporate into the original design or revision proposal. Resolve conflicts against the contract and explain adoption and rejection decisions in the research record. If essential research remains blocked, finish available investigation and obtain agreement to an evidence-limited draft before treating research as complete; reuse explicit agreement already supplied for that scope. This skill retains authoring, approval, attribution, lifecycle, and the decision whether objective checks are suitable for the target.

### 3A. Choose creation

Synthesize an original design from the contract and research. The user's creation request authorizes implementation within that scope.

### 3B. Choose approved revision

First present the observed problem, source evidence, concrete proposed changes, affected files and map connections, preserved behavior, and verification approach. Ask for implementation approval and wait before editing the target, its supporting resources, or map relationships. Research notes may be prepared beforehand. If the user already approved this specific proposal, proceed without requesting approval again. A materially expanded proposal needs renewed approval.

Combine related guideline and skill fixes into one proposal, and identify who owns each fix. When create-guidelines hands off a consumer update, use its approved scope and completed guideline changes. Update when and how the skill consults the guideline; keep domain conventions in the guideline instead of copying them into the skill. Send the outcome back to the create-guidelines coordinator. Identify any other affected callers, but do not change them unless they are included in the approved scope.

### 4A. Author the skill

For a skill, create `skills/<skill-name>/` and copy [skill template](../../templates/SKILL.md) to its `SKILL.md` before filling it in.

For a discipline, create `disciplines/<discipline-name>/` and copy [skill template](../../templates/SKILL.md) to its `SKILL.md` before filling it in.

Use this stack’s template rather than another creator’s initializer, and replace all scaffold placeholders. For every skill created or edited through this workflow, preserve these template sections verbatim:
- `### Default Procedures`, including both shared Inputs paragraphs, at the end of ## Inputs.
- `### N. Validate implementation` only when the skill has at least one meaningful, deterministic, task-specific check; replace N by the appropriate step number. When no such check is possible, omit this entire section and all Spawn Evals references from the target skill.

An authoring workflow prepares an objective package only when the authored skill has at least one meaningful, deterministic, task-specific condition that a script can verify from supplied output or evidence without judging meaning, quality, or correctness. Generic checks such as “an output exists” do not qualify. For skills with both qualitative goals and measurable requirements, package only the measurable requirements. If no meaningful objective check is possible, do not invoke Spawn Evals, create a package, or leave any Spawn Evals reference or runtime handoff in the target skill. Do not create an empty or placeholder rubric. In all cases, do not evaluate the authoring result. For Spawn Evals itself, preserve its bounded missing-input handling instead of adding shared clarification or delegation procedures. For a discipline, remove the template’s final runtime-check handoff; do not include evaluator references or create an `evals/<discipline-name>/` package. Verify discipline instructions and changed helpers with relevant local checks only. Disciplines neither invoke evaluations nor become evaluation targets.

Fill the template's top-level metadata: the chosen slug, a compact capability and activation description, version `0.1.0`, current date as `YYYY-MM-DD`, type `skill` or `discipline`, and status `draft`. The author should be set as the person creating the request, so ask the user for clarification if their name is unknown. Format `author` and `references` as YAML block lists. List only meaningful source influences in `references`, ordered by contribution, using verified personal names in given-name/family-name order or verified publishing organizations when individual authorship is not established. Keep source URLs and attribution evidence in the research record; use `references: []` if there are no external influences.

For a skill with at least one meaningful objective criterion, invoke [Spawn Evals](../../disciplines/spawn-evals/SKILL.md) after authoring to prepare a package containing a machine-readable rubric and executable checks for only those criteria. Pass the completed instructions, intended uses, original requirements, and documented defaults and ranges. Package preparation validates the package structure only; it does not execute checks against the authoring result. On a later real invocation, the target skill supplies the structured invocation record to the checker. Do not use sub-agents, model judges, qualitative assessments, or synthetic cases. If no meaningful objective criterion is possible, skip Spawn Evals entirely, create no package, and remove the template's validation section and every Spawn Evals reference from the target skill. Disciplines do not get evaluation packages.

### 4B. Author the skill

Preserve the name, status, authorship, invocation policy, and working behavior unless the approved change calls for an adjustment. Update the date and meaningful source attribution.

Increment the version according to [versioning guidelines](../../guidelines/versioning/reference.md). If the edit is significant, you may add to the `author` list the user making the request, so ask the user for claification if their name is unknown.

Edit in place rather than reinitializing the skill. Apply the authoring conventions to scope, decision points, required outputs, resource loading, handoffs, and completion criteria. Link substantial supporting guidance only where it is needed. Add helpers only for concrete recurring mechanics, and exercise any new or changed executable helper.

### 5. Maintain the map and lifecycle

Invoke [update-map](../../disciplines/update-map/SKILL.md) after authoring or changing a stack resource. Pass the changed paths, resource types, explicit calls and consulted references, obsolete relationships, and approved scope.

Invoke [update-router](../../disciplines/update-router/SKILL.md) and pass the repository root, changed capability paths and types, authorized scope, and the completed map update with its remaining gaps. If the refresh cannot complete, report discovery maintenance as incomplete; do not claim that the new or changed capability is exposed. Follow this order for skill and discipline additions, changes, moves, and removals without restarting route selection for the active task.

Research files stay local under the repository's existing ignore rule. Do not change that rule or force-add them.

### 6. Mirror the completed work

Before validation, show the user what has been created or changed, with links to the authored skill and relevant resources. Summarize how the resulting skill works: what activates it, what inputs it uses, its main workflow and handoffs, and what it returns. Compare the result with the original request. Explain any deviations, their reasons, and their effect on behavior; state explicitly when there are none. Include material limitations and outstanding work so the user can review the actual result.

Report the authored skill and prepared objective package when one applies, or state that objective checks do not apply without adding evaluator instructions to the skill. Report local verification only for a discipline. Do not evaluate the authoring result or request evaluation approval. Existing skills with objective criteria but no package remain unevaluated until a later authorized Create Skill edit prepares one.

### 7. Confirm implementation

For an authored skill with objective criteria, confirm the package rubric and checker are present and structurally valid. For a skill with no meaningful objective criteria, confirm there is no package and no Spawn Evals reference or handoff in the target. Package preparation is not an evaluation: do not run the skill's checks, create test scenarios, spawn producers, or grade the Create Skill result. Run appropriate local tests for changed evaluator infrastructure separately. When repairing a skill used for an original task, return the updated target and regenerated objective package to the owning workflow only when a package applies; it may run them on its completed invocation.

## Output

For a discipline, return the completed-work mirror, local verification results, and remaining gaps without an evaluation package. For a skill, return the completed-work mirror, updated map, and either the applicable objective package with its measurable checks or the reason no objective package was created. Do not report a verdict on the authoring output. Explain how the workflow operates and connects to skills, disciplines, and guidelines. Link the local research record while it is retained. For an unapproved proposed edit, return the concrete proposal and approval question instead of a completion claim.

## Boundaries

Creation does not authorize overwriting another skill, broad refactoring, host installation, publication, commits, or unrelated external writes. Editing follows the proposal approval boundary above. Keep evaluative side effects within the original authorization. A file on disk, a map node, and custom metadata do not install capabilities or establish host discovery.
