# NDR Master Classification Index
**Version:** 1.2 | **Date:** 2026-07-05 | **Maintainer:** ndrorchestration  
**Schema:** `[DOMAIN] [VISIBILITY] [STATUS]`

---

## Changelog

| Version | Date | Change |
|---|---|---|
| 1.0 | 2026-07-02 | Initial release |
| 1.1 | 2026-07-05 | Added TW domain; expanded Space routing; added 20+ artifacts across all domains; removed QUARANTINE status code; updated maintenance protocol |
| 1.2 | 2026-07-05 | Added ECOSYSTEM_INVENTORY.md (G-01 CLOSED); added vocabulary-taxonomy.md; registered both under OI and TW respectively; Drive mirror table updated |

---

## Domain Codes

| Code | Domain | Definition |
|---|---|---|
| `FG` | Frameworks & Governance | Constitutional rules, DGAF, NIST RMF, constraint gates, rubric standards, AOGA architecture |
| `PE` | Prompt & Eval Systems | Prompt templates, evaluation rubrics, Gold Star QA, audit checklists, template registries, incident reports |
| `CP` | Career & Portfolio | Resumes, headers, position strategies, Needle.app artifacts, ResumeApex, entrepreneur hub templates |
| `RT` | Research & Theory | LLM research, Phi-Calculus, Hensel Formalism, mathematical foundations, agent cognition, academic references |
| `OI` | Operations & Infra | Session logs, tracking, workflow automation, GCP infra, Vercel deployments, COLLEEN sweeps, email mgmt |
| `TW` | Team Wiki / Agent R&D | Agent R&D Bootstrap Workspace, team-facing docs, agent role specs, R&D process artifacts |

**Visibility:** `PUBLIC` / `PRIVATE` / `INTERNAL` (Drive only, not GitHub)  
**Status:** `ACTIVE` / `POLISH` / `ARCHIVE` / `DRAFT`

---

## Account Routing

| Account | Purpose | Link |
|---|---|---|
| `ndrorchestration` | Active development, current work, portfolio publishing, AOGA infra | https://github.com/ndrorchestration |
| `Flickerflash` | Legacy portfolio artifacts, Agent Lavender framework history, gold-standard references | https://github.com/Flickerflash |

> Both accounts are maintained. `Flickerflash` is the origin; `ndrorchestration` is the operational present.

---

## Space-to-Domain Routing

| Perplexity Space | Primary Domain | Secondary Domain | What Lives Here |
|---|---|---|---|
| LLM & Agent R&D | RT | FG | Architecture research, Phi work, agent cognition, DGAF theory, Hensel Formalism |
| Needle / Entrepreneur Hub | CP | OI | Needle analytics, workflow templates, business artifacts, income-track work, NMS analytics |
| Bootstrap Workspace & Beyond | OI | PE | Session management, master inventory, workflow bootstrapping, prompt testing |
| Team Wiki Agent R&D | TW | RT | Agent R&D process docs, team-facing agent role specs, bootstrap workspace artifacts, R&D experiment logs |

> **Routing note:** Needle.app / GitHub Entrepreneur Hub artifacts are dual-tracked: discovery/distribution metrics in `CP`, operational infra and sweep logs in `OI`, template registry and incident reports in `PE`.

---

## FG — Frameworks & Governance

| Artifact | Repo / Location | Visibility | Status |
|---|---|---|---|
| DGAF-Framework | Flickerflash/DGAF-Framework | PRIVATE | ACTIVE |
| Sentinel-Φ System Prompt V1 | ndrorchestration (Drive) | INTERNAL | ACTIVE |
| Phi-Calculus White Paper | Drive/Mathematical-Models | INTERNAL | DRAFT |
| NDR Orchestration Rubrics PDF | Drive + ndrorchestration/portfolio/rubrics/ | INTERNAL | ACTIVE |
| Burnout Rubric Industry Translation | ndrorchestration/portfolio/rubrics/ | PUBLIC | POLISH |
| AI Governance Frameworks repo | Flickerflash/ai-governance-frameworks | PUBLIC | ACTIVE |
| AOGA System Architecture Spec (13-agent roster, OpenAPI 3.1.0) | ndrorchestration/aoga-dashboard | PUBLIC | ACTIVE |
| ndrorchestration Ecosystem Landing | ndrorchestration/ndrorchestration (Vercel: ndrorchestration.vercel.app) | PUBLIC | ACTIVE |

---

