import fs from 'node:fs';

const read = path => fs.readFileSync(new URL(path, import.meta.url), 'utf8');
const orbit = read('../data/orbit.ts');
const evidence = read('../data/evidence.ts');
const config = read('../data/config.ts');
const api = read('../pages/api/orbit.ts');
const health = read('../pages/api/health.ts');
const schema = read('../pages/api/schema.ts');
const page = read('../pages/index.tsx');
const nextConfig = read('../next.config.js');
const packageJson = JSON.parse(read('../package.json'));

const required = ['empiricalN: 0', 'Pilot Authorization', 'Propagation Integrity', 'Claims do not upgrade epistemic status'];
for (const token of required) if (!orbit.includes(token)) throw new Error(`ORBIT invariant missing: ${token}`);
if (!/state: 'blocked'/.test(orbit)) throw new Error('ORBIT must contain a blocked gate');
if (!/state: 'verified'/.test(orbit)) throw new Error('ORBIT must contain a verified gate');
if (!evidence.includes("EVIDENCE_SCHEMA = 'orbit.evidence.v2'")) throw new Error('ORBIT evidence schema missing');
if (!evidence.includes("headSemantics: 'source-head'")) throw new Error('ORBIT source-head semantics missing');
if (!evidence.includes('v.head') || !evidence.includes('/^[0-9a-f]{40}$/')) throw new Error('ORBIT must validate full commit SHAs');
if (!evidence.includes('governance?.failClosed === true')) throw new Error('ORBIT evidence must be fail-closed');
if (!config.includes('ORBIT_REPOSITORY') || !config.includes('ORBIT_BRANCH')) throw new Error('ORBIT runtime configuration is not centralized');
if (!config.includes('githubTimeoutMs: 5000')) throw new Error('ORBIT GitHub timeout configuration missing');

if (packageJson.engines?.node !== '>=24.0.0') throw new Error('ORBIT requires Node >=24.0.0');
if (packageJson.dependencies?.next !== '15.5.21') throw new Error('ORBIT must remain on the reviewed Next.js 15.5.21 security baseline');
if (!api.includes('orbitConfig.githubTimeoutMs')) throw new Error('ORBIT live GitHub calls must use configured timeout');
if (!api.includes("req.method !== 'GET'")) throw new Error('ORBIT API must be GET-only');
if (!api.includes("Cache-Control', 'no-store")) throw new Error('ORBIT API must disable caching');
if (!api.includes('res.status(503)')) throw new Error('ORBIT live evidence failures must return HTTP 503');
if (!api.includes('readinessScoreFor(gates)')) throw new Error('ORBIT API readiness must reflect reconciled gates');
if (!api.includes('README contradiction')) throw new Error('ORBIT must fail closed on documentation contradiction');
if (!api.includes('orbitConfig.repository') || !api.includes('orbitConfig.branch')) throw new Error('ORBIT API must honor runtime repository configuration');
if (!/function scoreFor\(snapshot/.test(page)) throw new Error('ORBIT UI must support snapshot-derived readiness');
if (!page.includes("cache: 'no-store'")) throw new Error('ORBIT live refresh must bypass browser cache');
if (!health.includes("status: 'ok'") || !health.includes("req.method !== 'GET'")) throw new Error('ORBIT health endpoint incomplete');
if (!schema.includes('EVIDENCE_SCHEMA') || !schema.includes("'source-head semantics'")) throw new Error('ORBIT schema endpoint incomplete');

for (const header of ['X-Content-Type-Options', 'X-Frame-Options', 'Referrer-Policy', 'Permissions-Policy', 'Content-Security-Policy']) {
  if (!nextConfig.includes(header)) throw new Error(`ORBIT security header missing: ${header}`);
}

console.log('ORBIT invariants: PASS');
