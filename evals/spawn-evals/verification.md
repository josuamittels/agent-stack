# Initial verification

Date: 2026-10-25. Skill: spawn-evals 0.1.0, draft. This summary records synthetic and implementation checks, not a general performance guarantee or promotion to stable.

## Executed checks

- 23 deterministic Python regression tests passed. Coverage includes the 90 threshold, rejection despite a high total when a critical criterion fails, missing evidence, malformed and duplicate judgments, boolean-score rejection, applicability flags, exact repeatability, canonical hashing, changed inputs/outputs/evidence/configuration/resources/checks, frozen rubric versions, cache reuse, invocation deduplication, suite-marker requirements, path bounds and abstract storage.
- All four maintained SKILL.md files passed actual Ruby/Psych parsing, required metadata types, directory/name agreement, the exact Inputs paragraph and shared final-validation handoff. Maintained skill Markdown links resolve.
- The updated map parsed with Mermaid 11.17.2 and rendered in Chromium with @mermaid-js/layout-elk 0.2.0. The full rendering was inspected: the existing Admin Skills nodes are reused, shared validation and repair connections are visible, and no labels are clipped. Existing overall grouping/configuration was retained; the large map still has long connections.
- Privacy tests put sentinel strings into inputs, outputs, evidence and judge pointers and confirmed none reached saved records. Actual saved JSONL rows were also inspected against the allowlisted abstract field set. Runtime logs/cache are ignored by Git.
- An actual terminal self-verdict was recorded, then retrieved for an identical packet without another judge. Invocation deduplication and stale-suite rejection were independently exercised in temporary unit-test packages.

## Fresh-context synthetic suites

Each of four packages used three organic synthetic requests in separate low-effort producer contexts. Producers received temporary production copies with final validation omitted, so they did not see the scoring package or spawn recursive judges. Those adaptations limit these runs to production-stage behavior and are not a claim to have exercised a host's automatic live-skill activation.

Separate fresh Betabert contexts received neutral labels, task/input/output, frozen criteria and objective evidence. Expected verdicts, producer identity, prior scores and repair hypotheses were withheld. Judgment pointers were inspected before recording; only numeric outcomes and static abstract guidance were retained.

| Package | Active rubric | Latest three synthetic outcomes | Calibration result |
| --- | --- | --- | --- |
| natural-writing | v1 | 3/3 acceptable, 100/100 each | Satisfactory accepted; defective rejected at 57.5/100. |
| translate | v1 | 3/3 acceptable, 100/100 each | Satisfactory accepted; defective rejected at 50/100. |
| create-skill | v2 | 3/3 acceptable, 100/100 each | Satisfactory accepted; defective rejected at 0/100. |
| spawn-evals | v2 | 3/3 acceptable, 100/100 each | Satisfactory accepted; defective rejected at 25/100. |

The known-defective calibrations are intentionally rejected; these are successful discrimination checks, not live repair requests. Suite markers bind the completed records to current resource/setup/evaluator digests. Scores are small-suite observations, not estimates of real-world pass rates.

## Measurement corrections retained in history

The first evaluator-design rubric over-applied evaluator-internal obligations to a package designed for another skill. Its abbreviated satisfactory calibration lacked usable cases. Those failures were retained, the original rubric and cases preserved, and v2 made the requested-stage boundary explicit while replacing the abbreviated fixture with a concrete synthetic package. Weights, the acceptance threshold and critical gates were not relaxed.

The first authoring judge packets omitted original source material and preservation evidence. The judge correctly refused to infer those facts from a producer's claims. Later packets included source material and independently compared before/after resource digests. The authoring rubric was versioned to make research conditional on a predeclared research-stage flag; a naming clarification does not need research. Partial and incomplete earlier results remain distinguishable from later evidence-complete measurements.

No skill was silently edited as a response to a failed live evaluation. These were initial measuring-instrument and evidence-packet corrections within the approved setup work.

## Terminal evaluator assessment

One final fresh low-effort Betabert graded the implemented evaluator, maintained package, domain integrations and executed-check evidence. The deterministic engine scored that terminal meta-assessment at **100/100, acceptable**. It did not invoke a further validator or grade itself recursively.

This initial setup used 19 agents: 12 producers and seven judging passes, including calibration/evidence corrections and the terminal assessment. Ordinary use performs lightweight checks and one fresh Betabert call, or reuses an exact-match verdict without a new judge. Full synthetic suites run at setup or after relevant changes rather than after every ordinary invocation.

## Limits

The host's actual inherited model ID was not exposed; evaluator configuration is explicitly session-scoped rather than asserting an unverified model identity. Fresh AI judgment is not mathematically deterministic. Scoring arithmetic is deterministic, and identical complete evaluation packets reuse the stored verdict. Temporary producer copies and read-only judge assignments are context boundaries, not a claim to an OS-enforced sandbox.

Real host discovery and long-term live performance were not benchmarked. Shared invocation behavior is implemented through the template and skill instructions; no host hook, external service, installation, publication or commit was added. Rubric/example creation alone is never reported as a runtime pass.


## Bounded policy revision: 0.3.0 — 2026-10-25

This revision replaces the initial orchestration policy above. Live evaluation grades one existing result with at most one judge and no prerequisite suite. Post-edit evaluation consumes exactly three producer slots and one batched judge slot. Calibration and meta modes, caller self-evaluation, retries, repair/replay, automatic lifecycle changes, and upstream suite refreshes are removed. Reports end with good or not good.

The engine now records a request-bound target/mode budget before dispatch and rejects duplicate slots, extra scenarios, target switching, and replacement records. Historical larger packages and calibration records remain evidence only; the active suite selects only three cases. New callers must use begin/claim and carry the same evaluation ID. Stale suite markers no longer gate live recording. This is a breaking workflow change from 0.2.0, recorded as the next development minor.

All 36 local Python regression checks passed, including dispatch limits, cross-target binding, terminal missing evidence, absence of a live-suite prerequisite, legacy-case exclusion, score/evidence gates, retained stable sampling, and abstract storage. No model agents or qualitative evaluation were launched for this policy revision. Prior numeric scores in this record belong to the earlier revision and do not validate 0.3.0.
