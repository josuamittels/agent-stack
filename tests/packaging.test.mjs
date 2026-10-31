import test from "node:test";
import assert from "node:assert/strict";
import fs from "node:fs";
import os from "node:os";
import path from "node:path";
import { spawnSync } from "node:child_process";
import { parse, stringify } from "yaml";
import { unzipSync } from "fflate";
import {
  ROOT,
  load,
  closure,
  blockers,
  buildSkill,
  buildCatalog,
  validateSkill,
  releaseGate,
  artifacts,
  main,
  inside,
} from "../scripts/build-skills.mjs";

const ctx = load();
function temp(t) {
  const root = fs.mkdtempSync(path.join(os.tmpdir(), "agent-stack-test-"));
  t.after(() => fs.rmSync(root, { recursive: true, force: true }));
  return root;
}
function writePackage(dir, map) {
  for (const [name, v] of map) {
    const p = path.join(dir, name);
    fs.mkdirSync(path.dirname(p), { recursive: true });
    fs.writeFileSync(p, v.bytes, { mode: v.mode });
  }
}
function run(command, args, cwd, env = {}) {
  const result = spawnSync(command, args, {
    cwd,
    encoding: "utf8",
    env: { ...process.env, PYTHONDONTWRITEBYTECODE: "1", ...env },
  });
  assert.equal(result.status, 0, result.stderr + "\n" + result.stdout);
  return result.stdout;
}
function fixture(t) {
  const root = temp(t);
  fs.cpSync(path.join(ROOT, "src"), path.join(root, "src"), {
    recursive: true,
    filter: (p) =>
      !/(?:\/\.env$|__pycache__|\.DS_Store|\/\.local(?:\/|$))/.test(p),
  });
  for (const name of ["VERSIONS.md", "LICENSE"])
    fs.copyFileSync(path.join(ROOT, name), path.join(root, name));
  fs.mkdirSync(path.join(root, "docs"));
  return root;
}
function stableFixture(t) {
  const root = fixture(t);
  const catalog = parse(
    fs.readFileSync(path.join(root, "src/catalog.yaml"), "utf8"),
  );
  for (const name of Object.keys(catalog.skills)) {
    if (name !== "translate") catalog.skills[name].visibility = "internal";
  }
  fs.writeFileSync(path.join(root, "src/catalog.yaml"), stringify(catalog));
  for (const id of closure(load(root), "translate")) {
    const p = path.join(root, "src/skills", id, "SKILL.md.tmpl");
    fs.writeFileSync(
      p,
      fs
        .readFileSync(p, "utf8")
        .replace('status: "experimental"', 'status: "stable"'),
    );
  }
  for (const p of ["english", "german", "french", "dutch"]) {
    const f = path.join(root, "src/guidelines/languages", p + ".md");
    fs.writeFileSync(
      f,
      fs
        .readFileSync(f, "utf8")
        .replace('status: "experimental"', 'status: "stable"'),
    );
  }
  return root;
}

