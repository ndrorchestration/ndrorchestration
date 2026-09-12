export const ORBIT_VERSION = '1.1.0';
export const EVIDENCE_SCHEMA = 'orbit.evidence.v3';

function required(name: string, fallback: string) {
  const value = process.env[name]?.trim();
  return value || fallback;
}

export const orbitConfig = Object.freeze({
  // ORBIT is an observer, not an authority. Its default source is the
  // repository that owns DGAF governance/evidence state, not this public
  // profile repository.
  repository: required('ORBIT_REPOSITORY', 'ndrorchestration/DGAF-Framework'),
  branch: required('ORBIT_BRANCH', 'main'),
  githubTimeoutMs: 5000,
});
