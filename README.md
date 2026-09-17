# Andrew // Ndr "Ender" Hensel

### AI Systems Design · Evaluation · Agentic Governance · Provenance

I design and evaluate AI systems with a focus on a practical question:

> **What did the system actually do, what evidence supports that claim, and what is it authorized to do next?**

My work sits at the intersection of **AI evaluation, multi-agent systems, prompt engineering, provenance, reproducibility, and governance-aware orchestration**. I am especially interested in systems where capability, evidence, verification, and permission must remain distinct rather than collapsing into a generic “works” claim.

## Flagship: DGAF

### [DGAF-Framework](https://github.com/ndrorchestration/DGAF-Framework) — governance control plane for agentic systems

**Dynamic Governance Agentic Formation (DGAF)** is an experimental framework for governed multi-agent AI systems. It treats **capability, evidence, verification, authority, and permission to act as separate machine-relevant states**.

DGAF explores whether agentic systems can make consequential transitions only when the evidence and authority available at that exact state actually permit them.

**Implemented research/engineering surfaces include:**

- explicit governance and state-transition logic;
- provenance and source/evidence binding;
- deterministic validators and negative controls;
- fail-closed CI and authorization boundaries;
- custody, freeze, closure, and experimental-integrity machinery;
- blinded experimental infrastructure and reproducibility tooling;
- separation of implementation, verification, independent verification, authorization, execution, and empirical support.

**Current bounded research state:** Track A Epoch 002 collection is complete at **50 paired seed units / 2,250 blinded observations**, with dataset lock established. Controlled materialization is not yet established; primary analysis is not authorized or run; scientific-N increment remains 0; canonical efficacy and independent validation are not established. Broader High-Assurance DGAF remains **PRE-FREEZE / FAIL-CLOSED / NOT AUTHORIZED / N=0**.

**Start here:** [DGAF five-minute evaluator orientation](https://github.com/ndrorchestration/DGAF-Framework#five-minute-evaluator-orientation)

## What I build around that problem

### [Orbit-Driftwatch](https://github.com/ndrorchestration/Orbit-Driftwatch) — multi-agent evaluation & observability

A compact system for inspecting a multi-agent workflow rather than showing only its final answer.

**Demonstrates:** Planner / Researcher / Skeptic / Verifier role separation, provider boundaries, source-aware provenance, disagreement and evidence-coverage metrics, unsupported/conflicting-claim handling, deterministic controls, portable run artifacts, and fail-closed claim-readiness auditing.

**Stack:** JavaScript · Node.js · browser UI · provider abstraction · OpenAI Responses adapter · GitHub Actions

**Evidence boundary:** deterministic behavior and repository controls are CI-tested, including frozen reproducible artifacts. Live hosted OpenAI-backed execution/retrieval remains outside the currently verified public evidence boundary.

### [Collabration](https://github.com/ndrorchestration/Intellectro) — governed human+AI collaboration

A social application exploring accountable human/AI interaction without silently transferring authority to agents.

**Demonstrates:** deny-by-default capability decisions, human approval gates, provenance and revision-aware Content Passport contracts, governed action records, correction/appeal paths, authenticated application paths, and Supabase/Postgres row-level-security boundaries.

> The repository still uses the historical identifier `Intellectro`; **Collabration** is the canonical product name.

### [agent-control-plane](https://github.com/ndrorchestration/agent-control-plane) — minimal control-plane primitives

A smaller implementation surface for capability dispatch, rejection provenance, manifests, and explicit control boundaries.

### [ai-prompt-systems-portfolio](https://github.com/ndrorchestration/ai-prompt-systems-portfolio) — prompt/evaluation systems

Recruiter-readable prompt and evaluation specifications, structured-output contracts, failure-aware iteration, and reproducible comparison artifacts.

## Capabilities I am developing

| Area | Working focus |
|---|---|
| **AI evaluation & QA** | known-answer controls, negative tests, failure taxonomies, evidence classes, claim ceilings |
| **Agentic systems** | role separation, handoffs, state/control-plane design, orchestration boundaries |
| **Governance & authorization** | fail-closed gates, explicit permissions, transition constraints, approval/rejection semantics |
| **Provenance & reproducibility** | source binding, artifact identity, deterministic controls, audit trails |
| **Prompt systems** | prompt/evaluation specifications, structured outputs, failure-aware iteration |
| **Runtime verification** | source/deployment/runtime separation, health checks, exact-identity reasoning |
| **Research tooling** | preregistration, blinded workflows, reproducibility, adversarial and negative controls |

**Primary tools represented in current public work:** Python · JavaScript/Node.js · Next.js/React · Supabase/Postgres/RLS · GitHub Actions · Vercel · model/provider APIs

## How I work

I use a simple discipline across projects:

**defined → implemented → tested → computed → verified → independently verified → authorized → executed → empirically supported**

Those states are intentionally not interchangeable.

A passing test does not prove efficacy. A healthy deployment does not establish scientific validity. Provenance establishes origin and history, not truth. Governance controls do not automatically grant authorization. Historical evidence does not silently transfer to a new candidate, deployment, run, or artifact.

That is why several repositories deliberately preserve states such as **NOT VERIFIED**, **NOT AUTHORIZED**, **NOT ESTABLISHED**, or **blocked** when the required evidence does not exist.

## Current professional direction

I am building toward **AI Evaluator, Prompt Engineer, AI Training / Quality, AI Systems, and agentic-governance roles** where careful testing, failure-mode discovery, provenance, evidence quality, and system-level reasoning matter alongside implementation.

My broader goal is to help make increasingly capable AI systems easier to **inspect, constrain, verify, and trust for the right reasons**.

## Explore the ecosystem

The public profile is curated rather than exhaustive. The account also contains work in evaluation, observability, sensing, mathematical/control experiments, visualization, and supporting research infrastructure.

For the account-level classification of active, experimental, historical, external/reference, unresolved, and archived repositories, see the [Repository Lifecycle Map](docs/ECOSYSTEM_LIFECYCLE.md).

---

*Exact implementation, runtime, evidence, and governance facts remain authoritative in each project’s owning repository and relevant runtime providers. This profile does not transfer evidence or readiness claims between projects.*
