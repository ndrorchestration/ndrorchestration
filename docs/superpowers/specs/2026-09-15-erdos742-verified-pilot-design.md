# Erdős #742 Verified Proof-Certificate Pilot — Design

**Date:** 2026-09-15  
**Status:** APPROVED DESIGN / IMPLEMENTATION STAGING / FRONTIER COMPUTATION NOT AUTHORIZED  
**Canonical research record:** Notion — `AI-Era Open-Problem Prospecting — Research Scoping Record — 2026-09-15`  
**Repository role:** incubator implementation surface only; this repository is not the mathematical source of truth.

## Objective

Build a reproducible, fail-closed harness for a bounded Murty–Simon / Erdős #742 proof-certificate pilot using the existing LeanSMS verified graph-generation framework. The pilot must validate the complete trust chain on known instances before any n=25 frontier branch is run or promoted as research evidence.

The goal is not to claim a proof of the global Murty–Simon conjecture. The goal is to establish a trustworthy computational/formal pipeline capable of producing independently checkable branch-level evidence.

## Upstream trust anchor

Pin LeanSMS to:

- Repository: `leansolving/leansms`
- Commit: `8fa708e4c8a00a8951dadc5c0f68863d057fcfab`
- Lean toolchain: `leanprover/lean4:v4.24.0-rc1`
- mathlib: `v4.24.0-rc1`
- Certificate format: LRAT
- Symmetry strategy: SAT Modulo Symmetries (SMS)
- Final proof-checking trust anchor: Lean kernel

LeanSMS already provides the required architectural pieces: graph-level constraints, machine-checked CNF completeness arguments, isomorphism-invariance reasoning, verified symmetry-breaking clauses, CaDiCaL-generated LRAT, and Lean checking of the complete impossibility chain.

## Evidence classes

Keep the following states distinct:

1. `DEFINED` — claim contract and parameters are explicit.
2. `GENERATED` — CNF/artifacts exist.
3. `SOLVER-UNSAT` — a solver reported UNSAT; not sufficient.
4. `LRAT-VERIFIED` — LRAT checks against the exact extended CNF.
5. `LEAN-VERIFIED` — the formal theorem closes in Lean against the pinned framework.
6. `COLLISION-AUDITED` — same-day research collision audit complete.
7. `BRANCH-VERIFIED` — exact n/e/Δ branch has all required verification and provenance.
8. `FRONTIER-COMPLETE` — every required branch for the finite frontier has been independently verified.

No state may be inferred from a later-looking filename, solver exit code, timeout, or partial artifact set.

## Scope

### Included now

- Pin upstream identity and toolchain.
- Reproduce a supported LeanSMS smoke-test instance.
- Reproduce the published n=13 Murty–Simon benchmark end-to-end.
- Stage n=14 as the first extension stress point.
- Add manifest generation, hashing, environment capture, and fail-closed validation.
- Specify exact n=25 frontier branch contracts for `e(G)=157` and `Δ(G) ∈ {13,14,15,16,17}`.
- Define equal-budget feasibility probes across all five Δ values.
- Define collision-audit and promotion gates.

### Excluded until later gates close

- Treating n=25 computation as authorized merely because the harness builds.
- Claiming a single branch resolves n=25.
- Claiming n=25 resolves the global conjecture.
- Publishing novelty claims before same-day collision audit and expert review.
- Treating a timeout as evidence of satisfiability or unsatisfiability.

## Baseline ladder

1. **Smoke test:** run a small supported instance such as `n=9`.
2. **Published formal baseline:** reproduce `n=13`, the largest Murty–Simon instance explicitly reported by the 2026 LeanSMS paper as end-to-end formally verified.
3. **Extension bridge:** attempt `n=14` using the unchanged general Murty–Simon encoding. This is a scalability/extension test, not a novelty claim about the global problem.
4. **Optional scale calibration:** if n=14 succeeds, measure one or more larger known finite cases only when the same verified semantics apply and resource budgets remain bounded.
5. **Frontier-specific work:** only after a branch-specific encoding and its completeness/isomorphism obligations are proved, and after the same-day collision audit is complete.

## n=25 frontier contract

The research-scoping record currently identifies the bounded frontier as:

- `n = 25`
- `e(G) = 157`
- `Δ(G) ∈ {13,14,15,16,17}`

This enumeration remains source-bound to the working report until independently reconciled again on the day of execution.

A branch certificate for one value of Δ establishes only the impossibility of that exact branch, assuming the branch encoding's formal obligations close. All five branches are required before stating that this finite n=25 frontier is exhausted. Even that finite result does not by itself prove the global Murty–Simon conjecture.

## Frontier encoding requirements

The current LeanSMS `encodeMurtySimon n` searches for a non-bipartite diameter-2-critical graph with at least `floor(n²/4)` edges. The n=25 branch requires additional semantics:

