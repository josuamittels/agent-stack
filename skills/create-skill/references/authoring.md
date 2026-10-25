# Skill authoring conventions

Read while designing or revising a skill. These conventions supply instruction-writing, resource, handoff, and verification criteria; the creation workflow and approval boundaries remain in SKILL.md.

## Conventions

### Purpose and scope

Give each skill one clear responsibility. State the outcome it supports and when it applies. Add an exclusion when it prevents confusion with a neighboring skill. Search the existing stack before adding another owner for the same capability.

Include guidance that changes a decision: a non-obvious procedure, domain constraint, tool quirk, required artifact, verification standard, or stopping condition. Assume the agent already knows ordinary programming and writing practices. Ask of each paragraph: **What would the agent do differently because it read this?** Remove material that has no useful answer.

Keep personal preferences, account details, and machine-specific configuration in their authoritative context files. Reference those files when needed rather than embedding their values in reusable guidance.

### Language

Use plain language and imperative verbs for actions: read, compare, produce, verify, record. Name the object and expected result. Explain a rule when its reason helps the agent apply it correctly, especially when the constraint is surprising.

| Principle | Prefer | Avoid |
|---|---|---|
| Direct | “Read the existing API contract before changing the endpoint.” | “It is important to carefully consider existing contracts.” |
| Observable | “Continue when every requested behavior maps to a test or an explicit verification gap.” | “Continue once you understand everything.” |
| Conditional | “If the change alters a public interface, check its callers.” | “Always inspect every caller.” |
| Concrete | “Report the location, failure scenario, and supporting evidence.” | “Produce a thorough professional review.” |
| Positive | “Return findings in severity order.” | A list of prohibited output formats without a target format. |
| Proportionate | “Follow the repository’s existing error-handling convention.” | A tutorial on standard exception handling. |

Distinguish **required**, **default**, and **optional** behavior. Reserve “must,” “never,” and fixed sequences for real invariants, authorization boundaries, fragile operations, or demonstrated failures. Express exceptions as conditions the agent can observe. Keep recommendations flexible where several approaches can satisfy the task.

### Structure and context

Match the structure to the skill’s type. Routers need selection criteria and handoff behavior; workflows need actions and completion criteria; disciplines need decision principles; references need accessible conventions and examples. Use headings that serve the content rather than filling every possible section.

Keep the normal workflow and constraints shared by all branches in `SKILL.md`. Workflow steps can be listed directly in the skill. Move substantial branch-specific procedures, provider guidance, schemas, or detailed examples into supporting files when the current task needs only a subset.

Every external pointer states **when to read the file and what it supplies**. Resolve relative paths from the referring file’s directory. Keep each concept’s definition, rule, example, and exception together. Maintain one authoritative source for shared guidance; a simple reference is sufficient unless generation or host adaptation has a concrete benefit.

Split a capability into another skill when it needs independent discovery or reuse. Use a plain reference file for supporting knowledge that only needs to be reached from its owner. Loading every supporting file immediately defeats selective loading.

### Connections and handoffs

Name and locate the destination, then state the relationship: required method, conditional use, handoff, or optional recommendation. For a substantial handoff, specify the condition, required inputs, expected result, and what happens afterward. Keep the destination’s procedure in that skill.

For stack resource changes, invoke [update-map](../../../disciplines/update-map/SKILL.md) to maintain map structure and dependencies. Pass changed paths and calls or reference loading required for execution; exclude maintenance and repair coordination from map edges. Keep Mermaid conventions in the guideline it loads. Default disciplines `think-harder` and `ask-user-question` remain visible as nodes without relationship lines.

State whether a router recommends, invokes, or coordinates skills. Select by intent, current state, and available capabilities; trigger phrases are discovery hints. Respect explicit-only invocation policies. Reading a skill file does not necessarily reproduce the host’s invocation behavior, context isolation, or tool settings.

### Metadata, tools, and boundaries

Use valid YAML with spaces for indentation. Give `name` and `description` string values; match the name to its directory slug. Keep the description compact and discriminating: identify the capability and the situations that should select it. Put the procedure in the body. Use the shared template’s top-level metadata fields for version, date, type, and status; replace scaffold placeholders in completed skills.

Treat custom metadata as descriptive unless tooling explicitly consumes it. Invocation flags, tool allowlists, and model settings depend on the target host. A declaration does not install a tool, grant permissions, or authorize an external action.

Format `author` and `references` as YAML block lists with one name per item, including when there is only one author. Order references by relevance or contribution. Use verified real names in given-name then family-name order with conventional capitalization where available. Preserve established single names. Do not use source links or comma-separated strings for these properties.

Put repeatable mechanics in scripts when deterministic execution improves reliability. Keep command examples self-contained and make prerequisites discoverable. For state carried across steps, identify what is remembered or saved rather than assuming shell variables survive separate calls. Add bounded retries, cleanup, approval points, and missing-prerequisite behavior where the operation needs them.

## Examples

The following excerpts illustrate instruction patterns. Adapt them to the actual skill and available capabilities. Prefer one complete, representative example over several examples that repeat the same decision.

| Case | Example instruction |
|---|---|
| Router selection | “When requirements are settled and implementation is requested, invoke `build`. Pass the specification, constraints, and known verification gaps.” |
| Router ambiguity | “If the user wants an assessment of existing changes, choose `review-pr`. If they want those changes repaired, choose `build` and preserve the review findings as inputs.” |
| Workflow completion | “Before reporting the migration complete, verify that every source record is accounted for as migrated, rejected with a reason, or explicitly deferred. Report the counts and evidence.” |
| Reference guidance | “Use a sequence diagram for interactions over time. Use a flowchart for branching control flow.” |
| Discipline guidance | “Order findings by severity. For each finding, give the affected location, a concrete failure scenario, and evidence.” |
| Conditional loading | “For Cloudflare deployment, read `references/cloudflare.md` for provider-specific commands and verification. Load other provider guides only if the task involves them.” |
| Optional next action | “If independent review would resolve a contested design decision, recommend `fresh-setta-eyes`; explain the question the reviewer would answer.” |
| Missing prerequisite | “If the deployment target cannot be identified, finish local preparation and report the missing target before any deployment.” |

For a reusable skill handoff, make the contract explicit without copying the destination’s instructions:

```markdown
After implementation, use `review-pr` through the host’s supported skill mechanism.

Pass the requested outcome, complete change range, verification results,
and known gaps. Expect findings with severity, location, failure scenario,
and evidence. Resolve blocking findings within the authorized scope before
reporting completion; record unrelated suggestions separately.
```

For shared formatting or a rubric, use a plain reference with a loading condition:

```markdown
Before presenting a consequential choice, read
`../shared/decision-question-format.md` and apply its decision-brief format.
```

## Shared validation

Disciplines use relevant local checks only: omit the template’s final evaluation handoff, evaluator references, and discipline evaluation packages. Never evaluate a discipline, including through its caller.

For skills, use spawn-evals once for the requested completed result, unless the user excludes evaluation. After authoring, create-skill's separate approval checkpoint permits only the authored target's three scenarios and one judge. Do not add evaluation of create-skill, nested skills, dependencies, or the evaluator. No suite marker is a prerequisite for grading a live result.

Keep domain criteria in the target package, preserve the applicable handoff, and follow update-map for validation connections. Use the stack template's metadata schema and observable evidence. Prepared fixtures do not prove executed success. Report good or not good and stop, including on missing evidence or failure. The evaluator never starts repairs, replays, optimizations, or additional judging.
