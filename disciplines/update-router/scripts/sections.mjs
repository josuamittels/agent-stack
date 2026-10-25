import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

// This helper preserves section boundaries; the calling agent authors the prose.
export function mergeSection(original, body, name) {
  if (typeof body !== 'string' || !body.trim()) throw new Error(`${name}: empty body`);
  if (/agent-stack:(?:entry|route-catalog)/i.test(body)) {
    throw new Error(`${name}: body must not contain managed markers`);
  }
  const begin = `<!-- BEGIN agent-stack:${name} -->`;
  const end = `<!-- END agent-stack:${name} -->`;
  const mentions = original.match(new RegExp(`agent-stack:${name}`, 'gi')) || [];
  const eol = original.includes('\r\n') ? '\r\n' : '\n';
  const normalized = body.trim().replace(/\r?\n/g, eol);
  const block = `${begin}${eol}${normalized}${eol}${end}`;
  if (mentions.length === 0) {
    const separator = !original ? '' : original.endsWith(`${eol}${eol}`) ? '' : original.endsWith(eol) ? eol : `${eol}${eol}`;
    return `${original}${separator}${block}${eol}`;
  }
  const start = original.indexOf(begin);
  const finish = original.indexOf(end);
  const lineOnly = (offset, marker) => offset >= 0
    && (offset === 0 || original[offset - 1] === '\n')
    && /^(?:\r?\n|$)/.test(original.slice(offset + marker.length));
  if (mentions.length !== 2 || finish <= start
      || !lineOnly(start, begin) || !lineOnly(finish, end)) {
    throw new Error(`${name}: invalid managed markers; no files written`);
  }
  return original.slice(0, start) + block + original.slice(finish + end.length);
}

export function refresh(root, bodies) {
  if (!bodies || typeof bodies.entry !== 'string' || typeof bodies.catalog !== 'string') {
    throw new Error('Expected JSON with entry and catalog strings');
  }
  const base = fs.realpathSync(root);
  const specs = [
    ['AGENTS.md', 'entry', '# Agent Stack\n'],
    ['skills/skill-issue/SKILL.md', 'route-catalog', null],
  ];
  // Validate both files before writing either. Refuse symlinks outside this root.
  const changes = specs.map(([relative, name, initial]) => {
    const target = path.join(base, relative);
    const exists = fs.existsSync(target);
    if (!exists && initial === null) throw new Error(`${relative}: missing router`);
    const realParent = fs.realpathSync(path.dirname(target));
    if (realParent !== base && !realParent.startsWith(base + path.sep)) {
      throw new Error(`${relative}: parent escapes repository`);
    }
    if (fs.lstatSync(target, { throwIfNoEntry: false })?.isSymbolicLink()) {
      throw new Error(`${relative}: refusing a symlink`);
    }
    const old = exists ? fs.readFileSync(target, 'utf8') : null;
    const next = mergeSection(old ?? initial, name === 'entry' ? bodies.entry : bodies.catalog, name);
    return { relative, target, old, next };
  });
  for (const change of changes) {
    const current = fs.existsSync(change.target) ? fs.readFileSync(change.target, 'utf8') : null;
    if (current !== change.old) throw new Error(`${change.relative}: changed during refresh`);
  }
  const result = [];
  for (const { relative, target, old, next } of changes) {
    const changed = old !== next;
    if (changed) fs.writeFileSync(target, next, { flag: old === null ? 'wx' : 'w' });
    result.push({ path: relative, changed });
  }
  return result;
}

if (process.argv[1] && path.resolve(process.argv[1]) === fileURLToPath(import.meta.url)) {
  try {
    if (process.argv.length !== 3) throw new Error('Usage: node sections.mjs /absolute/stack < bodies.json');
    console.log(JSON.stringify(refresh(process.argv[2], JSON.parse(fs.readFileSync(0, 'utf8')))));
  } catch (error) {
    console.error(error.message);
    process.exitCode = 1;
  }
}
