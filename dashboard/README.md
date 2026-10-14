# NDR AI Systems Public Surface + ORBIT Evidence Observer

This Vercel application serves two deliberately separate responsibilities:

1. `/` is the curated public NDR AI Systems portfolio front door, synchronized to the canonical repository-root profile README.
2. `/orbit` is the ORBIT read-only evidence observability surface for DGAF/PDMAL.

The public home is not a governance authority. ORBIT is not a governance authority. Project-specific repositories and their canonical evidence/governance records remain authoritative for their own state.

## Product surface

- `/` — curated NDR AI Systems portfolio projection; the repository-root `README.md` is the canonical GitHub profile copy.
- `/orbit` — ORBIT observer for DGAF evidence state, provenance, blockers, and claim propagation.
- `/api/orbit` — machine-readable ORBIT reconciliation endpoint.
- `/api/health` — deployment health probe.
- `/api/schema` — machine-readable ORBIT version/evidence-schema metadata.

## ORBIT authority boundary

ORBIT is an **observer-only** surface. It may retrieve, compare, and display evidence, but it cannot establish freeze, grant experimental authorization, upgrade a claim, or create empirical authority.

By default ORBIT observes `ndrorchestration/DGAF-Framework` on `main`, because DGAF owns the governance/evidence state that ORBIT is displaying. It must not infer DGAF state from this public profile repository.

Runtime configuration:

- `ORBIT_REPOSITORY` — GitHub `owner/name`; defaults to `ndrorchestration/DGAF-Framework`.
- `ORBIT_BRANCH` — tracked branch; defaults to `main`.
- `GITHUB_TOKEN` — optional server-side GitHub token. Never expose it to the browser.
- `VERCEL_GIT_COMMIT_SHA` / `VERCEL_URL` — supplied by Vercel when available.

## Gate semantics

ORBIT reports a categorical observer state rather than a percentage readiness score:

- `BLOCKED` — at least one blocking gate is observed.
- `ATTENTION` — no blocking gate is observed, but warning or not-established state remains.
- `CLEAR` — the observed gate set contains neither blockers nor unresolved warning/not-established states.

These categories describe the **observed evidence state only**. `CLEAR` is not experimental authorization.

The DGAF authority check is fail-closed and requires canonical documentation to simultaneously affirm:

- `FAIL-CLOSED`;
- `NOT AUTHORIZED` (or equivalent explicit denial of authorization);
- empirical `N = 0`.

If any required state cannot be established, the observed authorization gate remains blocked.

## Local development

Requires Node 24+.

```bash
npm install
npm test
npm run build
npm run dev
```

Open `http://localhost:3000` for the public home and `http://localhost:3000/orbit` for ORBIT.

## CI / evidence boundary

`.github/workflows/orbit-evidence.yml` runs invariant tests, a production build, source-HEAD verification, claim propagation scanning, and immutable evidence-artifact creation. Pull-request evidence checks out the PR source SHA rather than GitHub's synthetic merge SHA.

Generated build output, dependency trees, VCS metadata, and ORBIT's generated evidence directory are excluded from claim scans.

### Runtime regression coverage

`npm test` runs both the existing source invariants and 24 production-logic runtime checks. The runtime suite uses Node 24 type erasure, a controlled GitHub transport, and a Next-style response collector to execute the API and snapshot validators. It also executes the same gate selector used by the UI. It is internal regression coverage, not live-deployment or browser acceptance.

Current projection admission requires the exact full historical DGAF source SHA and its owning repository. README declarations are fetched at the observed immutable SHA, so branch movement cannot mix revisions. A different commit sharing the display prefix, or another configured repository, cannot admit the historical DGAF projection.

Snapshot artifact validation checks UTC timestamps, full event/source identities, and PR/source or push/source identity consistency. The runtime response schema (`orbit.evidence.v3`) and workflow artifact schema (`orbit.evidence.v2`) are distinct contracts.

Until current evidence is admitted, the UI displays only explicit blocked authority-reconciliation gates. Loading and failed refreshes withhold previously admitted or historical gate rows and counts. Malformed snapshots are rejected before rendering; UI refresh requests have a ten-second timeout. Only the latest request may update the view; replacing a request or unmounting invalidates and aborts the older request. Browser visual acceptance remains a separate check.

## Governance invariant

**Claims do not upgrade epistemic status. Evidence does.**

ORBIT must fail closed when required evidence is missing, stale, contradictory, or unavailable. The existence of this dashboard, a successful deployment, or a favorable observed state never substitutes for DGAF's own governance controls.

## Deployment acceptance

A release is not considered operationally accepted until, on the exact release commit:

1. `npm test` passes.
2. `npm run build` passes.
3. CI source-HEAD verification passes.
4. Evidence artifacts required by the workflow are retained.
5. `/api/health` returns `status: ok`.
6. `/api/schema` reports the expected ORBIT version and evidence schema.
7. `/api/orbit` reconciles the configured DGAF source or correctly fails closed with HTTP 503.
8. Deployment commit and tracked source HEAD are explicitly compared when Vercel metadata is available.
9. No DGAF/PDMAL experimental authorization is inferred from ORBIT state.
