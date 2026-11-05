"""Regression tests for career executables and checker infrastructure, not skill evaluations."""
import hashlib
import importlib.util
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
S = ROOT / 'src/skills'

def module(name, path):
    sys.path.insert(0, str(path.parent))
    spec = importlib.util.spec_from_file_location(name, path)
    result = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result

workspace = module('career_workspace', S / 'compose-career-profile/scripts/career_workspace.py')
counter = module('count_answer', S / 'answer-interview/scripts/count_answer.py')
cv = module('cv_support', S / 'create-cv/scripts/cv_support.py')
answers = module('answer_checks', ROOT / 'src/evals/answer-interview/checks.py')

class CareerHelpers(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix='career-helpers-')
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        workspace.initialize(self.root, S / 'setup-career-stack/templates/AGENTS.md')

    def test_init_preserves_existing_instructions(self):
        (self.root / 'AGENTS.md').write_text('User instructions')
        workspace.initialize(self.root, S / 'setup-career-stack/templates/AGENTS.md')
        self.assertEqual((self.root / 'AGENTS.md').read_text(), 'User instructions')
        self.assertTrue((self.root / 'work').is_dir())

    def test_application_ids_and_numbers_survive_deleted_folders(self):
        first = workspace.application(self.root, 'vacancy-1', 'Example', 'Analyst')
        self.assertEqual(first, workspace.application(self.root, 'vacancy-1', 'Example', 'Analyst'))
        shutil.rmtree(first['application_folder'])
        second = workspace.application(self.root, 'vacancy-2', 'Example', 'Analyst')
        self.assertTrue(second['application_folder'].endswith('_002'))
        with self.assertRaises(ValueError):
            workspace.application(self.root, 'vacancy-2', 'Other', 'Analyst')

    def test_archive_requires_real_file_and_exact_source(self):
        source = self.root / 'posting.md'
        source.write_text('## Analyst\nC++ experience\n')
        item = workspace.application(self.root, 'vacancy-1', 'Example', 'Analyst', source)
        record = {'evidence': {'job_description_archive': item}, 'outputs': {'job_md': source.read_text()}}
        self.assertEqual(workspace.archive_result(record)['status'], 'pass')
        Path(item['job_md_path']).write_text('## Analyst\nC experience\n')
        self.assertEqual(workspace.archive_result(record)['status'], 'fail')
        with self.assertRaises(FileExistsError):
            workspace.application(self.root, 'vacancy-1', 'Example', 'Analyst', source)
        Path(item['job_md_path']).unlink()
        self.assertEqual(workspace.archive_result(record)['status'], 'unverified')

    def test_lock_and_symlink_do_not_mutate_workspace(self):
        lock = self.root / 'references/.career-lock'
        lock.mkdir()
        with self.assertRaises(FileExistsError):
            workspace.application(self.root, 'id', 'Example', 'Analyst')
        lock.rmdir()
        outside = self.root / 'elsewhere'; outside.mkdir()
        (self.root / 'work').rmdir()
        (self.root / 'work').symlink_to(outside)
        with self.assertRaises(ValueError):
            workspace.application(self.root, 'id', 'Example', 'Analyst')

    def test_qa_paths_stay_outside_application_folders(self):
        app = self.root / 'applications/example_analyst_001'
        app.mkdir()
        work = self.root / 'work/example_analyst_001/revision-1'
        work.mkdir(parents=True)
        for forbidden in (app, app / 'qa', app / 'nested/qa'):
            with self.assertRaises(ValueError): workspace.require_working_directory(forbidden)
        self.assertEqual(workspace.require_working_directory(work / 'qa'), (work / 'qa').resolve())
        self.assertEqual(workspace.require_working_directory(app / '../../work/revision-2'), (self.root / 'work/revision-2').resolve())
        self.assertEqual(workspace.require_working_directory(self.root / 'temporary-qa'), (self.root / 'temporary-qa').resolve())
        custom = self.root / 'custom-application'
        custom.mkdir(); (custom / 'job.md').write_text('Posting')
        with self.assertRaises(ValueError): workspace.require_working_directory(custom / 'qa')
        alias = self.root / 'qa-alias'; alias.symlink_to(app)
        with self.assertRaises(ValueError): workspace.require_working_directory(alias / 'qa')
        alias_in_app = app / 'work-alias'; alias_in_app.symlink_to(work)
        with self.assertRaises(ValueError): workspace.require_working_directory(alias_in_app / 'qa')
        generator = module('generate_cv_pdf', S / 'create-cv/scripts/generate_cv_pdf.py')
        with self.assertRaises(ValueError): generator.preflight(app / 'content.json', app / 'profile.json', app)
        for script, args in (
            ('generate_cv_pdf.py', ['--content', str(app / 'content.json'), '--profile', str(app / 'profile.json'), '--output-root', str(app)]),
            ('generate_cv_pdf.py', ['--content', str(alias_in_app / 'content.json'), '--profile', str(alias_in_app / 'profile.json')]),
            ('build_cv.py', [str(app / 'content.json'), '--profile', str(app / 'profile.json'), '--output-root', str(app), '--docx-only']),
        ):
            result = subprocess.run([sys.executable, str(S / 'create-cv/scripts' / script), *args], capture_output=True, text=True)
            self.assertNotEqual(result.returncode, 0)
            if script == 'generate_cv_pdf.py' or all(importlib.util.find_spec(name) for name in ('docx', 'pypdf', 'pypdfium2')):
                self.assertIn('outside application folders', result.stderr)
        verifier = module('verify_letter_pdf', S / 'draft-cover-letter/scripts/verify_letter_pdf.py')
        with self.assertRaises(ValueError): verifier.verify(app / 'Letter.pdf', app / 'letter.json', app / 'qa')
        self.assertFalse((app / 'qa').exists())
        self.assertFalse((app / 'CV.pdf').exists())
        self.assertFalse((app / 'CV.docx').exists())
        if all(importlib.util.find_spec(name) for name in ('docx', 'pypdf', 'pypdfium2')):
            build = module('build_cv', S / 'create-cv/scripts/build_cv.py')
            existing_qa = app / 'qa'; existing_qa.mkdir()
            sentinel = existing_qa / 'page-existing.png'; sentinel.write_bytes(b'preserve existing QA')
            with self.assertRaises(ValueError): build.verify_pdf(app / 'CV.pdf', app / 'CV.docx', {}, {}, existing_qa, app / 'content.json', app / 'profile.json')
            with self.assertRaises(ValueError): build.build_docx({}, {}, app / 'CV.docx')
            self.assertEqual(sentinel.read_bytes(), b'preserve existing QA')

    def test_delivery_copies_reviewed_bytes_and_preserves_existing_files(self):
        source = self.root / 'draft.pdf'; source.write_bytes(b'%PDF-reviewed')
        sha = hashlib.sha256(source.read_bytes()).hexdigest()
        report = self.root / 'validation.json'; report.write_text(json.dumps({'ok': True, 'pdf_sha256': sha}))
        dest = self.root / 'applications/example_analyst_001/CV.pdf'
        workspace.deliver(source, dest, sha, report)
        self.assertEqual(dest.read_bytes(), source.read_bytes())
        self.assertEqual(sorted(p.name for p in dest.parent.iterdir()), ['CV.pdf'])
        with self.assertRaises(FileExistsError): workspace.deliver(source, dest, sha, report)
        source.write_bytes(b'%PDF-changed')
        with self.assertRaises(ValueError): workspace.deliver(source, self.root / 'new.pdf', sha, report)
        self.assertEqual(dest.read_bytes(), b'%PDF-reviewed')

    def test_delivery_rejects_stale_content(self):
        source = self.root / 'CV.pdf'; source.write_bytes(b'%PDF-reviewed')
        content = self.root / 'content.json'; content.write_text('{}')
        sha = hashlib.sha256(source.read_bytes()).hexdigest()
        report = self.root / 'validation.json'; report.write_text(json.dumps({'ok': True, 'pdf_sha256': sha, 'content': 'content.json', 'content_sha256': hashlib.sha256(b'old').hexdigest()}))
        with self.assertRaises(ValueError): workspace.deliver(source, self.root / 'final.pdf', sha, report)

    def test_counter_defines_unicode_newlines_and_ranges(self):
        self.assertEqual(counter.counts('a\r\n🙂'), {'characters': 4, 'words': 2})
        path = self.root / 'answer.txt'; path.write_bytes('a\r\n🙂'.encode())
        result = subprocess.run([sys.executable, str(S / 'answer-interview/scripts/count_answer.py'), str(path), '--max-characters', '3'], capture_output=True, text=True)
        self.assertEqual(result.returncode, 1)
        self.assertEqual(json.loads(result.stdout)['counts']['characters'], 4)

    def test_counter_rejects_incomplete_or_invalid_bounds(self):
        for constraints in ({'max_words': {}}, {'max_words': {'value': True}}, {'min_words': {'value': 3}, 'max_words': {'value': 2}}):
            with self.assertRaises(ValueError): counter.bounds(constraints)

    def test_count_checker_requires_all_units_and_each_answer(self):
        record = {'constraints': {'max_characters': {'value': 20}, 'max_words': {'value': 4}}, 'evidence': {'answer_text': 'An answer', 'reported_counts': {'words': 2}}}
        self.assertEqual(answers.check_reported_count(record)['status'], 'unverified')
        record['evidence']['reported_counts']['characters'] = 999
        self.assertEqual(answers.check_reported_count(record)['status'], 'fail')
        record['evidence'] = {'answers': [
            {'id': 'one', 'text': 'An answer', 'constraints': {'max_words': {'value': 2}}, 'reported_counts': {'words': 2}},
            {'id': 'two', 'text': 'Short', 'constraints': {'min_words': {'value': 2}}, 'reported_counts': {'words': 1}}]}
        self.assertEqual(answers.check_answer_within_limit(record)['status'], 'fail')
        self.assertEqual(answers.check_reported_count(record)['status'], 'pass')

    def test_cv_absent_contacts_sections_and_grades_are_supported(self):
        profile = {'schema_version': 1, 'identity': {'name': 'Example Candidate'}, 'education': [{'institution': 'Example College', 'degree': 'Degree', 'dates': '2024'}]}
        content = {'schema_version': 1, 'document': {'company': 'Example', 'role': 'Analyst', 'language': 'de'}}
        cv.validate_inputs(profile, content)
        self.assertEqual(cv.active_sections(profile, content), ['AUSBILDUNG'])
        if importlib.util.find_spec('docx') and importlib.util.find_spec('pypdf') and importlib.util.find_spec('pypdfium2'):
            build = module('build_cv', S / 'create-cv/scripts/build_cv.py')
            output = self.root / 'CV.docx'; build.build_docx(profile, content, output)
            from docx import Document
            text = '\n'.join(p.text for p in Document(output).paragraphs) + '\n' + '\n'.join(c.text for t in Document(output).tables for row in t.rows for c in row.cells)
            self.assertIn('AUSBILDUNG', text)
            self.assertNotIn('GPA', text)
            self.assertNotIn('PROFESSIONAL EXPERIENCE', text)
        for language in ('en', 'de', 'fr', 'nl'):
            content['document']['language'] = language
            cv.validate_inputs(profile, content)
            self.assertEqual(len(cv.active_sections(profile, content)), 1)

    def test_cv_rejects_malformed_provided_data(self):
        with self.assertRaises(ValueError):
            cv.validate_inputs({'schema_version': 1, 'identity': {'name': 'Example', 'email': {'label': 'Email'}}}, {'schema_version': 1, 'document': {'company': '', 'role': ''}, 'hard_skills': [{'label': 'Tools', 'details': 'Python'}]})

    @unittest.skipUnless(importlib.util.find_spec('reportlab') and importlib.util.find_spec('pypdfium2'), 'PDF libraries unavailable in this Python')
    def test_letter_custom_structure_pdf_qa_and_overwrite_preservation(self):
        generator = module('generate_cover_letter_pdf', S / 'draft-cover-letter/scripts/generate_cover_letter_pdf.py')
        verifier = module('verify_letter_pdf', S / 'draft-cover-letter/scripts/verify_letter_pdf.py')
        source = self.root / 'letter.json'
        source.write_text(json.dumps({'greeting': 'Dear hiring team,', 'paragraphs': ['I am applying for the analyst role.', 'I would welcome a conversation.'], 'sign_off': 'Kind regards,', 'name': 'Example Candidate'}))
        letter = generator.read_letter(source)
        pdf = self.root / 'Letter.pdf'
        generator.create_pdf(letter, pdf, S / 'draft-cover-letter/references/fonts/EBGaramond-Regular.ttf', 1)
        report = verifier.verify(pdf, source, self.root / 'qa')
        self.assertTrue(report['ok'], report)
        original = pdf.read_bytes()
        result = subprocess.run([sys.executable, str(S / 'draft-cover-letter/scripts/generate_cover_letter_pdf.py'), str(source), str(pdf)], capture_output=True)
        self.assertEqual(result.returncode, 2)
        self.assertEqual(pdf.read_bytes(), original)

if __name__ == '__main__': unittest.main()
