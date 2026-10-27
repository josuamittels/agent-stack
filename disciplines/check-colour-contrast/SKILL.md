---
name: check-colour-contrast
description: "Calculate the WCAG contrast ratio for two opaque hex, RGB, or HSL colors and interpret the result."
version: "0.1.0"
updated: "2026-10-27"
author:
  - "Josua Mittelstaedt"
references:
  - "World Wide Web Consortium"
type: "discipline"
status: "draft"
---

# Check Colour Contrast

## Scope

Use when checking the contrast between two supplied colors.

## Inputs

Provide opaque foreground and background colors, each with its format (`hex`, `rgb`, or `hsl`) and value.

### Default Procedures

If you miss relevant information, first invoke [think-harder](../think-harder/SKILL.md), passing all unresolved constraints and all available context, including references and guidelines, over. If `think-harder` leaves one or more constraints unresolved, use [ask-user-question](../ask-user-question/SKILL.md) to inquire the missing information.

If any discipline is unavailable, perform it directly and report the fallback. Carry unresolved constraints forward and do not invent answers or pretend the dependency ran.

## Workflow

Run `node disciplines/check-colour-contrast/scripts/check-colour-contrast.mjs <format> '<foreground>' <format> '<background>'`, for example `node disciplines/check-colour-contrast/scripts/check-colour-contrast.mjs hex '#222' hex '#ffe66d'`.

Interpret the ratio for the element being checked:

| Element | WCAG AA | WCAG AAA |
| --- | ---: | ---: |
| Normal text | 4.5:1 or higher | 7:1 or higher |
| Large text | 3:1 or higher | 4.5:1 or higher |

Large text is at least 18 pt (24 CSS px) regular or 14 pt (about 18.67 CSS px) bold. For visual information needed to identify active UI components or states, and meaningful parts of graphics, WCAG AA requires at least 3:1 against adjacent colors when the criterion applies.

Return the ratio and the applicable result. A color-pair result alone does not establish page conformance; context such as transparency, images, gradients, thin strokes, and exemptions still matters.

## Output

Return the calculated ratio and pass/fail results for normal text, large text, and non-text UI/graphics.
