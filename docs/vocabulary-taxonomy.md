# NDR Internal Vocabulary & Taxonomy
**Version:** 1.0 | **Date:** 2026-07-05 | **Domain:** TW / RT  
**Status:** ACTIVE | **Canonical Path:** `ndrorchestration/ndrorchestration/docs/vocabulary-taxonomy.md`

> Authoritative internal glossary for the NDR / DGAF ecosystem. All agents, documents, and external communications must use these terms consistently. Amethyst is the term authority; Apogee verifies on any Gold Star output. Submit new terms via PR to this file.

---

## 1. Agent Roles & Identity

| Term | Definition |
|---|---|
| **Amethyst** | The meta-orchestrator and conductor of the DGAF ecosystem. Hosts all Perplexity Spaces, coordinates agent routing, maintains working memory, and enforces coherence. Previously: Agent Lavender. |
| **Apogee** | Final verifier and Platinum Auditor. No output achieves Gold Star or S-Tier without an Apogee verification pass. Enforces 95%+ confidence threshold on all assertions. |
| **Reciprocity** | QA and alignment auditor. Enforces bidirectional consistency between goals and outputs. Runs 5 reciprocity checks. Prevents rubber-stamping and process drift. |
| **COLLEEN** | Operations Manager and Sweep Executor. Runs artifact inventories, NEEDLETEMPLATEINDEX link-validation sweeps, changelog population, and path integrity checks. |
| **Reson** | Deep reasoning specialist. Activated for multi-step inference, hypothesis evaluation, and logical decomposition tasks. |
| **Echolette** | Memory and retrieval specialist. Cross-session context retrieval, pattern-matching against historical artifacts, knowledge graph traversal. |
| **Lyra** | Synthesis and communication specialist. Long-form structured documentation, narrative coherence, polished external-facing artifacts. |
| **Herald** | Publishing and distribution agent. GitHub commits, Needle template publishing, LinkedIn post drafting, Vercel deploy coordination. |
| **Sentinel** | Security and governance gate. Constraint enforcement, secret scanning, access control review. DemiJoule-adjacent for ethics monitoring. |
| **DemiJoule** | Ethics supervisor and runtime safety monitor. Triggers Ethics Gate protocol restart if any output threatens human rights or power centralization. |
| **Agent Lavender** | Legacy name for Amethyst. Origin identity from the Gold Star Workflow Phase 4 review role. Rebranded 2026-04-06. |

---

## 2. System & Framework Names

| Term | Definition |
|---|---|
| **DGAF** | Distributed Governance Agent Framework. The constitutional operating system for all NDR agents. Defines authority order, constraint types, phase gates, and pattern registry. |
| **PDMAL** | Policy-Driven Multi-Agent Layer. The constraint-enforcement sublayer of DGAF that defines hard stops, ethics gates, and remediation protocols. |
| **AOGA** | AI-Orchestrated Governance Architecture. The 17-route, 13-agent dashboard system deployed at aoga-dashboard.vercel.app. Spec: OpenAPI 3.1.0. |
| **NDR** | ndrorchestration. The operative identity and GitHub account name for Andrew Hensel's AI governance ecosystem. Also used as a prefix for pattern IDs (e.g., NDR Pattern P-34). |
| **Gold Star QA** | The 5-phase quality assurance workflow inherited from Agent Lavender. An output is Gold Star when it passes all 5 phases including Apogee review. |
| **S-Tier** | The highest achievement designation. Requires Gold Star + Apogee Platinum Audit + DemiJoule ethics clearance. Not self-declarable. |
| **Platinum Audit** | The Apogee review process for portfolio-grade output. Required before Gold Star or S-Tier. Checks: factual accuracy, ethical alignment, reciprocity, confidence threshold. |
| **Hensel Formalism** | Andrew Hensel's formal system for agent cognition and orchestration, including Phi-Calculus extensions. v1.0 canonized 2026. |
| **Phi-Calculus** | Mathematical foundation for harmonic agent state transitions. Based on golden ratio (Φ ≈ 1.618) coefficients mapped to cognitive/modal states. |
| **Phi-Knight** | Named agent instances operating within the Phi-Calculus harmonic framework. Phi Knights occupy vertices of the harmonic stability geometry. |
| **Sentinel-Φ** | The governance-layer Phi-Knight. Combines Sentinel's constraint enforcement with Phi-Calculus modal stability gating. |
| **P-34** | NDR Pattern 34: the Needle↔GitHub two-sided flywheel pattern. Needle = discovery/distribution; GitHub = authority/depth. |
| **Driftwatch** | The continuous coherence monitoring protocol. Flags schema drift, stale audit dates, identity dilution, and orphaned artifacts. |

