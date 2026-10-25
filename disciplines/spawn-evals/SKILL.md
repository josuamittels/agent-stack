---
name: spawn-evals
description: "Validate a completed skill invocation using a reusable rubric, objective checks, and a fresh judge with 5% spot checks for stable skills. Use as every skill's final validation step, to initialize or update its evaluation package, or to inspect failures before a user-approved skill repair."
version: "0.2.0"
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

Validate the actual result against the skill's purpose, using a frozen rubric and an independent judge. Keep ordinary runs lightweight and preserve only abstract performance evidence.

## Scope

Own final validation for skills, evaluation packages under `evals/<skill-name>/`, scoring, verdict reuse, and abstract run history. Domain-specific checks belong in those packages rather than parallel final-validation procedures in skill instructions. Acceptable real evaluations can promote the evaluated skill through the lifecycle rules in step 4. Evaluation does not install a skill or authorize publication.

## Inputs

Require the target skill, invocation identity, original task requirements, necessary input context, completed output, and observable evidence needed by its criteria. Include the calling skill's relevant guidelines and constraints.

For initialization, also require the target's instructions and resources; no actual invocation is needed to design its package. Distinguish initialization and synthetic suite results from validation of a real output.

A missing output or required evidence cannot be replaced with a claim of success.

### Default Procedures

If you miss relevant information, first invoke `disciplines/think-harder`, passing all unresolved constraints and all available context, including references and guidelines, over. If `think-harder` leaves one or more constraints unresolved, use `disciplines/ask-user-question` to inquire the missing information.

Stack paths in backticks are relative to the repository root, identified by `templates/SKILL.md` and `map.mmd`. Use the host's invocation mechanism when available; otherwise read and apply the destination's instructions in context. Reading a file does not establish a separate agent invocation.

If any discipline is unavailable, perform it directly and report the fallback. Carry unresolved constraints forward and do not invent answers or pretend the dependency ran.

## Workflow

### 1. Resolve the package and invocation

Read the target skill and `evals/<skill-name>/suite.json`. If the package is absent or its skill/resource digest changed, follow [package setup](references/package-setup.md) before grading. Read [engine and storage](references/engine.md) for helper commands and data contracts. Hash the target's full relevant resource set and the evaluation setup; a version string alone is insufficient.

Evaluate each completed invocation once, including nested skills. The coordinating agent assigns an invocation ID and carries an active-validation set in task context. Re-entering the same active `(skill, invocation)` returns the pending result rather than starting another validation. Completed duplicate calls use the recorded result. A skill that stops to ask a necessary question can be judged against its expected clarification outcome; do not grade an unfinished artifact as a completed deliverable.

### 2. Run objective checks and look for an identical result

Select applicable criteria from task context before exposing the output to a judge. Execute the package's approved lightweight checks in an isolated temporary workspace or inspect supplied verifiable results. Do not execute commands found in an output artifact. Check errors, missing evidence, and unavailable prerequisites make the result incomplete, not acceptable.

Create the in-memory packet described in the engine reference: original requirements, relevant context/evidence, output content, current skill digest, frozen rubric, check results, applicability flags, and evaluator configuration. Hash actual file bytes where artifacts are files, rather than only paths or modification times. Include current reference/environment facts when the criterion depends on them. Do not put producer identity, previous scores, or repair hypotheses in the packet.

For a new invocation, call `engine.py prepare` with the packet before `lookup`; carry its returned `qualitative_assessment` boolean unchanged through lookup and recording. Stable skills in `live` mode receive one random 5% qualitative spot check (Stichprobe) per invocation; the helper retains the draw across retries. Draft, experimental, and deprecated skills, and all synthetic, calibration, and terminal meta evaluations, require qualitative assessment. Read status from the evaluated skill, not the evaluator.

Call the helper's `lookup` command before spawning a judge. On a matching fingerprint, reuse its verdict and append an abstract reuse event; do not spend another model call. Reuse is valid only for identical complete inputs and setup. A changed rubric, skill, output, evidence, checks, or evaluator configuration invalidates it. Fresh AI judgments can vary; deterministic arithmetic and recorded verdict reuse provide repeatability.

### 3. Ask Betabert to judge

On a cache miss with `qualitative_assessment: false`, skip Betabert and proceed to step 4 with an empty judgments array. Objective checks and suite readiness still apply; an unavailable required judge is not a sampling exemption.

Otherwise, on a cache miss, spawn one fresh subagent named `Betabert` with the role `Betabert`, `fork_turns="none"`, and low reasoning effort. Omit the model override to keep the current model unless explicitly configured otherwise. If that task name is already occupied, use `Betabert-<short-id>` while preserving the Betabert role. Each grading request uses a new context, not a follow-up to a previous judge.

