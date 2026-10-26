---
name: translate
description: "Translate and localize human-facing text into a target language with fluent, culturally appropriate phrasing. Use for prose, product copy, documentation, and messages that should read naturally in their destination language while preserving the source's meaning, intent, and factual claims."
version: "0.4.1"
updated: "2026-10-26"
author:
  - "Josua Mittelstaedt"
references:
  - "Kostja Zhang"
  - "Ghaida Zahran"
type: "skill"
status: "draft"
---

# Translate

Prepare translation context, then use natural-writing to produce fluent target-language prose. Default to faithful localization: preserve meaning and intent while expressing them as the intended reader would naturally encounter them.

## Scope

Use for translation, localization, requested transcreation, and script conversion within a translation task. This skill does not own market rollout, interface redesign, publishing, or unrelated research workflows.

## Inputs

Apply this sequence before the clarification instructions below.

Require source text and a determinable target language. Infer the source language where clear. Ask for missing source material or a missing target language. Natural-writing's English guidance fallback does not choose the output language.

Use supplied locale, audience, purpose, medium, tone, style, examples, terminology, and length constraints. These contextual inputs are optional. Infer reasonable defaults from the task, and ask only when ambiguity materially changes the translation. Do not infer a country or a form of address from language alone when the distinction matters.

Read the relevant source material in context. Resolve consequential contradictions or ambiguous passages before choosing an interpretation. Distinguish ambiguity deliberately present in the source from confusion that needs clarification.

### Default Procedures

If you miss relevant information, first invoke [think-harder](../../disciplines/think-harder/SKILL.md), passing all unresolved constraints and all available context, including references and guidelines, over. If `think-harder` leaves one or more constraints unresolved, use [ask-user-question](../../disciplines/ask-user-question/SKILL.md) to inquire the missing information.

If any discipline is unavailable, perform it directly and report the fallback. Carry unresolved constraints forward and do not invent answers or pretend the dependency ran.

## Workflow

### 1. Prepare an internal translation brief

Before invoking natural-writing, establish:

- The source's explicit meaning, relevant implications, purpose, and intended response or action.
- Its register, emotional intensity, speaker-reader relationship, humor, rhetorical devices, and degree of directness.
- The audience's likely knowledge and the context needed to understand unfamiliar references.
- Target language and locale, requested style, medium, and space constraints.
- Approved terminology, established names, untranslated terms, and protected technical elements.
- Facts, qualifications, commitments, quantities, and other meanings that must remain intact.
- Idioms, cultural references, formats, and script choices needing adaptation.

Keep the brief internal unless requested. Distinguish supplied facts from inferred context. Do not manufacture cultural preferences or turn national stereotypes into writing requirements. Reuse an existing glossary or style brief rather than creating competing versions.

### 2. Choose the treatment

| Treatment | Application |
| --- | --- |
| Faithful localization | Default. Recast syntax, idioms, politeness, and phrasing to preserve meaning, register, and intended effect. |
| Direct translation | Use when meaning transfers cleanly or exact correspondence matters. Avoid unnatural source-language syntax. |
| Transcreation | Use only when explicitly requested. Permit broader changes to slogans, humor, or framing within the authorized scope while preserving factual claims and the underlying promise. |
| Transliteration | Treat script conversion separately from translation. Use established target-language spellings or an appropriate consistent convention where needed. |

Prefer an equivalent idiom when it preserves meaning and register. Otherwise express the meaning naturally. Do not force a saying, joke, or cultural replacement into a passage that does not need it.

Preserve names and brands unless an established localized form or explicit instruction supports a change. Do not automatically romanize text. For transliteration, honor a supplied convention and distinguish phonetic rendering from translation of meaning.

Localize presentation of dates, numbers, units, currencies, and forms of address without silently changing underlying values. Currency conversion, substituted locations, altered examples, market-specific offers, and changed legal obligations require an established basis or explicit direction. Do not invent exchange rates, local evidence, or product availability.

### 3. Invoke natural-writing

Before producing target prose, require [natural-writing](../natural-writing/SKILL.md). Pass the original source and internal brief, including the target locale, permitted adaptations, terminology, protected elements, and fidelity requirements.

Have natural-writing compose the target-language text using its mandatory language-guideline selection and fallback. Keep the requested output language even when its guidance falls back to English. Do not duplicate its prose guidelines here.

Use the host's invocation mechanism when available. Otherwise read and apply the skill in the current context. Do not claim a separate invocation occurred when it did not. If natural-writing or its required usable guidance is unavailable, report the dependency and withhold the translation rather than bypassing it.

Explicitly identify prose authorized for translation, including quoted passages. Distinguish it from citations, code, identifiers, interpolation variables, link destinations, and other elements that must remain exact. Preserve attribution and distinguish translated quotations from original-language wording where necessary.

## Output

When used as a helper inside another requested skill, return the completed translation to that owner.

Return the translation in the requested format. Add explanations, alternatives, or adaptation notes only when requested or needed to resolve material ambiguity. Report native-speaker review or rendered-context verification only when actually performed. Do not imply specialist approval, release readiness, or human authorship.

## Boundaries

Do not undertake market rollout, interface redesign, publishing, or unrelated research as part of a translation request. Do not change underlying values, product offers, or legal obligations without an established basis or explicit direction. Do not invent facts, cultural preferences, or product availability. If natural-writing or its required usable language guidance is unavailable, report the dependency and withhold the translation rather than bypassing it.
