import fs from "node:fs";
import { spawnSync } from "node:child_process";
import { ROOT, load, releaseGate } from "./build-skills.mjs";
try {
  const ctx = load();
  releaseGate(ctx);
  const tag = process.env.RELEASE_TAG;
  if (tag !== `v${ctx.version}`)
    throw new Error("Tag must match the stable stack version");
  const git = (...args) => {
    const r = spawnSync("git", args, { cwd: ROOT, encoding: "utf8" });
    if (r.status !== 0) throw new Error("Git release verification failed");
    return r.stdout.trim();
  };
  if (
    git("rev-parse", `refs/tags/${tag}^{commit}`) !== git("rev-parse", "HEAD")
  )
    throw new Error("Tag does not identify the checked-out release commit");
  if (git("status", "--porcelain"))
    throw new Error("Release checkout must be clean");
  const versions = fs.readFileSync(`${ROOT}/VERSIONS.md`, "utf8");
  if (!/\| Release date \| \d{4}-\d{2}-\d{2} \|/.test(versions))
    throw new Error("A stable release requires an actual release date");
  console.log(`Verified ${tag}`);
} catch (error) {
  console.error(error.message);
  process.exitCode = 1;
}
