import test from 'node:test'
import assert from 'node:assert/strict'
import { spawnSync } from 'node:child_process'
import { ROOT } from '../scripts/build-skills.mjs'

test('documentation deployment preserves destination ownership and public output boundaries', () => {
  const result = spawnSync('python3', ['tests/test_docs_deploy.py'], {
    cwd: ROOT,
    encoding: 'utf8',
    env: { ...process.env, PYTHONDONTWRITEBYTECODE: '1' },
  })
  assert.equal(result.status, 0, result.stdout + result.stderr)
})
