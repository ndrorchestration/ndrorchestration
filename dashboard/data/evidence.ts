export const EVIDENCE_SCHEMA = 'orbit.evidence.v2' as const;

export interface EvidenceSnapshot {
  schema: typeof EVIDENCE_SCHEMA;
  generatedAt: string;
  repository: string;
  head: string;
  headSemantics: 'source-head';
  githubEventSha: string;
  pullRequestHeadSha: string;
  readme: { empiricalN0: boolean; pilotUnauthorized: boolean };
  propagation: { '340PercentClaimOccurrences': number };
  governance: { failClosed: true };
}

export function isEvidenceSnapshot(value: unknown): value is EvidenceSnapshot {
  if (!value || typeof value !== 'object') return false;
  const v = value as Record<string, unknown>;
  const readme = v.readme as Record<string, unknown> | undefined;
  const propagation = v.propagation as Record<string, unknown> | undefined;
  const governance = v.governance as Record<string, unknown> | undefined;
  return v.schema === EVIDENCE_SCHEMA &&
    typeof v.generatedAt === 'string' &&
    typeof v.repository === 'string' &&
    typeof v.head === 'string' && /^[0-9a-f]{40}$/.test(v.head) &&
    v.headSemantics === 'source-head' &&
    typeof v.githubEventSha === 'string' &&
    typeof v.pullRequestHeadSha === 'string' &&
    typeof readme?.empiricalN0 === 'boolean' &&
    typeof readme?.pilotUnauthorized === 'boolean' &&
    Number.isInteger(propagation?.['340PercentClaimOccurrences']) &&
    Number(propagation?.['340PercentClaimOccurrences']) >= 0 &&
    governance?.failClosed === true;
}