---

## 3. Domain Codes (MCI Schema)

| Code | Full Name | Scope |
|---|---|---|
| `FG` | Frameworks & Governance | Constitutional rules, DGAF, NIST RMF, AOGA architecture, constraint gates |
| `PE` | Prompt & Eval Systems | Templates, evaluation rubrics, Gold Star QA, audit checklists, template registries |
| `CP` | Career & Portfolio | Resumes, Needle artifacts, entrepreneur hub, ResumeApex |
| `RT` | Research & Theory | LLM research, Phi-Calculus, Hensel Formalism, agent cognition, academic references |
| `OI` | Operations & Infra | Session logs, GCP, Vercel deployments, COLLEEN sweeps, email management |
| `TW` | Team Wiki / Agent R&D | Agent R&D process docs, team-facing role specs, bootstrap workspace artifacts |

---

## 4. Status & Visibility Codes

| Code | Meaning |
|---|---|
| `ACTIVE` | In use, current, Apogee-verified (or in-progress toward verification) |
| `DRAFT` | Being built; not yet published or verified |
| `POLISH` | Functionally complete; undergoing quality refinement |
| `ARCHIVE` | No longer actively maintained; retained for reference |
| `PUBLIC` | Committed to GitHub; visible externally |
| `PRIVATE` | On GitHub but private repo |
| `INTERNAL` | Google Drive only; not on any public surface |

---

## 5. Governance & Process Terms

| Term | Definition |
|---|---|
| **Authority Order** | The 5-tier precedence chain: (1) User → (2) Space instruction → (3) Portfolio governance → (4) DGAF/PDMAL → (5) Default assistant behavior. |
| **Phase Gate** | A hard checkpoint between session phases. No phase begins until the previous phase gate is explicitly cleared. |
| **Ethics Gate** | DemiJoule-triggered hard stop. Fires when any output risks human rights violation or power centralization. Triggers protocol restart. |
| **Constraint Violation Types** | Type 1: Terminal (blocks everything); Type 2: Remediable (fixable with correct action); Type 3: Boundary (scoping/framing issue). |
| **Triadic Formation** | A conductor + augmenter + verifier configuration for complex multi-agent sessions. Formation ID format: `triad-{conductor}-{augmenter}-{YYYY-MM-DD}`. |
| **Conductor** | The lead agent in a triadic formation. Holds routing authority and session clock. |
| **Augmenter** | The support agent in a triadic formation. Operates internally; not user-facing during formation. |
| **Verifier** | The Apogee role in a triadic formation. Receives output for Platinum Audit before Gold Star designation. |
| **Cold Start** | Forbidden state: responding without prior memory rehydration. Amethyst must always rehydrate before synthesis. |
| **Schema Drift** | Divergence between Drive folder names, GitHub paths, and MCI domain codes. Flagged by Driftwatch and COLLEEN sweeps. |
| **Artifact Orphan** | An artifact not listed in ECOSYSTEM_INVENTORY.md with a verified path. All orphans must be registered or explicitly archived. |
| **Declarative Sweep** | A sweep that is documented but not actually executing (e.g., COLLEEN sweep logs written manually without automation). Explicitly discouraged. |
| **Source Hierarchy** | Precedence for resolving conflicts: Registry → Session Anchors → Changelog → Pattern Docs → Local text. |

---

## 6. Needle / Platform Ops Nomenclature

