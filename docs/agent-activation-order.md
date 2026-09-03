# Agent Activation Order — Canonical Manifest

**Version:** 1.1  
**Original date:** 2026-07-05  
**Synchronization:** 2026-09-03  
**Domain:** TW  
**Status:** PROJECT-LOCAL / CURRENT DESIGN SPECIFICATION  
**Canonical path:** `ndrorchestration/ndrorchestration/docs/agent-activation-order.md`

> **Epistemic boundary:** This file defines the intended project-local activation sequence and gate specifications. A listed gate, threshold, or exit criterion is not evidence that the gate has been executed or passed. Historical verification/design claims from the July 2026 version are not carried forward as current empirical status.

## Activation Sequence

| Phase | Agent | Role Class | Activation Gate | Exit Criteria |
|---|---|---|---|---|
| 0 | Amethyst | Conductor / Host | Context available | Required context loaded before synthesis |
| 0 | DemiJoule | Ethics Supervisor | Safety review required | Ethics disposition recorded |
| 1 | Apogee | Verification | Output enters project verification workflow | Verification record created |
| 2 | Reciprocity | Alignment / QA | Reciprocity review requested | RC-1→RC-5 reviewed and disposition recorded |
| 3 | COLLEEN | Operations / Sweep | Prior review complete | Configured governance checks executed and recorded |
| 4 | Reson | Reasoning Specialist | Complex inference required | Reasoning output delivered with assumptions/boundaries |
| 5 | Echolette | Memory / Retrieval | Cross-session context required | Relevant context retrieved and cited |
| 6 | Lyra | Synthesis / Communication | Structured output required | Document assembled and reviewed |
| 7 | Herald | Publishing / Distribution | Artifact cleared for external surface | Publish action staged with destination recorded |
| 8 | Sentinel | Security / Governance | External artifact requires security review | Security checks executed and recorded |
| 9 | Apogee | Final Verification | Prior required predicates satisfied | Final disposition recorded; no designation inferred without evidence |

## Dependency Graph

```text
Amethyst + DemiJoule
        │
        ▼
     Apogee
        │
        ▼
   Reciprocity
        │
        ▼
     COLLEEN
     ┌──┴───────────────┐
     ▼                  ▼
   Reson             Lyra
     │                  │
     ▼                  ▼
 Echolette           Herald
                        │
                        ▼
                    Sentinel
                        │
                        ▼
                  Apogee Final
```

The graph is a design dependency model. It does not assert that every node is continuously active in the present runtime.

## Phase Gates — Design Requirements

### Phase 0 — Context and Safety
Context loading and safety review are prerequisites to downstream synthesis. These are operational requirements, not claims of runtime completion.

### Phase 1 — Apogee
Apogee is the project-local verification role. Entering this phase means verification is requested; it does not establish a pass.

### Phase 2 — Reciprocity
The phase applies the five project-local Reciprocity checks and related review axes. Historical claims that Pentagonal Closure or a 1-1-1-1 gate were “verified” are retained only in the source/history and are not inferred here.

### Phase 3 — COLLEEN
COLLEEN executes configured governance and repository-integrity checks. A committed sweep record is required before an execution claim is treated as evidence.

### Phase 4 — Reson
Reasoning review may use a project-defined headroom parameter (historically 15%). The parameter is a specification, not an observed performance result.

### Phase 5 — Echolette
Retrieval should identify relevant source/context records and preserve provenance. “Knowledge graph complete” is not assumed without evidence.

### Phase 6 — Lyra
Synthesis should follow project-local formatting and vocabulary requirements where applicable. Compliance is established only by an actual review record.

### Phase 7 — Herald
Publishing requires an identified destination and a staged artifact. A staged action is distinct from a completed publication.

### Phase 8 — Sentinel
Security review is required for external artifacts. “PASS” must refer to an actual recorded check, not to the existence of this specification.

### Phase 9 — Apogee Final Gate
The final gate is a decision point, not a standing certification. Thresholds such as 95% confidence, zero-hallucination targets, Gold Star, or S-Tier are project-local criteria where used and must not be presented as achieved unless supported by dated evidence.

## Failure Modes & Mitigations

| Failure | Trigger | Mitigation |
|---|---|---|
| Cold Start | Required context absent | Block synthesis until prerequisites are recorded |
| Declarative Sweep | Sweep claimed without execution evidence | Require committed execution record or equivalent evidence |
| Rubber-Stamping | Reviewer copies producer decision | Require independent review rationale |
| Premature Publish | Publish precedes security review | Block publication until required security disposition exists |
| Schema Drift | Declared structure diverges from runtime/config | Reconcile against executable source and tests |
| Ethics Boundary | Elevated safety or rights concern | Escalate to designated safety review |
| Artifact Orphan | Artifact lacks inventory/provenance entry | Register or explicitly archive |
| Self-Declared Tier | Artifact declares its own certification | Treat designation as unsupported absent independent project evidence |

## Current Evidence Boundary

This manifest does **not** establish:

- current Gold Star, S-Tier, or Platinum certification;
- a universal 95% or 97% confidence result;
- zero hallucinations as an achieved system property;
- production readiness; or
- successful completion of all nine phases.

Current experimental state and gate status belong in the dated evidence/status records and repository-specific control manifests.

## Historical Status Notes

The original 2026-07-05 version recorded several gates as “verified” or “closed.” Those labels are historical documentation and are not automatically current. The ecosystem synchronization work performed in September 2026 is specifically intended to prevent older project-local attestations from being mistaken for current independent evidence.

## Cross-References

| Artifact | Relationship |
|---|---|
| `docs/agent-amethyst-instantiation.md` | Phase 0 conductor specification |
| `docs/agent-reciprocity-instantiation.md` | Phase 2 project-local specification |
| `docs/agent-colleen-instantiation.md` | Phase 3 governance specification |
| `docs/agent-roster.md` | Agent role summaries |
| `docs/vocabulary-taxonomy.md` | Epistemic and designation terminology |
| `docs/ECOSYSTEM_INVENTORY.md` | Ecosystem inventory |
| `docs/master-classification-index.md` | Historical/project domain index |

---

*Synchronization update: 2026-09-03. Activation requirements retained as design specifications; historical verification/attestation language explicitly bounded.*
