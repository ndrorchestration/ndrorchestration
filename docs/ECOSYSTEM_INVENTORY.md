# NDR Ecosystem Inventory

**Version:** 2.1 | **Date:** 2026-08-17 | **Domain:** OI  
**Status:** ACTIVE / NORMALIZATION IN PROGRESS  
**Canonical Path:** `ndrorchestration/ndrorchestration/docs/ECOSYSTEM_INVENTORY.md`

> Historical inventory material below is retained for provenance. Current state is maintained in the normalization addendum and the linked project evidence records.

---

## Current source of truth

The live `ndrorchestration` GitHub owner inventory contains the repositories exposed through the connected GitHub account. The current mechanical inventory includes `Acoustic-mesh`, `Meshsense`, and `ndrorchestration`; no separately named ASIS-AR Android repository is exposed by the current repository listing/search.

## Current canonical system boundaries

| System | Canonical repository | Current evidence state |
|---|---|---|
| DGAF | `DGAF-Framework` | CI verified partial; empirical claims bounded |
| ASIS | `Acoustic-mesh` | acoustic/WebRTC engineering track; physical evidence pending |
| ASIS-AR | **No separately verified repository** | Galaxy S24 implementation is documented; canonical Android source recovery open |
| MeshSense / RuView Status | `Meshsense` | runtime surface coded; production provenance verified; FM-01 real-data evidence pending |
| AHG Zeta-Pell | `AHG-Zeta-Pell-Autonomous-Lattice` | Pass-2 source evidence pending |
| Agent Control Plane | `agent-control-plane` | executable kernel/CI present; production-scale claims excluded |
| Phi-Calculus | `phi-calculus-app` | empirical evidence bounded |
| Driftwatch | `Driftwatch` | detector benchmark pending |
| 3D Visualization Hub | `3d-visualization-hub` | evidence audit pending |
| Acoustic-Mesh / Acoustic Trio | `Acoustic-mesh` | acoustic analysis/teaching scope; physical evidence pending |
| Canonical ecosystem index | `ndrorchestration` | inventory/documentation surface |

## ASIS / Galaxy S24 source-recovery finding — 2026-08-17

The connected GitHub repository inventory was rechecked for ASIS/ASIS-AR naming variants. No separately named `ASIS-AR`, `ASIS_AR`, `ASIS-Android`, or equivalent Galaxy S24 Android repository was exposed.

`Acoustic-mesh` was checked for `ASIS-AR` and Android source markers through the connected GitHub file search; no matching Android implementation source was found through the connector surface. This is a **source-visibility/recovery finding, not proof of source absence**.

Do not create a competing Android repository solely to satisfy the gap. The current ASIS-AR gate remains:

**Source recovery → SensorManager implementation → physical Galaxy S24 execution → evidence manifest → S24-1 PASS/FAIL.**

## MeshSense / RuView separation

- `Meshsense` is the independent companion-layer experiment around the existing third-party `ruvnet/RuView` system.
- MeshSense investigates six provisional failure-mode compensation hypotheses.
- ESP32-S3/NIC hardware belongs to the **RuView/FM-01 experiment only**.
- It is **not** the primary hardware path for ASIS/ASIS-AR.
- Deployment/runtime provenance does not transfer between systems.

## ASIS-AR hardware path

**Primary platform:** Samsung Galaxy S24.

The current implementation target is the Android-exposed sensor stack and associated platform channels, followed by synchronization, calibration, sensor fusion, and spatial-state construction.

The first implementation gate is **S24-1 — runtime sensor inventory**. It requires a physical S24 execution that produces a non-empty sensor inventory, observed event timestamps/counts, rate statistics, device/build/API provenance, and a deterministic hashable manifest.

Raw Wi-Fi CSI is explicitly outside the S24-1 gate. Wi-Fi metadata availability must not be treated as raw CSI access.

## Cross-system rules

- ASIS = **Acoustic Spatial Insight System**.
- ASIS-AR = Galaxy S24 implementation of the ASIS architecture, pending recovery of canonical source evidence.
- `Meshsense` is the GitHub repository identifier.
- `MeshSense / RuView Status` is the MeshSense system identity.
- `meshsense-ruview-status` is the Vercel project identifier.
- Acoustic-Mesh and MeshSense/RuView are separate repositories/systems.
- Relationships between projects do not transfer validation.
- A commit is not a deployment; a deployment is not runtime verification; runtime verification is not physical or empirical validation.
- Unknown repository or deployment identity remains unresolved rather than being inferred from naming.

## Current open evidence gates

- ASIS-AR canonical Android source recovery.
- ASIS-AR S24-1 physical sensor inventory.
- S24 synchronized acquisition and calibration.
- Acoustic-Mesh acoustic and sensor measurements.
- MeshSense FM-01 real-CSI/physical validation.
- DGAF empirical validation and broader repository security/provenance audit.

## Synchronization rule

This inventory is a mechanical index, not an assertion that every repository is validated. Current state must be read together with the relevant Notion project records and repository-specific experiment/quality documents. Historical logs remain historical.

*Last updated: 2026-08-17 during ASIS/ASIS-AR source-recovery normalization.*
