import type { Gate } from './orbit';

type Snapshot = typeof import('./orbit').orbitSnapshot;

// A response may mutate the view only while it owns the latest refresh.
export function createObserverRefreshOwner() {
  let generation = 0;
  return {
    begin: () => ++generation,
    owns: (request: number) => request === generation,
    invalidate: () => { generation++; },
  };
}

// Until admission succeeds, only explicit reconciliation blockers may be shown.
export function visibleObserverGates(gates: Gate[], currentProjection: boolean): Gate[] {
  return currentProjection ? gates : gates.filter(gate => gate.id === 'AUTHORITY' && gate.state === 'blocked');
}

export function isObserverSnapshot(value: unknown): value is Snapshot {
  if (!value || typeof value !== 'object') return false;
  const snapshot = value as Record<string, unknown>;
  const states = new Set(['verified', 'ready', 'blocked', 'not-established', 'warning']);
  const stringKeys = ['project', 'projectionKind', 'epistemicState', 'capturedRepository', 'capturedHead', 'historicalEvidence', 'capturedDeployment'];
  return stringKeys.every(key => typeof snapshot[key] === 'string') &&
    Number.isInteger(snapshot.empiricalN) && Number(snapshot.empiricalN) >= 0 &&
    Array.isArray(snapshot.gates) && snapshot.gates.every(gate =>
      gate && typeof gate === 'object' && ['id', 'name', 'evidence', 'detail'].every(key => typeof gate[key] === 'string') && states.has(gate.state)) &&
    Array.isArray(snapshot.claims) && snapshot.claims.every(claim =>
      claim && typeof claim === 'object' && typeof claim.claim === 'string' && ['warning', 'blocked'].includes(claim.status) &&
      ['occurrences', 'qualified', 'bare'].every(key => Number.isInteger(claim[key]) && claim[key] >= 0));
}
