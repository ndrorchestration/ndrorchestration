**Andrew Hensel // Ndr “Ender”**

### AI Systems Design · Evaluation · Agentic Governance · Provenance

I design and evaluate AI systems around a practical question:

> **What did the system actually do, what evidence supports that claim, and what is it authorized to do next?**

My work focuses on **AI evaluation, multi-agent systems, prompt engineering, provenance, reproducibility, and governance-aware orchestration**.

I’m especially interested in systems that keep **capability, evidence, verification, authority, and permission** distinct—so that producing an output is not automatically treated as proving a claim, passing evaluation, or earning authorization for the next action.

## Flagship: DGAF

### [DGAF-Framework](https://github.com/ndrorchestration/DGAF-Framework) — governance control plane for agentic systems

**Dynamic Governance Agentic Formation (DGAF)** is an experimental framework for governed multi-agent AI systems. Its central design principle is that **capability, evidence, verification, authority, and permission to act are separate machine-relevant states** rather than interchangeable signals that a system “works.”

It explores how agentic systems can make consequential transitions only when the evidence and authority required for that specific transition are established.

**Implemented research and engineering surfaces include:**

- explicit governance states and machine-checkable transition logic;
- provenance, lineage, and source/evidence binding;
- deterministic validators, adversarial tests, and negative controls;
- fail-closed CI and authorization boundaries;
- custody, freeze, closure, and experimental-integrity controls;
- blinded experimental infrastructure and reproducibility tooling;
- controlled materialization and content-addressed evidence receipts;
- separation of implementation, verification, independent verification, authorization, execution, interpretation, and empirical support.

### Current research boundary

DGAF has progressed beyond architecture-only work into bounded experimental execution.

**Track A Epoch 002** completed a preregistered blinded collection of **50 paired seed units / 2,250 observations**, followed by governed dataset lock, bounded unblinding, controlled materialization, locked-primary-analysis authorization and execution, content-addressed result admission, and bounded same-system interpretation/adjudication. The epoch is **closed for its exact preregistered scope**.

Those results deliberately do **not** transfer into broader claims:

`SCIENTIFIC_N_INCREMENT = 0`  
`CANONICAL_DGAF_EFFICACY = NOT_ESTABLISHED`  
`INDEPENDENT_VALIDATION = NOT_ESTABLISHED`  
`HIGH_ASSURANCE = NOT_AUTHORIZED`

