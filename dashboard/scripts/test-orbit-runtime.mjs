import fs from 'node:fs';
import vm from 'node:vm';
import { stripTypeScriptTypes } from 'node:module';
import assert from 'node:assert/strict';
import { createHash } from 'node:crypto';

const root = new URL('../', import.meta.url);
const read = path => fs.readFileSync(new URL(path, root), 'utf8');
function load(path, expression, extras = {}) {
  // Type erasure only; transport and Next response boundaries are fixtures.
  const source = read(path).replace(/^import .*\n/gm, '');
  const code = stripTypeScriptTypes(source).replace(/export default /g, '').replace(/export /g, '');
  return vm.runInNewContext(code + '\n;' + expression, {
    Buffer, AbortController, setTimeout, clearTimeout, createHash,
    process: { env: {} }, ...extras,
  });
}
const snapshot = load('data/orbit.ts', 'orbitSnapshot');
const fullHead = 'c55476746126ca29f3963887c1c81ad6110c5738';
const text = 'FAIL-CLOSED\nNOT AUTHORIZED\nempirical N = 0';
const bytes = Buffer.from(text);
const blob = createHash('sha1').update(Buffer.from('blob ' + bytes.length + '\0')).update(bytes).digest('hex');
async function invoke({ head = fullHead, method = 'GET', fail = false, repository = 'ndrorchestration/DGAF-Framework', encoding = 'base64' } = {}) {
  const calls = [];
  const handler = load('pages/api/orbit.ts', 'handler', {
    orbitSnapshot: snapshot,
    orbitConfig: { repository, branch: 'main', githubTimeoutMs: 5000 },
    EVIDENCE_SCHEMA: 'orbit.evidence.v3',
    fetch: async url => {
      calls.push(url);
      if (fail) throw new Error('network unavailable');
      return { ok: true, json: async () => url.includes('/branches/')
        ? { commit: { sha: head } }
        : { content: bytes.toString('base64'), sha: blob, encoding } };
    },
  });
  const out = { headers: {} };
  const response = {
    setHeader: (key, value) => { out.headers[key] = value; },
    status: value => { out.status = value; return response; },
    json: value => { out.payload = value; return response; },
  };
  await handler({ method }, response);
  return { ...out, calls };
}
let passed = 0;
const failures = [];
async function check(name, run) {
  try { await run(); passed++; console.log('PASS ' + name); }
  catch (error) { failures.push(name); console.error('FAIL ' + name + ': ' + error.message); }
}
await check('matching full historical identity admits current projection', async () => {
  const result = await invoke(); assert.equal(result.status, 200); assert.equal(result.payload.live.currentProjection, true);
});
await check('different full commit sharing captured prefix is withheld', async () => {
  const result = await invoke({ head: 'c5547674' + 'f'.repeat(32) }); assert.equal(result.payload.live.currentProjection, false);
});
await check('README is requested at the observed immutable source head', async () => {
  const result = await invoke(); assert.ok(result.calls[1].endsWith('?ref=' + fullHead));
});
await check('foreign repository cannot admit DGAF historical projection', async () => {
  const result = await invoke({ repository: 'another/repository' }); assert.equal(result.payload.live.currentProjection, false);
});
await check('unrelated source drift withholds claims and exposes authority blocker', async () => {
  const result = await invoke({ head: 'd'.repeat(40) }); assert.equal(result.payload.live.currentProjection, false);
  assert.equal(result.payload.snapshot.claims.length, 0); assert.equal(result.payload.snapshot.gates[0].id, 'AUTHORITY');
});
await check('unavailable source responds 503 with no current gates or claims', async () => {
  const result = await invoke({ fail: true }); assert.equal(result.status, 503);
  assert.equal(result.payload.live.currentProjection, false); assert.equal(result.payload.snapshot.gates.length, 0); assert.equal(result.payload.snapshot.claims.length, 0);
});
await check('non-GET is rejected without fetching evidence', async () => {
  const result = await invoke({ method: 'POST' }); assert.equal(result.status, 405); assert.equal(result.calls.length, 0);
});
await check('malformed README transport encoding fails closed', async () => {
  const result = await invoke({ encoding: 'utf-8' }); assert.equal(result.status, 503);
});
const guard = load('data/evidence.ts', 'isEvidenceSnapshot');
const artifact = {
  schema: 'orbit.evidence.v2', generatedAt: '2026-10-14T11:07:11Z', repository: 'ndrorchestration/ndrorchestration',
  head: fullHead, headSemantics: 'source-head', githubEventSha: fullHead, pullRequestHeadSha: '',
  readme: { empiricalN0: false, pilotUnauthorized: false }, propagation: { '340PercentClaimOccurrences': 2 }, governance: { failClosed: true },
};
await check('valid push snapshot accepted', () => assert.equal(guard(artifact), true));
await check('valid PR snapshot accepts distinct synthetic event head', () => assert.equal(guard({ ...artifact, githubEventSha: 'd'.repeat(40), pullRequestHeadSha: fullHead }), true));
for (const [name, change] of [
  ['invalid timestamp', { generatedAt: 'not-a-time' }],
  ['impossible calendar timestamp', { generatedAt: '2026-02-31T00:00:00Z' }],
  ['invalid event identity', { githubEventSha: 'not-a-sha' }],
  ['invalid PR identity', { pullRequestHeadSha: 'not-a-sha' }],
  ['PR/source identity mismatch', { pullRequestHeadSha: 'd'.repeat(40) }],
  ['push/source identity mismatch', { githubEventSha: 'd'.repeat(40) }],
]) await check('snapshot rejects ' + name, () => assert.equal(guard({ ...artifact, ...change }), false));
// This pure selector is the same production function used by the page.
if (fs.existsSync(new URL('data/observer-view.ts', root))) {
  const select = load('data/observer-view.ts', 'visibleObserverGates');
  const validate = load('data/observer-view.ts', 'isObserverSnapshot');
  await check('loading and failed refresh hide prior historical/admitted gates', () => assert.equal(select(snapshot.gates, false).length, 0));
  await check('source drift shows only explicit blocked authority reconciliation', () => {
    const gates = select([...snapshot.gates, { id: 'AUTHORITY', state: 'blocked' }], false);
    assert.equal(gates.length, 1); assert.equal(gates[0].id, 'AUTHORITY');
  });
  await check('admitted current projection displays its gates', () => assert.equal(select(snapshot.gates, true).length, snapshot.gates.length));
  await check('older refresh cannot overwrite the current request', () => {
    const owner = load('data/observer-view.ts', 'createObserverRefreshOwner')();
    const older = owner.begin(); const newer = owner.begin();
    assert.equal(owner.owns(older), false); assert.equal(owner.owns(newer), true);
  });
  await check('effect cleanup invalidates every outstanding refresh', () => {
    const owner = load('data/observer-view.ts', 'createObserverRefreshOwner')();
    const pending = owner.begin(); owner.invalidate(); assert.equal(owner.owns(pending), false);
  });
  await check('valid observer snapshot accepted', () => assert.equal(validate(snapshot), true));
  await check('malformed gate collection rejected before rendering', () => assert.equal(validate({ ...snapshot, gates: 'bad' }), false));
  await check('unknown gate state rejected before rendering', () => assert.equal(validate({ ...snapshot, gates: [{ ...snapshot.gates[0], state: 'made-up' }] }), false));
} else { failures.push('missing observer-view selector'); console.error('FAIL missing observer-view selector'); }
console.log('ORBIT runtime checks: ' + passed + ' passed, ' + failures.length + ' failed');
if (failures.length) process.exitCode = 1;
