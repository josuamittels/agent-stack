---
name: natural-writing
description: "Write, edit, and translate any prose people will read, including product interfaces, websites, documentation, articles, and messages. Apply when producing human-facing text, including within implementation tasks, to preserve meaning, fit the intended voice and audience, and remove formulaic AI phrasing."
version: "0.4.1"
updated: "2026-10-26"
author:
  - "Josua Mittelstaedt"
references:
  - "Affaan Mustafa"
  - "Matt Pocock"
type: "skill"
status: "draft"
---

# Natural writing

Produce clear, natural prose suited to its reader, purpose, and medium. Apply this base layer alongside specialized skills for the requested artifact. Keep detailed writing rules in the language references.

## Scope

Use when writing, editing, or translating prose people will read. Apply it alongside a specialized skill when that skill owns the artifact or domain workflow.

### Boundaries

Preserve facts, uncertainty, attribution, scope, and intended meaning. Do not invent evidence or experiences, alter protected code or data, or change unrelated material when editing. Do not claim human authorship or guarantee that text will evade a detector.

## Inputs

Apply this sequence before the clarification instructions below.

### Default Procedures

If you miss relevant information, first invoke [think-harder](../../disciplines/think-harder/SKILL.md), passing all unresolved constraints and all available context, including references and guidelines, over. If `think-harder` leaves one or more constraints unresolved, use [ask-user-question](../../disciplines/ask-user-question/SKILL.md) to inquire the missing information.

If any discipline is unavailable, perform it directly and report the fallback. Carry unresolved constraints forward and do not invent answers or pretend the dependency ran.

## Workflow

### 1. Establish the writing context

Use the user's purpose, audience, output language, format, length, tone, brand guidance, and writing samples when supplied. These inputs are optional. Infer reasonable defaults from the task, surrounding content, and intended use. Ask only when missing information materially prevents an accurate or useful result.

Default to clear language appropriate to the reader and medium. Do not impose a generic persona, forced friendliness, or an operator voice. A brief interface message needs different treatment from an essay.

The user's direct instructions take priority over defaults. An explicit stylistic deviation overrides the relevant convention only. Continue to apply the remaining guidance. Stylistic permission does not authorize factual invention or misrepresentation.

### 2. Read the required language guidance

Before composing on every writing task, including a small edit or short label, determine the intended output language from explicit instructions first, then the requested artifact and context. Read the corresponding reference:

| Output Language | Required reference |
| --- | --- |
| English | [English guidelines](../../guidelines/languages/english.md) |
| German | [German guidelines](../../guidelines/languages/german.md) |
| Dutch | [Dutch guidelines](../../guidelines/languages/dutch.md) |
| French | [French guidelines](../../guidelines/languages/french.md) |

Read its general guidance and applicable style sections before drafting. Metadata, a contents list, or remembered advice is insufficient. Apply only the style conventions relevant to the artifact, including narrative guidance only for narrative work.

Use English when the language is unspecified or unsupported. If the selected output language's reference is missing, unreadable, or only a scaffold, read the English reference instead.

Fallback selects guidance, not output language. Keep the requested language and apply transferable principles without imposing English grammar, punctuation, or idiom on another language. For multilingual output, read and apply the corresponding guidance to each language, using the same fallback where necessary.

A usable reference is mandatory. If neither the selected reference nor the English fallback can be read, report the missing dependency and withhold the prose deliverable. Do not silently substitute general writing advice.

### 3. Tailor and compose

Turn supplied style descriptions into concrete choices about vocabulary, formality, rhythm, explanatory depth, directness, questions, emphasis, and closing language.

When samples are supplied, derive voice from recurring characteristics rather than incidental words. Favor examples relevant to the current audience and medium. Keep distinct public, private, or situational voices separate when the material supports that distinction. Explicit directions govern when samples conflict with the current request.

Reuse established preferences within the task. Do not repeat style analysis, invent a personality, collect more samples by default, or save a voice profile unless requested. Adapt structure and length to the medium while preserving the intended voice and meaning.

Use the available material to build a coherent progression. Establish concepts before relying on them, allowing for what the reader already knows. Give each paragraph or larger movement a distinct contribution, preserve the opening's promise, and end when the reader's purpose is fulfilled. Do not force every source fragment into the result or require approval for each paragraph.

Preserve facts, uncertainty, attribution, scope, and the intended meaning. Do not invent evidence or experiences for vividness. Change only the requested prose when editing. Preserve code, data, quotations, and identifiers rather than restyling them.

### 4. Return to owner

When used as a helper inside another requested skill, return the completed prose to that owner.

## Output

Return the requested text or artifact in its required format. Omit internal notes and voice analysis. Preserve any surrounding application or artifact structure required by the task. Do not claim human authorship or a detector guarantee.
