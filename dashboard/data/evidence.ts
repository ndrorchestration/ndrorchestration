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
  const validSha = (sha: unknown): sha is string => typeof sha === 'string' && /^[0-9a-f]{40}$/.test(sha);
  const timestamp = typeof v.generatedAt === 'string' ? Date.parse(v.generatedAt) : NaN;
  const validTimestamp = typeof v.generatedAt === 'string' &&
    /^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d{3})?Z$/.test(v.generatedAt) &&
    Number.isFinite(timestamp) &&
    new Date(timestamp).toISOString().replace('.000Z', 'Z') === v.generatedAt.replace('.000Z', 'Z');
  const validSourceIdentity = validSha(v.head) && validSha(v.githubEventSha) &&
    (v.pullRequestHeadSha === '' ? v.githubEventSha === v.head : v.pullRequestHeadSha === v.head);
  return v.schema === EVIDENCE_SCHEMA &&
    validTimestamp &&
    typeof v.repository === 'string' && /^[A-Za-z0-9_.-]+\/[A-Za-z0-9_.-]+$/.test(v.repository) &&
    typeof v.head === 'string' && /^[0-9a-f]{40}$/.test(v.head) &&
    v.headSemantics === 'source-head' &&
    validSourceIdentity &&
    typeof readme?.empiricalN0 === 'boolean' &&
    typeof readme?.pilotUnauthorized === 'boolean' &&
    Number.isInteger(propagation?.['340PercentClaimOccurrences']) &&
    Number(propagation?.['340PercentClaimOccurrences']) >= 0 &&
    governance?.failClosed === true;
}
