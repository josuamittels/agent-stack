# Engine and storage contract

Read before using the Python helper. It uses only Python 3.9+ standard-library modules on Unix-like hosts; it does not call an API or choose a model. The coordinating agent runs checks and dispatches Betabert through the host's subagent tool. Invoke with a usable Python interpreter, not necessarily the system Python.

## Commands

Run from the repository root, or pass `--root /absolute/stack`:

```sh
python3 disciplines/spawn-evals/scripts/engine.py validate --skill translate
python3 disciplines/spawn-evals/scripts/engine.py status --skill translate
python3 disciplines/spawn-evals/scripts/engine.py prepare --skill translate
python3 disciplines/spawn-evals/scripts/engine.py lookup --skill translate
python3 disciplines/spawn-evals/scripts/engine.py record --skill translate
python3 disciplines/spawn-evals/scripts/engine.py mark-suite --skill translate
```

`validate` reads the package without stdin. Every other command reads one JSON value from stdin. Supply raw packets through an in-memory pipe or temporary file outside the repository; never interpolate user data into shell commands. No raw packets are stored by this helper.

The coordinator records the actual model identity when exposed. If the host exposes only inheritance, use `model: "inherited-parent"` plus an opaque `session_scope` in evaluator configuration; do not reuse those judgments across sessions or an observed model switch.

`status` takes `{"evaluator":{"model":"<actual model id>","reasoning":"low"}}` and reports whether a suite is required for the current setup. `mark-suite` takes the same evaluator configuration plus `fingerprints`, the returned record fingerprints for every synthetic case and both calibration artifacts. It verifies exact setup identity, expected verdicts, and actual completed records before writing the local suite marker. A rejected calibration artifact is an expected measurement, not a request to repair the real skill. Do not pass calibration results into the live repair loop.

`prepare` takes this packet before lookup and returns it with a boolean `qualitative_assessment`. It reads the authoritative target status from the manifest-listed `skills/<skill-name>/SKILL.md` or `disciplines/<skill-name>/SKILL.md` (a simple top-level status field). For stable live invocations it draws an integer uniformly from 0–99 and selects Betabert for 0–4. The draw is stored under `.local/sampling/` using only the hashed invocation ID, resource digest, and boolean; retries reuse it, and a changed revision needs a new invocation. Other statuses/modes always select qualitative assessment. Carry the returned field unchanged into `lookup` and `record`. Omitting the field preserves the older always-judge behavior. A caller cannot submit `false` without a matching stored skip decision for a stable live target.

`lookup` takes this packet:

```json
{
  "invocation_id": "opaque invocation token assigned by the coordinator",
  "mode": "live",
  "qualitative_assessment": true,
  "input": {"requirements": "original task requirements", "context": {}},
  "output": "completed output, or a JSON mapping of artifact paths to contents",
  "evidence": {},
  "flags": {},
  "checks": [{"id": "structure", "score": 2, "evidence": true}],
  "evaluator": {"model": "actual model id", "reasoning": "low"}
}
```

Allowed modes are `live`, `suite`, `calibration`, and terminal `meta` for spawn-evals itself. Synthetic modes also require `case_id` matching the maintained cases or calibrations. The identity covers every field except the invocation token, plus current resource bytes, active package/check bytes, engine and evaluator instructions. Reuse cannot be requested by an old version string alone. Repeated identical outcomes with changed input context or setup are different measurements.

`record` takes `{"packet": <that packet>, "judgments": <Betabert's judgments array>}`. Objective results belong only in `packet.checks`; judge results belong only in `judgments`. Each applicable evaluated criterion needs exactly one outcome from the correct source. For an authorized qualitative skip, pass an empty judgments array; all judge criteria are marked `qualitative-skipped` and excluded, including critical judge criteria. Each has `id`, integer `score` (0/1/2), and `evidence: true`; `error`, null scores, duplicate IDs, unknown IDs, or missing criteria produce incomplete. Evidence can demonstrate failure; lack of evidence cannot demonstrate success. Extra transient fields such as `pointer` are stripped before persistence. The coordinator verifies those pointers before recording.

On a cache hit, call `record` with the same packet and no new judgments; it reuses the saved result and records an abstract cache-reuse event. Repeated calls with the same invocation token return the existing result without a second log entry. Reusing that token for a different fingerprint is rejected; a repaired/replayed invocation needs a new token. Only complete outcomes enter the verdict cache. Live acceptance also requires a completed suite marker matching current resource, setup and evaluator digests.

## Storage and scoring

The weighted score is `100 × sum(weight × score/2) / sum(applicable weights)`. The script uses exact rational arithmetic for the acceptance threshold and rounds only the displayed score to one decimal. Conditional criteria require predeclared boolean context flags; critical criteria always apply within the evaluated sources. An authorized qualitative skip excludes judge criteria from scoring and evidence/critical gates, and normalizes only over remaining applicable objective weights. Thus all objective criteria scoring 2 yields 100, while no applicable objective criteria yields incomplete. A selected judge with missing evidence still yields incomplete; it cannot be turned into a skip. The threshold is fixed at 90, and every critical score must be 2.

Run records contain only timestamp, content fingerprints, skill/setup/evaluator digests, rubric version, mode, synthetic case ID when applicable, criterion numeric outcomes/status, aggregate score/verdict, cache-reuse status, the `qualitative_assessment` selection boolean, and static category/guidance from the maintained rubric. There is no stored original task, output, quotation, judge explanation, producer identity, or transcript. Active task context supplies detailed failure evidence for an approved repair. Abstract history alone cannot recreate a request.

All logging, verdict reuse and invocation deduplication share a package lock. Atomic JSON writes protect local cache/marker files, and JSONL appends occur under the same lock. Keep `runs.jsonl` and `.local/` ignored. Rubric and synthetic setup files remain maintained source. Never put real request details into rubric guidance; that guidance is intentionally persisted. Delete temporary packet files/snapshots when grading is complete.

## Check and delegation limits

The helper validates setup, identities, arithmetic and record shape. It does not verify that a model's evidence claim is true, provision a sandbox, enforce producer blinding, or execute arbitrary check commands. Those are explicit coordinator responsibilities. If a selected judge is unavailable or a necessary check fails to run, return incomplete. The record boolean indicates whether qualitative assessment was selected; the coordinator reports it as conducted only after the required evidence was verified (or reports a reused assessment from cache). Lifecycle metadata changes and the five-result history check in step 4 belong to the coordinator, not this scoring helper. Structural validation and evidence quality are criteria handled by this shared workflow, not a separate final validator in each skill.

## Approved adapters

`checks.py` accepts `protected` and `ui-limits` with transient packet JSON on stdin. Put specified tokens in `input.protected_tokens` and, when available, original source text in `input.source`; the checker preserves their source occurrence counts. Put a hard character limit in `input.max_characters`. No UI check is supplied when the predeclared `ui-limits` flag is false.

`checks.py structure --files <SKILL.md paths> --template templates/SKILL.md` parses YAML through Ruby/Psych and checks core template structure. If Ruby is unavailable, evidence is incomplete; it does not silently replace YAML parsing with a regex. `checks.py measurement` runs `test_engine.py` using the active Python interpreter. These are shared workflow adapters, not another final validation step. Point evidence at their actual command result. Execute new domain-specific checks directly from the package's approved checks directory.