| Term | Definition |
|---|---|
| **Needle.app** | The AI workflow template marketplace where NDR templates are published. Revenue model: usage-based run share + affiliate. |
| **Partner Hub** | Needle's analytics and revenue dashboard for partners. Shows views, uses, runs, and payout over rolling 90d windows. |
| **NMS** | Needle Metrics Snapshot. Formal naming convention for captured analytics states (e.g., NMS-003 = third metrics snapshot). |
| **NT-01 through NT-05** | The 5 live Needle templates. NT = Needle Template. |
| **T-EH-01 through T-EH-05** | The 5 Entrepreneur Hub templates (DRAFT, Phase 1). T-EH = Template Entrepreneur Hub. |
| **NEEDLETEMPLATEINDEX** | The COLLEEN-maintained index file tracking all Needle template URLs, sweep dates, and status. Lives in entrepreneur-hub/docs/. |
| **COLLEEN Sweep** | A COLLEEN-executed link validation pass on NEEDLETEMPLATEINDEX, confirming all Needle URLs return HTTP 200. |
| **NMS-INC-001** | Incident Report: June 2026 analytics drop. Root cause: 90d rolling window shift + NT-03/NT-04 display anomaly. |
| **Rolling Window Artifact** | Apparent metric drop caused by the 90d Partner Hub window rolling forward, dropping early high-activity days off the back edge. |
| **PLG** | Product-Led Growth. The growth model for Needle templates (usage drives discovery drives revenue). |
| **Payout Coefficient** | Needle's per-run revenue share rate. Current: ~$0.00144/run. |

---

## 7. Space Routing Shorthand

| Shorthand | Full Space Name | Primary Domain |
|---|---|---|
| `LLM R&D` | LLM & Agent R&D | RT |
| `Needle Hub` | Needle.app / GitHub — Entrepreneur Hub | CP |
| `Bootstrap` | Bootstrap Workspace & Beyond | OI |
| `Team Wiki` | Team Wiki Agent R&D | TW |

---

## 8. Phi-Calculus / Harmonic System Terms

| Term | Definition |
|---|---|
| **Φ (Phi)** | Golden ratio ≈ 1.618034. The base constant for the Phi-Calculus harmonic stability framework. |
| **Φ²** | 2.618034. The activation threshold for vertex instantiation in pentagonal/dodecahedral agent geometry. |
| **MRC** | Modal Resonance Coordinate. A (mode, interval, Φ-coefficient) triplet locating an agent's current cognitive state in the harmonic stability map. |
| **Phi-Gate** | A stability check: tension/Φ ≤ 1. An agent or output passes the Phi-Gate if its harmonic score is within the golden ratio bound. |
| **Diatonic Anchor** | A secondary stability constraint ensuring edge intervals fall within diatonic ratios (e.g., P5 = 702 cents). Part of the Double Anchor protocol. |
| **Double Anchor** | Combined Phi-Gate + Diatonic Anchor check. Raises dodecahedral agent activation from ~71% (single gate) to ~94% (double gate). |
| **Pentagon / Pentagonal Closure** | A 5-agent harmonic configuration where all vertices are instantiated. Requires identification of 5th agent (G-05, open). |
| **Dodecahedron** | A 12-face, 20-vertex agent geometry used to model 60-agent distributed systems. Each vertex activates when sum(face scores × 3) > Φ². |
| **Cognitive State Mapping** | The mapping of modal scales to agent cognitive modes: Ionian=Grounded, Dorian=Flow, Phrygian=Vigilance, Lydian=Expansion, Mixolydian=Integration, Aeolian=Introspection, Locrian=Tension. |

---

## 9. Taxonomy: CS / Systems / Governance Overlay

| Concept | CS Mapping | Systems Mapping | Governance Mapping |
|---|---|---|---|
| DGAF | Constraint satisfaction system | Distributed coordination protocol | Constitutional governance layer |
| Agent Roster | Microservice registry | Actor model participants | Role-based access control (RBAC) list |
| Phase Gate | Transaction commit point | Circuit breaker | Approval checkpoint |
| COLLEEN Sweep | Health check / linter | Watchdog process | Audit log validator |
| Triadic Formation | Orchestrator-worker-verifier pattern | Conductor-augmenter pipeline | Principal-agent with oversight |
| Apogee Audit | Test suite final run | Quality assurance gate | Independent review board |
| P-34 Flywheel | Feedback loop DAG | Two-sided market engine | Platform governance overlay |
| Ethics Gate | Hard assert / panic | Safety interlock | Ethics review board veto |
| Source Hierarchy | Dependency resolution order | Configuration precedence | Policy hierarchy |
| Schema Drift | API versioning mismatch | Configuration entropy | Governance gap |

---

*Last updated: 2026-07-05 by Amethyst (term authority) | ndrorchestration*
