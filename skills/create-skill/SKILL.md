---
name: create-skill
description: "Create new skills and disciplines, or propose and implement approved improvements to existing ones in the agent stack. Prepare objective checks only when a skill has meaningful script-verifiable criteria."
version: "0.14.0"
created: "2026-10-25"
updated: "2026-10-30"
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

Own creation and improvement of `skills/<name>/SKILL.md` files, their capabilities, ownership and scopes, necessary supporting resources, research records, and relationships.

Create both skills and disciplines under `skills/`. Set `type: skill` for reusable workflows that produce a specific outcome, and `type: discipline` for reusable methods that guide how work is approached across different tasks. Disciplines can be used directly or through skills.

Route guideline creation to [create-guidelines](../create-guidelines/SKILL.md).

### Boundaries

Creation does not authorize overwriting another skill, broad refactoring, host installation, publication, commits, or unrelated external writes. Editing follows the proposal approval boundary above. Keep evaluative side effects within the original authorization. A file on disk, a map node, and custom metadata do not install capabilities or establish host discovery.

## Inputs

For a new capability, require the intended outcome, its type (`skill` or `discipline`), and a precise name.

If the name or type was not supplied, use [ask-user-question](../ask-user-question/SKILL.md) to resolve the user-owned choice. If the issue is instead uncertainty about a supplied name, inspect existing files and apply Think Harder before asking. Never silently rename or overwrite an existing capability. Check for a collision across all directories in `skills/`, regardless of their `type`, because skills and disciplines share one namespace. You may include suggestions to resolve the conflict in the request. From the name, derive a lowercase slug of letters, digits, and single hyphens, at most 64 characters, without leading or trailing hyphens.

For a capability modification, require an identifiable existing skill or discipline and the desired change or observed problem.

