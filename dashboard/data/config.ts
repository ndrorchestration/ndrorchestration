export const ORBIT_VERSION = '1.0.0';
export const EVIDENCE_SCHEMA = 'orbit.evidence.v2';

function required(name: string, fallback: string) {
  const value = process.env[name]?.trim();
  return value || fallback;
}

export const orbitConfig = Object.freeze({
  repository: required('ORBIT_REPOSITORY', 'ndrorchestration/ndrorchestration'),
  branch: required('ORBIT_BRANCH', 'main'),
  githubTimeoutMs: 5000,
});
