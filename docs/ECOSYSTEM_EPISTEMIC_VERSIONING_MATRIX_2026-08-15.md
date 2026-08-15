# Ecosystem Epistemic + Versioning Matrix — 2026-08-15

## Purpose

This is the current mechanical reconciliation layer for the ndrorchestration repository ecosystem. It separates repository role, evidence maturity, descriptive language, and release/versioning posture.

The matrix is intentionally conservative: a repository may be technically useful while still being experimental, incomplete, historical, or portfolio-oriented.

## Canonical evidence ladder

`DEFINED → IMPLEMENTED → COMPUTED → VERIFIED → ATTESTED → HISTORICAL → HYPOTHESIS → METAPHOR → UNSUPPORTED → DEPRECATED`

A version number describes a software/research artifact state; it does not certify scientific validity.

## Core repositories

| Repository | Role | Evidence posture | Versioning assessment | Required descriptive posture |
|---|---|---|---|---|
| `agent-control-plane` | orchestration infrastructure | local kernel implemented; CI-tested | **0.1.x appropriate** | call it an experimental deterministic control-plane kernel; do not call it production/distributed/autonomous |
| `Meshsense` | spatial/runtime application | deployment exists; runtime equivalence remains constrained | **0.x / pre-release appropriate** until runtime closure | distinguish GitHub `Meshsense` from Vercel `meshsense-ruview-status`; do not claim independently verified production health while SSO blocks direct endpoint evidence |
| `Driftwatch` | drift/evaluation system | application infrastructure implemented; detector benchmark pending | **0.x appropriate** until benchmark evidence | describe detector as experimental/benchmark-pending; infrastructure existence is not detector validation |
| `Acoustic-mesh` | acoustic/network engineering | implementation and CI exist; empirical acoustic/sensor evidence pending | **0.x appropriate** | describe as engineering prototype/experimental system; separate network implementation from physical/acoustic claims |
| `phi-calculus-app` | mathematical visualization/experimental app | computational/visual artifact; formal validation remains scoped | **0.x appropriate** | call mathematical constructs project-local/proposed unless independently derived or verified |
| `AHG-Zeta-Pell-Autonomous-Lattice` | mathematical/control research | evidence checkpoint/pass work exists; Pass 2/source-dependent | **0.x / research versioning** | avoid presenting mathematical/control claims as established theory without derivation and reproducible evidence |
| `DGAF-Framework` | governance/research framework | substantial implementation/documentation; active draft material remains project-local | **retain existing v3.x component/version vocabulary; do not imply framework-wide scientific certification** | distinguish project-local governance mechanisms from external authority/validation |
| `Amethyst-Governance-Eval-Stack` | evaluation/governance stack | structured protocols, schemas, risk register; effectiveness evidence varies | **v0.x / schema-versioned artifacts** | distinguish specifications and rubrics from demonstrated governance effectiveness |
| `sentinel-governance` | GitHub operator/governance automation | implemented operator path; live integrations depend on external configuration | **0.x / deployment-dependent** | distinguish implemented observe/repair modes from live production operation |

## Portfolio/support repositories

These should not be artificially promoted to research-system maturity.

| Repository family | Classification | Versioning posture |
|---|---|---|
| `ai-prompt-systems-portfolio` | portfolio/presentation | date/release snapshots; semver only if software is independently released |
| `ai-prompt-engineering-portfolio` | portfolio/archive | descriptive/date versioning preferred |
| `AI-Prompt-Engineer` | portfolio/support | descriptive/date versioning preferred |
| `resumeapex-eval` | evaluation/portfolio support | 0.x while evaluation methodology evolves |
| `3d-visualization-hub` | visualization support | 0.x unless packaged as a stable application |
| `junior-apogee-app` | application/demo | 0.x until stable contract exists |
| `entrepreneur-hub` | portfolio/business support | date-based/content releases preferred |
| `career-positioning` | portfolio/support | date-based revisions preferred |
| `prompt-optimization-library` | library/research support | 0.x until API and benchmark contract stabilizes |

## Governance/operations/support repositories

| Repository | Classification | Correction posture |
|---|---|---|
| `Gold-star-standards` | standards/support | treat standards as project-defined criteria, not external certification |
| `gold-star-qa-framework` | archived QA | preserve as historical; do not imply current canonical status |
| `ai-governance-frameworks` | research/reference | distinguish synthesis/reference material from original validated framework claims |
| `dgaf-ops` | operations | operational artifact; do not conflate with DGAF framework semantics |
| `aoga-dashboard` | dashboard | interface/aggregation artifact; claims depend on underlying data |
| `pptl-governance-dashboard` | dashboard | interface/aggregation artifact; verify source data before claims |
| `automation-scripts` | utility | script maturity depends on individual tool; no blanket production claim |
| `api` | API scaffold/support | status remains implementation-dependent; avoid implied public API stability |
| `.github` | organization configuration | configuration repository; not a project/system |
| `chat-archives` | archive | historical record; not canonical implementation evidence |
| `ndrorchestration` | ecosystem/portfolio index | canonical map/index; should not be treated as implementation proof |

## Naming corrections

- `Meshsense` is the canonical GitHub repository identity.
- `meshsense-ruview-status` is the Vercel project/deployment identity.
- Historical names such as RuView or MeshSense/RuView should be described as aliases/history where necessary, not silently substituted for the canonical repository name.
- `ASIS` means **Acoustic Spatial Insight System** in the ecosystem vocabulary.
- `Acoustic-mesh` remains the acoustic/network engineering repository and should not be described as the entirety of ASIS.
- `ACP` means **Agent Control Plane** and is the repository/project identity for the orchestration kernel.

## Versioning policy

Use SemVer where a repository exposes a stable software API or package contract.

Use `0.x.y` while the contract is still changing or evidence is incomplete.

Use date/revision identifiers for portfolio, archival, and documentation artifacts where a software version would falsely imply API stability.

Use schema-specific versions (for example `v1`) for durable data/protocol formats; schema version does not imply scientific validation.

Do not increment a major version merely because a conceptual framework received a new research draft. Promote versions according to actual compatibility/evidence changes.

## Required status language

Prefer:

- "implemented and tested locally"
- "CI-tested"
- "experimental"
- "benchmark pending"
- "runtime verification constrained"
- "project-local specification"
- "historical"
- "hypothesis"

Avoid unsupported blanket language such as:

- "validated framework"
- "production-ready"
- "autonomous" when autonomy is not demonstrated
- "scientifically proven"
- "certified"
- "secure" without a security assessment
- "real-time" without measured latency evidence

## Current closure gates

1. Repository identity and role — reconciled.
2. Naming and cross-system distinctions — reconciled at the canonical-map level.
3. Evidence-language standard — established.
4. Versioning assessment — established for core repository classes.
5. Core repository descriptive corrections — ongoing/priority-driven.
6. Runtime/deployment evidence — still requires direct verification where access controls intervene.
7. Experimental evidence propagation — pending actual experiments/benchmarks.
8. Full repository-by-repository mechanical synchronization — not yet certified complete.

This matrix is itself a dated control artifact and should be revised when repository roles, implementation maturity, or evidence state materially changes.
