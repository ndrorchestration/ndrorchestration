export type GateState = 'verified' | 'ready' | 'blocked' | 'not-established' | 'warning';

export interface Gate {
  id: string;
  name: string;
  state: GateState;
  evidence: string;
  detail: string;
}

export const orbitSnapshot = {
  project: 'DGAF / PDMAL',
  epistemicState: 'Historical freeze → corrected runner → candidate apparatus → new freeze not authorized',
  empiricalN: 0,
  head: 'c5547674',
  historicalEvidence: 'e1f077f',
  deployment: 'dpl_8YCHnqd4ZLGXnk9U2CuAJozUYLZ7',
  gates: [
    { id: 'P0', name: 'Truth Layer', state: 'verified', evidence: 'CI evidence', detail: 'Historical P0 evidence passed on e1f077f.' },
    { id: 'P2', name: 'Live POST Matrix', state: 'blocked', evidence: 'Environment', detail: 'Execution was not performed from this environment.' },
    { id: 'P4', name: 'Comparative Baselines', state: 'not-established', evidence: 'N = 0', detail: 'No empirical comparative baseline has been established.' },
    { id: 'P6a', name: 'CORS Verification', state: 'verified', evidence: 'Run #32092041579', detail: 'Four assertions passed; retained artifact verified.' },
    { id: 'DOC', name: 'Propagation Integrity', state: 'warning', evidence: 'propagation_check.py', detail: 'Claim occurrences still require propagation review.' },
    { id: 'FREEZE', name: 'Pilot Authorization', state: 'blocked', evidence: 'Governance state', detail: 'Pilot authorization is not granted; empirical execution must remain stopped.' },
  ] as Gate[],
  claims: [
    { claim: '340% coordination gain', status: 'warning', occurrences: 9, qualified: 5, bare: 4 },
    { claim: 'PDMAL empirical efficacy', status: 'blocked', occurrences: 0, qualified: 0, bare: 0 },
  ],
};

export function readinessScore() {
  const weights: Record<GateState, number> = { verified: 1, ready: 0.75, warning: 0.5, 'not-established': 0.25, blocked: 0 };
  const total = orbitSnapshot.gates.reduce((sum, gate) => sum + weights[gate.state], 0);
  return Math.round((total / orbitSnapshot.gates.length) * 100);
}