For **AOSS Stage A**, an independent-validation handoff has been accepted and the system includes a bounded internal operator self-test path. Actual external review remains outstanding under [Issue #929](https://github.com/ndrorchestration/DGAF-Framework/issues/929).

**Start here:** [Five-minute evaluator orientation](https://github.com/ndrorchestration/DGAF-Framework#five-minute-evaluator-orientation) · [Current-state record](https://github.com/ndrorchestration/DGAF-Framework/blob/main/docs/CURRENT_STATE.md)

## Selected work

### [Orbit-Driftwatch](https://github.com/ndrorchestration/Orbit-Driftwatch) — multi-agent evaluation & observability

A compact system for inspecting a multi-agent workflow rather than exposing only its final answer. It demonstrates **Planner / Researcher / Skeptic / Verifier role separation**, provider boundaries, source-aware provenance, disagreement and evidence-coverage metrics, unsupported/conflicting-claim handling, deterministic controls, portable run artifacts, and fail-closed claim-readiness auditing.

**Evidence boundary:** deterministic behavior, repository controls, and frozen reproducible artifacts are CI-tested. OpenAI-backed execution and web retrieval are implemented behind a server-side provider boundary, but live hosted execution/retrieval remains outside the currently verified public evidence boundary.

### [Collabration](https://github.com/ndrorchestration/Collabration) — governed human+AI collaboration

A social application exploring accountable human/AI interaction without silently transferring authority to agents. It combines **deny-by-default capability decisions, human approval gates, provenance and revision-aware Content Passports, governed action records, correction and appeal paths, authenticated application flows, and Supabase/Postgres row-level-security boundaries**.

The system distinguishes social participation from agent authority: relationships, content creation, and AI involvement do not implicitly grant capabilities or permission to act.

> **Collabration** is the canonical product identity. Historical artifacts and provider records may retain the former **Intellectro** identifier where preserving provenance requires it.

### [agent-control-plane](https://github.com/ndrorchestration/agent-control-plane) — minimal control-plane primitives

An executable deterministic kernel for **capability dispatch, explicit policy allow/deny decisions, fail-closed rejection provenance, cooperative execution budgets, run-scoped provenance, and portable manifests**.

Its guarantees are deliberately narrow: tested local software invariants rather than claims of distributed reliability, production security, durable authorization infrastructure, or provider-level resource accounting.

### [ai-prompt-systems-portfolio](https://github.com/ndrorchestration/ai-prompt-systems-portfolio) — prompt & evaluation systems

Public, recruiter-readable examples of prompt-system design and evaluation specifications covering **state anchoring, constraint gates, multi-agent role decomposition, parametric behavior, structured evaluation, and failure-aware recovery**.

The repository deliberately distinguishes written specifications and evaluation rubrics from executed benchmark evidence.

## Capabilities

| Area | Working focus |
| --- | --- |
| **AI evaluation & QA** | Known-answer controls, negative tests, failure taxonomies, evidence classes, claim ceilings |
| **Agentic systems** | Role separation, handoffs, control-plane design, orchestration boundaries |
| **Governance & authorization** | Fail-closed gates, explicit permissions, transition constraints, approval/rejection semantics |
| **Provenance & reproducibility** | Source binding, artifact identity, deterministic controls, audit trails |
| **Prompt systems** | Prompt/evaluation specifications, structured outputs, constraint design, failure-aware iteration |
| **Runtime verification** | Source/deployment/runtime separation, health checks, exact-identity reasoning |
| **Research tooling** | Preregistration, blinded workflows, reproducibility, adversarial and negative controls |

**Primary technologies represented in current public work:** Python · JavaScript/Node.js · TypeScript · Next.js/React · Supabase/Postgres/RLS · GitHub Actions · Vercel · model/provider APIs

## Evidence discipline

Across projects, I treat states such as

**defined → implemented → tested → computed → verified → independently verified → authorized → executed → empirically supported**

as distinct rather than interchangeable.

A passing test does not prove efficacy. A healthy deployment does not establish scientific validity. Provenance establishes origin and history, not truth. Authorization does not follow automatically from capability. Historical evidence does not silently transfer to a new candidate, deployment, run, or artifact.

That is why my repositories deliberately preserve states such as **NOT VERIFIED**, **NOT AUTHORIZED**, **NOT ESTABLISHED**, and **BLOCKED** when the evidence required for a stronger claim does not yet exist.

## Professional direction

I am building toward work in **AI evaluation, prompt engineering, AI quality/training, agentic systems, and governance-aware AI engineering**—particularly where careful testing, failure-mode discovery, provenance, evidence quality, and system-level reasoning matter alongside implementation.

My broader goal is to help make increasingly capable AI systems easier to **inspect, constrain, evaluate, verify, and trust for the right reasons**.

## Explore the ecosystem

This profile is a curated portfolio rather than a complete repository inventory. The account also contains supporting infrastructure, experimental research, historical lineage, external/reference work, and incubating projects.

For account-level classification and provenance boundaries, see the [Repository Lifecycle Map](https://github.com/ndrorchestration/ndrorchestration/blob/main/docs/ECOSYSTEM_LIFECYCLE.md).

---

*Exact implementation, runtime, evidence, governance, and scientific facts remain authoritative in each project's owning repository and relevant runtime providers. This profile does not transfer evidence, validation, authorization, or readiness claims between projects.*
