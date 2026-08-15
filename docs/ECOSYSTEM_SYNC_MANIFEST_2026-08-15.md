# Ecosystem Synchronization Manifest — 2026-08-15

## Purpose

Canonical mechanical inventory for the connected `ndrorchestration` ecosystem. This manifest distinguishes repository inventory from runtime and experimental evidence.

## Status vocabulary

- **VERIFIED** — direct current evidence exists.
- **NOT APPLICABLE** — the connection does not apply.
- **PENDING** — a specific evidence or synchronization action remains.
- **HISTORICAL** — evidence is dated and must not be treated as current state.

## GitHub inventory

Current connected owner inventory: **29 repositories**.

### Core systems / research

| Repository | System / role | State |
|---|---|---|
| `Acoustic-mesh` | Acoustic/WebRTC mesh; ASIS engineering track | VERIFIED inventory; physical/acoustic validation PENDING |
| `Meshsense` | MeshSense / RuView Status | VERIFIED inventory; runtime/source equivalence PENDING |
| `DGAF-Framework` | Dynamic Governance Agentic Formation; PDMAL lineage | VERIFIED inventory; empirical claims remain bounded |
| `Driftwatch` | Drift simulation/detection research | VERIFIED inventory; detector benchmark PENDING |
| `Amethyst-Governance-Eval-Stack` | Guardrail/evaluation stack | VERIFIED inventory; effectiveness validation PENDING |
| `phi-calculus-app` | Phi-calculus research/visualization | VERIFIED inventory; empirical claims bounded |
| `AHG-Zeta-Pell-Autonomous-Lattice` | AHG/Pell/lattice research | VERIFIED inventory; Pass 2 source work PENDING |
| `agent-control-plane` | Proposed orchestration/control plane | VERIFIED inventory; specification-stage |

### Evaluation / governance tooling

| Repository | Role | State |
|---|---|---|
| `sentinel-governance` | CI/CD integrity and governance automation | VERIFIED inventory |
| `ai-governance-frameworks` | Governance-framework research/mapping | VERIFIED inventory |
| `junior-apogee-app` | Agent evaluation/QA application | VERIFIED inventory |
| `resumeapex-eval` | Resume/evaluation benchmark tooling | VERIFIED inventory |
| `Gold-star-standards` | QA/rating standards | VERIFIED inventory |
| `gold-star-qa-framework` | Historical/archived QA framework | VERIFIED inventory; ARCHIVED |
| `pptl-governance-dashboard` | Governance dashboard | VERIFIED inventory |
| `aoga-dashboard` | Agentic orchestration/governance dashboard | VERIFIED inventory |
| `dgaf-ops` | DGAF operational internals | VERIFIED inventory |
| `entrepreneur-hub` | Governance/evaluation templates and workflows | VERIFIED inventory |

### Portfolio / support / archive infrastructure

| Repository | Role | State |
|---|---|---|
| `AI-Prompt-Engineer` | Prompt-engineering portfolio/archive | VERIFIED inventory |
| `ai-prompt-engineering-portfolio` | Prompt-engineering portfolio | VERIFIED inventory |
| `ai-prompt-systems-portfolio` | Public prompt-systems portfolio | VERIFIED inventory |
| `prompt-optimization-library` | Prompt optimization archive/library | VERIFIED inventory |
| `3d-visualization-hub` | Visualization infrastructure | VERIFIED inventory |
| `career-positioning` | Career strategy | VERIFIED inventory |
| `automation-scripts` | Ecosystem automation utilities | VERIFIED inventory |
| `chat-archives` | Conversation archive/knowledge base | VERIFIED inventory |
| `ndrorchestration` | Public ecosystem portfolio/index | VERIFIED inventory |
| `api` | Phi-Knight Vertical Corridor API surface | VERIFIED inventory |
| `.github` | Organization community-health files | VERIFIED inventory |

## Canonical system mappings

