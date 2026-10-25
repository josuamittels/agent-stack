---
name: create-skill
description: "Create new skills and disciplines, or propose and implement approved improvements to existing ones in the agent stack. Use when turning a described workflow into a skill, authoring SKILL.md, or fixing a skill's instructions, discovery, dependencies, or completion criteria."
version: "0.2.0"
updated: "2026-10-25"
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

If the name was not supplied, ask thoughtfully: "What shall we name this one? A skill deserves a name you've chosen." Reasoning cannot choose the name on the user's behalf. Use `disciplines/ask-user-question` to resolve a missing, invalid, or colliding name; do not silently rename or overwrite an existing skill. You may include suggestions to resolve the conflict in the request. From the name, derive a lowercase slug of letters, digits, and single hyphens, at most 64 characters, without leading or trailing hyphens.

For a skill modification, require an identifiable existing skill and the desired change or observed problem.

### Default Procedures

If you miss relevant information, first invoke `disciplines/think-harder`, passing all unresolved constraints and all available context, including references and guidelines, over. If `think-harder` leaves one or more constraints unresolved, use `disciplines/ask-user-question` to inquire the missing information.

Stack paths in backticks are relative to the repository root, identified by `templates/SKILL.md` and `map.mmd`. Use the host's invocation mechanism when available; otherwise read and apply the destination's instructions in context. Reading a file does not establish a separate agent invocation.

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

1. Invoke `disciplines/browse-skills` for related-skill discovery and inspection. Pass the contract, chosen name, relevant context and references, constraints, research questions, useful search terms, supplied sources or prior findings, and `sources/research_<skill-name>.md` as the record path.

2. Use `disciplines/research-web` to research domain facts, standards, or tool behavior beyond the skill sources. Keep that evidence in the same research record. Do not duplicate browse-skills' discovery procedure here or treat a listing as an inspected source.

Use the returned findings to choose what to incorporate into the original design or revision proposal. Resolve conflicts against the contract and explain adoption and rejection decisions in the research record. If essential research remains blocked, finish available investigation and obtain agreement to an evidence-limited draft before treating research as complete; reuse explicit agreement already supplied for that scope. This skill retains authoring, approval, attribution, lifecycle, and final evaluation responsibilities.

### 3A. Choose creation

Synthesize an original design from the contract and research. The user's creation request authorizes implementation within that scope.

### 3B. Choose approved revision

First present the observed problem, source evidence, concrete proposed changes, affected files and map connections, preserved behavior, and verification approach. Ask for implementation approval and wait before editing the target, its supporting resources, or map relationships. Research notes may be prepared beforehand. If the user already approved this specific proposal, proceed without requesting approval again. A materially expanded proposal needs renewed approval.

Combine related guideline and skill fixes into one proposal, and identify who owns each fix. When create-guidelines hands off a consumer update, use its approved scope and completed guideline changes. Update when and how the skill consults the guideline; keep domain conventions in the guideline instead of copying them into the skill. Send the outcome back to the create-guidelines coordinator. Identify any other affected callers, but do not change them unless they are included in the approved scope.

### 4A. Author the skill

For a skill, create `skills/<skill-name>/` and copy `templates/SKILL.md` to its `SKILL.md` before filling it in.

For a discipline, create `disciplines/<discipline-name>/` and copy `templates/SKILL.md` to its `SKILL.md` before filling it in.

Use this stack’s template rather than another creator’s initializer, and replace all scaffold placeholders. For every skill created or edited through this workflow, preserve these template sections verbatim:
- `### Default Procedures`, including all three shared Inputs paragraphs, at the end of ## Inputs.
- `### N. Validate implementation`, including its mandatory spawn-evals handoff, as the last step in the workflow (replacing N by the appropriate step number).

For a discipline, leave final evaluation to the calling workflow; do not add a nested final handoff. Put domain-specific checks and acceptance criteria in the target’s evaluation package rather than writing a second final-validation procedure.

Fill the template's top-level metadata: the chosen slug, a compact capability and activation description, version `0.1.0`, current date as `YYYY-MM-DD`, type `skill` or `discipline`, and status `draft`. The author should be set as the person creating the request, so ask the user for clarification if their name is unknown. Format `author` and `references` as YAML block lists. List only meaningful source influences in `references`, ordered by contribution, using verified personal names in given-name/family-name order or verified publishing organizations when individual authorship is not established. Keep source URLs and attribution evidence in the research record; use `references: []` if there are no external influences.

