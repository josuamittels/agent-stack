---
name: check-colour-contrast
description: "Calculate the WCAG contrast ratio for two opaque hex, RGB, or HSL colors and interpret the result."
version: "1.1.0"
created: "2026-10-27"
updated: "2026-10-28"
author:
  - "Josua Mittelstaedt"
references:
  - "World Wide Web Consortium"
type: "discipline"
status: "stable"
---

# Check Colour Contrast

## Scope

Use when checking the contrast between two supplied colors.

## Inputs

Provide opaque foreground and background colors, each with its format (`hex`, `rgb`, or `hsl`) and value.

### Default Procedures

When task input is needed from the user, route the question through [ask-user-question](../ask-user-question/SKILL.md) for preparation, delivery, and interpretation. First invoke [think-harder](../think-harder/SKILL.md) when ambiguity, missing information, or competing interpretations may be resolved from context, relevant guidance, evidence, or a reasonable default. Skip Think Harder for direct permission or approval gates, explicitly requested interviews, and facts or preferences only the user can supply. Ask only about consequential unresolved items. Continue independent work and preserve approval requirements.

If any discipline is unavailable, perform it directly and report the fallback. Carry unresolved constraints forward and do not invent answers or pretend the dependency ran.

## Workflow

Run `node skills/check-colour-contrast/scripts/check-colour-contrast.mjs <format> '<foreground>' <format> '<background>'`, for example `node skills/check-colour-contrast/scripts/check-colour-contrast.mjs hex '#222' hex '#ffe66d'`.

Interpret the ratio for the element being checked:

| Element | WCAG AA | WCAG AAA |
| --- | ---: | ---: |
| Normal text | 4.5:1 or higher | 7:1 or higher |
| Large text | 3:1 or higher | 4.5:1 or higher |

Large text is at least 18 pt (24 CSS px) regular or 14 pt (about 18.67 CSS px) bold. For visual information needed to identify active UI components or states, and meaningful parts of graphics, WCAG AA requires at least 3:1 against adjacent colors when the criterion applies.

Return the ratio and the applicable result. A color-pair result alone does not establish page conformance; context such as transparency, images, gradients, thin strokes, and exemptions still matters.

## Output

Return the calculated ratio and pass/fail results for normal text, large text, and non-text UI/graphics.
