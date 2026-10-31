#!/usr/bin/env node
import fs from "node:fs";
import path from "node:path";
import crypto from "node:crypto";
import { fileURLToPath } from "node:url";
import { spawnSync } from "node:child_process";
import { parse, stringify } from "yaml";
import { unified } from "unified";
import remarkParse from "remark-parse";
import { zipSync } from "fflate";

export const ROOT = path.resolve(
  path.dirname(fileURLToPath(import.meta.url)),
  "..",
);
const parser = unified().use(remarkParse);
const MARKER = ".agent-stack-generated.json";
const slug = /^[a-z0-9]+(?:-[a-z0-9]+)*$/;
const semver = /^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)$/;
const hash = (data) => crypto.createHash("sha256").update(data).digest("hex");
const json = (value) => JSON.stringify(value, null, 2) + "\n";
const fail = (message) => {
  throw new Error(message);
};
const posix = (value) => value.split(path.sep).join("/");
const exists = (file) => fs.existsSync(file);
export function files(root) {
  if (!exists(root)) return [];
  return fs
    .readdirSync(root, { withFileTypes: true })
    .sort((a, b) => a.name.localeCompare(b.name, "en"))
    .flatMap((e) => {
      const file = path.join(root, e.name);
      if (e.isSymbolicLink()) fail(`Symlinks are not permitted: ${file}`);
      return e.isDirectory() ? files(file) : [file];
    });
}
export function inside(root, relative) {
  if (
    typeof relative !== "string" ||
    !relative ||
    relative.includes("\\") ||
    path.isAbsolute(relative)
  )
    fail(`Invalid relative path: ${relative}`);
  const dest = path.resolve(root, relative);
  if (
    dest !== path.resolve(root) &&
    !dest.startsWith(path.resolve(root) + path.sep)
  )
    fail(`Path escapes root: ${relative}`);
  let current = path.resolve(root);
  for (const part of path.relative(current, dest).split(path.sep)) {
    current = path.join(current, part);
    if (exists(current) && fs.lstatSync(current).isSymbolicLink())
      fail(`Symlink path: ${relative}`);
  }
  return dest;
}
export function frontmatter(text, label = "Markdown") {
  const m = text.match(/^---\r?\n([\s\S]*?)\r?\n---(?:\r?\n|$)/);
  if (!m) fail(`Missing frontmatter: ${label}`);
  const metadata = parse(m[1], { uniqueKeys: true });
  if (!metadata || typeof metadata !== "object")
    fail(`Invalid frontmatter: ${label}`);
  return { metadata, body: text.slice(m[0].length), offset: m[0].length };
}
function visit(node, fn) {
  fn(node);
  for (const child of node.children ?? []) visit(child, fn);
}
function links(text) {
  const out = [];
  visit(parser.parse(text), (n) => {
    if (["link", "image", "definition"].includes(n.type)) out.push(n);
  });
  return out;
}
const prohibited = (file) =>
  /(^|\/)(?:\.env(?!\.example$)[^/]*|__pycache__|node_modules|\.local|\.git|\.DS_Store)(\/|$)|(?:^|\/)(?:test[^/]*\.(?:py|mjs)|runs\.jsonl)$|\.pyc$/.test(
    file,
  );
