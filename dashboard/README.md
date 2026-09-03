# ORBIT — Evidence & Readiness Command Center

ORBIT is an evidence-first operational control plane for DGAF/PDMAL. It separates current repository state, historical evidence, deployment identity, experimental state, governance gates, and documentation claim propagation.

## Product surface

- `/` — operational dashboard with live reconciliation and fail-closed status.
- `/api/orbit` — live evidence/readiness API.
- `/api/health` — deployment health probe.
- `/api/schema` — machine-readable ORBIT version/evidence-schema metadata.

## Runtime configuration

The dashboard is configurable without changing source code:

- `ORBIT_REPOSITORY` — GitHub `owner/name`; defaults to `ndrorchestration/ndrorchestration`.
- `ORBIT_BRANCH` — tracked branch; defaults to `main`.
- `GITHUB_TOKEN` — optional GitHub token for higher API limits/private repositories. Never expose this to the browser.
- `VERCEL_GIT_COMMIT_SHA` / `VERCEL_URL` — automatically supplied by Vercel when available.

## Local development

Requires Node 24+.

```bash
npm install
npm test
npm run build
npm run dev
```

Open `http://localhost:3000`.

## CI / evidence boundary

`.github/workflows/orbit-evidence.yml` runs invariant tests, a production build, source-HEAD verification, claim propagation scanning, and immutable evidence-artifact creation. Pull-request evidence checks out the PR source SHA rather than GitHub's synthetic merge SHA.

Generated build output, dependency trees, VCS metadata, and ORBIT's generated evidence directory are excluded from claim scans.

## Governance invariant

**Claims do not upgrade epistemic status. Evidence does.**

The PDMAL pilot remains unauthorized while the required freeze and authorization chain is incomplete. ORBIT is observational: it must never authorize an experiment merely because a dashboard state looks ready.

## Fail-closed behavior

If live GitHub evidence cannot be established, `/api/orbit` returns HTTP 503 and retains the immutable baseline snapshot. Documentation contradictions force the freeze gate blocked. SHA values must be full 40-character Git commit identifiers. Browser responses are non-cacheable for live evidence.

## Deployment acceptance

A release is not considered product-ready until all of the following are true on the exact release commit:

1. `npm test` passes.
2. `npm run build` passes.
3. CI source-HEAD verification passes.
4. Evidence artifact is uploaded and retained.
5. `/api/health` returns `status: ok`.
6. `/api/schema` reports the expected ORBIT version and evidence schema.
7. `/api/orbit` successfully reconciles the configured GitHub repository, or correctly fails closed with HTTP 503.
8. Deployment commit and tracked source HEAD are explicitly compared when Vercel metadata is available.
9. No DGAF/PDMAL experimental authorization is inferred from ORBIT readiness.
