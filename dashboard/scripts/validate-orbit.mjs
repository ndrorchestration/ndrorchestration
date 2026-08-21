import fs from 'node:fs';

const orbit = fs.readFileSync(new URL('../data/orbit.ts', import.meta.url), 'utf8');
const api = fs.readFileSync(new URL('../pages/api/orbit.ts', import.meta.url), 'utf8');
const page = fs.readFileSync(new URL('../pages/index.tsx', import.meta.url), 'utf8');
const packageJson = JSON.parse(fs.readFileSync(new URL('../package.json', import.meta.url), 'utf8'));

const required = [
  'empiricalN: 0',
  'Pilot Authorization',
  'Propagation Integrity',
  'Claims do not upgrade epistemic status',
];
for (const token of required) {
  if (!orbit.includes(token)) throw new Error(`ORBIT invariant missing: ${token}`);
}
if (!/state: 'blocked'/.test(orbit)) throw new Error('ORBIT must contain a blocked gate');
if (!/state: 'verified'/.test(orbit)) throw new Error('ORBIT must contain a verified gate');

if (packageJson.engines?.node !== '>=24.0.0') throw new Error('ORBIT requires Node >=24.0.0');
if (packageJson.dependencies?.next !== '14.2.35') throw new Error('ORBIT must remain on patched Next.js 14.2.35');
if (!api.includes('GITHUB_TIMEOUT_MS = 5000')) throw new Error('ORBIT live GitHub calls must have a timeout');
if (!api.includes('res.status(503)')) throw new Error('ORBIT live evidence failures must return HTTP 503');
if (!api.includes('readinessScoreFor(gates)')) throw new Error('ORBIT API readiness must reflect reconciled gates');
if (!page.includes('scoreFor(snapshot)')) throw new Error('ORBIT UI must support snapshot-derived readiness');
if (!page.includes('cache: \'no-store\'')) throw new Error('ORBIT live refresh must bypass browser cache');

console.log('ORBIT invariants: PASS');
