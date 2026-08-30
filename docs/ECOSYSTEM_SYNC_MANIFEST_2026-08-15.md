# Ecosystem Synchronization Manifest — 2026-08-30 Refresh

## Purpose
Canonical mechanical inventory for the connected `ndrorchestration` ecosystem. This manifest distinguishes repository inventory from runtime and experimental evidence.

## Status vocabulary

- **VERIFIED** — direct current evidence exists.
- **NOT APPLICABLE** — the connection does not apply.
- **PENDING** — a specific evidence or synchronization action remains.
- **HISTORICAL** — evidence is dated and must not be treated as current state.

## 2026-08-30 epistemic refresh

The ecosystem-wide evidence boundary has been refreshed. Active canonical repositories now carry a dated `docs/EVIDENCE_STATUS_2026-08-30.md` (or equivalent ecosystem-standard file) recording that implementation, CI, deployment, benchmarks, governance mappings, and project-local terminology must not be promoted beyond their directly supported evidence.

The refresh does **not** convert any PENDING gate into VERIFIED. In particular:

- PDMAL empirical efficacy remains PENDING until the current candidate apparatus is authorized and reproducible results exist.
- Driftwatch detector effectiveness remains PENDING independent benchmark evidence.
- Acoustic/ASIS physical validation remains PENDING physical measurement and replication.
- MeshSense exact source/runtime equivalence remains PENDING unless current deployment metadata establishes it.
- AOGA endpoint/runtime and end-to-end behavior remain separate verification gates.
- AHG Pass 2 remains PENDING where previously identified.
- Historical repositories remain historical and are not current authorities.

## Canonical inventory

The 2026-08-15 manifest's 29-repository canonical set remains the governance inventory. GitHub currently exposes additional repositories in the connected owner account, including forks, transient test repositories, and other newly created surfaces; these are not silently promoted into the canonical ecosystem set without classification.

## Normalization rule

A mathematically correct calculation is not automatically a useful engineering signal. Repository claims must distinguish calculation correctness from engineering usefulness, and neither should be promoted beyond the evidence actually produced by the repository.

A commit is not a deployment; a deployment is not runtime verification; runtime verification is not physical or empirical validation; a benchmark specification is not benchmark validation; and a numerical target is not an achieved result.

## Refresh status

- Canonical active repositories: epistemic-boundary refresh applied where writable.
- `gold-star-qa-framework`: archived/read-only; refresh could not be written. Its archived state remains the authoritative boundary.
- Cross-repository validation transfer: NOT PERMITTED.

*Last refreshed: 2026-08-30.*