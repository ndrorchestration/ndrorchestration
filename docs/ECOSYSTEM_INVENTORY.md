# NDR Ecosystem Inventory
**Version:** 1.0 | **Date:** 2026-07-05 | **Domain:** OI  
**Sweep:** COLLEEN-EH-004 | **Status:** ACTIVE  
**Canonical Path:** `ndrorchestration/ndrorchestration/docs/ECOSYSTEM_INVENTORY.md`

> This file closes Gap G-01 from `agent-amethyst-instantiation.md`. It is the authoritative file-tree record and sweep log for the full NDR ecosystem. COLLEEN updates this on every sweep. Amethyst verifies before any session synthesis.

---

## GitHub Repositories

### ndrorchestration/ndrorchestration (Primary Operational Repo)

```
ndrorchestration/ndrorchestration/
├── README.md                                    (8,065 bytes) PUBLIC ACTIVE
├── vercel.json                                  (135 bytes)   PUBLIC ACTIVE
├── dashboard/                                   (dir)
├── docs/
│   ├── agent-amethyst-instantiation.md          (13,814 bytes) PUBLIC ACTIVE  [2026-07-05]
│   ├── agent-roster.md                          (7,746 bytes)  PUBLIC ACTIVE  [prior]
│   ├── cross-account-bridge.md                  (5,526 bytes)  PUBLIC ACTIVE  [prior]
│   ├── ECOSYSTEM_INVENTORY.md                   (this file)    PUBLIC ACTIVE  [2026-07-05]
│   ├── master-classification-index.md           (9,688 bytes)  PUBLIC ACTIVE  [2026-07-05 v1.1 -> v1.2]
│   ├── vocabulary-taxonomy.md                   (new)          PUBLIC ACTIVE  [2026-07-05]
│   └── workspace-maintenance-protocol.md        (3,162 bytes)  PUBLIC ACTIVE  [prior]
├── logs/                                        (dir)
├── portfolio/                                   (dir)
└── profile/                                     (dir)
```

**Missing / Not Yet Committed (Open Gaps):**

| Gap ID | File | Status |
|---|---|---|
| G-02 | `docs/SESSION_ANCHORS.md` | OPEN |
| G-03 | `docs/NDR_PATTERN_REGISTRY_UNIFIED.md` | OPEN |
| G-04 | `CHANGELOG.md` | OPEN |
| G-05 | 5th pentagonal agent spec | PENDING |
| G-06 | `.github/workflows/colleen-sweep.yml` | DRAFT |

---

### ndrorchestration/entrepreneur-hub

```
entrepreneur-hub/
├── README.md
├── docs/
│   ├── MONETIZATIONFLYWHEEL.md     P-34 v1.0 flywheel spec         ACTIVE
│   ├── NEEDLETEMPLATEINDEX.md      COLLEEN Sweep-EH-003            ACTIVE
│   ├── ROADMAP.md                  Phase 0 closed / Phase 1 open   ACTIVE
│   └── NEEDLETEMPLATEINDEX.md      COLLEEN Sweep-EH-003 stamp      ACTIVE
├── ai-product-launch-checklist/     T-EH-01 folder                  DRAFT
├── governance-starter-pack/         T-EH-05 folder                  DRAFT
├── marketplace-optimizer/           T-EH-03 folder                  DRAFT
├── monetization-diagnostic/         T-EH-04 folder                  DRAFT
└── sprint-planner/                  T-EH-02 folder                  DRAFT
```

**Needle template links:** All 5 T-EH templates listed as PENDING Phase 1 in NEEDLETEMPLATEINDEX. No live Needle URLs yet.

---

### ndrorchestration/aoga-dashboard

```
aoga-dashboard/
├── (17 routes, OpenAPI 3.1.0 spec)
├── 13-agent roster wired
└── dark theme | Vercel: aoga-dashboard.vercel.app
```

**Status:** v1.2.0 ACTIVE | Last deployment: READY (post-2026-06-09 chain fix)

---

### ndrorchestration/phiknightverticalcorridor

```
phiknightverticalcorridor/
└── (Vercel project, created 2026-05-05)
```

**Status:** DRAFT | Deployment status: unconfirmed (no verified READY deployment)

---

### Flickerflash (Legacy / Gold-Standard Account)

| Repo | Purpose | Status |
|---|---|---|
| Flickerflash/DGAF-Framework | Core DGAF framework, PDMAL, agent governance | ACTIVE PRIVATE |
| Flickerflash/ai-governance-frameworks | Public governance templates | ACTIVE PUBLIC |
| Flickerflash/gold-star-qa-framework | Gold Star QA, Phase 4 rubrics | ARCHIVE PUBLIC |

---

## Vercel Projects (ndrorchestration team)

