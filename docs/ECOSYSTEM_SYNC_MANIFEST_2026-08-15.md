# Ecosystem Synchronization Manifest — 2026-08-15

## Status vocabulary

- **VERIFIED** — direct current evidence exists.
- **NOT APPLICABLE** — connection does not apply to the repository.
- **PENDING** — a specific evidence or synchronization action remains.
- **HISTORICAL** — evidence is dated and should not be treated as current.

## Canonical connections

| Connection | State | Notes |
|---|---|---|
| GitHub repository inventory | VERIFIED | Current repository inventory was reconciled during the August 15 sweep. |
| GitHub naming taxonomy | VERIFIED | Meshsense, Acoustic-mesh, ACP, ASIS distinctions recorded. |
| Notion master registry ↔ GitHub topology | VERIFIED at registry level | Conceptual/system mappings reconciled; runtime evidence is tracked separately. |
| Meshsense GitHub ↔ Vercel project | VERIFIED | GitHub `Meshsense`; Vercel `meshsense-ruview-status`. |
| Meshsense production runtime | PENDING | Deployment is READY, but direct endpoint verification is authentication-constrained. |
| Driftwatch detector evidence | PENDING | Specification exists; benchmark evidence remains to be generated. |
| Acoustic-mesh physical/acoustic evidence | PENDING | Software/CI evidence does not substitute for sensor/acoustic experiments. |
| PDMAL experimental propagation | PENDING | New experimental evidence must be propagated after experiments run. |
| AHG Pass 2 | PENDING | Source-dependent formal/evidence work remains. |
| Secondary/portfolio repo rewriting | NOT APPLICABLE by default | Classification is preferred over forcing core-system documentation onto support repositories. |

## Core evidence gates

### Meshsense

`canonical source → production deployment → authenticated endpoint verification → runtime/source equivalence → behavioral evidence`

Current gate: runtime/source equivalence and endpoint evidence pending.

### Driftwatch

`signal specification → detector implementation → frozen baseline → benchmark → error analysis → reproducible artifact`

Current gate: detector benchmark pending.

### Acoustic-mesh

`network implementation → software tests → acoustic/sensor protocol → physical measurement → uncertainty/replication`

Current gate: physical measurement evidence pending.

### PDMAL / Phi-Calulus / AHG lattice

`definition → derivation → computation → reproducible experiment → independent/appropriate review`

Current gate: evidence remains project-local/experimental where the chain is incomplete.

## Documentation rule

Documentation must describe the current evidence state rather than the intended future state. A roadmap is not an implementation record; a deployment record is not an endpoint verification; a benchmark specification is not a benchmark result; a mathematical notation is not a proof.

## Final closure condition

The ecosystem documentation-and-connections layer should only be marked fully closed when every applicable repository/connection has a current entry in this manifest and each is marked `VERIFIED`, `NOT APPLICABLE`, or explicitly `PENDING` with an actionable reason.
