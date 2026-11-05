import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import {spawnSync} from 'node:child_process';
import {ROOT, load, buildSkill, validateSkill} from '../scripts/build-skills.mjs';

test('career executable and checker regressions', () => {
  const result = spawnSync('python3', ['tests/test_career_helpers.py'], {cwd: ROOT, encoding: 'utf8', env: {...process.env, PYTHONDONTWRITEBYTECODE:'1'}});
  assert.equal(result.status, 0, result.stdout + result.stderr);
});

test('career packages share one voice, bundle helpers and exclude private dependencies', () => {
  const ctx = load();
  for (const name of ['answer-interview', 'draft-cover-letter', 'create-cv', 'setup-career-stack', 'compose-career-profile']) {
    const out = buildSkill(ctx, name, {preview:true});
    validateSkill(out, name, {preview:true});
    assert.ok(out.has('references/_stack/skills/compose-career-profile/scripts/career_workspace.py'));
    if (name !== 'compose-career-profile' && name !== 'create-cv') {
      assert.ok(out.has('references/_stack/skills/compose-voice-profile/references/professional-voice-profile.md'));
      assert.ok(!out.has('references/_stack/skills/answer-interview/references/professional-voice-profile.md'));
      assert.ok(!out.has('references/_stack/skills/draft-cover-letter/references/professional-voice-profile.md'));
    }
  }
});

test('build rejects reintroduced private career dependencies', t => {
  const root = fs.mkdtempSync(path.join(os.tmpdir(), 'career-build-'));
  t.after(()=>fs.rmSync(root,{recursive:true,force:true}));
  fs.cpSync(path.join(ROOT,'src'),path.join(root,'src'),{recursive:true});
  for (const name of ['VERSIONS.md','LICENSE']) fs.copyFileSync(path.join(ROOT,name),path.join(root,name));
  fs.appendFileSync(path.join(root,'src/skills/answer-interview/SKILL.md.tmpl'),'\nRead 01_Personal_Context/MASTER_PROFILE.md.\n');
  assert.throws(()=>load(root), /private or legacy career dependency/);
});

test('packaged career helpers execute outside the repository', t => {
  const root = fs.mkdtempSync(path.join(os.tmpdir(), 'career-isolated-'));
  t.after(()=>fs.rmSync(root,{recursive:true,force:true}));
  const packageRoot=path.join(root,'package');
  for (const [name,value] of buildSkill(load(),'setup-career-stack',{preview:true})) {
    const target=path.join(packageRoot,name);
    fs.mkdirSync(path.dirname(target),{recursive:true});
    fs.writeFileSync(target,value.bytes);
  }
  const base=path.join(packageRoot,'references/_stack/skills');
  const workspace=path.join(root,'workspace');
  const run=(args)=>{
    const result=spawnSync('python3',args,{cwd:os.tmpdir(),encoding:'utf8',env:{...process.env,PYTHONDONTWRITEBYTECODE:'1'}});
    assert.equal(result.status,0,result.stderr+result.stdout);
    return JSON.parse(result.stdout);
  };
  const helper=path.join(base,'compose-career-profile/scripts/career_workspace.py');
  run([helper,'init','--workspace',workspace,'--agents-template',path.join(base,'setup-career-stack/templates/AGENTS.md')]);
  const posting=path.join(root,'posting.md');fs.writeFileSync(posting,'Analyst\nReview service requests.\n');
  const app=run([helper,'application','--workspace',workspace,'--id','example-vacancy','--company','Example','--role','Analyst','--source',posting]);
  assert.equal(fs.readFileSync(app.job_md_path,'utf8'),fs.readFileSync(posting,'utf8'));
  const answer=path.join(root,'answer.txt');fs.writeFileSync(answer,'A concise answer.');
  const counted=run([path.join(base,'answer-interview/scripts/count_answer.py'),answer,'--max-words','4']);
  assert.equal(counted.counts.words,3);
});