| Project | URL | Last Deploy | Status |
|---|---|---|---|
| ndrorchestration | ndrorchestration.vercel.app | 2026-06-09 (sweep date update) | READY |
| aoga-dashboard | aoga-dashboard.vercel.app | 2026-05-29 (chain fix, READY) | READY |
| phiknightverticalcorridor | (TBD) | 2026-05-05 (created) | UNCONFIRMED |

**Deployment audit note:** ndrorchestration had 10 consecutive ERROR deployments (2026-05-25–29) before READY was achieved. Root cause: fatal syntax error in `Layout.tsx` (unclosed array, no export). All resolved by 2026-05-29.

---

## GCP Infrastructure

| Project | Service | Region | Status |
|---|---|---|---|
| pentagonal | Cloud Run | europe-west1 | ACTIVE |

---

## Google Drive Folder Registry

| Drive Folder | GitHub Equivalent | Domain |
|---|---|---|
| `Agent-Frameworks/Orchestration/` | `portfolio/frameworks/` | FG |
| `Evaluation-Tools/` | `portfolio/rubrics/` | PE |
| `Visualizations/Architecture/` | `portfolio/visualizations/` | RT |
| `Mathematical-Models/` | `portfolio/math-models/` | RT |
| `Resume/Career/` | `portfolio/resume/` | CP |
| `[03] SYSTEM_GOVERNANCE/` | `docs/` | FG/OI |
| `Team-Wiki/Agent-R&D/` | `docs/team-wiki/` | TW |

**Key Drive artifacts (INTERNAL, not committed to GitHub):**
- MASTER PORTFOLIO INVENTORY v1.8
- Master Context File — PEL
- NDR Stasis Manifest (Patterns 1–132)
- Hardened Multi-Agent Substrate Spec
- Triadic Orchestration Choreography
- Agent Orchestration Matrix (xlsx)
- Phi Helix Interactive Model
- 3D Multi-Agent Architecture HTML
- Driftwatch Progress Report
- Auditing Engineering Terminology Taxonomy
- COLLEEN + Lavender Agent Cognition Map
- Hensel Formalism v1.0
- Incident Report NMS-INC-001
- Vercel Deployment Audit 2026-05-25→06-09
- Phi Harmonic Stability Map (Enhanced).html
- Agent Amethyst Rebrand GoogleAppsScript 2026-04-06

---

## Needle.app Template Registry

| Template ID | Name | Needle URL | Runs (90d) | Status |
|---|---|---|---|---|
| NT-01 | Evaluate LLM Output Quality | live | 860 | ACTIVE |
| NT-02 | Generate Grounded KB Answers | live | 1,248 | ACTIVE |
| NT-03 | KB Answer With Quality Check | live | 476 | ACTIVE (flat anomaly Jun 2026, NMS-INC-001) |
| NT-04 | Define AI Governance Specification | live | 320 | ACTIVE (flat anomaly Jun 2026, NMS-INC-001) |
| NT-05 | Test Governance API Gates | live | 0 | ACTIVE (high views, 0 runs — discovery/conversion gap) |
| T-EH-01 | AI Product Launch Checklist | pending | — | DRAFT (Phase 1) |
| T-EH-02 | Sprint Planner | pending | — | DRAFT (Phase 1) |
| T-EH-03 | Marketplace Optimizer | pending | — | DRAFT (Phase 1) |
| T-EH-04 | Monetization Diagnostic | pending | — | DRAFT (Phase 1) |
| T-EH-05 | AI Governance Starter Pack | pending | — | DRAFT (Phase 1 — priority launch) |

**Aggregate (90d window, Jun 26 2026):** 13,138 views / 1,144 uses / 2,904 runs / $4.19 LTV

---

## Sweep Log

| Sweep ID | Date | Executor | Scope | Outcome |
|---|---|---|---|
| SWEEP-001 | 2026-06-16 | COLLEEN | entrepreneur-hub NEEDLETEMPLATEINDEX | Completed; all 5 T-EH links pending Phase 1 |
| SWEEP-002 | 2026-06-26 | COLLEEN | ndrorchestration S044 | Closed; repo table updated, AOGA row added |
| SWEEP-EH-003 | 2026-06-26 | COLLEEN | entrepreneur-hub NEEDLETEMPLATEINDEX | Completed; 5 stubs confirmed unresolved |
| COLLEEN-EH-004 | 2026-07-05 | COLLEEN | Full ecosystem inventory (this file) | Completed; ECOSYSTEM_INVENTORY.md created, G-01 closed |

**Automation status:** `colleen-sweep.yml` GitHub Action is DRAFT. No automated sweeps are executing yet. All sweeps above are manually executed by Amethyst+COLLEEN in session.

---

*Last updated: 2026-07-05 by COLLEEN (sweep executor) / Amethyst (verifier) | ndrorchestration*
