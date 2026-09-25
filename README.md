**Andrew Hensel // Ndr “Ender”**

### AI Systems Design · Evaluation · Agentic Governance · Provenance

I design and evaluate AI systems around a practical question:

> **What did the system actually do, what evidence supports that claim, and what is it authorized to do next?**

My work focuses on **AI evaluation, multi-agent systems, prompt engineering, provenance, reproducibility, and governance-aware orchestration**.

I’m especially interested in systems that keep **capability, evidence, verification, authority, and permission** distinct—so that producing an output is not automatically treated as proving a claim, passing evaluation, or earning authorization for the next action.

## Flagship: DGAF

### [DGAF-Framework](https://github.com/ndrorchestration/DGAF-Framework) — governance control plane for agentic systems

**Dynamic Governance Agentic Formation (DGAF)** is an experimental framework for governed multi-agent AI systems. It models capability, evidence, verification, authority, and permission to act as separate machine-relevant states.

**Implemented research/engineering surfaces include:**

- explicit governance and state-transition logic;
- provenance and source/evidence binding;
- deterministic validators, adversarial tests, and negative controls;
- fail-closed CI and authorization boundaries;
- custody, freeze, closure, and experimental-integrity machinery;
- blinded experimental infrastructure and reproducibility tooling;
- separation of implementation, verification, independent verification, authorization, execution, and empirical support.

**Bounded research state — September 24, 2026:** Track A Epoch 002 completed its preregistered blinded collection at **50 paired seed units / 2,250 observations**. Dataset lock, bounded unblinding, controlled materialization and its immutable receipt, locked-primary-analysis authorization, local execution of the frozen primary analysis, content-addressed result admission, and bounded same-system interpretation/adjudication are established at their exact scopes. The Epoch 002 lifecycle is **closed for its exact preregistered scope**. Scientific-N increment remains **0**; canonical DGAF efficacy, independent validation, production certification, and High-Assurance authorization remain **NOT ESTABLISHED / NOT AUTHORIZED**. AOSS Stage A has an accepted independent-validation handoff; external review remains outstanding under [Issue #929](https://github.com/ndrorchestration/DGAF-Framework/issues/929).

**Start here:** [five-minute evaluator orientation](https://github.com/ndrorchestration/DGAF-Framework#five-minute-evaluator-orientation) · [current-state record](https://github.com/ndrorchestration/DGAF-Framework/blob/main/docs/CURRENT_STATE.md)

## Selected work

### [Orbit-Driftwatch](https://github.com/ndrorchestration/Orbit-Driftwatch) — multi-agent evaluation & observability

A compact system for inspecting a multi-agent workflow rather than showing only its final answer. It demonstrates Planner / Researcher / Skeptic / Verifier role separation, provider boundaries, source-aware provenance, disagreement and evidence-coverage metrics, unsupported/conflicting-claim handling, deterministic controls, portable run artifacts, and fail-closed claim-readiness auditing.

**Evidence boundary:** deterministic behavior and repository controls are CI-tested, including frozen reproducible artifacts. Live hosted OpenAI-backed execution/retrieval remains outside the currently verified public evidence boundary.

### [Collabration](https://github.com/ndrorchestration/Intellectro) — governed human+AI collaboration

A social application exploring accountable human/AI interaction without silently transferring authority to agents. It includes deny-by-default capability decisions, human approval gates, provenance and revision-aware Content Passport contracts, governed action records, correction/appeal paths, authenticated application paths, and Supabase/Postgres row-level-security boundaries.

> The repository still uses the historical identifier `Intellectro`; **Collabration** is the canonical product name.

### [agent-control-plane](https://github.com/ndrorchestration/agent-control-plane) — minimal control-plane primitives

An executable deterministic kernel for capability dispatch, explicit policy allow/deny decisions, fail-closed rejection provenance, cooperative execution budgets, run-scoped provenance, and portable manifests. Its guarantees are deliberately scoped to tested local software invariants rather than production security or distributed reliability.

### [ai-prompt-systems-portfolio](https://github.com/ndrorchestration/ai-prompt-systems-portfolio) — prompt/evaluation systems

Public, recruiter-readable prompt-system artifacts and evaluation specifications covering state anchoring, constraint gates, multi-agent role decomposition, parametric behavior, and failure-aware recovery. Written specifications are kept distinct from executed benchmark evidence.

## Capabilities

| Area | Working focus |
|---|---|
| **AI evaluation & QA** | known-answer controls, negative tests, failure taxonomies, evidence classes, claim ceilings |
| **Agentic systems** | role separation, handoffs, state/control-plane design, orchestration boundaries |
| **Governance & authorization** | fail-closed gates, explicit permissions, transition constraints, approval/rejection semantics |
| **Provenance & reproducibility** | source binding, artifact identity, deterministic controls, audit trails |
| **Prompt systems** | prompt/evaluation specifications, structured outputs, failure-aware iteration |
| **Runtime verification** | source/deployment/runtime separation, health checks, exact-identity reasoning |
| **Research tooling** | preregistration, blinded workflows, reproducibility, adversarial and negative controls |

**Primary tools represented in current public work:** Python · JavaScript/Node.js · TypeScript · Next.js/React · Supabase/Postgres/RLS · GitHub Actions · Vercel · model/provider APIs

## Evidence discipline

Across projects I use a progression such as:

**defined → implemented → tested → computed → verified → independently verified → authorized → executed → empirically supported**

Those states are intentionally not interchangeable. A passing test does not prove efficacy. A healthy deployment does not establish scientific validity. Provenance establishes origin and history, not truth. Governance controls do not automatically grant authorization. Historical evidence does not silently transfer to a new candidate, deployment, run, or artifact.

That is why several repositories deliberately preserve states such as **NOT VERIFIED**, **NOT AUTHORIZED**, **NOT ESTABLISHED**, or **blocked** when the required evidence does not exist.

## Professional direction

I am building toward **AI Evaluator, Prompt Engineer, AI Training / Quality, AI Systems, and agentic-governance roles** where careful testing, failure-mode discovery, provenance, evidence quality, and system-level reasoning matter alongside implementation.

My broader goal is to help make increasingly capable AI systems easier to **inspect, constrain, verify, and trust for the right reasons**.

## Explore the ecosystem

This profile is a curated portfolio, not a complete repository inventory. The account also contains experimental, supporting, historical, external/reference, and incubating work.

For the account-level classification and provenance boundary, see the [Repository Lifecycle Map](docs/ECOSYSTEM_LIFECYCLE.md).

---

*Exact implementation, runtime, evidence, governance, and scientific facts remain authoritative in each project’s owning repository and relevant runtime providers. This profile does not transfer evidence or readiness claims between projects.*
