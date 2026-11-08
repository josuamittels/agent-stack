import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { setup, targetFor, merge, BEGIN, END } from '../src/skills/setup-agent-stack/scripts/setup.mjs';
import { load, buildSkill, validateSkill } from '../scripts/build-skills.mjs';

function fixture(t) {
  const root = fs.mkdtempSync(path.join(os.tmpdir(), 'agent-stack-setup-'));
  t.after(() => fs.rmSync(root, { recursive: true, force: true }));
  const skillsDir = path.join(root, 'skills');
  for (const name of ['skill-issue']) {
    fs.mkdirSync(path.join(skillsDir, name), { recursive: true });
    fs.writeFileSync(path.join(skillsDir, name, 'SKILL.md'), `---\nname: ${name}\n---\n# ${name}\nInstalled instructions.\n`);
  }
  const configDir = path.join(root, 'profile');
  fs.mkdirSync(configDir);
  return { root, skillsDir, configDir, host: 'codex' };
}

test('preview is read-only; apply preserves manual bytes, file mode and an exact backup', t => {
  const options = fixture(t);
  const target = path.join(options.configDir, 'AGENTS.md');
  const original = Buffer.from('# Personal\r\n\r\nKeep café and 日本語.\r\n');
  fs.writeFileSync(target, original, { mode: 0o640 });
  const preview = setup(options);
  assert.deepEqual(fs.readFileSync(target), original);
  assert.deepEqual(fs.readdirSync(options.configDir), ['AGENTS.md']);
  const applied = setup({ ...options, apply: true, expectedSha256: preview.before_sha256 });
  assert.deepEqual(fs.readFileSync(target).subarray(0, original.length), original);
  assert.deepEqual(fs.readFileSync(applied.backup), original);
  assert.equal(fs.statSync(target).mode & 0o777, 0o640);
  assert.equal(fs.statSync(applied.backup).mode & 0o777, 0o600);
  assert.equal(applied.rerun_unchanged, true);
  const stat = fs.statSync(target);
  const again = setup({ ...options, apply: true, expectedSha256: applied.after_sha256 });
  assert.equal(again.changed, false);
  assert.equal(again.backup, null);
  assert.equal(fs.statSync(target).mtimeMs, stat.mtimeMs);
  assert.equal(fs.readdirSync(options.configDir).length, 2);
});

test('refresh replaces only the owned block and preserves a manual suffix', t => {
  const options = fixture(t);
  const original = `# Manual\n\n${BEGIN}\nold routing\n${END}\n\n# More manual\nKeep this.\n`;
  const target = path.join(options.configDir, 'AGENTS.md');
  fs.writeFileSync(target, original);
  const preview = setup(options);
  setup({ ...options, apply: true, expectedSha256: preview.before_sha256 });
  const after = fs.readFileSync(target, 'utf8');
  assert.ok(after.startsWith('# Manual\n\n' + BEGIN));
  assert.ok(after.endsWith('\n\n# More manual\nKeep this.\n'));
  assert.ok(!after.includes('old routing'));
});

test('Codex uses its active override and honors custom environment homes', t => {
  const options = fixture(t);
  const env = { CODEX_HOME: options.configDir, CLAUDE_CONFIG_DIR: path.join(options.root, 'claude') };
  const override = path.join(options.configDir, 'AGENTS.override.md');
  fs.writeFileSync(override, '');
  assert.equal(targetFor('codex', { env }), path.join(options.configDir, 'AGENTS.md'));
  fs.writeFileSync(override, '# Active override\n');
  assert.equal(targetFor('codex', { env }), override);
  assert.equal(targetFor('claude-code', { env }), path.join(env.CLAUDE_CONFIG_DIR, 'CLAUDE.md'));
  const preview = setup(options);
  setup({ ...options, apply: true, expectedSha256: preview.before_sha256 });
  assert.ok(fs.readFileSync(override, 'utf8').includes(BEGIN));
  assert.equal(fs.existsSync(path.join(options.configDir, 'AGENTS.md')), false);
});

test('Claude creates only its selected global file', t => {
  const options = { ...fixture(t), host: 'claude-code' };
  const preview = setup(options);
  assert.equal(fs.existsSync(preview.target), false);
  const applied = setup({ ...options, apply: true, expectedSha256: 'missing' });
  assert.equal(applied.action, 'created');
  assert.equal(path.basename(applied.target), 'CLAUDE.md');
  assert.equal(fs.statSync(applied.target).mode & 0o777, 0o600);
  assert.deepEqual(fs.readdirSync(options.configDir), ['CLAUDE.md']);
});

test('concurrent edits, malformed markers, symlinks, and missing installations stop writes', t => {
  const options = fixture(t);
  const target = path.join(options.configDir, 'AGENTS.md');
  fs.writeFileSync(target, '# Original\n');
  const preview = setup(options);
  fs.writeFileSync(target, '# Concurrent edit\n');
  assert.throws(() => setup({ ...options, apply: true, expectedSha256: preview.before_sha256 }), /changed since preview/);
  assert.equal(fs.readFileSync(target, 'utf8'), '# Concurrent edit\n');
  for (const content of [BEGIN, END, `${END}\n${BEGIN}`, `${BEGIN}\n${END}\n${BEGIN}\n${END}`, `inline ${BEGIN}\n${END}`]) {
    fs.writeFileSync(target, content);
    assert.throws(() => setup(options), /markers/);
    assert.equal(fs.readFileSync(target, 'utf8'), content);
  }
  fs.unlinkSync(target);
  const other = path.join(options.root, 'shared.md');
  fs.writeFileSync(other, '# Do not modify\n');
  fs.symlinkSync(other, target);
  assert.throws(() => setup(options), /regular instruction file/);
  assert.equal(fs.readFileSync(other, 'utf8'), '# Do not modify\n');
  fs.unlinkSync(target);
  fs.rmSync(path.join(options.skillsDir, 'skill-issue'), { recursive: true });
  assert.throws(() => setup(options), /ENOENT/);
  assert.equal(fs.existsSync(target), false);
});

test('merge is byte-stable on rerun even without an original trailing newline', () => {
  const first = merge('# Personal notes', 'New routing');
  assert.ok(first.next.startsWith('# Personal notes\n\n'));
  assert.equal(merge(first.next, 'New routing').next, first.next);
});

test('setup package is self-contained and declares its helper, template and objective package', () => {
  const out = buildSkill(load(), 'setup-agent-stack');
  validateSkill(out, 'setup-agent-stack');
  for (const file of [
    'references/_stack/skills/setup-agent-stack/scripts/setup.mjs',
    'references/_stack/skills/setup-agent-stack/templates/global-routing.md',
    'references/_stack/evals/setup-agent-stack/rubric.json',
    'references/_stack/evals/setup-agent-stack/checks.py',
  ]) assert.ok(out.has(file), file);
});
