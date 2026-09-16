import fs from 'node:fs';

const read = path => fs.readFileSync(new URL(path, import.meta.url), 'utf8');
const orbit = read('../data/orbit.ts');
const evidence = read('../data/evidence.ts');
const config = read('../data/config.ts');
const api = read('../pages/api/orbit.ts');
const health = read('../pages/api/health.ts');
const schema = read('../pages/api/schema.ts');
const page = read('../pages/orbit.tsx');
const nextConfig = read('../next.config.js');
const packageJson = JSON.parse(read('../package.json'));

const required = ['empiricalN: 0', 'Pilot Authorization', 'Propagation Integrity', 'Claims do not upgrade epistemic status'];
for (const token of required) if (!orbit.includes(token)) throw new Error(`ORBIT invariant missing: ${token}`);
if (!/state: 'blocked'/.test(orbit)) throw new Error('ORBIT must contain a blocked gate');
if (!/state: 'verified'/.test(orbit)) throw new Error('ORBIT must contain a verified gate');
if (!orbit.includes("projectionKind: 'historical-fallback'")) throw new Error('ORBIT bundled state must be explicitly historical/fallback');
if (!orbit.includes('capturedHead:')) throw new Error('ORBIT historical source identity must be labeled as captured, not current');
if (!orbit.includes('capturedDeployment:')) throw new Error('ORBIT historical deployment identity must be labeled as captured, not current');
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
if (!api.includes('readinessStateFor(gates)')) throw new Error('ORBIT API observed state must reflect reconciled gates');
if (!api.includes("return 'BLOCKED'") || !api.includes("return 'ATTENTION'") || !api.includes("return 'CLEAR'")) {
  throw new Error('ORBIT API categorical state contract is incomplete');
}
if (!api.includes('!declaredN0 || !declaredUnauthorized || !declaredFailClosed')) {
  throw new Error('ORBIT must detect incomplete canonical governance declarations');
}
if (!api.includes("freeze.state = 'blocked'")) throw new Error('ORBIT documentation contradiction must fail closed');
if (!api.includes('orbitConfig.repository') || !api.includes('orbitConfig.branch')) throw new Error('ORBIT API must honor runtime repository configuration');
if (!api.includes("const projectionAdmissible = sourceFreshness === 'ALIGNED' && declarationsComplete")) {
  throw new Error('ORBIT must make current-projection admission explicit');
}
if (!api.includes('currentProjection: projectionAdmissible')) {
  throw new Error('ORBIT API must disclose whether the bundled projection is admissible as current');
}
if (!api.includes('Current DGAF authority moved beyond the bundled historical fallback')) {
  throw new Error('ORBIT source drift must withhold stale bundled gate state');
}
if (!api.includes("currentProjection: false")) {
  throw new Error('ORBIT live-evidence failure must explicitly deny current projection status');
}
if (!page.includes('overallState: payload.overallState')) throw new Error('ORBIT UI must render API-derived categorical observed state');
if (!page.includes("live?.overallState || 'CHECKING'")) throw new Error('ORBIT UI observed-state display missing');
if (!page.includes("cache: 'no-store'")) throw new Error('ORBIT live refresh must bypass browser cache');
if (!page.includes('live?.currentProjection === true')) {
  throw new Error('ORBIT UI must distinguish current authority from historical fallback');
}
if (!page.includes('HISTORICAL FALLBACK')) {
  throw new Error('ORBIT UI must visibly label bundled fallback state as historical');
}
if (!page.includes('CURRENT AUTHORITY STATE')) {
  throw new Error('ORBIT UI must reserve current-state labeling for admitted live authority state');
}
if (!health.includes("status: 'ok'") || !health.includes("req.method !== 'GET'")) throw new Error('ORBIT health endpoint incomplete');
if (!schema.includes('EVIDENCE_SCHEMA') || !schema.includes("'source-head semantics'")) throw new Error('ORBIT schema endpoint incomplete');

for (const header of ['X-Content-Type-Options', 'X-Frame-Options', 'Referrer-Policy', 'Permissions-Policy', 'Content-Security-Policy']) {
  if (!nextConfig.includes(header)) throw new Error(`ORBIT security header missing: ${header}`);
}

console.log('ORBIT invariants: PASS');