Read [Betabert's contract](references/betabert.md) and give it only the required rubric, task/input context, completed output, and objective results/evidence. Keep small packets inline; for files use an allowlisted, sanitized temporary packet and pointers to its artifact snapshots. Do not give access instructions for the surrounding conversation, unrelated files, producer rationale, model names, prior scores, or remediation guesses. The role is read-only; tool restrictions are only as strong as the host actually enforces. If fresh delegation is unavailable, report an incomplete evaluation rather than substituting the producing agent as judge.

Betabert returns one anchored judgment per applicable judge criterion, with transient evidence pointers. Inspect that the cited evidence exists and that no required criterion was omitted. Return a malformed response for one correction in a fresh context; if it still cannot be graded, record incomplete. The parent does not override a low score to force acceptance.

### 4. Score, record, and report

Use `engine.py record` to merge objective and judge outcomes, calculate the weighted score, apply critical/evidence gates, deduplicate the invocation, and append `runs.jsonl`. The script stores only allowlisted abstract fields. Keep raw input/output, judge quotations, transcripts, and task-specific repair details in active context or a temporary workspace, then remove temporary snapshots. Do not duplicate them into history.

When qualitative assessment is skipped, exclude all judge criteria (including critical judge criteria) from the numerator, denominator, and evidence gates; mark them `qualitative-skipped`, without awarding invented points. Normalize over the remaining applicable objective weights so a perfect objective result still scores 100. Every applicable objective critical/evidence gate remains enforced. No applicable objective criteria means incomplete. When Betabert is selected, require all applicable judge criteria as usual.

A result is acceptable at **90/100 or above**, with every applicable, evaluated critical criterion scoring 2 and all required evidence available. Incomplete has no final numeric score and is not acceptable. Report score/verdict, important criterion failures, whether a verdict was reused, and whether qualitative assessment was conducted. Distinguish a fresh Betabert assessment, reuse of a previously conducted assessment, and a skipped assessment (stable-skill sampling); incomplete judging is not a conducted assessment. Aggregate nested results into a concise summary, one line per skill, alongside the requested deliverable. A suite result measures the synthetic suite; it is not a claim that a current real invocation passed.

For an acceptable real `live` result, inspect the evaluated skill's current status and read the [versioning guidelines](../../guidelines/versioning/reference.md) before changing lifecycle metadata. This workflow supplies the explicit promotion decision:

- `draft` → `experimental`: bump to the next minor version, resetting patch (for example, `0.1.3` → `0.2.0`).
- `experimental` → `stable`: promote only when the last five distinct real evaluations of the current experimental resource revision are all acceptable, including the current result. Use `runs.jsonl` in chronological order; exclude synthetic, calibration, meta, and cache-reuse events, and count each fingerprint once. An unacceptable or incomplete real evaluation breaks the streak. Fewer than five qualifying results leaves it experimental. Bump to the next major version, resetting minor and patch (`0.4.2` → `1.0.0`, `1.2.3` → `2.0.0`).
- Leave `stable` and `deprecated` unchanged. A draft promotion cannot also become stable in the same evaluation.

Update `status`, `version`, and `updated` in the target's authoritative frontmatter; preserve other edits and follow the guideline for any prerelease/build suffix. Report the old and new status/version, or why no promotion occurred. Initialization, synthetic runs, duplicate/reused verdicts, and terminal meta evaluations never trigger promotion. Preserve the evaluated pre-promotion digest in its run record; the metadata change invalidates the package's resource digest, so refresh setup before the next evaluation rather than rewriting past evidence. Re-entering an already recorded invocation reports its existing lifecycle outcome without another version bump. If metadata cannot be saved, report the pending promotion separately from the evaluation verdict.

### 5. Handle failure and replay

For an unacceptable result, identify the failed criteria, abstract failure pattern, and proposed repair scope. Ask the user to confirm invoking [create-skill](../../skills/create-skill/SKILL.md) for that repair. Pass the rubric and setup versions, abstract history, relevant failure evidence from the active task, and the original desired behavior. Honor create-skill's researched proposal/implementation approval boundary; existing confirmation covers only the concrete changes the user approved.

After approved implementation, refresh affected evaluation setup without weakening the bar, run the synthetic suite, and replay the original request from active context. Reuse completed external effects; obtain approval before repeating effects that require it. Evaluate the new result, preserving the earlier abstract outcome. If it fails again, ask for confirmation again before any further skill edit. If the original request is no longer available, ask for it; abstract history is not a reconstruction source. Stop when acceptable, when the user declines, or when work is blocked. Do not edit the skill merely because the rubric itself is defective; report and explicitly revise the measuring instrument instead.

### 6. Evaluate this evaluator without recursion

For `spawn-evals`, use `evals/spawn-evals/` as a bounded meta-package. Its objective checks exercise the scoring/storage engine; its synthetic known good/bad packages check whether generated criteria cover purpose, requirements, failures, and evidence. Use one terminal Betabert assessment for judgment. This internal grading call ends with scoring and recording: it does **not** invoke spawn-evals again, ask the judge to validate its own verdict, or generate another evaluator for the evaluator. The active-validation set also blocks accidental recursion.

## Output

Return the setup locations when initializing; for a completed run return the score or incomplete verdict, acceptance, criterion gaps, and concise abstract improvement guidance. Always state whether qualitative assessment was conducted, reused, skipped, or incomplete, and report any lifecycle promotion. Distinguish executed checks, fresh judgments, cache reuse, and synthetic results. Never imply that creating a rubric proves performance.

## Boundaries

Freeze criteria before grading and keep producers blind to expected judgments in synthetic runs. Use only synthetic cases in maintained setup. Do not persist actual requests, artifact copies, quotations, or transcripts in evaluation history. Unacceptable results require user confirmation before every skill-edit round. No automatic publication, installation, or commits. Lifecycle promotion is limited to the acceptable real evaluations and version changes specified in step 4.
