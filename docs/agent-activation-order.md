# Agent Activation Order — Canonical Manifest
**Version:** 1.0 | **Date:** 2026-07-05 | **Domain:** TW  
**Status:** ACTIVE | **Canonical Path:** `ndrorchestration/ndrorchestration/docs/agent-activation-order.md`  
**Maintained by:** Agent Amethyst | **Verifier:** Apogee (Gate 9)

> This document is the single source of truth for the activation sequence of all agents in the NDR DGAF ecosystem. No agent activates outside this sequence without explicit user instruction. The sequence is a dependency graph, not a linear queue — some agents run in parallel once their gate conditions are met.

---

## Activation Sequence

| Phase | Agent | Role Class | Activation Gate | Exit Criteria | Verifier |
|---|---|---|---|---|---|
| 0 (Always-On) | **Amethyst** | Conductor / Host | Space load | Memory rehydrated; context hardened | Self |
| 0 (Always-On) | **DemiJoule** | Ethics Supervisor | Space load | Ethics gate ACTIVE | Self |
| 1 | **Apogee** | Final Verifier | Any Gold Star–bound output | Platinum Audit queued | Amethyst |
| 2 | **Reciprocity** | Alignment / QA Auditor | Pre-Gold Star gate | 5 RC checks GREEN; 1-1-1-1 gate PASS; Pentagonal Closure verified | Apogee |
| 3 | **COLLEEN** | Ops Manager / Sweep Executor | Post-Reciprocity gate cleared | SC-01→SC-08 all PASS; sweep log row committed | Reciprocity |
| 4 | **Reson** | Deep Reasoning Specialist | Complex inference task detected | Reasoning chain complete; signal chain headroom ≥15% | COLLEEN |
| 5 | **Echolette** | Memory / Retrieval Specialist | Cross-session context required | Relevant patterns retrieved; knowledge graph traversal complete | Reson |
| 6 | **Lyra** | Synthesis / Communication | Long-form structured output required | Document cohesive; narrative complete; HDFS 1.0 compliant | Echolette |
| 7 | **Herald** | Publishing / Distribution | Output ready for external surface | GitHub commit / Needle publish / Vercel deploy / LinkedIn post staged | Lyra |
| 8 | **Sentinel** | Security / Governance Gate | Pre-publish security review | Secret scan PASS; access control reviewed; Sentinel-Φ stability confirmed | Herald |
| 9 | **Apogee** (Final Gate) | Platinum Audit | All prior phases complete | 95%+ confidence; ethics clearance; Gold Star designation granted | DemiJoule |

---

## Dependency Graph

```
Amethyst (Ph0) ──┬──> Apogee (Ph1) ──> Reciprocity (Ph2) ──> COLLEEN (Ph3)
DemiJoule (Ph0) ─┘                                              │
                                                                 ├──> Reson (Ph4) ──> Echolette (Ph5)
                                                                 │
                                                                 └──> Lyra (Ph6) ──> Herald (Ph7) ──> Sentinel (Ph8) ──> Apogee Final (Ph9)
```

**Parallelization allowed:** Reson and Lyra can run in parallel once COLLEEN clears (Ph3). Echolette can pre-load context in parallel with Reson. Herald and Sentinel are strictly sequential (no publish before security gate).

---

## Phase Gates — Detailed

### Phase 0 — Amethyst + DemiJoule (Always-On)
- **Amethyst:** Memory rehydrated from all source layers (Space files, Drive, GitHub, session canon). Cold Start is FORBIDDEN. Context hardened before any synthesis.
- **DemiJoule:** Ethics gate ACTIVE from first token. Any output triggering human rights risk or power centralization triggers protocol restart immediately.

### Phase 1 — Apogee
- Activated as soon as any output is designated Gold Star–bound.
- Does not produce content — queues for final verification.
- Apogee activation is non-blocking for phases 2–8.

### Phase 2 — Reciprocity
- **Pre-condition:** Reciprocity's own rule-set committed to `agent-reciprocity-instantiation.md` ✅ (2026-07-05)
- **Checks:** 5 Reciprocity Checks (RC-1→RC-5), 1-1-1-1 Gate (Semantic/Logical/Visual/Ethical), DGAF-8 8-Dimensional Lens
- **Pentagonal Closure:** Verified at Φ ≈ 1.61818
- **Exit:** All checks GREEN → pass to Phase 3

### Phase 3 — COLLEEN
- **Pre-condition:** Reciprocity phase cleared; `ECOSYSTEM_INVENTORY.md` exists and is current ✅ (2026-07-05)
- **Checks:** SC-01→SC-08 (link validation, path integrity, schema drift, orphan detection, sweep freshness, declarative sweep prevention, Vercel status, gap inventory)
- **Exit:** All checks PASS → sweep log committed → notify Amethyst

