import fs from 'node:fs';

const orbit = fs.readFileSync(new URL('../data/orbit.ts', import.meta.url), 'utf8');
const evidence = fs.readFileSync(new URL('../data/evidence.ts', import.meta.url), 'utf8');
const api = fs.readFileSync(new URL('../pages/api/orbit.ts', import.meta.url), 'utf8');
const page = fs.readFileSync(new URL('../pages/index.tsx', import.meta.url), 'utf8');
const nextConfig = fs.readFileSync(new URL('../next.config.js', import.meta.url), 'utf8');
const packageJson = JSON.parse(fs.readFileSync(new URL('../package.json', import.meta.url), 'utf8'));

const required = ['empiricalN: 0', 'Pilot Authorization', 'Propagation Integrity', 'Claims do not upgrade epistemic status'];
for (const token of required) if (!orbit.includes(token)) throw new Error(`ORBIT invariant missing: ${token}`);
if (!/state: 'blocked'/.test(orbit)) throw new Error('ORBIT must contain a blocked gate');
if (!/state: 'verified'/.test(orbit)) throw new Error('ORBIT must contain a verified gate');
if (!evidence.includes("EVIDENCE_SCHEMA = 'orbit.evidence.v2'")) throw new Error('ORBIT evidence schema missing');
if (!evidence.includes("headSemantics: 'source-head'")) throw new Error('ORBIT source-head semantics missing');
if (!evidence.includes('v.head') || !evidence.includes('/^[0-9a-f]{40}$/')) throw new Error('ORBIT must validate full commit SHAs');
if (!evidence.includes('governance?.failClosed === true')) throw new Error('ORBIT evidence must be fail-closed');

if (packageJson.engines?.node !== '>=24.0.0') throw new Error('ORBIT requires Node >=24.0.0');
if (packageJson.dependencies?.next !== '14.2.35') throw new Error('ORBIT must remain on patched Next.js 14.2.35');
if (!api.includes('GITHUB_TIMEOUT_MS = 5000')) throw new Error('ORBIT live GitHub calls must have a timeout');
if (!api.includes("req.method !== 'GET'")) throw new Error('ORBIT API must be GET-only');
if (!api.includes("Cache-Control', 'no-store")) throw new Error('ORBIT API must disable caching');
if (!api.includes('res.status(503)')) throw new Error('ORBIT live evidence failures must return HTTP 503');
if (!api.includes('readinessScoreFor(gates)')) throw new Error('ORBIT API readiness must reflect reconciled gates');
if (!api.includes('README contradiction')) throw new Error('ORBIT must fail closed on documentation contradiction');
if (!page.includes('scoreFor(snapshot)')) throw new Error('ORBIT UI must support snapshot-derived readiness');
if (!page.includes("cache: 'no-store'")) throw new Error('ORBIT live refresh must bypass browser cache');

for (const header of ['X-Content-Type-Options', 'X-Frame-Options', 'Referrer-Policy', 'Permissions-Policy', 'Content-Security-Policy']) {
  if (!nextConfig.includes(header)) throw new Error(`ORBIT security header missing: ${header}`);
}

console.log('ORBIT invariants: PASS');
