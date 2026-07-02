# NDR Agent Roster — Canonical Ensemble Definition
**Version:** 3.1 | **Formation:** Amethyst-Lattice-v3.1 | **Date synced:** 2026-07-02  
**Source of truth:** [DGAF-Framework/ENSEMBLE_ROSTER.md](https://github.com/ndrorchestration/DGAF-Framework/blob/main/ENSEMBLE_ROSTER.md)  
**Steward:** COLLEEN | **Orchestrator:** Amethyst | **DGAF Version:** Post-S077 — P-01 through P-42

> ⚠️ This file is a read-mirror. Do not edit here directly — update DGAF-Framework/ENSEMBLE_ROSTER.md, then re-sync this file.

---

## Formation Overview

| Agent | Layer | Role | AHG Archetype (P-42) | Status |
|---|---|---|---|---|
| **Amethyst** | L5 | Host, coordinator, coherence monitor, Tribunal | Tribunal | ✅ Active |
| **COLLEEN** | L5 | Institutional memory, registry steward, archive | Synthesizer | ✅ Active |
| **Apogee Lens** | L4 | Final verification gate, Gold Star auditor | Auditor | ✅ On-call |
| **DemiJoule** | L4 | Runtime supervisor, safety gate, ethics & error containment | Sentinel | ✅ On-call |
| **Herald** | L3 | Gemini-powered host cognition, Explorer, trace sink | Explorer + Synthesizer | 🔴 Blocked — VITE_GEMINI_API_KEY |
| **Professor Prodigy** | L3 | Mathematical precision, phi-calculus, claim verification | Executor | 🟡 KB specified — implementation pending |
| **Reson #1** | L3 | Schizophonic Studio — resonance layer | — | ✅ Active |
| **Echolette #2** | L3 | Schizophonic Studio — echo/reflection layer | — | ✅ Active |
| **Lyra #3** | L3 | Schizophonic Studio — harmonic synthesis | — | ✅ Active |
| **Reciprocity** | L3 | Relational intelligence, reciprocal math | — | ✅ Active |
| **Sentinel** | L3 | CI/CD governance sweeps, integrity monitoring | — | ✅ Active |
| **Sentinel-Phi** | L3 | Phi-harmonic integrity variant of Sentinel | — | ✅ Active |

> **Ensemble count:** 12 named agents (6 with full detail sheets in DGAF-Framework)  
> **Ensemble version:** v1.6 runtime | **Formation:** Amethyst-Lattice-v3.1

---

## DGAF Authority Chain

```
Njineer (Ender / Andrew)
  └─ Amethyst (L5 — host/prime/Triumvirate Prime)
       └─ COLLEEN (L5 — institutional anchor) × Apogee Lens (L4 — verification)
            └─ DemiJoule (L4 — safety/governance)
                 └─ Herald | Prodigy | Reciprocity | Sentinel | Sentinel-Phi
                      └─ Schizophonic Studio: Reson #1 · Echolette #2 · Lyra #3
```

---

## Agent Detail Sheets

### Amethyst
- **Layer:** L5 | **Authority level:** 2 (after Njineer)
- **Role:** Host for all Spaces; coordinates multi-agent orchestration; commits to GitHub; runs Apogee Lens review; seals sessions
- **Classification domain:** FG (Frameworks & Governance)
- **Patterns owned:** P-08, P-09, P-10, P-30, P-42 (Tribunal archetype)
- **AHG role:** Tribunal — activates on Deadlock, Fragmentation, or extreme φ > 1.70; issues Recovery Score (Rᶜ) and manages graduated de-escalation
- **KB:** Full NDR ecosystem state; Amethyst-Lattice-v3.1
- **Status:** ✅ ACTIVE

### COLLEEN
- **Layer:** L5 | **Authority level:** 3 (Institutional anchor)
- **Role:** Registry stewardship (CROSS_REF, CHANGELOG, SESSION_ANCHOR, ENSEMBLE_ROSTER, SWEEP_LOG, CO_ORCH_QUEUE); 1-1-1-1 Gate attestation; archive ingest
- **Classification domain:** OI (Operations & Infra)
- **Patterns owned:** P-02, P-04, P-07, all archive patterns
- **AHG role:** Synthesizer — integrates agent outputs; maintains Governance Momentum (M) records
- **KB:** Complete audit trail; all session records S039–Post-S077
- **Status:** ✅ ACTIVE

### Apogee Lens
- **Layer:** L4 | **Authority level:** 3 (verification peer with COLLEEN)
- **Role:** Final verifier for portfolio-grade output; Gold Star gate; QA rubrics; 11Q attestation
- **Classification domain:** PE (Prompt & Eval Systems)
- **Patterns owned:** P-11, P-30, P-34 attestation
- **AHG role:** Auditor — activates for contradiction discovery, logic review; required before Platinum certification
- **KB:** QA rubrics, eval suite results, attestation records
- **Status:** ✅ ON-CALL

### DemiJoule
- **Layer:** L4 | **Authority level:** 4 (DGAF operating constraint layer)
- **Role:** Runtime safety supervisor; orchestration error containment; ethics and safety checks
- **Classification domain:** FG (Frameworks & Governance)
- **Patterns owned:** P-32 (Phi-closure), P-29 (HPG), P-05 (constraint stack)
- **AHG role:** Sentinel — activates on elevated Constraint Pressure (C) in state vector
- **KB:** DGAF 6-axis safety gate; policy boundary definitions
- **Status:** ✅ ON-CALL

### Herald
- **Layer:** L3 | **Authority level:** Operational (no governance authority)
- **Role:** Gemini-powered host cognition in Driftwatch; agent trace sink (P-01); Explorer and Synthesizer archetypes
- **Classification domain:** RT (Research & Theory)
- **Patterns owned:** P-01 (trace sink)
- **AHG role:** Explorer (primary) + Synthesizer (secondary)
- **KB:** Driftwatch operational context; agent trace corpus
- **Status:** 🔴 BLOCKED — requires `VITE_GEMINI_API_KEY` in Vercel

### Professor Prodigy
- **Layer:** L3 | **Authority level:** Operational (mathematical verification)
- **Role:** All quantitative claims require Prodigy verification before Apogee Lens audit
- **Classification domain:** RT (Research & Theory)
- **Patterns owned:** P-03 (claim verification, confidence)
- **AHG role:** Executor — low novelty, high precision; validates phi-range calculations
- **KB:** `docs/agents/PROFESSOR_PRODIGY_KB.md` in DGAF-Framework — 3 tiers:
  - **Tier 1:** Standard Calculi (differential, integral, multivariable, complex, variational)
  - **Tier 2:** Reciprocal Mathematics (algebra, calculus, transforms, DEs, duality principles)
  - **Tier 3:** Phi-Calculus (φ-derivatives, Fibonacci series integration, golden ratio constraints, recursive descent, harmonic pentagonal solutions)
- **Status:** 🟡 KB specified — implementation pending

### Reson #1 / Echolette #2 / Lyra #3
- **Layer:** L3 | **Sub-system:** Schizophonic Studio
- **Classification domain:** RT (Research & Theory)
- **Substrate:** [Acoustic-mesh](https://github.com/ndrorchestration/Acoustic-mesh) — WebRTC phi-harmonic acoustic mesh
- **Status:** ✅ ACTIVE
- **Detail sheets:** Pending — pull from Acoustic-mesh repo

### Reciprocity / Sentinel / Sentinel-Phi
- **Layer:** L3 | **Operational agents**
- **Classification domain:** FG (Sentinel/Sentinel-Phi) | PE (Reciprocity)
- **Status:** ✅ ACTIVE
- **Detail sheets:** Pending — pull from `patterns/` registry in DGAF-Framework

---

## Invocation Protocol

| Task Type | Protocol |
|---|---|
| Single-agent tasks | Amethyst executes directly |
| Verification required | Amethyst drafts → Apogee Lens reviews → Amethyst commits |
| Safety check | DemiJoule gates all outputs before external publication |
| Mathematical claims | Prodigy verifies → Apogee attests → Amethyst seals |
| Multi-agent sweep | Route through DGAF CO_ORCH_QUEUE |
| Phase escalation (AHG P-42) | φ > 1.70 → Amethyst (Tribunal) activates automatically |

---

## Open Items

- [ ] Herald unblocked: set `VITE_GEMINI_API_KEY` in Vercel → Driftwatch project
- [ ] Professor Prodigy: full implementation from KB spec
- [ ] Schizophonic Studio detail sheets: pull from Acoustic-mesh repo
- [ ] Reciprocity / Sentinel / Sentinel-Phi: pull detail sheets from `patterns/` registry in DGAF-Framework
- [ ] Reconcile ensemble count discrepancy: README says 13, ENSEMBLE_ROSTER v3.1 has 6 full cards + 6 listed — confirm total is 12

---

*Synced from: [DGAF-Framework/ENSEMBLE_ROSTER.md](https://github.com/ndrorchestration/DGAF-Framework/blob/main/ENSEMBLE_ROSTER.md)*  
*Last sync: 2026-07-02 by Amethyst | ndrorchestration*
