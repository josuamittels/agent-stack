---
name: spawn-evals
description: "Prepare and run deterministic, objective checks for completed skill outputs without qualitative assessment or agent delegation."
version: "0.9.0"
updated: "2026-10-26"
author:
  - "Josua Mittelstaedt"
references:
  - "OpenAI"
type: "discipline"
status: "draft"
---

# Spawn Evals

### Boundaries

Do not dispatch producers, graders, calibration runs, or nested agents. Do not carry out target repairs. A failed result identifies the exact check; the skill owner decides whether to revise the skill. Do not rebuild old evaluation packages during general evaluator maintenance.

## Scope

Prepare an objective evaluation package only for a skill with at least one meaningful, deterministic, task-specific condition that a script can verify from supplied output or evidence. Run an existing package against one completed invocation. Checks are executable scripts with explicit inputs and pass conditions. Do not spawn agents, use model judges, create synthetic producer cases, infer qualitative quality, or calculate weighted scores. Skills with no meaningful objective check do not use this discipline and receive no package or runtime handoff.

Use [package setup](references/package-setup.md) when Create Skill hands off a newly created or edited skill. Use [the runner contract](references/runner.md) when executing checks or constructing an invocation record.

## Inputs

For package preparation, require the completed target skill, its intended uses, documented defaults and ranges, and the user's original requirements; Create Skill must first determine that at least one meaningful objective check is possible. For a live check, require the target skill, original request, resolved constraints, completed output files, evidence, and a unique invocation ID.

Each resolved constraint must include its value and provenance: `request` or `skill_default`. Explicit request bounds take precedence over skill defaults. The skill supplies normalized values it already used; the checker does not infer arbitrary limits from prose.

## Workflow

### Prepare a package after skill authoring

1. List only meaningful, task-specific conditions that a deterministic script can verify from the invocation record, output, or independent machine-readable evidence. Exclude writing quality, semantic correctness, and any criterion that depends on a model judgment. A generic existence or formatting check alone is insufficient. If no meaningful condition remains, do not create a package; return to Create Skill, which must omit this handoff and all Spawn Evals references from the target skill.
2. Create `evals/<skill>/rubric.json` and `evals/<skill>/checks.py` using the package contract. The rubric describes every check, its required inputs, its handler, and whether it is mandatory. The script returns one result per rubric check and names the verification step and aspect.
3. Build checks from the skill's declared request overrides and default ranges. Include boundary handling and a clear unverified outcome for missing inputs or unavailable external verification. For external links, check reachability only; do not claim that a reachable page validates its content.
4. Run `python disciplines/spawn-evals/scripts/runner.py --validate-package --skill <skill-slug>` to validate package shape and Python syntax without executing check handlers. Do not run target checks, authoring-result evaluations, synthetic scenarios, or agent calls during package preparation.
5. Return the package paths and summarize the measurable checks and their inputs. Do not claim that the skill passed an evaluation.

### Run checks for a completed skill invocation

1. Read the exact target package and the invocation record described in [the runner contract](references/runner.md). Do not create or rebuild a missing package during a skill invocation.
2. Run `python disciplines/spawn-evals/scripts/runner.py --skill <skill-slug> --record <record.json>` from the repository root. The runner loads the target package, reads complete output files, validates check results, and prints one JSON result.
3. If the package is missing, a required check cannot be verified, or checker inputs are unavailable, report **NOT PASSED — UNVERIFIED** and name the missing package, check, or input. Do not substitute a manual review.
4. Report **FAIL** for any mandatory check that returns `fail`. Report **PASS** only when all mandatory applicable checks pass. Include each failed or unverified check's verification step, aspect, observed value, expected value, and evidence location.
5. Return the artifact with the concise evaluation result. Do not add a separate score or qualitative assessment.

## Result contract

Each check returns `pass`, `fail`, `unverified`, or `not_applicable`. A mandatory failure determines overall `fail`; otherwise an unverified mandatory check determines `not_passed_unverified`; otherwise the result is `pass`. Optional and not-applicable checks do not block a pass. A missing package is unverified, never automatically generated or silently skipped.

The checker validates only its stated objective. Link reachability does not establish bibliographic identity or source findings. Counts and lengths establish only the supplied measurable limits. Report these boundaries plainly.
