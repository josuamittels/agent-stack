import ast
import io
import tokenize


def check_python_no_comments(record):
    inventory = record.get("evidence", {}).get("source_inventory")
    outputs = record.get("outputs", {})
    violations = []
    unavailable = []
    checked = []
    evidence = ["/evidence/source_inventory"]

    if not isinstance(inventory, list):
        unavailable.append("source_inventory must be an explicit array")
        inventory = []

    for item in inventory:
        if not isinstance(item, dict):
            unavailable.append("source inventory entry is not an object")
            continue
        path = item.get("path")
        language = item.get("language")
        if not isinstance(path, str) or not isinstance(language, str):
            unavailable.append("source entry needs path and language")
            continue
        if language != "python" and not path.endswith((".py", ".pyi")):
            continue
        key = item.get("output_key")
        source = outputs.get(key) if isinstance(key, str) else None
        ranges = item.get("ranges")
        if not isinstance(source, str) or not isinstance(ranges, list) or not ranges:
            unavailable.append(f"{path}: missing complete source or authored ranges")
            continue
        line_count = max(1, len(source.splitlines()))
        if any(
            not isinstance(span, list)
            or len(span) != 2
            or any(type(value) is not int for value in span)
            or not 1 <= span[0] <= span[1] <= line_count
            for span in ranges
        ):
            unavailable.append(f"{path}: invalid authored ranges")
            continue
        pointer = key.replace("~", "~0").replace("/", "~1")
        evidence.append(f"/outputs/{pointer}")
        try:
            tree = ast.parse(source, filename=path)
            tokens = list(tokenize.generate_tokens(io.StringIO(source).readline))
        except (SyntaxError, ValueError, tokenize.TokenError, IndentationError) as error:
            unavailable.append(f"{path}: cannot parse source: {type(error).__name__}")
            continue

        def overlaps(start, end):
            return any(start <= right and end >= left for left, right in ranges)

        for token in tokens:
            if token.type == tokenize.COMMENT and overlaps(token.start[0], token.end[0]):
                violations.append({"path": path, "line": token.start[0], "kind": "comment"})
        for node in ast.walk(tree):
            if not isinstance(node, (ast.Module, ast.ClassDef, ast.FunctionDef, ast.AsyncFunctionDef)):
                continue
            if not node.body:
                continue
            first = node.body[0]
            if (
                isinstance(first, ast.Expr)
                and isinstance(first.value, ast.Constant)
                and isinstance(first.value.value, str)
                and overlaps(first.lineno, first.end_lineno)
            ):
                violations.append({"path": path, "line": first.lineno, "kind": "docstring"})
        checked.append(path)

    status = "fail" if violations else "unverified" if unavailable else "pass" if checked else "not_applicable"
    return {
        "status": status,
        "step": "Check authored Python units",
        "aspect": "Python comments and docstrings",
        "observed": {"checked": checked, "violations": violations, "unavailable": unavailable},
        "expected": "Zero Python comment tokens or docstrings in inventoried authored ranges; other languages are not checked",
        "evidence": evidence,
    }
