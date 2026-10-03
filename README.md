**Andrew Hensel // Ndr “Ender”**

### AI Systems Design · Evaluation · Agent Orchestration · Governance · Provenance

I build and evaluate AI systems around a practical question:

> **What did the system actually do, what evidence supports that claim, and what is it authorized to do next?**

My work focuses on **AI evaluation, multi-agent systems, prompt engineering, provenance, reproducibility, and governance-aware orchestration**. I design systems that keep **capability, evidence, verification, authority, and permission** distinct so that producing an output is not automatically treated as proving a claim, passing evaluation, or earning authorization for the next action.

## Start here

| If you want to inspect… | Start with |
| --- | --- |
| **Governance, evidence, authorization, and research controls** | [DGAF-Framework](https://github.com/ndrorchestration/DGAF-Framework) |
| **Observable multi-agent reasoning and claim auditing** | [Orbit-Driftwatch](https://github.com/ndrorchestration/Orbit-Driftwatch) |
| **Minimal execution/control-plane primitives** | [agent-control-plane](https://github.com/ndrorchestration/agent-control-plane) |
| **Governed human + AI product design** | [Collabration](https://github.com/ndrorchestration/Collabration) |
| **Prompt-system and evaluation specifications** | [ai-prompt-systems-portfolio](https://github.com/ndrorchestration/ai-prompt-systems-portfolio) |
| **Executable evaluation-harness design** | [resumeapex-eval](https://github.com/ndrorchestration/resumeapex-eval) |
| **Public governance / evidence explanation** | [Tektite live demo](https://project-7ybao.vercel.app/demo) |

## Flagship: DGAF

### [DGAF-Framework](https://github.com/ndrorchestration/DGAF-Framework) — governance control plane for agentic systems

**Dynamic Governance Agentic Formation (DGAF)** is an experimental framework for governed multi-agent AI systems. Its central design principle is that **capability, evidence, verification, authority, and permission to act are separate machine-relevant states** rather than interchangeable signals that a system “works.”

Implemented surfaces include explicit governance states and machine-checkable transitions; provenance and source/evidence binding; deterministic validators and negative controls; fail-closed CI and authorization boundaries; custody/freeze/closure controls; blinded experimental infrastructure; controlled materialization; content-addressed evidence receipts; and explicit separation of implementation, verification, independent verification, authorization, execution, interpretation, and empirical support.

### Current research boundary

**Track A Epoch 002** completed a preregistered blinded collection of **50 paired seed units / 2,250 observations**, followed by governed dataset lock, bounded unblinding, controlled materialization, locked-primary-analysis authorization and execution, content-addressed result admission, and bounded same-system interpretation/adjudication. The epoch is **closed for its exact preregistered scope**.

Those results deliberately do **not** transfer into broader claims:

`SCIENTIFIC_N_INCREMENT = 0`  
`CANONICAL_DGAF_EFFICACY = NOT_ESTABLISHED`  
`INDEPENDENT_VALIDATION = NOT_ESTABLISHED`  
`HIGH_ASSURANCE = NOT_AUTHORIZED`

DGAF now also maintains an explicit architecture ownership model spanning governance-kernel components, cross-cutting assurance, governed profiles, and external integrations. That architecture work is engineering/governance evidence only and does not promote scientific, efficacy, independent-validation, or High-Assurance state.

For **AOSS Stage A**, an independent-validation handoff has been accepted and the system includes a bounded internal operator self-test path. Actual external review remains outstanding under [Issue #929](https://github.com/ndrorchestration/DGAF-Framework/issues/929).

**Evaluate DGAF:** [60-second bounded public demo](https://project-7ybao.vercel.app/demo) · [Five-minute evaluator orientation](https://github.com/ndrorchestration/DGAF-Framework#five-minute-evaluator-orientation) · [Developer self-test](https://github.com/ndrorchestration/DGAF-Framework/blob/main/docs/qa/DGAF_OPERATOR_SELFTEST.md) · [Outside-operator trial](https://github.com/ndrorchestration/DGAF-Framework/blob/main/docs/governance/GOVERNED_REPO_OUTSIDE_OPERATOR_TRIAL_V0.md) · [Current-state record](https://github.com/ndrorchestration/DGAF-Framework/blob/main/docs/CURRENT_STATE.md)

The outside-operator trial is a **currently open usability gate**, not an achieved validation claim. It requires an uninvolved technically capable human operator working from the published packet without implementation-author coaching; same-owner automation, ChatGPT execution, and author execution do not satisfy it.

**Tektite** is the public-facing explanation layer for this work: it exposes governed action/evidence state and claim boundaries without becoming a source of governance authority. Its live demo is bounded engineering evidence only; availability does not establish independent validation, canonical efficacy, production-executor authority, or High-Assurance status.

## Selected work

### [Orbit-Driftwatch](https://github.com/ndrorchestration/Orbit-Driftwatch) — multi-agent evaluation & observability

A compact system for inspecting a multi-agent workflow rather than exposing only its final answer. It demonstrates **Planner / Researcher / Skeptic / Verifier role separation**, provider boundaries, source-aware provenance, disagreement and evidence-coverage metrics, unsupported/conflicting-claim handling, deterministic controls, portable run artifacts, and fail-closed claim-readiness auditing.

**Evidence boundary:** deterministic behavior, repository controls, and frozen reproducible artifacts are CI-tested. OpenAI-backed execution and web retrieval are implemented behind a server-side provider boundary, but live hosted execution/retrieval remains outside the currently verified public evidence boundary.

### [agent-control-plane](https://github.com/ndrorchestration/agent-control-plane) — execution-control primitives

An executable deterministic kernel for **capability dispatch, explicit policy allow/deny decisions, fail-closed rejection provenance, cooperative execution budgets, run-scoped provenance, portable manifests, bounded remote-execution contracts, and non-executing mutation-governance controls**.

ACP's current executor profile is **`BOUNDED_LOCAL_TEST`**. Protected `main` now includes the bounded disposable-repository executor accepted in PR [#156](https://github.com/ndrorchestration/agent-control-plane/pull/156), together with admission, path-safety, journal/recovery, postcondition, result-binding, single-use authorization/closure, and fresh-adjudication requirements for consequential follow-on effects. That executor is limited to explicitly marked disposable local test repositories and does **not** establish a live real-project mutation or rollback executor.

Its guarantees remain deliberately narrow: the retained local-test profile does not establish final path-to-syscall TOCTOU elimination, hostile-local-actor resistance, trusted process identity, peer-process tamper resistance, production execution, real-project mutation authority, rollback authority, independent validation, or High-Assurance.

### [Collabration](https://github.com/ndrorchestration/Collabration) — governed human + AI collaboration

A social application exploring accountable human/AI interaction without silently transferring authority to agents. It combines **deny-by-default capability decisions, human approval gates, provenance and revision-aware Content Passports, governed action records, correction and appeal paths, authenticated application flows, and Supabase/Postgres row-level-security boundaries**.

> **Collabration** is the canonical product identity. Historical artifacts and provider records may retain the former **Intellectro** identifier where preserving provenance requires it.

### [ai-prompt-systems-portfolio](https://github.com/ndrorchestration/ai-prompt-systems-portfolio) — prompt & evaluation systems

Public, recruiter-readable examples of prompt-system design and evaluation specifications covering **state anchoring, constraint gates, multi-agent role decomposition, parametric behavior, structured evaluation, and failure-aware recovery**.

The repository deliberately distinguishes written specifications and evaluation rubrics from executed benchmark evidence.

### [resumeapex-eval](https://github.com/ndrorchestration/resumeapex-eval) — executable evaluation harness

A reproducible evaluation repository demonstrating **known-answer fixtures, deterministic-repeatability checks, evidence-state separation, metric computation, bootstrap analysis, and explicit boundaries between evaluator verification and real-model empirical results**.

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
