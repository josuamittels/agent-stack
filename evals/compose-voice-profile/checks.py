"""Objective template conformance checks for Compose Voice Profile."""

from pathlib import Path
import re


def _result(status, step, aspect, observed, expected, evidence):
    return {
        "status": status,
        "step": step,
        "aspect": aspect,
        "observed": observed,
        "expected": expected,
        "evidence": evidence,
    }


def _inputs(context):
    output = context.get("outputs", {}).get("main")
    template_path = context.get("evidence", {}).get("template_path")
    if not isinstance(output, str) or not isinstance(template_path, str) or not template_path:
        return None, None, "main output and evidence.template_path are required"
    path = Path(template_path)
    try:
        template = path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        return None, None, f"template could not be read: {exc}"
    return output, template, None


def check_template_heading_coverage(context):
    output, template, issue = _inputs(context)
    evidence = ["/outputs/main", "/evidence/template_path"]
    if issue:
        return _result("unverified", "template review", "section heading coverage", issue,
                       "readable output and current voice-profile template", evidence)

    heading_pattern = re.compile(r"^(#{2,3})[ \t]+(.+?)[ \t]*$", re.MULTILINE)
    required = heading_pattern.findall(template)
    present = heading_pattern.findall(output)
    cursor = 0
    missing = []
    for heading in required:
        try:
            cursor = present.index(heading, cursor) + 1
        except ValueError:
            missing.append("#" * len(heading[0]) + " " + heading[1])

    return _result(
        "fail" if missing else "pass",
        "template review",
        "second- and third-level heading coverage and order",
        {"required_count": len(required), "output_count": len(present), "missing_or_out_of_order": missing},
        "all template headings appear in the same order",
        evidence,
    )


def check_template_prompt_resolution(context):
    output, template, issue = _inputs(context)
    evidence = ["/outputs/main", "/evidence/template_path"]
    if issue:
        return _result("unverified", "template review", "fill-in prompt resolution", issue,
                       "readable output and current voice-profile template", evidence)

    # Exclude Markdown links. Their bracketed labels are references, not prompts.
    prompt_pattern = re.compile(r"\[([^\]\n]+)\](?!\()")
    prompts = set(prompt_pattern.findall(template))
    remaining = sorted(f"[{prompt}]" for prompt in prompts if f"[{prompt}]" in output)

    return _result(
        "fail" if remaining else "pass",
        "template review",
        "unresolved bracketed fill-in prompts",
        remaining,
        "none of the template's bracketed prompts remain",
        evidence,
    )
