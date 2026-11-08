import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { createHash, randomUUID } from 'node:crypto';
import { fileURLToPath } from 'node:url';

export const BEGIN = '<!-- BEGIN agent-stack:global-routing -->';
export const END = '<!-- END agent-stack:global-routing -->';
const template = fileURLToPath(new URL('../templates/global-routing.md', import.meta.url));
const digest = value => createHash('sha256').update(value).digest('hex');

function read(target) {
  const stat = fs.lstatSync(target, { throwIfNoEntry: false });
  if (!stat) return null;
  if (!stat.isFile() || stat.isSymbolicLink()) throw new Error(`Not a regular instruction file: ${target}`);
  const bytes = fs.readFileSync(target);
  if (!Buffer.from(bytes.toString('utf8')).equals(bytes)) throw new Error(`Not UTF-8: ${target}`);
  return bytes;
}

export function targetFor(host, { configDir, env = process.env, home = os.homedir() } = {}) {
  if (!['codex', 'claude-code'].includes(host)) throw new Error('Choose codex or claude-code');
  const directory = path.resolve(configDir || (host === 'codex' ? env.CODEX_HOME : env.CLAUDE_CONFIG_DIR)
    || path.join(home, host === 'codex' ? '.codex' : '.claude'));
  if (host === 'codex') {
    const override = path.join(directory, 'AGENTS.override.md');
    if (read(override)?.toString('utf8').trim()) return override;
  }
  return path.join(directory, host === 'codex' ? 'AGENTS.md' : 'CLAUDE.md');
}

export function merge(original, body) {
  const eol = original.includes('\r\n') ? '\r\n' : '\n';
  if (!body.trim() || body.includes('agent-stack:global-routing')) throw new Error('Invalid routing body');
  const block = `${BEGIN}${eol}${body.trim().replace(/\r?\n/g, eol)}${eol}${END}`;
  const mentions = original.match(/agent-stack:global-routing/gi) || [];
  let prefix = original, suffix = '', separator = '';
  if (mentions.length) {
    const start = original.indexOf(BEGIN), end = original.indexOf(END);
    const lineOnly = (offset, marker) => offset >= 0
      && (offset === 0 || original[offset - 1] === '\n')
      && /^(?:\r?\n|$)/.test(original.slice(offset + marker.length));
    if (mentions.length !== 2 || end <= start || !lineOnly(start, BEGIN) || !lineOnly(end, END)) {
      throw new Error('Malformed or duplicate Agent Stack routing markers; no files written');
    }
    prefix = original.slice(0, start);
    suffix = original.slice(end + END.length);
  } else {
    separator = !original || original.endsWith(eol + eol) ? '' : original.endsWith(eol) ? eol : eol + eol;
    suffix = '';
  }
  const next = prefix + separator + block + (mentions.length ? suffix : eol);
  return { next, prefix, suffix, block };
}

function checkSkills(directory) {
  if (!directory || !path.isAbsolute(directory)) throw new Error('Provide an absolute --skills-dir containing installed public skills');
  for (const name of ['skill-issue']) {
    const target = path.join(directory, name, 'SKILL.md');
    const content = fs.readFileSync(target, 'utf8');
    const metadata = content.match(/^---\r?\n([\s\S]*?)\r?\n---\r?\n([\s\S]+)$/);
    const declared = metadata?.[1].match(/^name:\s*["']?([a-z-]+)["']?\s*$/m)?.[1];
    if (declared !== name || !metadata[2].trim()) throw new Error(`Invalid installed entry: ${target}`);
  }
}

export function setup({ host, skillsDir, configDir, apply = false, expectedSha256, env, home }) {
  checkSkills(skillsDir);
  const target = targetFor(host, { configDir, env, home });
  const before = read(target);
  const beforeHash = before === null ? 'missing' : digest(before);
  if (apply && expectedSha256 !== beforeHash) throw new Error('Instruction file changed since preview, or --expected-sha256 is missing; preview again');
  const body = fs.readFileSync(template, 'utf8');
  const result = merge(before?.toString('utf8') ?? '', body);
  const after = Buffer.from(result.next);
  const changed = before === null || !before.equals(after);
  let backup = null;
  if (apply && changed) {
    const parent = path.dirname(target);
    fs.mkdirSync(parent, { recursive: true });
    const mode = before === null ? 0o600 : fs.statSync(target).mode & 0o777;
    const currentHash = () => { const value = read(target); return value === null ? 'missing' : digest(value); };
    if (targetFor(host, { configDir, env, home }) !== target || currentHash() !== beforeHash) {
      throw new Error('Active instruction file changed during setup; preview again');
    }
    if (before !== null) {
      backup = `${target}.agent-stack.${randomUUID()}.bak`;
      fs.writeFileSync(backup, before, { flag: 'wx', mode: 0o600 });
    }
    const temporary = path.join(parent, `.agent-stack-${randomUUID()}.tmp`);
    try {
      fs.writeFileSync(temporary, after, { flag: 'wx', mode });
      if (currentHash() !== beforeHash) throw new Error('Instruction file changed before replacement; preview again');
      // Exclusive creation avoids replacing a concurrently created base file.
      if (before === null) fs.linkSync(temporary, target);
      else fs.renameSync(temporary, target);
    } finally {
      fs.rmSync(temporary, { force: true });
    }
    if (!read(target)?.equals(after)) throw new Error(`Write verification failed: ${target}`);
  }
  return {
    host, target, applied: apply, changed,
    action: !changed ? 'unchanged' : before === null ? 'created' : before.includes(Buffer.from(BEGIN)) ? 'updated' : 'appended',
    before_sha256: beforeHash, after_sha256: digest(after), backup,
    prefix_bytes: Buffer.byteLength(result.prefix), prefix_sha256: digest(result.prefix),
    suffix_bytes: Buffer.byteLength(result.suffix), suffix_sha256: digest(result.suffix),
    rerun_unchanged: merge(result.next, body).next === result.next,
    block: result.block,
  };
}

if (process.argv[1] && path.resolve(process.argv[1]) === fileURLToPath(import.meta.url)) {
  try {
    const options = {};
    const names = { '--host': 'host', '--skills-dir': 'skillsDir', '--config-dir': 'configDir', '--expected-sha256': 'expectedSha256' };
    const args = process.argv.slice(2);
    while (args.length) {
      const flag = args.shift();
      if (flag === '--apply') options.apply = true;
      else if (names[flag] && args.length && !args[0].startsWith('--')) options[names[flag]] = args.shift();
      else throw new Error(`Unknown or incomplete option: ${flag}`);
    }
    console.log(JSON.stringify(setup(options), null, 2));
  } catch (error) {
    console.error(error.message);
    process.exitCode = 1;
  }
}