### 4B. Author the skill

Preserve the name, status, authorship, invocation policy, and working behavior unless the approved change calls for an adjustment. Update the date and meaningful source attribution.

Increment the version according to `guidelines/versioning`. If the edit is significant, you may add to the `author` list the user making the request, so ask the user for claification if their name is unknown.

Edit in place rather than reinitializing the skill. Apply the authoring conventions to scope, decision points, required outputs, resource loading, handoffs, and completion criteria. Link substantial supporting guidance only where it is needed. Add helpers only for concrete recurring mechanics, and exercise any new or changed executable helper.

### 5. Maintain the map and lifecycle

Invoke `disciplines/update-map` after authoring or changing a stack resource. Pass the changed paths, resource types, explicit calls and consulted references, obsolete relationships, and approved scope.

Invoke `disciplines/update-router` and pass the repository root, changed capability paths and types, authorized scope, and the completed map update with its remaining gaps. If the refresh cannot complete, report discovery maintenance as incomplete; do not claim that the new or changed capability is exposed. Follow this order for skill and discipline additions, changes, moves, and removals without restarting route selection for the active task.

Research files stay local under the repository's existing ignore rule. Do not change that rule or force-add them.

### 6. Mirror the completed work and request evaluation

Before validation, show the user what has been created or changed, with links to the authored skill and relevant resources. Summarize how the resulting skill works: what activates it, what inputs it uses, its main workflow and handoffs, and what it returns. Compare the result with the original request. Explain any deviations, their reasons, and their effect on behavior; state explicitly when there are none. Include material limitations and outstanding work so the user can review the actual result.

Then ask whether to complete evaluation through spawn-evals and wait for an explicit answer. Approval to create or edit a skill does not by itself approve this evaluation handoff. If the user already explicitly approved evaluation of this completed result, provide the mirror and reuse that approval. If evaluation is declined or deferred, leave the authored work in place and report evaluation as pending, without a score or passing verdict. If feedback changes the result, complete the authorized changes and mirror the revised result before requesting evaluation again.

This checkpoint covers the entire create-skill evaluation handoff: target package initialization or refresh, synthetic suite execution, and create-skill's own final grading. It applies when create-skill is called directly or by another skill. It does not add an approval step to ordinary invocations of the skills it authors.

### 7. Validate implementation

After the completed-work mirror and explicit evaluation approval, invoke `disciplines/spawn-evals` as the single final validator. First initialize or refresh the authored target's package under `evals/<skill-name>/`, passing the skill and resources, intended use, quality requirements, dependencies, and failure modes. Have it run the lightweight synthetic suite after initialization or relevant changes. Keep target setup/synthetic results distinct from evidence of real use.

Then pass create-skill's own completed authoring output, original requirements, research and change evidence, necessary input context, and invocation ID to spawn-evals for this invocation's final score. Its [evaluation package](../../evals/create-skill/suite.json) owns template metadata, YAML types, slug agreement, the required Default Procedures subsection at the end of Inputs, links, author attribution, approval boundaries, map correctness, discovery boundaries, and completion criteria. Use the stack template's schema rather than a foreign host validator's allowlist. For map checks, pass the update-map discipline and its Mermaid guideline with the returned evidence, including the rendering actually inspected.

Do not claim success from an authored rubric or an unexecuted fixture. Use spawn-evals' verdict and report material gaps. After an unacceptable result, ask for confirmation before another skill-edit round; specific prior approval is not permission for an unlimited repair loop. Target quality checks stay in its package rather than duplicated in this workflow. The original request remains in active task context for approved replay; keep only abstract outcomes in run history.

## Output

Before evaluation, return the completed-work mirror and evaluation approval question from step 6, with evaluation marked pending. After approved evaluation, return the skill and useful resources, the updated map, and evaluation package locations with the shared score and verdict. Concisely explain what was created or changed, which consulted skills meaningfully informed it and how, how the workflow handles its task, and how it connects to other skills, disciplines, and guidelines. Include verification results and material limitations; link the local research record while it is retained. For a proposed edit, return the concrete proposal and approval question instead of a completion claim.

## Boundaries

Creation does not authorize overwriting another skill, broad refactoring, host installation, publication, commits, or unrelated external writes. Editing follows the proposal approval boundary above. Keep evaluative side effects within the original authorization. A file on disk, a map node, and custom metadata do not install capabilities or establish host discovery.
