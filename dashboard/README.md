# ORBIT — Evidence & Readiness Command Center

ORBIT is the evidence-first control surface for DGAF/PDMAL. It separates current repository state, historical evidence, deployment identity, experimental state, governance gates, and documentation claim propagation.

## Current MVP

- Evidence gate matrix with fail-closed states.
- Epistemic state and empirical-N visibility.
- Claim propagation monitor.
- Readiness index derived from gate state.
- JSON API at `/api/orbit`.
- Snapshot model designed to prevent unsupported claims from upgrading project status.

## Run

```bash
npm install
npm run dev
```

Open `http://localhost:3000`.

## Governance invariant

A claim never upgrades epistemic status. Evidence does. The DGAF/PDMAL pilot remains unauthorized until the required freeze and authorization chain is complete.

## Next integration layer

Replace the static snapshot with signed ingestion from GitHub Actions artifacts, repository HEAD, Vercel deployment metadata, and propagation-check output. Preserve immutable snapshots so historical evidence cannot be silently relabeled as current evidence.