| System | GitHub | Vercel | Connection state |
|---|---|---|---|
| MeshSense / RuView Status | `ndrorchestration/Meshsense` | `meshsense-ruview-status` | **VERIFIED** identity mapping; runtime endpoint equivalence **PENDING** |
| Driftwatch | `ndrorchestration/Driftwatch` | `driftwatch` | **VERIFIED** identity/name match; detector evidence **PENDING** |
| Phi-Calculus | `ndrorchestration/phi-calculus-app` | `phi-calculus` | **VERIFIED** identity/name mapping; runtime/evidence state tracked separately |
| Portfolio / ecosystem index | `ndrorchestration/ndrorchestration` | `ndrorchestration` | **VERIFIED** as deployment/project surface; scope is presentation/infrastructure |
| AOGA Dashboard | `ndrorchestration/aoga-dashboard` | `aoga-dashboard` | **VERIFIED** identity/name mapping; runtime claims evidence-specific |
| DGAF RuView mitigation | DGAF ecosystem surface | `dgaf-ruview-mitigation` | **PENDING** exact source binding; do not infer from project name |
| Quintet hardening report | DGAF/evaluation ecosystem surface | `quintet-hardening-report` | **PENDING** exact source binding; do not infer from project name |
| Phi-Knight Vertical Corridor | `ndrorchestration/api` | `phiknightverticalcorridor` | **VERIFIED** functional naming relationship; runtime evidence tracked separately |

## Vercel team inventory

Current connected team exposes 8 projects:

- `driftwatch`
- `phiknightverticalcorridor`
- `phi-calculus`
- `ndrorchestration`
- `meshsense-ruview-status`
- `aoga-dashboard`
- `dgaf-ruview-mitigation`
- `quintet-hardening-report`

Presence in Vercel does **not** imply that the corresponding GitHub source binding has been verified.

## High-value evidence gates

### Meshsense

`canonical source → CI → production deployment → authenticated endpoint verification → runtime/source equivalence → behavioral evidence`

Current gate: endpoint/runtime equivalence remains PENDING because direct `/api/status` verification is authentication-constrained.

### Driftwatch

`signal specification → detector implementation → frozen baseline → benchmark → error analysis → reproducible artifact`

Current gate: detector implementation/benchmark evidence PENDING.

### Acoustic-Mesh / ASIS

`network implementation → software tests → acoustic/sensor protocol → physical measurement → uncertainty/replication`

Current gate: physical measurement evidence PENDING.

### PDMAL / Phi-Calculus / AHG lattice

`definition → derivation → computation → reproducible experiment → appropriate review`

Current gate: project-local experimental evidence remains incomplete where explicitly marked.

## Cross-system rules

- ASIS = **Acoustic Spatial Insight System**.
- `Meshsense` is the shortened GitHub repository identifier.
- `MeshSense / RuView Status` is the system identity.
- `meshsense-ruview-status` is the Vercel project/deployment identifier for that system.
- `Acoustic-Mesh` is separate from MeshSense/RuView.
- PDMAL is a DGAF research lineage; do not create a duplicate repository solely for documentation symmetry.
- Repository relationships do not transfer validation.
- A commit is not a deployment; a deployment is not runtime verification; runtime verification is not physical or empirical validation.
- Historical connector limitations remain historical and must not be represented as current access state.

## Closure classification

| Layer | State |
|---|---|
| GitHub repository inventory | **VERIFIED** |
| GitHub taxonomy/classification | **VERIFIED** |
| GitHub ↔ Notion registry representation | **VERIFIED at inventory/registry level** |
| Known GitHub ↔ Vercel identity mappings | **VERIFIED where explicitly listed** |
| Unknown GitHub ↔ Vercel bindings | **PENDING; not inferred** |
| MeshSense runtime/source equivalence | **PENDING** |
| Driftwatch detector effectiveness | **PENDING** |
| Acoustic/ASIS physical validation | **PENDING** |
| PDMAL comparative experiment | **PENDING** |
| AHG Pass 2 | **PENDING** |
| Documentation layer | **MECHANICALLY SYNCHRONIZED at inventory level** |

## Final closure condition

The documentation-and-connections layer is considered synchronized when every accessible repository has an inventory classification and every applicable cross-system connection is marked `VERIFIED`, `NOT APPLICABLE`, or `PENDING` with an actionable reason. This manifest satisfies that inventory-level condition. Runtime and empirical closure remain separate gates.