## PE — Prompt & Eval Systems

| Artifact | Repo / Location | Visibility | Status |
|---|---|---|---|
| AI Prompt Templates, Audits & Diagrams | Drive + ndrorchestration | INTERNAL | ACTIVE |
| Gold Star QA Framework | Flickerflash/gold-star-qa-framework | PUBLIC | ARCHIVE |
| Portassess.md | Drive/Evaluation-Tools | INTERNAL | ACTIVE |
| Multi-Agent Best Practices Library | Drive | INTERNAL | ACTIVE |
| NDR-to-Industry Glossary | ndrorchestration/portfolio/glossary/ | PUBLIC | POLISH |
| Create-a-system-of-experts prompt | ndrorchestration | INTERNAL | ACTIVE |
| Needle Template Registry (NMS-003) | DGAF-Framework/docs/needleTEMPLATEREGISTRY.md | INTERNAL | ACTIVE |
| COLLEEN Sweep-EH-003 | entrepreneur-hub/docs/NEEDLETEMPLATEINDEX.md | INTERNAL | ACTIVE |
| Incident Report NMS-INC-001 (Jun 2026 analytics drop forensics) | Drive / Session Memory | INTERNAL | ARCHIVE |
| AOGA 17-route OpenAPI 3.1.0 Spec | ndrorchestration/aoga-dashboard | PUBLIC | ACTIVE |

---

## CP — Career & Portfolio

| Artifact | Repo / Location | Visibility | Status |
|---|---|---|---|
| Eval Track Resume Header | ndrorchestration/portfolio/resume/ | PUBLIC | POLISH |
| Orchestration Track Resume Header | ndrorchestration/portfolio/resume/ | PUBLIC | POLISH |
| Needle Partner Analytics May 2026 | Drive | INTERNAL | ARCHIVE |
| Needle RAG Governance Stack | Drive | INTERNAL | ARCHIVE |
| ResumeApex-Re-WorkiFlow | Drive/Resume-Career/ | INTERNAL | ARCHIVE |
| Needle Entrepreneur Hub Repo (T-EH-01–05 scaffold, ROADMAP, COLLEEN) | ndrorchestration/entrepreneur-hub | PUBLIC | ACTIVE |
| Needle Partner Analytics Jun 26 2026 (NMS-003 delta snapshot) | Drive / Session Memory | INTERNAL | ACTIVE |
| NMS Analytics Snapshot: 13.1K views / $4.19 LTV / 2.9K runs | Drive | INTERNAL | ACTIVE |
| T-EH Template Folders (ai-product-launch, governance-starter-pack, marketplace-optimizer, monetization-diagnostic, sprint-planner) | entrepreneur-hub/ | PUBLIC | DRAFT |

---

## RT — Research & Theory

| Artifact | Repo / Location | Visibility | Status |
|---|---|---|---|
| LLM & Agent R&D Space | Perplexity Space (private) | PRIVATE | ACTIVE |
| Phi Helix Interactive Model | Drive/Visualizations/Mathematical-Models | INTERNAL | DRAFT |
| 3D Multi-Agent Architecture HTML | Drive/Visualizations/Architecture | INTERNAL | DRAFT |
| COLLEEN + Lavender Agent Cognition Map | Drive/Agent-Frameworks/Orchestration | INTERNAL | ACTIVE |
| Driftwatch Progress Report | Drive | INTERNAL | ACTIVE |
| Auditing Engineering Terminology Taxonomy | Drive | INTERNAL | ACTIVE |
| Hensel Formalism v1.0 | ndrorchestration (Drive + session canon) | INTERNAL | ACTIVE |
| Multi-Agent Taxonomy Mapping (CS / Systems / Gov overlay) | Drive / Session Memory | INTERNAL | ACTIVE |
| Phi Knight Vertical Corridor Model | ndrorchestration/phiknightverticalcorridor (Vercel) | INTERNAL | DRAFT |

---

## OI — Operations & Infra