test("translate is self-contained, with a finite cyclic dependency closure", (t) => {
  const root = temp(t),
    packageDir = path.join(root, ".agents/skills/translate");
  const out = buildSkill(ctx, "translate", { preview: true });
  writePackage(packageDir, out);
  assert.deepEqual(closure(ctx, "translate"), [
    "ask-user-question",
    "natural-writing",
    "think-harder",
    "translate",
  ]);
  validateSkill(out, "translate", { preview: true });
  assert.deepEqual(
    [...out.keys()].filter((f) => path.basename(f) === "SKILL.md"),
    ["SKILL.md"],
  );
  assert.equal(fs.existsSync(path.join(root, "src")), false);
  for (const language of ["english", "german", "french", "dutch"])
    assert.ok(
      fs.existsSync(
        path.join(
          packageDir,
          "references/_stack/guidelines/languages",
          language + ".md",
        ),
      ),
    );
  writePackage(
    path.join(root, ".agents/skills/natural-writing"),
    buildSkill(ctx, "natural-writing", { preview: true }),
  );
  assert.ok(
    fs.existsSync(path.join(root, ".agents/skills/natural-writing/SKILL.md")),
  );
  assert.ok(
    !out
      .get("references/_stack/skills/translate/instructions.md")
      .bytes.toString()
      .includes("../natural-writing/SKILL.md"),
  );
});
test("packaged color helpers run from an unrelated working directory", (t) => {
  const root = temp(t);
  for (const name of ["convert-colour", "check-colour-contrast"])
    writePackage(
      path.join(root, name),
      buildSkill(ctx, name, { preview: true }),
    );
  const conversion = run(
    "node",
    [
      path.join(
        root,
        "convert-colour/references/_stack/skills/convert-colour/scripts/convert-colour.mjs",
      ),
      "hex",
      "#ff0000",
      "rgb",
    ],
    os.tmpdir(),
  );
  assert.match(conversion, /255/);
  const contrast = run(
    "node",
    [
      path.join(
        root,
        "check-colour-contrast/references/_stack/skills/check-colour-contrast/scripts/check-colour-contrast.mjs",
      ),
      "hex",
      "#000000",
      "hex",
      "#ffffff",
    ],
    os.tmpdir(),
  );
  assert.match(contrast, /21/);
});
test("Research bundles checker packages, imports, templates, CSV and attribution", (t) => {
  const root = temp(t),
    out = buildSkill(ctx, "research", { preview: true });
  writePackage(root, out);
  const base = path.join(root, "references/_stack");
  for (const file of [
    "evals/research/checks.py",
    "evals/research/rubric.json",
    "skills/research-literature/references/journals.csv",
    "skills/research/references/csl/README.md",
    "skills/research/references/csl/apa.csl",
  ])
    assert.ok(fs.existsSync(path.join(base, file)), file);
  run(
    "python3",
    [
      path.join(base, "skills/spawn-evals/scripts/runner.py"),
      "--validate-package",
      "--skill",
      "research",
    ],
    os.tmpdir(),
  );
  run(
    "python3",
    [path.join(base, "skills/research/scripts/research.py"), "--help"],
    os.tmpdir(),
  );
  run(
    "python3",
    [path.join(base, "skills/research/scripts/complete.py"), "--help"],
    os.tmpdir(),
  );
  run(
    "python3",
    [
      path.join(base, "skills/research-literature/scripts/verify_sources.py"),
      "--help",
    ],
    os.tmpdir(),
  );
});
test("packages exclude secrets, development files and nested discovery entries", () => {
  for (const name of ["research", "create-skill", "ship"]) {
    const out = buildSkill(ctx, name, { preview: true });
    for (const file of out.keys())
      assert.doesNotMatch(
        file,
        /(?:\/\.env$|\.pyc$|__pycache__|\/test[^/]*\.py$|runs\.jsonl)/,
      );
    assert.equal(
      [...out.keys()].filter((f) => path.basename(f) === "SKILL.md").length,
      1,
    );
  }
});
test("stable gates include transitive dependencies and do not change lifecycle status", () => {
  assert.throws(() => releaseGate(ctx), /Publication blocked/);
  assert.throws(() => buildSkill(ctx, "translate"), /unstable dependency/);
  assert.deepEqual(buildCatalog(ctx).eligible, []);
  assert.ok(
    blockers(ctx, "check-colour-contrast").some((x) =>
      x.includes("think-harder"),
    ),
  );
  assert.equal(ctx.status, "draft");
});
test("unknown dependencies, missing assets, escaping paths and unsafe examples fail", (t) => {
  const root = fixture(t),
    file = path.join(root, "src/catalog.yaml");
  const original = fs.readFileSync(file, "utf8");
  let c = parse(original);
  c.skills.translate.required.push("missing");
  fs.writeFileSync(file, stringify(c));
  assert.throws(() => load(root), /unknown dependency/);
  c = parse(original);
  c.skills.translate.resources.push("guidelines/missing.md");
  fs.writeFileSync(file, stringify(c));
  assert.throws(() => load(root), /Missing required/);
  c = parse(original);
  c.skills.translate.files.push("skills/translate/../../../../outside");
  fs.writeFileSync(file, stringify(c));
  assert.throws(() => load(root), /escapes/);
  fs.writeFileSync(file, original);
  const example = path.join(
    root,
    "src/skills/research-literature/references/.env.example",
  );
  fs.writeFileSync(example, "OPENALEX_API_KEY=should-never-be-shipped\n");
  assert.throws(() => load(root), /Credential example/);
  assert.throws(() => inside(root, "../escape"), /escapes/);
});
test("undeclared Markdown and Python runtime dependencies fail", (t) => {
  const root = fixture(t),
    file = path.join(root, "src/catalog.yaml"),
    c = parse(fs.readFileSync(file, "utf8"));
  c.skills.translate.required = c.skills.translate.required.filter(
    (n) => n !== "natural-writing",
  );
  fs.writeFileSync(file, stringify(c));
  assert.throws(
    () => buildSkill(load(root), "translate", { preview: true }),
    /undeclared or missing/,
  );
  const original = parse(
    fs.readFileSync(path.join(ROOT, "src/catalog.yaml"), "utf8"),
  );
  original.skills.research.files = original.skills.research.files.filter(
    (f) => !f.endsWith("/research_common.py"),
  );
  fs.writeFileSync(file, stringify(original));
  assert.throws(
    () => buildSkill(load(root), "research", { preview: true }),
    /undeclared Python runtime import research_common/,
  );
});
test("stable build is deterministic; dependencies invalidate consumers; stale owned files disappear", (t) => {
  const root = stableFixture(t);
  main(["build"], root);
  main(["check-generated"], root);
  main(["check"], root);
  const before = fs.readFileSync(
    path.join(root, "skills/translate/package-manifest.json"),
    "utf8",
  );
  const stale = path.join(root, "skills/translate/stale-generated-file");
  fs.writeFileSync(stale, "stale");
  assert.throws(() => main(["check-generated"], root), /stale/);
  main(["build"], root);
  assert.equal(fs.existsSync(stale), false);
  assert.equal(
    fs.readFileSync(
      path.join(root, "skills/translate/package-manifest.json"),
      "utf8",
    ),
    before,
  );
  const dep = path.join(root, "src/guidelines/languages/english.md");
  fs.appendFileSync(dep, "\nA new canonical instruction.\n");
  main(["build"], root);
  assert.notEqual(
    fs.readFileSync(
      path.join(root, "skills/translate/package-manifest.json"),
      "utf8",
    ),
    before,
  );
});
test("state and configuration stay outside packages and survive replacement", (t) => {
  const root = temp(t),
    state = path.join(root, "state"),
    config = path.join(root, "config");
  fs.mkdirSync(config);
  const keyfile = path.join(config, "research-literature.env");
  fs.writeFileSync(keyfile, "OPENALEX_API_KEY=local-test-value\n");
  const out = buildSkill(ctx, "research", { preview: true }),
    install = path.join(root, "installed");
  writePackage(install, out);
  const base = path.join(install, "references/_stack");
  const script = `import sys\nsys.path.insert(0,${JSON.stringify(path.join(base, "skills/spawn-evals/scripts"))})\nimport runner\nrunner.record_history(None,{'skill':'research','status':'not_passed_unverified','invocation_id':'test'},__import__('pathlib').Path(${JSON.stringify(path.join(base, "evals/research"))}))`;
  run("python3", ["-c", script], os.tmpdir(), {
    AGENT_STACK_STATE_DIR: state,
    AGENT_STACK_CONFIG_DIR: config,
  });
  assert.ok(fs.existsSync(path.join(state, "evals/runs.jsonl")));
  assert.equal(fs.existsSync(path.join(base, "evals/.local")), false);
  fs.rmSync(install, { recursive: true });
  writePackage(install, out);
  assert.match(fs.readFileSync(keyfile, "utf8"), /local-test-value/);
  assert.ok(fs.existsSync(path.join(state, "evals/runs.jsonl")));
  const paths = JSON.parse(
    run(
      "python3",
      [
        path.join(base, "runtime/paths.py"),
        "--config-dir",
        config,
        "--state-dir",
        state,
      ],
      os.tmpdir(),
    ),
  );
  assert.equal(paths.openalex_env, keyfile);
});
test("archives and both native plugin manifests use the same isolated packages", (t) => {
  const out = artifacts(ctx, ["translate"], { preview: true });
  const root = temp(t);
  writePackage(root, out);
  const openai = JSON.parse(
    out.get("plugins/agent-stack-translate/plugin.json").bytes,
  );
  const claude = JSON.parse(
    out.get("plugins/agent-stack-translate/.claude-plugin/plugin.json").bytes,
  );
  assert.equal(openai.name, claude.name);
  assert.equal(openai.version, ctx.version);
  assert.equal(
    openai.$schema,
    "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json",
  );
  const market = JSON.parse(out.get(".agents/plugins/marketplace.json").bytes);
  for (const entry of market.plugins) {
    assert.equal(entry.category, "Productivity");
    assert.ok(fs.existsSync(path.join(root, entry.source.path, "plugin.json")));
  }
  const archive = unzipSync(
    out.get(`archives/translate-${ctx.version}.zip`).bytes,
  );
  assert.ok(archive["SKILL.md"]);
  assert.ok(
    archive["references/_stack/skills/natural-writing/instructions.md"],
  );
  assert.deepEqual(
    out.get(`archives/translate-${ctx.version}.zip`).bytes,
    artifacts(ctx, ["translate"], { preview: true }).get(
      `archives/translate-${ctx.version}.zip`,
    ).bytes,
  );
});
test("public router excludes internal capabilities and checks installed availability", () => {
  const out = buildSkill(ctx, "skill-issue", { preview: true });
  const text = out
    .get("references/_stack/skills/skill-issue/instructions.md")
    .bytes.toString();
  assert.doesNotMatch(
    text,
    /\*\*(?:release-agent-stack|update-map|update-router)\*\*/,
  );
  assert.match(text, /not proof of installation/);
});
test("publication succeeds only for a nonempty stable release and rejects tampered packages", (t) => {
  const root = stableFixture(t);
  let v = fs.readFileSync(path.join(root, "VERSIONS.md"), "utf8");
  v = v
    .replace("| Version | `" + ctx.version + "`", "| Version | `1.0.0`")
    .replace("| Status | `draft`", "| Status | `stable`");
  fs.writeFileSync(path.join(root, "VERSIONS.md"), v);
  main(["build"], root);
  main(["package"], root);
  assert.ok(fs.existsSync(path.join(root, "dist/release/SHA256SUMS")));
  const out = buildSkill(load(root), "translate");
  out.get("SKILL.md").bytes = Buffer.from("tampered");
  assert.throws(() => validateSkill(out, "translate"), /digest mismatch/);
});

