"""Small deterministic helpers for per-skill objective check packages."""
from urllib.error import HTTPError, URLError
from urllib.parse import urlparse
from urllib.request import Request, urlopen
import math
import re


def word_count(text):
    return len(text.split())


def character_count(text):
    return len(text)


def protected_tokens(text, tokens):
    return all(isinstance(token, str) and token and token in text for token in tokens)


JOURNAL_PRESETS = {
    'lenient': {'article_influence': 1.0, 'influence_percentile': 60.0},
    'default': {'article_influence': 2.5, 'influence_percentile': 80.0},
    'strict': {'article_influence': 5.0, 'influence_percentile': 90.0},
}


def normalize_issn(value):
    return re.sub(r'[-\s]', '', value or '').upper()


def journal_rows(rows, title='', issns=None):
    """Match a journal by ISSN when supplied, otherwise by normalized title."""
    issns = {normalize_issn(value) for value in (issns or []) if normalize_issn(value)}
    if issns:
        matches = [row for row in rows if issns & {
            normalize_issn(row.get('issn_print', '')), normalize_issn(row.get('issn_online', ''))
        }]
        method = 'issn'
    else:
        key = ' '.join(re.findall(r'\w+', title.casefold()))
        matches = [row for row in rows if ' '.join(re.findall(r'\w+', row.get('journal', '').casefold())) == key]
        method = 'title'
    identities = {(row.get('journal'), normalize_issn(row.get('issn_print', '')),
                   normalize_issn(row.get('issn_online', ''))) for row in matches}
    if not matches:
        return {'status': 'unverified', 'method': method, 'rows': []}
    if len(identities) != 1:
        return {'status': 'unverified', 'method': method, 'rows': matches}
    return {'status': 'matched', 'method': method, 'rows': matches}


def _finite_score(value, maximum=None):
    try:
        number = float(value)
    except (TypeError, ValueError):
        return None
    if not math.isfinite(number) or number < 0 or maximum is not None and number > maximum:
        return None
    return number


def journal_qualification(rows, article_influence=None, influence_percentile=None,
                          category=None, combination='or', disabled=False):
    """Apply inclusive journal thresholds; missing scores remain unverified."""
    if disabled:
        return {'status': 'pass', 'branch': 'filter-disabled', 'matched_rows': []}
    if article_influence is None and influence_percentile is None:
        return {'status': 'unverified', 'branch': None, 'matched_rows': []}
    if combination not in {'or', 'and'}:
        return {'status': 'unverified', 'branch': None, 'matched_rows': [], 'reason': 'invalid-combination-rule'}
    selected = [row for row in rows if category is None or row.get('category') == category]
    if not selected:
        return {'status': 'unverified', 'branch': None, 'matched_rows': [], 'reason': 'no-eligible-category-row'}
    uncertain = False
    for row in selected:
        ai = _finite_score(row.get('article_influence')) if article_influence is not None else None
        percentile = _finite_score(row.get('influence_percentile'), 100) if influence_percentile is not None else None
        active = []
        if article_influence is not None:
            active.append(('article_influence', ai, article_influence))
        if influence_percentile is not None:
            active.append(('influence_percentile', percentile, influence_percentile))
        row_passes = []
        for _, value, threshold in active:
            if value is None:
                row_passes.append(None)
            else:
                row_passes.append(value >= threshold)
        passed = any(value is True for value in row_passes) if combination == 'or' else all(value is True for value in row_passes)
        if passed:
            branches = [name for (name, _, _), value in zip(active, row_passes) if value is True]
            return {'status': 'pass', 'branch': branches, 'matched_rows': [row]}
        row_failed = any(value is False for value in row_passes) if combination == 'and' else all(value is False for value in row_passes)
        uncertain |= not row_failed and any(value is None for value in row_passes)
    if uncertain:
        return {'status': 'unverified', 'branch': None, 'matched_rows': selected, 'reason': 'score-missing-or-invalid'}
    return {'status': 'fail', 'branch': None, 'matched_rows': selected, 'reason': 'below-selected-thresholds'}


def _http_error(error):
    code = error.code
    status = 'fail' if code in {404, 410} or 400 <= code < 500 and code not in {401, 403, 408, 425, 429} else 'unverified'
    if 200 <= code < 400:
        status = 'pass'
    return {'status': status, 'status_code': code, 'final_url': error.geturl()}


def url_reachable(url, timeout=8):
    """Check URL reachability only; this does not validate the linked content."""
    parsed = urlparse(url)
    if parsed.scheme not in {'http', 'https'} or not parsed.netloc:
        return {'status': 'fail', 'detail': 'invalid-http-url'}
    headers = {'User-Agent': 'AgentStackObjectiveCheck/1.0'}
    try:
        request = Request(url, method='HEAD', headers=headers)
        with urlopen(request, timeout=timeout) as response:
            if 200 <= response.status < 400:
                return {'status': 'pass', 'status_code': response.status, 'final_url': response.geturl()}
            if response.status not in {403, 405, 501}:
                return {'status': 'fail' if 400 <= response.status < 500 and response.status not in {408, 425, 429} else 'unverified',
                        'status_code': response.status, 'final_url': response.geturl()}
    except HTTPError as error:
        if error.code not in {403, 405, 501}:
            return _http_error(error)
    except (URLError, TimeoutError, OSError):
        # A failed HEAD can reflect host restrictions. Retry with a small GET.
        pass
    try:
        request = Request(url, method='GET', headers={**headers, 'Range': 'bytes=0-0'})
        with urlopen(request, timeout=timeout) as response:
            return {'status': 'pass' if 200 <= response.status < 400 else 'fail',
                    'status_code': response.status, 'final_url': response.geturl()}
    except HTTPError as error:
        return _http_error(error)
    except (URLError, TimeoutError, OSError) as error:
        return {'status': 'unverified', 'detail': type(error).__name__}