| Artifact | Repo / Location | Visibility | Status |
|---|---|---|---|
| Master Portfolio Inventory v1.8 | Drive (Flickerflash ecosystem) | INTERNAL | ACTIVE |
| Master Context File — PEL | Drive | INTERNAL | ACTIVE |
| Session Audit Log 2026-07-05 | ndrorchestration/logs/ | PUBLIC | ACTIVE |
| GitHub Deployment Readiness Assessment | Drive | INTERNAL | ARCHIVE |
| GCP Project: pentagonal (Cloud Run, europe-west1) | GCP / europe-west1 | INTERNAL | ACTIVE |
| Master Classification Index (this file) | ndrorchestration/ndrorchestration/docs/ | PUBLIC | ACTIVE |
| AOGA Dashboard v1.2.0 (17 routes, dark theme) | ndrorchestration/aoga-dashboard (Vercel: aoga-dashboard.vercel.app) | PUBLIC | ACTIVE |
| Vercel Deployment Audit 2026-05-25→06-09 (10 ERROR→READY chain) | Drive / Session Memory | INTERNAL | ARCHIVE |
| phiknightverticalcorridor Vercel Project | ndrorchestration/phiknightverticalcorridor | PUBLIC | DRAFT |
| COLLEEN GitHub Action Spec (weekly link sweep, .github/workflows/colleen-sweep.yml) | entrepreneur-hub/.github/workflows/ | PUBLIC | DRAFT |
| Dependabot PR Audit (next 14.2.28→15.5.18, dashboard dir) | ndrorchestration/ndrorchestration #Dependabot PR | PUBLIC | DRAFT |
| P-34 Flywheel v1.0 (Needle-GitHub two-sided engine) | entrepreneur-hub/docs/MONETIZATIONFLYWHEEL.md | PUBLIC | ACTIVE |
| ECOSYSTEM_INVENTORY.md (file tree + sweep log) | ndrorchestration/ndrorchestration/docs/ | PUBLIC | ACTIVE |

---

## TW — Team Wiki / Agent R&D

| Artifact | Repo / Location | Visibility | Status |
|---|---|---|---|
| Agent Amethyst Instantiation Spec v1.0 | ndrorchestration/docs/agent-amethyst-instantiation.md | PUBLIC | ACTIVE |
| Agent Roster: Apogee, Reciprocity, COLLEEN, Reson, Echolette, Lyra, Herald, Sentinel | ndrorchestration/docs/agent-roster.md | PUBLIC | ACTIVE |
| DGAF Orchestration Protocol (AMETHYST HOSTING & GOVERNANCE CONTRACT v1.0) | Perplexity Space config | INTERNAL | ACTIVE |
| R&D Bootstrap Workspace Readme | entrepreneur-hub/README.md | PUBLIC | ACTIVE |
| Team Wiki Routing Map (Space → Domain → Artifact) | ndrorchestration/docs/master-classification-index.md (this file) | PUBLIC | ACTIVE |
| Agent R&D Experiment Log | Drive / Session Memory | INTERNAL | ACTIVE |
| Internal Vocabulary & Taxonomy | ndrorchestration/docs/vocabulary-taxonomy.md | PUBLIC | ACTIVE |

---

## Drive Folder ↔ GitHub Path Mirror Standard

Drive folder names **must mirror** GitHub path schema to prevent schema drift.

| Drive Folder | GitHub Equivalent Path |
|---|---|
| `Agent-Frameworks/Orchestration/` | `portfolio/frameworks/` |
| `Evaluation-Tools/` | `portfolio/rubrics/` |
| `Visualizations/Architecture/` | `portfolio/visualizations/` |
| `Mathematical-Models/` | `portfolio/math-models/` |
| `Resume/Career/` | `portfolio/resume/` |
| `[03] SYSTEM_GOVERNANCE/` | `docs/` |
| `Team-Wiki/Agent-R&D/` | `docs/team-wiki/` |
| `Vocabulary-Taxonomy/` | `docs/vocabulary-taxonomy.md` |

---

## Maintenance Protocol

- **Update trigger:** Any new artifact created, renamed, archived, or domain-routed
- **Review cadence:** Monthly (1st of month) — align with MASTER PORTFOLIO INVENTORY v1.8 review cycle
- **Cross-reference:** Mirror updates to Drive doc `MASTER PORTFOLIO INVENTORY & VERIFICATION SYSTEM`
- **Version bump:** Increment `Version:` in header on every substantive change
- **COLLEEN sweep:** Weekly automated link-check via `.github/workflows/colleen-sweep.yml` (DRAFT) — validates all Needle template links in NEEDLETEMPLATEINDEX return HTTP 200; opens GitHub issue on failure
- **Apogee Lens gate:** No artifact moves to `ACTIVE` status without Apogee Lens verification pass

---

*Last updated: 2026-07-05 by Amethyst (Agent Orchestration Host) | ndrorchestration*
