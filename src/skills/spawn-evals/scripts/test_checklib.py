import unittest
from unittest.mock import patch
from urllib.error import HTTPError

import checklib


class Response:
    status = 200

    def __enter__(self):
        return self

    def __exit__(self, *args):
        return False

    def geturl(self):
        return 'https://example.test/final'


class ChecklibTests(unittest.TestCase):
    def test_word_and_character_counts(self):
        self.assertEqual(checklib.word_count('one  two\nthree'), 3)
        self.assertEqual(checklib.character_count('abc'), 3)

    def test_protected_tokens(self):
        self.assertTrue(checklib.protected_tokens('Open {{name}}', ['{{name}}']))
        self.assertFalse(checklib.protected_tokens('Open name', ['{{name}}']))

    def test_journal_preset_thresholds_are_inclusive(self):
        row = {'article_influence': '2.5', 'influence_percentile': '79.9', 'category': 'CS'}
        self.assertEqual(checklib.journal_qualification(
            [{'article_influence': '0.9', 'influence_percentile': '59', 'category': 'CS'}],
            **checklib.JOURNAL_PRESETS['lenient'])['status'], 'fail')
        self.assertEqual(checklib.journal_qualification(
            [row], **checklib.JOURNAL_PRESETS['default'])['status'], 'pass')
        self.assertEqual(checklib.journal_qualification(
            [row], **checklib.JOURNAL_PRESETS['strict'])['status'], 'fail')

    def test_journal_override_can_use_one_branch(self):
        row = {'article_influence': 'bad', 'influence_percentile': '60', 'category': 'CS'}
        result = checklib.journal_qualification([row], influence_percentile=60)
        self.assertEqual(result['status'], 'pass')
        self.assertEqual(result['branch'], ['influence_percentile'])

    def test_missing_journal_score_is_unverified(self):
        row = {'article_influence': '', 'influence_percentile': '', 'category': 'CS'}
        self.assertEqual(checklib.journal_qualification(
            [row], **checklib.JOURNAL_PRESETS['strict'])['status'], 'unverified')

    def test_or_rule_needs_unknown_branch_before_confirming_failure(self):
        row = {'article_influence': '1', 'influence_percentile': '', 'category': 'CS'}
        result = checklib.journal_qualification([row], article_influence=5, influence_percentile=90)
        self.assertEqual(result['status'], 'unverified')

    def test_and_rule_can_fail_on_one_known_below_threshold_metric(self):
        row = {'article_influence': '1', 'influence_percentile': '', 'category': 'CS'}
        result = checklib.journal_qualification(
            [row], article_influence=5, influence_percentile=90, combination='and')
        self.assertEqual(result['status'], 'fail')

    def test_journal_category_restriction_is_respected(self):
        rows = [
            {'article_influence': '10', 'influence_percentile': '99', 'category': 'A'},
            {'article_influence': '1', 'influence_percentile': '20', 'category': 'B'},
        ]
        result = checklib.journal_qualification(rows, article_influence=5, category='B')
        self.assertEqual(result['status'], 'fail')

    def test_journal_matching_prefers_issn(self):
        rows = [{'journal': 'Example Journal', 'issn_print': '1234-567X', 'issn_online': '', 'category': 'A'}]
        self.assertEqual(checklib.journal_rows(rows, title='Different Title', issns=['1234 567x'])['status'], 'matched')

    def test_url_reachable_uses_head_and_accepts_redirected_target(self):
        with patch.object(checklib, 'urlopen', return_value=Response()) as open_url:
            result = checklib.url_reachable('https://example.test/start')
        self.assertEqual(result['status'], 'pass')
        self.assertEqual(result['final_url'], 'https://example.test/final')
        self.assertEqual(open_url.call_count, 1)

    def test_invalid_url_is_a_confirmed_failure(self):
        self.assertEqual(checklib.url_reachable('file:///tmp/article')['status'], 'fail')

    def test_missing_url_is_a_confirmed_failure(self):
        error = HTTPError('https://example.test/missing', 404, 'Not Found', {}, None)
        with patch.object(checklib, 'urlopen', side_effect=error):
            result = checklib.url_reachable('https://example.test/missing')
        self.assertEqual(result['status'], 'fail')

    def test_access_denied_is_unverified(self):
        error = HTTPError('https://example.test/private', 403, 'Forbidden', {}, None)
        with patch.object(checklib, 'urlopen', side_effect=error):
            result = checklib.url_reachable('https://example.test/private')
        self.assertEqual(result['status'], 'unverified')

    def test_network_failure_is_unverified(self):
        from urllib.error import URLError
        with patch.object(checklib, 'urlopen', side_effect=URLError('offline')):
            result = checklib.url_reachable('https://example.test/paper')
        self.assertEqual(result['status'], 'unverified')


if __name__ == '__main__':
    unittest.main()
