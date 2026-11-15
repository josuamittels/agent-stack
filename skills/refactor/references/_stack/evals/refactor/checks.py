def check_migration(record):
    data = record.get("evidence", {}).get("migration")
    result = {
        "status": "unverified",
        "step": "Validate migration plan",
        "aspect": "Task graph and execution dependency order",
        "observed": "Missing or malformed migration evidence",
        "expected": "Unique task IDs, resolvable acyclic dependencies, dependency-first execution",
        "evidence": ["/evidence/migration"],
    }
    if not isinstance(data, dict):
        return result
    tasks = data.get("tasks")
    order = data.get("execution_order")
    if not isinstance(tasks, list) or not isinstance(order, list):
        return result
    if any(not isinstance(t, dict) or not isinstance(t.get("id"), str) or not t["id"].strip() or not isinstance(t.get("depends_on"), list) or any(not isinstance(d, str) or not d.strip() for d in t["depends_on"]) for t in tasks):
        return result
    if any(not isinstance(t, str) or not t.strip() for t in order):
        return result
    graph = {t["id"]: t["depends_on"] for t in tasks}
    errors = []
    if len(graph) != len(tasks):
        errors.append("Duplicate task IDs")
    if len(set(order)) != len(order):
        errors.append("Duplicate executed tasks")
    unknown = {d for deps in graph.values() for d in deps if d not in graph} | (set(order) - set(graph))
    if unknown:
        errors.append("Unknown task references: " + ", ".join(sorted(unknown)))
    remaining = set(graph)
    resolved = set()
    while remaining:
        ready = {t for t in remaining if set(graph[t]) <= resolved}
        if not ready:
            errors.append("Cyclic or unresolved dependency graph")
            break
        resolved.update(ready)
        remaining.difference_update(ready)
    seen = set()
    for task in order:
        if task in graph and not set(graph[task]) <= seen:
            errors.append("Executed before dependencies: " + task)
        seen.add(task)
    result["status"] = "fail" if errors else "pass"
    result["observed"] = errors if errors else {"tasks": len(tasks), "executed": len(order)}
    return result
