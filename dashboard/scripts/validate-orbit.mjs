import fs from 'node:fs';

const orbit = fs.readFileSync(new URL('../data/orbit.ts', import.meta.url), 'utf8');
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
console.log('ORBIT invariants: PASS');