test("full preview catalog contains only public candidates and validates every package", () => {
  const result = buildCatalog(ctx, { preview: true });
  assert.equal(result.eligible.length, 22);
  for (const name of ["release-agent-stack", "update-map", "update-router"])
    assert.ok(!result.eligible.includes(name));
  assert.equal(
    [...result.out.keys()].filter((f) => f.endsWith("/SKILL.md")).length,
    22,
  );
});
test("canonical sources and authoring scaffold cannot be mistaken for installable entries", () => {
  function check(dir) {
    for (const e of fs.readdirSync(dir, { withFileTypes: true })) {
      const p = path.join(dir, e.name);
      if (e.isDirectory() && !["__pycache__", ".local"].includes(e.name))
        check(p);
      else if (e.isFile()) assert.notEqual(e.name, "SKILL.md", p);
    }
  }
  check(path.join(ROOT, "src"));
});
test("removed declared resources disappear and unowned output is protected", (t) => {
  const root = stableFixture(t),
    catalogFile = path.join(root, "src/catalog.yaml"),
    catalog = parse(fs.readFileSync(catalogFile, "utf8"));
  const relative = "skills/translate/extra.txt";
  catalog.skills.translate.files.push(relative);
  fs.writeFileSync(path.join(root, "src", relative), "resource");
  fs.writeFileSync(catalogFile, stringify(catalog));
  main(["build"], root);
  assert.ok(
    fs.existsSync(
      path.join(root, "skills/translate/references/_stack", relative),
    ),
  );
  catalog.skills.translate.files = catalog.skills.translate.files.filter(
    (p) => p !== relative,
  );
  fs.writeFileSync(catalogFile, stringify(catalog));
  fs.unlinkSync(path.join(root, "src", relative));
  main(["build"], root);
  assert.equal(
    fs.existsSync(
      path.join(root, "skills/translate/references/_stack", relative),
    ),
    false,
  );
  fs.rmSync(path.join(root, "skills"), { recursive: true });
  fs.mkdirSync(path.join(root, "skills"));
  fs.writeFileSync(path.join(root, "skills/user-file"), "keep");
  assert.throws(() => main(["build"], root), /unowned directory/);
  assert.equal(
    fs.readFileSync(path.join(root, "skills/user-file"), "utf8"),
    "keep",
  );
});
test("symlink resources and absolute Markdown links cannot escape the package", (t) => {
  const root = fixture(t),
    entry = path.join(root, "src/skills/translate/SKILL.md.tmpl"),
    original = fs.readFileSync(entry, "utf8");
  fs.appendFileSync(entry, "\n[bad](/etc/passwd)\n");
  assert.throws(
    () => buildSkill(load(root), "translate", { preview: true }),
    /absolute local link/,
  );
  fs.writeFileSync(entry, original);
  const file = path.join(root, "src/guidelines/languages/english.md");
  fs.unlinkSync(file);
  fs.symlinkSync(path.join(ROOT, "src/guidelines/languages/english.md"), file);
  assert.throws(() => load(root), /Symlink/);
});

test("archive bytes are independent of the builder timezone", () => {
  const code = `import{load,artifacts}from${JSON.stringify(new URL("../scripts/build-skills.mjs", import.meta.url).href)};import{createHash}from'node:crypto';const c=load();const out=artifacts(c,['translate'],{preview:true});console.log(createHash('sha256').update(out.get('archives/translate-'+c.version+'.zip').bytes).digest('hex'));`;
  const utc = run(process.execPath, ["--input-type=module", "-e", code], ROOT, {
    TZ: "UTC",
  });
  const pacific = run(
    process.execPath,
    ["--input-type=module", "-e", code],
    ROOT,
    { TZ: "America/Los_Angeles" },
  );
  assert.equal(utc, pacific);
});
