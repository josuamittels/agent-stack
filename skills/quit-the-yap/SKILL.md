---
name: "quit-the-yap"
description: "Write concise, direct in-chat answers in English Absolute style while preserving the details needed for meaning and action."
version: "0.2.0"
created: "2026-10-25"
updated: "2026-10-28"
author:
  - "Josua Mittelstaedt"
references:
  - "softaworks"
  - "refoundai"
type: "discipline"
status: "experimental"
---

# Quit the Yap

Give the useful answer with minimal reading effort. Keep it clear, complete, and calm.

## Scope

Use when composing an English reply in chat. Apply it alongside the task's owning skill or workflow; it governs the reply's wording and structure, not the work itself. Follow an explicit request for another tone, format, or level of detail when it remains accurate and useful.

### Boundaries

Do not change the underlying answer, omit a necessary warning, or imply certainty the evidence does not support for the sake of brevity. Do not force a short reply when the user asks for detail or the subject needs explanation.

## Inputs

Use the user's latest request, relevant conversation context, established facts, and the answer or action the caller needs to communicate. Before drafting, invoke [Natural Writing](../natural-writing/SKILL.md) as the required writing method. Pass the answer's context and ask it to apply English Absolute style. Natural Writing selects and applies the English language guidance, including its Absolute style section; do not read the English guideline separately here.

### Default Procedures

If you miss relevant information, first invoke [think-harder](../think-harder/SKILL.md), passing all unresolved constraints and all available context, including references and guidelines, over. If `think-harder` leaves one or more constraints unresolved, use [ask-user-question](../ask-user-question/SKILL.md) to inquire the missing information.

If any discipline is unavailable, perform it directly and report the fallback. Carry unresolved constraints forward and do not invent answers or pretend the dependency ran.

## Workflow

### 1. Apply Natural Writing

Have Natural Writing compose or edit the reply using the supplied context and English Absolute style. Preserve the user's intended meaning and all necessary facts, qualifications, and actions.

### 2. Lead with the answer

Start with the answer, decision, result, or next action. Add context only when it helps the user understand the answer or act on it.

### 3. Remove padding

Cut greetings, canned acknowledgments, preambles, praise, filler, decorative headings, repeated summaries, and generic invitations to continue. Prefer familiar words and concrete verbs. Use formatting only when it makes the reply easier to scan.

### 4. Keep necessary detail

Retain any reason, condition, uncertainty, warning, limitation, or distinction between a recommendation and a requirement that could change the answer or the user's action. State what is known as known and what is uncertain as uncertain. Do not shorten by deleting essential context.

### 5. Keep sentences complete and the tone neutral

Use concise, grammatically complete sentences. Do not turn brevity into cryptic fragments, brusqueness, hostility, or unsupported certainty. Match the reply's length to the complexity of the request and the detail the user asked for.

### 6. Check the draft

For each sentence, ask: does it answer the request, explain a necessary reason or limit, or give a needed action? Remove it only when its removal leaves meaning, confidence, and safe action unchanged. Confirm that the first sentence gives the useful answer and that no necessary qualification was lost.

## Output

Return the requested answer in the requested format. Keep it direct and complete. If a necessary fact is missing, state the specific gap and ask only for the information needed to continue.
