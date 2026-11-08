"""Check persisted routing and preservation receipts, not agent behavior."""
import hashlib
from pathlib import Path

BEGIN = "<!-- BEGIN agent-stack:global-routing -->"
END = "<!-- END agent-stack:global-routing -->"


def result(status, aspect, observed, expected):
    return {
        "status": status,
        "step": "global routing setup",
        "aspect": aspect,
        "observed": observed,
        "expected": expected,
        "evidence": ["/outputs/instructions", "/evidence/setup"],
    }


def check_routing_section(context):
    text = context.get("outputs", {}).get("instructions")
    receipt = context.get("evidence", {}).get("setup")
    expected = "one balanced managed section with the bundled routing policy"
    if not isinstance(text, str) or not isinstance(receipt, dict) or receipt.get("applied") is not True:
        return result("unverified", "routing section", "complete applied output or receipt unavailable", expected)
    template = Path(__file__).resolve().parents[2] / "skills/setup-agent-stack/templates/global-routing.md"
    try:
        body = template.read_text(encoding="utf-8").strip()
    except OSError as error:
        return result("unverified", "routing section", str(error), expected)
    normalized = text.replace("\r\n", "\n")
    block = BEGIN + "\n" + body + "\n" + END
    valid = (normalized.count("agent-stack:global-routing") == 2
             and normalized.count(block) == 1
             and (normalized.startswith(block) or "\n" + block in normalized)
             and (normalized.endswith(block) or block + "\n" in normalized))
    return result("pass" if valid else "fail", "routing section", {"matches_policy": valid}, expected)


def check_manual_content(context):
    text = context.get("outputs", {}).get("instructions")
    receipt = context.get("evidence", {}).get("setup")
    expected = "manual prefix and suffix bytes and full resulting file match the pre-write receipt"
    fields = ["prefix_bytes", "suffix_bytes", "prefix_sha256", "suffix_sha256", "after_sha256"]
    if not isinstance(text, str) or not isinstance(receipt, dict) or any(k not in receipt for k in fields):
        return result("unverified", "manual content preservation", "preservation evidence unavailable", expected)
    if receipt.get("applied") is not True:
        return result("unverified", "manual content preservation", "receipt is preview-only", expected)
    data = text.encode("utf-8")
    prefix, suffix = receipt["prefix_bytes"], receipt["suffix_bytes"]
    if type(prefix) is not int or type(suffix) is not int or min(prefix, suffix) < 0 or prefix + suffix > len(data):
        return result("fail", "manual content preservation", "invalid byte boundaries", expected)
    digest = lambda value: hashlib.sha256(value).hexdigest()
    checks = {
        "prefix_preserved": digest(data[:prefix]) == receipt["prefix_sha256"],
        "suffix_preserved": digest(data[-suffix:] if suffix else b"") == receipt["suffix_sha256"],
        "complete_file_matches": digest(data) == receipt["after_sha256"],
    }
    return result("pass" if all(checks.values()) else "fail", "manual content preservation", checks, expected)
