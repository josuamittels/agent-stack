---
name: convert-colour
description: "Convert a color value between hex, RGB, HSL, HSV, CMYK, Lab, LCH, and Display P3 with the standalone script."
version: "0.1.0"
updated: "2026-10-27"
author:
  - "Josua Mittelstaedt"
references:
  - "W3C"
type: "discipline"
status: "draft"
---

# Convert Colour

## Scope

Use when converting one color value between supported formats.

## Inputs

Provide the input format, color value, and output format.

### Default Procedures

If you miss relevant information, first invoke [think-harder](../think-harder/SKILL.md), passing all unresolved constraints and all available context, including references and guidelines, over. If `think-harder` leaves one or more constraints unresolved, use [ask-user-question](../ask-user-question/SKILL.md) to inquire the missing information.

If any discipline is unavailable, perform it directly and report the fallback. Carry unresolved constraints forward and do not invent answers or pretend the dependency ran.

## Workflow

Run `node disciplines/convert-colour/scripts/convert-colour.mjs <input-format> '<value>' <output-format>`, for example `node disciplines/convert-colour/scripts/convert-colour.mjs rgb '255 0 0' lab`.

Supported formats: `hex`, `rgb`, `hsl`, `hsv`, `cmyk`, `lab`, `lch`, and `p3`.

## Output

Return the converted value printed by the script.