function sourceFile(root, relative) {
  if (prohibited(relative)) fail(`Excluded source file: ${relative}`);
  const file = inside(path.join(root, "src"), relative);
  if (!exists(file) || !fs.statSync(file).isFile())
    fail(`Missing required resource: src/${relative}`);
  if (relative.endsWith(".env.example")) {
    for (const line of fs.readFileSync(file, "utf8").split("\n")) {
      if (!line.trim() || line.trim().startsWith("#")) continue;
      if (
        !/^[A-Z_][A-Z0-9_]*\s*=\s*(?:["']?["']?|["']?<[^>]+>["']?)\s*$/.test(
          line,
        )
      )
        fail(
          `Credential example must be blank or a placeholder: src/${relative}`,
        );
    }
  }
  return file;
}
export function load(root = ROOT) {
  const catalog = parse(
    fs.readFileSync(path.join(root, "src/catalog.yaml"), "utf8"),
    { uniqueKeys: true },
  );
  if (
    catalog.schema_version !== 1 ||
    !catalog.skills ||
    !Array.isArray(catalog.runtime)
  )
    fail("Invalid catalog schema");
  if (!/^[\w.-]+\/[\w.-]+$/.test(catalog.repository))
    fail("Invalid repository identity");
  const metas = {};
  const actual = fs
    .readdirSync(path.join(root, "src/skills"))
    .filter((n) => exists(path.join(root, "src/skills", n, "SKILL.md.tmpl")))
    .sort();
  if (json(actual) !== json(Object.keys(catalog.skills).sort()))
    fail("Catalog must declare every canonical skill exactly once");
  for (const [name, item] of Object.entries(catalog.skills)) {
    if (!slug.test(name) || !["public", "internal"].includes(item.visibility))
      fail(`Invalid catalog entry: ${name}`);
    for (const key of [
      "required",
      "conditional",
      "optional",
      "routes",
      "files",
      "resources",
      "evaluations",
      "hosts",
      "requirements",
    ])
      if (!Array.isArray(item[key])) fail(`${name}: ${key} must be an array`);
    for (const dep of [
      ...item.required,
      ...item.conditional,
      ...item.optional,
      ...item.routes,
    ])
      if (!catalog.skills[dep]) fail(`${name}: unknown dependency ${dep}`);
    if (!item.files.includes(`skills/${name}/SKILL.md.tmpl`))
      fail(`${name}: missing instruction entry`);
    if (new Set(item.files).size !== item.files.length)
      fail(`${name}: duplicate file declaration`);
    for (const file of item.files) {
      if (!file.startsWith(`skills/${name}/`))
        fail(`${name}: owned file outside skill`);
      sourceFile(root, file);
    }
    for (const file of item.resources) {
      if (!file.startsWith("guidelines/"))
        fail(`${name}: invalid guideline path`);
      sourceFile(root, file);
    }
    for (const id of item.evaluations) {
      if (!slug.test(id)) fail("Invalid evaluation slug");
      for (const f of ["rubric.json", "checks.py"])
        sourceFile(root, `evals/${id}/${f}`);
    }
    const meta = frontmatter(
      fs.readFileSync(sourceFile(root, `skills/${name}/SKILL.md.tmpl`), "utf8"),
      name,
    ).metadata;
    if (
      meta.name !== name ||
      typeof meta.description !== "string" ||
      !meta.description.trim() ||
      !semver.test(meta.version) ||
      !["draft", "experimental", "stable", "deprecated"].includes(meta.status)
    )
      fail(`Invalid skill metadata: ${name}`);
    metas[name] = meta;
  }
  for (const file of catalog.runtime) sourceFile(root, file);
  const versionText = fs.readFileSync(path.join(root, "VERSIONS.md"), "utf8");
  const version = versionText.match(/\| Version \| `([^`]+)`/)?.[1];
  const status = versionText.match(/\| Status \| `([^`]+)`/)?.[1];
  if (
    !semver.test(version ?? "") ||
    !["draft", "experimental", "stable", "deprecated"].includes(status)
  )
    fail("Invalid stack version record");
  return { root, catalog, metas, version, status };
}
export function closure(ctx, name) {
  const seen = new Set();
  function add(id) {
    if (seen.has(id)) return;
    seen.add(id);
    const item = ctx.catalog.skills[id];
    for (const dep of [...item.required, ...item.conditional]) add(dep);
  }
  add(name);
  return [...seen].sort();
}
function resourceSet(ctx, name) {
  const set = new Set(ctx.catalog.runtime);
  for (const id of closure(ctx, name)) {
    const item = ctx.catalog.skills[id];
    for (const f of [...item.files, ...item.resources]) set.add(f);
    for (const target of item.evaluations)
      for (const f of ["rubric.json", "checks.py"])
        set.add(`evals/${target}/${f}`);
  }
  return [...set].sort();
}
export function blockers(ctx, name) {
  const out = [];
  for (const id of closure(ctx, name))
    if (ctx.metas[id].status !== "stable")
      out.push(`skill ${id}: ${ctx.metas[id].status}`);
  for (const file of resourceSet(ctx, name).filter(
    (f) => f.endsWith(".md") && !f.includes("/templates/"),
  )) {
    const text = fs.readFileSync(sourceFile(ctx.root, file), "utf8");
    if (!text.startsWith("---\n")) continue;
    const m = frontmatter(text, file).metadata;
    if (m.version && m.status && m.status !== "stable")
      out.push(`resource ${file}: ${m.status}`);
  }
  return [...new Set(out)].sort();
}
function destination(relative) {
  let output = `references/_stack/${relative}`;
  if (
    relative.startsWith("skills/") &&
    /^skills\/[^/]+\/SKILL\.md\.tmpl$/.test(relative)
  )
    output = output.replace(/SKILL\.md\.tmpl$/, "instructions.md");
  else if (path.basename(relative) === "SKILL.md") output += ".template";
  return output;
}
function routerBody(ctx, preview) {
  const names = Object.keys(ctx.catalog.skills)
    .filter(
      (n) =>
        n !== "skill-issue" &&
        ctx.catalog.skills[n].visibility === "public" &&
        (preview || blockers(ctx, n).length === 0),
    )
    .sort();
  return (
    "# Skill Issue\n\nChoose the smallest sufficient installed capability for the user’s outcome. Honor explicit choices and keep the selected workflow in charge of handoffs. Guidelines are references, never route destinations.\n\n## Catalog\n\n" +
    names.map((n) => `- **${n}**: ${ctx.metas[n].description}`).join("\n") +
    "\n\n## Handoff\n\nThis catalog is not proof of installation. Check the host’s installed skill catalog and read the selected installed entry before handing off. If unavailable, report the missing capability or handle the request directly; do not install, fetch, or fabricate an invocation. Do not discover skills from private dependency snapshots, templates, or research sources. Do not change project instructions.\n"
  );
}
function transform(ctx, relative, text, mapping, preview) {
  if (relative === "skills/skill-issue/SKILL.md.tmpl")
    return routerBody(ctx, preview);
  if (relative.includes("/templates/")) return text;
  const isMD = relative.endsWith(".md") || relative.endsWith(".md.tmpl");
  if (!isMD) return text;
  const prefix = text.startsWith("---\n")
    ? frontmatter(text, relative)
    : { body: text, offset: 0 };
  const edits = [];
  for (const node of links(prefix.body)) {
    const url = node.url;
    if (!url || /^(?:[a-z][\w+.-]*:|#|\/\/)/i.test(url)) continue;
    if (url.startsWith("/")) fail(`${relative}: absolute local link ${url}`);
    const [raw, fragment] = url.split(/(?=#)/, 2);
    const target = posix(
      path.normalize(
        path.join(path.dirname(relative), decodeURIComponent(raw)),
      ),
    );
    let dest = mapping.get(target);
    if (
      !dest &&
      [...mapping.keys()].some((k) =>
        k.startsWith(target.replace(/\/$/, "") + "/"),
      )
    )
      dest = destination(target);
    if (
      !dest &&
      ctx.catalog.project_files?.includes(target.replace(/^\.\.\//, "")) &&
      target.startsWith("../")
    ) {
      const start = prefix.offset + node.position.start.offset,
        end = prefix.offset + node.position.end.offset;
      edits.push({
        start,
        end,
        text: "`" + target.slice(3) + "` in the target repository",
      });
      continue;
    }
    if (!dest) fail(`${relative}: undeclared or missing runtime link ${url}`);
    const replacement =
      posix(path.relative(path.dirname(mapping.get(relative)), dest)) +
      (fragment ?? "");
    const start = prefix.offset + node.position.start.offset,
      end = prefix.offset + node.position.end.offset;
    const original = text.slice(start, end);
    const index = original.lastIndexOf(url);
    if (index < 0) fail(`Cannot rewrite Markdown link: ${relative}`);
    edits.push({
      start: start + index,
      end: start + index + url.length,
      text: replacement,
    });
  }
  for (const edit of edits.sort((a, b) => b.start - a.start))
    text = text.slice(0, edit.start) + edit.text + text.slice(edit.end);
  // Only execution examples get a package location; target-project authoring paths remain unchanged.
  text = text.replace(
    /\b(python3?|node) src\/(skills\/[^\s`]+)(?=\s|`|$)/g,
    (_, cmd, file) => `${cmd} "$AGENT_STACK_ROOT/${file}"`,
  );
  return text;
}
function add(map, name, bytes, mode = 0o644) {
  if (map.has(name)) fail(`Conflicting output mapping: ${name}`);
  map.set(name, {
    bytes: Buffer.isBuffer(bytes) ? bytes : Buffer.from(bytes),
    mode,
  });
}
function validateRuntime(ctx, sources) {
  const selected = new Set(sources);
  const python = sources.filter((f) => f.endsWith(".py"));
  if (!python.length) return;
  const script = `import ast,json,sys
from pathlib import Path
r=Path(sys.argv[1]); selected=set(json.load(sys.stdin)); external=set(json.loads(sys.argv[2])); modules={}
for base in ['skills','evals','runtime']:
 for p in (r/base).rglob('*.py'):
  if '__pycache__' not in p.parts and not p.name.startswith('test'):
   modules.setdefault(p.stem,[]).append(p.relative_to(r).as_posix())
errors=[]
for rel in sorted(selected):
 if not rel.endswith('.py'):continue
 for n in ast.walk(ast.parse((r/rel).read_text(),filename=rel)):
  imports=[a.name.split('.')[0] for a in n.names] if isinstance(n,ast.Import) else [n.module.split('.')[0]] if isinstance(n,ast.ImportFrom) and n.module else []
  for name in imports:
   if name in sys.stdlib_module_names or name=='__future__' or name in external:continue
   candidates=modules.get(name,[])
   if not any(p in selected for p in candidates): errors.append(rel+': undeclared Python runtime import '+name)
print(json.dumps(errors))`;
  const result = spawnSync(
    "python3",
    [
      "-c",
      script,
      path.join(ctx.root, "src"),
      JSON.stringify(ctx.catalog.python_packages ?? []),
    ],
    { input: JSON.stringify([...selected]), encoding: "utf8" },
  );
  if (result.status !== 0)
    fail(
      "Python syntax/import inspection failed: " +
        (result.error?.message ?? result.stderr),
    );
  const errors = JSON.parse(result.stdout);
  if (errors.length) fail(errors.join("\n"));
}
export function buildSkill(ctx, name, { preview = false } = {}) {
  const entry = ctx.catalog.skills[name];
  if (!entry) fail(`Unknown skill: ${name}`);
  if (entry.visibility !== "public")
    fail(`Internal skill is not installable: ${name}`);
  const blocked = blockers(ctx, name);
  if (!preview && blocked.length)
    fail(`${name}: unstable dependency closure: ${blocked.join("; ")}`);
  const sources = resourceSet(ctx, name);
  validateRuntime(ctx, sources);
  const mapping = new Map(sources.map((f) => [f, destination(f)]));
  const out = new Map();
  const sourceHashes = {};
  for (const file of sources) {
    const src = sourceFile(ctx.root, file),
      bytes = fs.readFileSync(src);
    sourceHashes[`src/${file}`] = hash(bytes);
    const text = /\.md(?:\.tmpl)?$/.test(file)
      ? transform(ctx, file, bytes.toString("utf8"), mapping, preview)
      : bytes;
    add(
      out,
      mapping.get(file),
      text,
      fs.statSync(src).mode & 0o111 ? 0o755 : 0o644,
    );
  }
  const meta = ctx.metas[name];
  const publicMeta = {
    name,
    description: meta.description,
    license: "MIT",
    metadata: {
      version: meta.version,
      status: meta.status,
      "stack-version": ctx.version,
      distribution: preview ? "preview" : "stable",
    },
  };
  const warning = preview ? "\nThis is an unpublished local preview.\n" : "";
  add(
    out,
    "SKILL.md",
    "---\n" +
      stringify(publicMeta) +
      "---\n\n# " +
      name +
      "\n" +
      warning +
      "\nRead and apply [the complete bundled workflow](references/_stack/skills/" +
      name +
      "/instructions.md) before doing the task. Load its linked resources when instructed.\n\nResolve `AGENT_STACK_ROOT` to this package’s absolute `references/_stack` directory before running command examples (set it explicitly in the command environment). Source references beginning `src/skills/`, `src/guidelines/`, or `src/evals/` map to the corresponding directories under `AGENT_STACK_ROOT` with `src/` removed. This location supplies instructions and checker resources; it is not the caller’s project. Files authored for a target project belong in that project, never in the installed package. Use bundled dependency snapshots for internal handoffs, even if another version is installed separately. Read them in the current context when native invocation cannot guarantee the bundled version. Do not fetch required instructions online or treat private files as separately installed skills. Save configuration and runtime state outside this package.\n",
  );
  add(out, "LICENSE", fs.readFileSync(path.join(ctx.root, "LICENSE")));
  const manifest = {
    schema_version: 1,
    catalog_sha256: hash(
      fs.readFileSync(path.join(ctx.root, "src/catalog.yaml")),
    ),
    name,
    version: meta.version,
    status: meta.status,
    stack_version: ctx.version,
    channel: preview ? "preview" : "stable",
    dependencies: closure(ctx, name).map((id) => ({
      name: id,
      version: ctx.metas[id].version,
      status: ctx.metas[id].status,
    })),
    source_sha256: sourceHashes,
    files: Object.fromEntries(
      [...out]
        .sort(([a], [b]) => a.localeCompare(b))
        .map(([f, v]) => [f, { sha256: hash(v.bytes), mode: v.mode }]),
    ),
  };
  add(out, "package-manifest.json", json(manifest));
  validateSkill(out, name, { preview });
  return out;
}
export function validateSkill(out, name, { preview = false } = {}) {
  const manifest = JSON.parse(
    out.get("package-manifest.json")?.bytes ?? "null",
  );
  if (!manifest || manifest.name !== name)
    fail(`Invalid package manifest: ${name}`);
  const actual = [...out.keys()]
    .filter((f) => f !== "package-manifest.json")
    .sort();
  if (json(actual) !== json(Object.keys(manifest.files).sort()))
    fail(`${name}: manifest file set mismatch`);
  if (
    !preview &&
    (manifest.channel !== "stable" ||
      manifest.dependencies.some((d) => d.status !== "stable"))
  )
    fail(`${name}: unstable package`);
  for (const [f, v] of out) {
    inside("/package", f);
    if (prohibited(f)) fail(`Excluded packaged file: ${f}`);
    if (
      f !== "package-manifest.json" &&
      (manifest.files[f]?.sha256 !== hash(v.bytes) ||
        manifest.files[f]?.mode !== v.mode)
    )
      fail(`Package digest mismatch: ${f}`);
    if (path.basename(f) === "SKILL.md" && f !== "SKILL.md")
      fail(`Private skill exposed to discovery: ${f}`);
    if (!f.endsWith(".md") || f.includes("/templates/")) continue;
    const text = v.bytes.toString("utf8");
    const body = text.startsWith("---\n") ? frontmatter(text, f).body : text;
    for (const node of links(body)) {
      const url = node.url;
      if (!url || /^(?:[a-z][\w+.-]*:|#|\/\/)/i.test(url)) continue;
      if (url.startsWith("/")) fail(`${name}: absolute package link ${url}`);
      const raw = decodeURIComponent(url.split("#")[0]);
      const resolved = posix(path.normalize(path.join(path.dirname(f), raw)));
      inside("/package", resolved);
      if (
        !out.has(resolved) &&
        ![...out.keys()].some((k) =>
          k.startsWith(resolved.replace(/\/$/, "") + "/"),
        )
      )
        fail(`${name}: broken package link ${f} -> ${url}`);
    }
  }
  frontmatter(out.get("SKILL.md").bytes.toString(), name);
}
function writeTree(dir, map) {
  for (const [relative, value] of map) {
    const file = inside(dir, relative);
    fs.mkdirSync(path.dirname(file), { recursive: true });
    fs.writeFileSync(file, value.bytes, { mode: value.mode });
  }
}
function tree(dir) {
  return new Map(
    files(dir).map((f) => [
      posix(path.relative(dir, f)),
      {
        bytes: fs.readFileSync(f),
        mode: fs.statSync(f).mode & 0o111 ? 0o755 : 0o644,
      },
    ]),
  );
}
function same(a, b) {
  return (
    a.size === b.size &&
    [...a].every(
      ([k, v]) =>
        b.has(k) && v.mode === b.get(k).mode && v.bytes.equals(b.get(k).bytes),
    )
  );
}
function installDocs(ctx, names) {
  return (
    "# Generated installation reference\n\nGenerated from `src/catalog.yaml`. Commands target the eventual stable catalog; local previews use paths under `dist/preview/skills`.\n\n```sh\nnpx skills add " +
    ctx.catalog.repository +
    " --skill '*' -a codex\nnpx skills add " +
    ctx.catalog.repository +
    " --skill '*' -a claude-code\n```\n\nUse `-g` for a user-wide installation. Project scope is the default.\n\n" +
    names
      .map(
        (n) =>
          `## ${n}\n\nStatus: ${blockers(ctx, n).length ? "blocked for public release (see skills/catalog.json)" : "eligible stable candidate"}.\n\n${ctx.metas[n].description}\n\n\`npx skills add ${ctx.catalog.repository} --skill ${closure(
            ctx,
            n,
          )
            .filter((id) => ctx.catalog.skills[id].visibility === "public")
            .join(" ")} -a codex\`\n\nBundled dependencies: ${
            closure(ctx, n)
              .filter((id) => id !== n)
              .join(", ") || "none"
          }.\n\nRequirements: ${[...new Set(closure(ctx, n).flatMap((id) => ctx.catalog.skills[id].requirements))].join("; ")}.\n`,
      )
      .join("\n")
  );
}
export function buildCatalog(ctx, { preview = false, skill } = {}) {
  const candidates = Object.keys(ctx.catalog.skills)
    .filter((n) => ctx.catalog.skills[n].visibility === "public")
    .sort();
  if (skill && !candidates.includes(skill))
    fail(`Not a public candidate: ${skill}`);
  const selected = skill ? [skill] : candidates;
  const eligible = selected.filter(
    (n) => preview || blockers(ctx, n).length === 0,
  );
  const out = new Map();
  for (const name of eligible)
    for (const [f, v] of buildSkill(ctx, name, { preview }))
      add(out, `${name}/${f}`, v.bytes, v.mode);
  add(
    out,
    "README.md",
    "# Generated public skills\n\nEdit canonical files in `src/`; run `npm run build`. Only stable candidates with stable required dependencies appear here.\n",
  );
  add(
    out,
    MARKER,
    json({
      schema_version: 1,
      owner: "agent-stack",
      channel: preview ? "preview" : "stable",
    }),
  );
  add(
    out,
    "catalog.json",
    json({
      schema_version: 1,
      stack_version: ctx.version,
      channel: preview ? "preview" : "stable",
      skills: eligible,
      blocked: Object.fromEntries(
        selected
          .filter((n) => !eligible.includes(n))
          .map((n) => [n, blockers(ctx, n)]),
      ),
    }),
  );
  return {
    out,
    eligible,
    candidates,
    documentation: installDocs(ctx, selected),
  };
}
function replaceOwned(dest, map, { check = false } = {}) {
  const existing = tree(dest);
  if (check) {
    if (!same(existing, map))
      fail(`Generated files are stale: ${dest}; run npm run build`);
    return;
  }
  if (
    existing.size &&
    !existing.has(MARKER) &&
    [...existing.keys()].some((k) => k !== "README.md")
  )
    fail(`Refusing to replace unowned directory: ${dest}`);
  if (
    existing.has(MARKER) &&
    JSON.parse(existing.get(MARKER).bytes).owner !== "agent-stack"
  )
    fail(`Invalid output ownership: ${dest}`);
  fs.mkdirSync(path.dirname(dest), { recursive: true });
  const stage = fs.mkdtempSync(
    path.join(path.dirname(dest), ".agent-stack-stage-"),
  );
  const backup = stage + "-previous";
  try {
    writeTree(stage, map);
    if (exists(dest)) fs.renameSync(dest, backup);
    try {
      fs.renameSync(stage, dest);
    } catch (error) {
      if (exists(backup)) fs.renameSync(backup, dest);
      throw error;
    }
    if (exists(backup)) fs.rmSync(backup, { recursive: true });
  } finally {
    fs.rmSync(stage, { recursive: true, force: true });
  }
}
export function releaseGate(ctx) {
  if (ctx.status !== "stable" || Number(ctx.version.split(".")[0]) < 1)
    fail(
      `Publication blocked: stack ${ctx.version} is ${ctx.status}; stable >=1.0.0 required`,
    );
}
function zip(map) {
  const entries = {};
  for (const [f, v] of [...map].sort(([a], [b]) => a.localeCompare(b)))
    entries[f] = [
      new Uint8Array(v.bytes),
      {
        mtime: new Date(1980, 0, 1, 0, 0, 0),
        os: 3,
        attrs: (0o100000 | v.mode) << 16,
      },
    ];
  return Buffer.from(zipSync(entries, { level: 6 }));
}
function plugin(ctx, name, names, packages) {
  const out = new Map();
  for (const id of names)
    for (const [f, v] of packages.get(id))
      add(out, `skills/${id}/${f}`, v.bytes, v.mode);
  const identity = {
    name,
    version: ctx.version,
    description: "Mento reusable agent capabilities",
    author: { name: "Josua Mittelstaedt" },
    repository: `https://github.com/${ctx.catalog.repository}`,
    license: "MIT",
  };
  add(
    out,
    "plugin.json",
    json({
      $schema: "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json",
      ...identity,
    }),
  );
  add(out, ".claude-plugin/plugin.json", json(identity));
  add(out, "LICENSE", fs.readFileSync(path.join(ctx.root, "LICENSE")));
  return out;
}
export function artifacts(ctx, names, { preview = false } = {}) {
  const out = new Map(),
    packages = new Map(names.map((n) => [n, buildSkill(ctx, n, { preview })]));
  const claude = [],
    openai = [];
  const groups = [
    ["agent-stack", names],
    ...names.map((n) => [`agent-stack-${n}`, [n]]),
  ];
  for (const [name, ids] of groups) {
    const bundle = plugin(ctx, name, ids, packages);
    for (const [f, v] of bundle)
      add(out, `plugins/${name}/${f}`, v.bytes, v.mode);
    add(out, `archives/${name}-${ctx.version}.zip`, zip(bundle));
    claude.push({ name, source: `./plugins/${name}`, version: ctx.version });
    openai.push({
      name,
      source: { source: "local", path: `./plugins/${name}` },
      policy: { installation: "AVAILABLE", authentication: "ON_INSTALL" },
      category: "Productivity",
    });
  }
  for (const [name, map] of packages)
    add(out, `archives/${name}-${ctx.version}.zip`, zip(map));
  add(
    out,
    ".claude-plugin/marketplace.json",
    json({
      name: "mento-agent-stack",
      owner: { name: "Josua Mittelstaedt" },
      plugins: claude,
    }),
  );
  add(
    out,
    ".agents/plugins/marketplace.json",
    json({
      name: "mento-agent-stack",
      interface: { displayName: "Mento Agent Stack" },
      plugins: openai,
    }),
  );
  add(out, "INSTALL.md", installDocs(ctx, names));
  add(
    out,
    "agent-stack-distribution.zip",
    zip(new Map([...out].filter(([f]) => !f.startsWith("archives/")))),
  );
  const sums =
    [...out]
      .filter(
        ([f]) =>
          f.startsWith("archives/") || f === "agent-stack-distribution.zip",
      )
      .sort(([a], [b]) => a.localeCompare(b))
      .map(([f, v]) => `${hash(v.bytes)}  ${f}`)
      .join("\n") + "\n";
  add(out, "SHA256SUMS", sums);
  add(
    out,
    MARKER,
    json({
      schema_version: 1,
      owner: "agent-stack",
      channel: preview ? "preview" : "stable",
    }),
  );
  return out;
}
export function main(argv = process.argv.slice(2), root = ROOT) {
  const [command, ...args] = argv;
  const opts = {};
  while (args.length) {
    const flag = args.shift();
    if (!["--skill", "--root"].includes(flag) || !args.length)
      fail(`Unknown or incomplete option: ${flag}`);
    opts[flag.slice(2)] = args.shift();
  }
  if (opts.root) root = path.resolve(opts.root);
  const ctx = load(root),
    preview = command === "preview";
  if (
    !["build", "preview", "check-generated", "check", "package"].includes(
      command,
    )
  )
    fail(
      "Usage: build-skills.mjs build|preview|check-generated|check|package [--skill name]",
    );
  if (opts.skill && !preview)
    fail("--skill is supported only for preview builds");
  if (command === "package") releaseGate(ctx);
  const result = buildCatalog(ctx, { preview, skill: opts.skill });
  if (command === "package") {
    if (!result.eligible.length)
      fail("Publication blocked: empty stable catalog");
    replaceOwned(path.join(root, "skills"), result.out, { check: true });
    replaceOwned(
      path.join(root, "dist/release"),
      artifacts(ctx, result.eligible),
    );
  } else if (command === "check") {
    for (const name of result.eligible)
      validateSkill(tree(path.join(root, "skills", name)), name);
    replaceOwned(path.join(root, "skills"), result.out, { check: true });
  } else {
    const dest = path.join(root, preview ? "dist/preview/skills" : "skills");
    replaceOwned(dest, result.out, { check: command === "check-generated" });
    if (preview) {
      replaceOwned(
        path.join(root, "dist/preview/distribution"),
        artifacts(ctx, result.eligible, { preview: true }),
      );
    }
  }
  if (command === "build") {
    const dest = path.join(root, "docs/installation.generated.md");
    fs.writeFileSync(dest, result.documentation);
  } else if (
    command === "check-generated" &&
    fs.readFileSync(
      path.join(root, "docs/installation.generated.md"),
      "utf8",
    ) !== result.documentation
  )
    fail("Generated installation documentation is stale");
  console.log(
    json({
      command,
      stack_version: ctx.version,
      status: ctx.status,
      skills: result.eligible,
      blocked: result.candidates.filter((n) => !result.eligible.includes(n)),
    }),
  );
}
if (
  process.argv[1] &&
  path.resolve(process.argv[1]) === fileURLToPath(import.meta.url)
)
  try {
    main();
  } catch (error) {
    console.error(error.message);
    process.exitCode = 1;
  }
