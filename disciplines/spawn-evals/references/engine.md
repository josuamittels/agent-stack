# Engine and storage contract

The Python helper owns arithmetic, abstract history, invocation deduplication, and dispatch budgets. The coordinator owns dispatch through host tools and must claim each slot before spawning. The helper does not call a model or intercept host tools.

## Bounded sessions

Run from the repository root with a usable Python 3.9+ interpreter. Commands take `--skill <target>` and optional `--root /absolute/stack`. The manifest must list `skills/<target>/SKILL.md` as its authoritative target; discipline targets are rejected. Except `validate`, each reads one JSON object from stdin. Keep raw packets outside the repository.

1. `begin`: pass `{"evaluation_id":"opaque ID for this authorized request","mode":"live"}` or mode `suite`. This binds the request to one target, mode, resource revision, and (for suite) the first three maintained cases. Re-entry returns the existing budget; it never resets attempts. Use the same evaluation ID throughout the request, including any nested callers.
2. `claim`: pass the evaluation ID and `role:"judge"`, or `role:"producer"` plus a selected `case_id`. Live permits one judge and no producers. Suite permits one producer per selected case and one judge after the three producer attempts. Slots are consumed before dispatch; failure does not refund them. A duplicate claim is terminal: report and stop.
3. `prepare`: pass the grading packet. This retains one 5% qualitative sample for stable live targets. Other statuses and suite mode require judging. Carry the returned boolean unchanged; a forged skip is rejected.
4. `lookup`: pass the prepared packet before dispatch. Reuse only identical complete inputs/setup. A changed digest invalidates reuse but never requests another suite. Suite readiness is never a live prerequisite.
5. `record`: pass `{"packet":<prepared packet>,"judgments":[...]}`. The request must have a begun budget and the applicable consumed slots. Record once per live result or selected scenario. Duplicate identical records return the old result; a replacement attempt is rejected.
6. `mark-suite`: pass evaluator configuration and exactly three recorded fingerprints from this evaluation. It summarizes good or not good even when a scenario failed or was incomplete; it does not demand a passing rerun.

`status` is informational: `suite_required` is always false. `suite_current` describes the historical marker only. There are no calibration or meta modes.

## Grading packet

Use `evaluation_id`, a per-result `invocation_id`, `mode` (`live` or `suite`), `case_id` for suite only, `input`, completed `output`, `evidence`, `flags`, `checks`, and `evaluator`. Evaluator configuration requires `model` and `reasoning:"low"`; if only inheritance is exposed, use `model:"inherited-parent"` and an opaque `session_scope`. No extra suite is authorized by a configuration change.

The packet hashes actual output/evidence content and relevant resource bytes. Do not pass producer identity, prior scores, expected judgments, or repair hypotheses. Missing output/evidence is a failed verification, not permission for another agent.

Each applicable objective outcome goes in `checks`; each judge outcome goes in `judgments`. An outcome needs a known `id`, integer `score` 0/1/2, and `evidence:true`. Missing, duplicate, malformed, or unsupported outcomes produce incomplete. Evidence pointers are transient and checked before recording; no correction pass is allowed.

## Decision and history

The internal weighted score is `100 × sum(weight × score/2) / sum(evaluated weights)`. Good requires at least 90 and every evaluated critical score equal to 2. A stable live qualitative skip excludes judge weights and gates; no objective weight means incomplete. Incomplete has no numeric score and reports **not good—unable to verify**. The `decision` field is `good` or `not-good`; legacy numeric outcomes and verdict fields remain for arithmetic/history compatibility.

A suite is good only when all three cases are good. Report per-case gaps, never an average that hides failure. No result triggers repair, optimization, lifecycle promotion, version changes, or another evaluation.

Package history, cache and locks stay under ignored `evals/<target>/.local/` and `runs.jsonl`. Cross-target request budgets stay under ignored `evals/.local/`. Persist only fingerprints, digests, numeric outcomes, static categories, and budget counters—not requests, artifact copies, explanations, or transcripts. Clean up temporary snapshots when done. Existing calibration records and larger case lists are historical; they never expand dispatch limits.
