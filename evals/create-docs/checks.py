"""Deterministic navigation checks on complete rendered documentation pages."""

from html.parser import HTMLParser
from urllib.parse import unquote, urljoin, urlsplit

BASE = "https://docs.invalid"
EVIDENCE = ["/evidence/pages", "/evidence/landing_route", "/outputs"]


class PageHTML(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.links = []
        self.ids = set()
        self.has_base = False

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "base":
            self.has_base = True
        if attrs.get("id"):
            self.ids.add(attrs["id"])
        if tag == "a":
            if attrs.get("name"):
                self.ids.add(attrs["name"])
            if "href" in attrs and attrs["href"] is not None:
                self.links.append(attrs["href"])


def _result(status, aspect, observed, expected):
    return {"status": status, "step": "rendered documentation navigation",
            "aspect": aspect, "observed": observed, "expected": expected,
            "evidence": EVIDENCE}


def _route(value):
    if not isinstance(value, str) or not value.startswith("/") or value.startswith("//"):
        raise ValueError("page routes must be absolute paths on the docs origin")
    parts = urlsplit(value)
    if parts.query or parts.fragment:
        raise ValueError("page routes cannot contain queries or fragments")
    return urljoin(BASE, value).rstrip("/") or BASE


def _load(context):
    evidence = context.get("evidence", {})
    pages = evidence.get("pages")
    outputs = context.get("outputs", {})
    if not isinstance(pages, list) or not pages:
        raise ValueError("complete nonempty page inventory is unavailable")
    rendered = {}
    for page in pages:
        if not isinstance(page, dict) or set(page) != {"route", "html_key", "source_key"}:
            raise ValueError("each page requires route, html_key, and source_key")
        route = _route(page["route"])
        if route in rendered:
            raise ValueError("duplicate normalized page route")
        html = outputs.get(page["html_key"])
        source = outputs.get(page["source_key"])
        if not isinstance(html, str) or not html.strip() or not isinstance(source, str) or not source.strip():
            raise ValueError("complete source or rendered HTML is unavailable")
        parser = PageHTML()
        parser.base_url = urljoin(BASE, page["route"])
        parser.feed(html)
        parser.close()
        if parser.has_base:
            raise ValueError("HTML base element requires unsupported URL normalization")
        rendered[route] = parser
    landing = _route(evidence.get("landing_route"))
    if landing not in rendered:
        raise ValueError("landing route is absent from page inventory")
    return rendered, landing


def _links(route, page):
    for href in page.links:
        parts = urlsplit(urljoin(page.base_url, href))
        target = parts._replace(fragment="", query="").geturl().rstrip("/")
        yield target, unquote(parts.fragment), href


def _reachable(graph, start):
    seen = set()
    pending = [start]
    while pending:
        node = pending.pop()
        if node not in seen:
            seen.add(node)
            pending.extend(graph.get(node, set()) - seen)
    return seen


def check_navigation(context):
    aspect = "page reachability and basic return navigation"
    expected = "all pages reachable from landing; basic pages can return to landing"
    try:
        pages, landing = _load(context)
        mode = context.get("constraints", {}).get("mode", {}).get("value")
        if mode not in {"basic", "interactive"}:
            raise ValueError("resolved basic or interactive mode is unavailable")
        graph = {route: {target for target, _, _ in _links(route, page) if target in pages}
                 for route, page in pages.items()}
        orphaned = sorted(set(pages) - _reachable(graph, landing))
        reverse = {route: set() for route in pages}
        for route, targets in graph.items():
            for target in targets:
                reverse[target].add(route)
        no_return = sorted(set(pages) - _reachable(reverse, landing)) if mode == "basic" else []
    except (ValueError, TypeError, KeyError) as exc:
        return _result("unverified", aspect, str(exc), expected)
    result = _result("fail" if orphaned or no_return else "pass", aspect,
                     {"orphaned": orphaned, "no_return": no_return, "page_count": len(pages)}, expected)
    result["evidence"] = EVIDENCE + ["/constraints/mode"]
    return result


def check_fragments(context):
    aspect = "fragment targets within the supplied documentation set"
    expected = "every linked fragment in a supplied page resolves to an ID or named anchor"
    try:
        pages, _ = _load(context)
        missing = []
        count = 0
        for route, page in pages.items():
            for target, fragment, href in _links(route, page):
                if target in pages and fragment:
                    count += 1
                    if fragment not in pages[target].ids:
                        missing.append({"source": route, "href": href, "target": target})
    except (ValueError, TypeError, KeyError) as exc:
        return _result("unverified", aspect, str(exc), expected)
    return _result("fail" if missing else "pass", aspect,
                   {"checked_fragments": count, "missing": missing}, expected)
