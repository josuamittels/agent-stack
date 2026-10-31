---
name: "research-workflow"
description: "Fixed document structures, phase completion requirements, and Research handoff ownership."
version: "0.3.2"
created: "2026-10-30"
updated: "2026-10-31"
author:
  - "Josua Mittelstaedt"
references:
  - "Federico De Ponte"
type: "reference"
status: "experimental"
---

# Research workflow and handoffs

Read before starting or resuming a report. The skill owns orchestration; [artifact contracts](artifacts.md) own record fields. All phases run in the caller's context. Scripts never author findings or make model calls.

## Fixed structures

The machine-readable [structures template](../templates/structures.json) fixes section IDs, purposes and headings. `init` copies these into the outline and creates ordered files. Depth changes content and word budgets, not the document type or section inventory.

| Research report | Literature review |
| --- | --- |
| Executive summary | Summary |
| Research question and scope | Review question and scope |
| Search and selection methods | Search and selection methods |
| Findings and evidence synthesis | Evidence overview |
| Discussion and implications | Thematic synthesis |
| Limitations and unresolved questions | Disagreements and evidence gaps |
| Conclusion | Interpretation and limitations |
| References | Conclusion |
| | References |

Use the configured report language in prose. Required top-level headings remain the template's stable English labels for this revision; this is an explicit structural limitation, not a translation of the user's content. Additional topic-specific headings use level 3 or deeper within the assigned section. A venue requiring a different top-level structure is outside these templates; report the mismatch rather than silently changing the contract.

## Phase requirements

| Phase | Inputs | Completion and return on failure |
| --- | --- | --- |
| Brief | Request, scope, selected type/depth and constraints | Brief fields complete, provenance explicit, method and outside check planned. Unresolved user-owned scope choices return through Ask User Question. |
| Discovery | Brief and Research Literature's criteria | For deep depth, freeze initial sources, retrieve reference lists, rank overlaps, screen one backward hop and record additions/limits in citation-candidates.json. Other depths do no automatic expansion. Final Literature qualification gate is handoff-ready, including after one top-up if still short. Raw records, generated qualified list and exclusions remain separate. Actual source records and search receipt retained, with one searched and explained outcome per optional `brief.source_requests` entry. Eligible requested papers enter appraisal; exclusions, unresolved author identities and access gaps stay explicit. Inadequate evidence returns to discovery or a bounded-limit report. |
| Evidence | Retrieved sources and accessible texts | Appraisals carry inspection basis and locators; claims point to actual findings and counterevidence. Unsupported claims return to appraisal/discovery or are removed. |
| Outline | Claims, appraisals, fixed template | Every section has a purpose, assigned sources/claims, word budget and context. Citation keys have been generated before prose uses them. |
| Draft | Brief, section outline, evidence excerpts and keys | Natural Writing returns the assigned section with its heading intact. New source needs return to Research, never to invented citations. |
| Assembly | Manifest and complete section files | Script creates draft.md in manifest order. Structural failures return to section drafting. |
| Review | Current canonical draft, claims and source locators | Both review templates describe actual checks and issues. Critical/major issues require repair; at most two substantive repair passes. |
| Polish | Canonical draft, review findings, protected evidence | Natural Writing improves prose; Research rechecks material changes and refreshes summary/title. Review hashes must describe the latest draft. |
| Compile | Settled draft, source inventory, local style | Citation keys resolve; generated bibliography contains cited works. Script outputs are hash-linked to input revisions. |
| Export | Compiled report and requested formats | Converter receipts plus actual files. Word/PDF require rendered page inspection. Missing tools/content-loss errors block that format, not honest delivery of available requested outputs. |

Run the CLI's phase validator at these boundaries. A successful validation confirms required artifact relationships, not that research or review judgments are true. Do not manufacture a completed check to satisfy a validator.

## Natural Writing handoff

Supply the original question, document type, language, audience, field, citation style and depth. For each section additionally supply its fixed heading/purpose, word budget, source and claim assignments, inspected evidence with locators and limitations, citation-key map, terminology, neighboring context and unresolved restrictions. Natural Writing selects and applies the language reference, including Academic style for English. It returns prose, not new study facts or a separately evaluated artifact.

For polish, supply the whole canonical draft and review findings. Treat citation keys, attribution, numbers, quotations and claim qualifications as protected evidence. After changes, Research checks support and refreshes review records against the new draft hash. English prose rules remain authoritative in the English guideline instead of being duplicated here.

## Editing and recovery

The initialized numbered section files own prose until assembly. After assembly, edit draft.md only. Reassembly with `--replace` intentionally replaces canonical edits; do it only when returning to section drafting. `init --resume` never resets records. Generated output replacement is explicit. Recompile citations after draft/source changes and regenerate dependent exports. Keep the artifact receipts so a resumed run can identify stale work.

If two repair passes leave a material blocker, preserve the draft and open issue, and report blocked/provisional status. Do not extend the loop indefinitely, silently reduce standards, or call a script's success independent peer review.