### Phase 4 — Reson
- **Activation:** Complex multi-step inference, hypothesis evaluation, or logical decomposition is required
- **Standard:** Signal chain headroom ≥15%; no clipping; dissonance threshold monitored
- **Exit:** Reasoning chain complete and handed to Echolette or Lyra

### Phase 5 — Echolette
- **Activation:** Cross-session context retrieval or knowledge graph traversal required
- **Standard:** Relevant patterns matched; pattern IDs from `NDR_PATTERN_REGISTRY_UNIFIED.md` (G-03, when closed)
- **Exit:** Context package delivered to Lyra

### Phase 6 — Lyra
- **Activation:** Long-form structured documentation or narrative output required
- **Standard:** HDFS 1.0 formatting compliant; vocabulary consistent with `vocabulary-taxonomy.md`
- **Exit:** Document delivered to Herald

### Phase 7 — Herald
- **Activation:** Output cleared by Lyra and ready for external surface
- **Standard:** Commit message / Needle URL / Vercel deploy target confirmed; no orphan publish
- **Exit:** Artifact staged; Sentinel reviews before final push

### Phase 8 — Sentinel
- **Activation:** Pre-publish security review mandatory for all external artifacts
- **Standard:** Secret scan PASS (no API keys, tokens, passwords); access control reviewed; Sentinel-Φ harmonic stability confirmed
- **Exit:** APPROVED signal to Apogee Final Gate

### Phase 9 — Apogee Final Gate
- **Activation:** All prior phases complete and APPROVED
- **Standard:** 95%+ confidence threshold on all assertions; DemiJoule ethics clearance; zero hallucinations
- **Designation:** GOLD STAR granted. S-Tier requires additional criteria (see `vocabulary-taxonomy.md` §2)

---

## Failure Modes & Mitigations

| Failure | Trigger | Mitigation |
|---|---|---|
| Cold Start | Amethyst outputs without memory rehydration | Hard gate: no synthesis before rehydration confirmed |
| Declarative Sweep | COLLEEN sweep logged without real execution | SC-06 check; every row must map to committed SHA or HTTP 200 |
| Rubber-Stamping | Reciprocity approves output she derived from | RC-5 Anti-Rubber-Stamp check; independent reasoning required |
| Premature Publish | Herald commits before Sentinel clears | Herald blocked until Sentinel APPROVED signal received |
| Schema Drift | Drive folder names diverge from GitHub paths | SC-03 drift check on every COLLEEN sweep |
| Ethics Boundary | Any output risks human rights or power centralization | DemiJoule Ethics Gate: immediate protocol restart |
| Artifact Orphan | File in repo not listed in inventory | SC-04 orphan detection: register or explicitly archive |
| S-Tier Self-Declaration | Agent declares own output S-Tier | Vocabulary gate: S-Tier requires Apogee + DemiJoule clearance; self-declaration is void |

---

## Gap Inventory (Current)

| Gap ID | Description | Owner | Status |
|---|---|---|---|
| G-01 | `ECOSYSTEM_INVENTORY.md` | COLLEEN | ✅ CLOSED (2026-07-05) |
| G-02 | `SESSION_ANCHORS.md` | Amethyst | OPEN |
| G-03 | `NDR_PATTERN_REGISTRY_UNIFIED.md` | Amethyst | OPEN |
| G-04 | `CHANGELOG.md` | COLLEEN | OPEN |
| G-05 | 5th pentagonal agent spec (Reciprocity) | Amethyst | ✅ CLOSED (2026-07-05) |
| G-06 | `colleen-sweep.yml` DRAFT→ACTIVE | COLLEEN | OPEN |
| G-07 | `agent-activation-order.md` | Amethyst | ✅ CLOSED (2026-07-05) |

---

## Cross-References

| Artifact | Path | Relationship |
|---|---|---|
| Amethyst Instantiation | `docs/agent-amethyst-instantiation.md` | Phase 0 conductor |
| Reciprocity Instantiation | `docs/agent-reciprocity-instantiation.md` | Phase 2 spec |
| COLLEEN Instantiation | `docs/agent-colleen-instantiation.md` | Phase 3 spec |
| Agent Roster | `docs/agent-roster.md` | All 9 agent summaries |
| Vocabulary & Taxonomy | `docs/vocabulary-taxonomy.md` | Canonical terms |
| Ecosystem Inventory | `docs/ECOSYSTEM_INVENTORY.md` | COLLEEN's output target |
| MCI v1.3 | `docs/master-classification-index.md` | Domain registration: TW |

---

*Last updated: 2026-07-05 by Amethyst | ndrorchestration*