Before composing or revising skill or discipline instruction prose, apply [natural-writing](../natural-writing/SKILL.md) as an authoring helper. Read the [English guidelines](../../guidelines/languages/english.md), including the general guidance and specifically the [Technical style](../../guidelines/languages/english.md#technical). Use them to write the instructions in English. Return to this workflow without a separate writing evaluation.

This requirement governs the authored instructions. The resulting skill's task and user requirements determine the language and style of its output artifacts. Keep language rules in the English guideline and skill-specific workflow conventions in [authoring conventions](references/authoring.md).

### Default Procedures

When task input is needed from the user, route the question through [ask-user-question](../ask-user-question/SKILL.md) for preparation, delivery, and interpretation. First invoke [think-harder](../think-harder/SKILL.md) when ambiguity, missing information, or competing interpretations may be resolved from context, relevant guidance, evidence, or a reasonable default. Skip Think Harder for direct permission or approval gates, explicitly requested interviews, and facts or preferences only the user can supply. Ask only about consequential unresolved items. Continue independent work and preserve approval requirements.

If any discipline is unavailable, perform it directly and report the fallback. Carry unresolved constraints forward and do not invent answers or pretend the dependency ran.

## Workflow

For new skills, follow steps 1A, 2, 3, 4A, 5A, 6, 7, 8.
For skill revisions, follow steps 1B, 2, 3, 4B, 5B, 6, 7, 8.

### 1A. Establish the contract

Read the target or neighboring skills, the [shared template](templates/SKILL.md), and [authoring conventions](references/authoring.md).

Establish what should select the skill, its nearest competing capability, required and optional inputs, expected artifacts, relevant tools, boundaries, and observable completion criteria. Reuse supplied requirements rather than interviewing the user again. Continue when consequential gaps are resolved and the new name or existing target is settled.

### 1B. Understand the contract

Inspect supporting files, callers, existing metadata, and evidence of the reported failure. Treat unrelated local changes as work to preserve.

For evaluation-driven improvements, or changes involving a guideline you consulted, first read [repair ownership and handoffs](../create-guidelines/references/repair-handoffs.md). Trace the failure to the instructions that were actually used, then identify where the fix belongs:
- **Guideline:** domain rules, quality standards, and instructions for using tools or languages.
- **Skill:** selecting and loading guidelines, ordering workflow steps, managing handoffs, and validating results.

Before changing instructions, check whether the failure came from incorrect execution or flawed evaluation criteria.

If the evidence shows a guideline defect, invoke [create-guidelines](../create-guidelines/SKILL.md). Include the evidence, affected callers, approved scope, and the context needed to identify the coordinator and return the result. Resume any pending skill work when the result comes back. Do not start another handoff for the same issue if one is already active or completed.

### 2. Research comparable skills and web sources

When the user supplies one specific source to improve an existing skill or discipline, read that source directly and use it to adjust the existing instructions within the requested scope. Skip Browse Skills and broader source discovery. Record the source, relevant findings, limits, and proposed changes in `sources/research_<skill-name>.md`, then continue to step 3. Local inspection of the target and its supporting instructions still applies. If the source is inaccessible or leaves an essential gap, report the limit rather than substituting a broader search. Broaden research only when the user requests it.

For new capabilities and other revisions, use the research process below.

Establish the research questions from the contract: which comparable workflows, decision rules, tools, handoffs, and failure-handling approaches could improve this capability?

For an edit, include the reported domain and failure mechanism as well as the overall capability. Keep the intended outcome and constraints authoritative when assessing inspiration.

1. Invoke [Browse Skills](../browse-skills/SKILL.md) for related-skill discovery and inspection. Pass the contract, chosen name, context, constraints, research questions, search terms, supplied sources or prior findings, and `sources/research_<skill-name>.md` as the record path.

2. Research domain facts, standards, or tool behavior beyond the skill sources with Research Web when usable instructions are available. Otherwise use available web search and page-reading tools directly. Prefer primary sources. Record queries, sources, retrieval dates, findings, and limits in the same research record. If no web tool is available, record the gap and follow the evidence-limited-draft agreement rule below. Do not duplicate Browse Skills' discovery or treat a listing as an inspected source.

Use both research streams to inform the design. Resolve conflicts against the contract and record what to adopt or reject and why. If essential research remains blocked, finish available investigation and obtain agreement to an evidence-limited draft before treating research as complete; reuse explicit agreement already supplied for that scope.

### 3. Design and stress-test the skill

Invoke [Think Deeper](../think-deeper/SKILL.md) with the contract and research findings. Ask it to define the reusable outcome, trigger, inputs, boundaries, workflow and decisions, tools and resources, handoffs, outputs, and completion criteria. Decide which research insights fit this stack and which do not. Keep the user's goal and scope fixed.

Then invoke [Pre-Mortem](../pre-mortem/SKILL.md) on that concrete design. Use the first intended invocation as the horizon. Imagine the skill fails; probe its trigger, workflow, dependencies, handoffs, and completion conditions for omissions or failure paths. Apply actionable findings to the design and record changes, unresolved assumptions, or that no change was needed in the research record. Keep this pass proportionate and do not add scores or artifacts unless they change a decision. Begin authoring only after this review.

### 4A. Choose creation

Synthesize the final design from the contract, research, and pre-mortem changes. The user's creation request authorizes implementation within that scope.

### 4B. Choose approved revision

Present the observed problem, source evidence, post-pre-mortem changes, affected files, preserved behavior, and verification approach. Ask for implementation approval and wait before editing the target or supporting resources. If the user already approved this specific proposal, proceed without asking again. A materially expanded proposal needs renewed approval.

Combine related guideline and skill fixes into one proposal, and identify who owns each fix. When create-guidelines hands off a consumer update, use its approved scope and completed guideline changes. Update when and how the skill consults the guideline; keep domain conventions in the guideline instead of copying them into the skill. Send the outcome back to the create-guidelines coordinator. Identify any other affected callers, but do not change them unless they are included in the approved scope.

### 5A. Author a new skill

For a skill, create `skills/<skill-name>/` and copy [skill template](templates/SKILL.md) to its `SKILL.md` before filling it in.

For a discipline, create `skills/<discipline-name>/`, set `type: discipline`, and copy [skill template](templates/SKILL.md) to its `SKILL.md` before filling it in.

Store every reusable template used by the new skill under `skills/<skill-name>/templates/` (or `skills/<discipline-name>/templates/`). Do not put template files in `references/` or in a shared top-level template directory. Keep explanatory material and source guidance in `references/`.

Use this stack’s template rather than another creator’s initializer, and replace all scaffold placeholders. For every skill created or edited through this workflow, preserve these template sections verbatim:
- `### Default Procedures`, including both shared Inputs paragraphs, at the end of ## Inputs.
- `### N. Validate implementation` only when the skill has at least one meaningful, deterministic, task-specific check; replace N by the appropriate step number. When no such check is possible, omit this entire section and all Spawn Evals references from the target skill.

An authoring workflow prepares an objective package only for the distinct target skill it creates or edits, and only when that target has at least one meaningful, deterministic, task-specific condition that a script can verify from supplied output or evidence without judging meaning, quality, or correctness. `create-skill` is the authoring workflow, never an evaluation target: do not invoke Spawn Evals for `create-skill`, create or maintain `evals/create-skill/`, or evaluate the authoring workflow through Spawn Evals, including when revising `create-skill` itself. Generic checks such as “an output exists” do not qualify. For target skills with both qualitative goals and measurable requirements, package only the measurable requirements. If no meaningful objective check is possible, do not invoke Spawn Evals, create a package, or leave any Spawn Evals reference or runtime handoff in the target skill. Do not create an empty or placeholder rubric. In all cases, do not evaluate the authoring result. For Spawn Evals itself, preserve its bounded missing-input handling instead of adding shared clarification or delegation procedures. For a discipline, remove the template’s final runtime-check handoff; do not include evaluator references or create an `evals/<discipline-name>/` package. Verify discipline instructions and changed helpers with relevant local checks only. Disciplines neither invoke evaluations nor become evaluation targets.

Fill the template's top-level metadata: the chosen slug, a compact capability and activation description, version `0.1.0`, current date as `YYYY-MM-DD`, type `skill` or `discipline`, and status `draft`. Set the author to the person creating the request; when their identity is unknown, ask through [ask-user-question](../ask-user-question/SKILL.md) because only the user can supply it. Format `author` and `references` as YAML block lists. List only meaningful source influences in `references`, ordered by contribution, using verified personal names in given-name/family-name order or verified publishing organizations when individual authorship is not established. Keep source URLs and attribution evidence in the research record; use `references: []` if there are no external influences.

For an eligible target skill with at least one meaningful objective criterion, invoke [Spawn Evals](../spawn-evals/SKILL.md) after authoring to prepare a package containing a machine-readable rubric and executable checks for only those criteria. Pass the completed target instructions, intended uses, original requirements, and documented defaults and ranges. Package preparation validates the package structure only; it does not execute checks against the authoring result. On a later real invocation, the target skill supplies the structured invocation record to the checker. Do not use sub-agents, model judges, qualitative assessments, or synthetic cases. Never pass `create-skill` as the target to Spawn Evals. If no meaningful objective criterion is possible, skip Spawn Evals entirely, create no package, and remove the template's validation section and every Spawn Evals reference from the target skill. Disciplines do not get evaluation packages.

### 5B. Author a skill revision

Preserve the name, status, authorship, invocation policy, and working behavior unless the approved change calls for an adjustment. Update the date and meaningful source attribution.

Increment the version according to [versioning guidelines](../../guidelines/versioning/reference.md). If the edit is significant, you may add to the `author` list the user making the request, so ask the user for claification if their name is unknown.

Edit in place rather than reinitializing the skill. Apply the authoring conventions to scope, decision points, required outputs, resource loading, handoffs, and completion criteria. Link substantial supporting guidance only where it is needed. Add helpers only for concrete recurring mechanics, and exercise any new or changed executable helper.

### 6. Leave discovery maintenance to release

Do not refresh stack discovery during skill authoring. Release Agent Stack coordinates those updates when an authorized release changes capability availability, scope, or dependencies.

Research files stay local under the repository's existing ignore rule. Do not change that rule or force-add them.

### 7. Mirror the completed work

Before validation, show the user what has been created or changed, with links to the authored skill and relevant resources. Summarize how the resulting skill works: what activates it, what inputs it uses, its main workflow and handoffs, and what it returns. Compare the result with the original request. Explain any deviations, their reasons, and their effect on behavior; state explicitly when there are none. Include material limitations and outstanding work so the user can review the actual result.

Report the authored skill and prepared objective package when one applies, or state that objective checks do not apply without adding evaluator instructions to the skill. Report local verification only for a discipline. Do not evaluate the authoring result or request evaluation approval. Existing skills with objective criteria but no package remain unevaluated until a later authorized Create Skill edit prepares one.

### 8. Confirm implementation

For an authored skill with objective criteria, confirm the package rubric and checker are present and structurally valid. For a skill with no meaningful objective criteria, confirm there is no package and no Spawn Evals reference or handoff in the target. Package preparation is not an evaluation: do not run the skill's checks, create test scenarios, spawn producers, or grade the Create Skill result. Run appropriate local tests for changed evaluator infrastructure separately. When repairing a skill used for an original task, return the updated target and regenerated objective package to the owning workflow only when a package applies; it may run them on its completed invocation.

## Output

For a discipline, return the completed-work mirror, local verification results, and remaining gaps without an evaluation package. For a skill, return the completed-work mirror and either the applicable objective package with its measurable checks or the reason no objective package was created. Do not report a verdict on the authoring output. Explain how the workflow operates and connects to skills, disciplines, and guidelines. Link the local research record while it is retained. For an unapproved proposed edit, return the concrete proposal and approval question instead of a completion claim.
