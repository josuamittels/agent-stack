---
name: convert-colour
description: "Convert a color value between hex, RGB, HSL, HSV, CMYK, Lab, LCH, and Display P3 with the standalone script."
version: "1.1.0"
created: "2026-10-27"
updated: "2026-10-28"
author:
  - "Josua Mittelstaedt"
references:
  - "W3C"
type: "discipline"
status: "stable"
---

# Convert Colour

## Scope

Use when converting one color value between supported formats.

## Inputs

Provide the input format, color value, and output format.

### Default Procedures

When task input is needed from the user, route the question through [ask-user-question](../ask-user-question/SKILL.md) for preparation, delivery, and interpretation. First invoke [think-harder](../think-harder/SKILL.md) when ambiguity, missing information, or competing interpretations may be resolved from context, relevant guidance, evidence, or a reasonable default. Skip Think Harder for direct permission or approval gates, explicitly requested interviews, and facts or preferences only the user can supply. Ask only about consequential unresolved items. Continue independent work and preserve approval requirements.

If any discipline is unavailable, perform it directly and report the fallback. Carry unresolved constraints forward and do not invent answers or pretend the dependency ran.

## Workflow

Run `node skills/convert-colour/scripts/convert-colour.mjs <input-format> '<value>' <output-format>`, for example `node skills/convert-colour/scripts/convert-colour.mjs rgb '255 0 0' lab`.

Supported formats: `hex`, `rgb`, `hsl`, `hsv`, `cmyk`, `lab`, `lch`, and `p3`.

## Output

Return the converted value printed by the script.