- exactly 157 edges, not merely at least 156;
- maximum degree exactly d for the selected branch;
- no auxiliary-variable collisions when composing cardinality/degree encodings;
- completeness proof from the graph-level branch property to the generated CNF;
- isomorphism-invariance proof for the complete branch property;
- verified SMS symmetry clauses for the branch encoding;
- LRAT verification against the exact base-plus-symmetry CNF.

The preferred implementation is an additive branch-specific `EncodingSpec`; do not weaken or bypass LeanSMS's trust model.

## Exact-degree semantics

For branch parameter d, `Δ(G)=d` must be represented semantically as:

- every vertex has degree at most d; and
- at least one vertex has degree at least d.

Because the first condition already imposes degree ≤ d, the conjunction yields maximum degree exactly d. The implementation must use separately allocated auxiliary-variable ranges for each sequential counter and prove the composed encoding complete.

## Exact-edge semantics

`e(G)=157` must be represented semantically as both:

- edge count ≥ 157; and
- edge count ≤ 157.

The composed cardinality encoding must use disjoint auxiliary-variable ranges and a proof that any graph with exactly 157 edges extends to a satisfying assignment of both counters.

## Reproducibility manifest

Every retained run directory must contain a machine-readable manifest with:

- upstream repository and commit;
- local harness version / git commit;
- Lean and mathlib versions;
- SMS and CaDiCaL version strings when available;
- OS, architecture, CPU count, and memory metadata when available;
- exact command and parameters;
- start/end UTC timestamps and duration;
- exit codes per phase;
- SHA-256 for CNF, symmetry JSON, extended CNF, LRAT, logs, and theorem source;
- artifact sizes;
- evidence classification;
- collision-audit status;
- explicit claim ceiling.

Manifest validation fails closed if a required artifact is absent, hash-mismatched, or associated with a different parameter set.

## Resource and stop rules

Initial operational budgets are deliberately provisional and are not mathematical thresholds:

- Feasibility probe: ≤ 60 minutes wall-clock per Δ branch.
- First full branch attempt: ≤ 24 hours wall-clock unless a later reviewed budget supersedes this value.
- A timeout/resource limit is recorded as `NOT_REFUTED_WITHIN_BUDGET`.
- Resource exhaustion must not be translated into SAT, UNSAT, or likely truth/falsity.

After the n=13/n=14 reproduction measurements, budgets may be recalibrated in a new reviewed record.

## Branch-order rule

The earlier provisional choice of Δ=17 first is superseded. After prerequisites close, run equal-budget feasibility probes for d ∈ {13,14,15,16,17}; choose the first full branch based on measured tractability, not list order or intuition.

## Same-day collision audit

Before any novel frontier run is authorized, check and record:

- canonical Erdős problem status page;
- relevant problem discussion/forum surface;
- arXiv, especially math.CO;
- GitHub repositories/code for active #742/Murty–Simon work;
- Zenodo or other artifact repositories for certificate releases;
- recent papers/preprints and named-worker records.

If a required canonical source is inaccessible, status is `INCOMPLETE`; the default action is to defer novelty promotion and frontier authorization.

## Test strategy

The incubator harness must include tests for:

- manifest schema and required fields;
- SHA-256 recomputation and mismatch rejection;
- parameter identity (`n`, `edges`, `delta`) binding;
- evidence-state transition rules;
- timeout classification;
- collision-audit completeness gating;
- artifact-set completeness;
- command construction for baseline versus frontier modes.

These tests validate the orchestration/provenance wrapper. They do not substitute for Lean verification of mathematical encodings or certificates.

## Success criteria for this implementation cycle

This cycle is complete when:

1. The incubator branch contains a pinned design, plan, harness, tests, and operator runbook.
2. Local wrapper tests pass.
3. A reproducibility manifest can be generated and independently revalidated from a synthetic artifact set.
4. The exact commands for n=9 and n=13 LeanSMS reproduction are frozen.
5. n=14 is staged as an extension command but not falsely reported as verified unless actually run in an environment with LeanSMS/SMS available.
6. The n=25 branch specification is explicit but remains `NOT_AUTHORIZED` until formal branch-encoding obligations and collision audit close.
7. Notion is updated with the exact repository branch/PR and the evidence boundary.

## Current environment limitation

The present execution environment cannot resolve external Git hosts from the local container, so the LeanSMS repository/toolchain cannot be cloned or executed here. GitHub source inspection is available through the connected GitHub integration, allowing the upstream identity and source interfaces to be pinned. Therefore this implementation cycle can fully build and test the provenance/orchestration harness, but it must record Lean/SMS runtime reproduction as `NOT_EXECUTED` until run in a suitable environment (for example Codespaces or another machine with network/toolchain access).
