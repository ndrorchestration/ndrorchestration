# Ndr Repository Lifecycle Map

**Status:** ACTIVE ACCOUNT-LEVEL CLASSIFICATION  
**Authority scope:** `ACCOUNT_LEVEL_LIFECYCLE_ONLY`  
**Machine-readable source:** [`../ecosystem/repository-lifecycle.json`](../ecosystem/repository-lifecycle.json)  
**Reviewed:** 2026-09-16

## Authority boundary

This document classifies how repositories relate to the `ndrorchestration` account. It does **not** override repository-local source code, tests, CI, evidence, runtime facts, governance state, scientific state, security claims, or authorization.

Project repositories remain authoritative for their own implementation and evidence. Runtime providers remain authoritative for runtime facts. DGAF may maintain a bounded DGAF-related projection, but it is not the canonical account-wide repository inventory.

Cross-repository relationships are descriptive only and never transfer validation or authority.

## Lifecycle vocabulary

- `ACTIVE_CORE` — current flagship or strategically important system with a unique responsibility.
- `ACTIVE_SUPPORTING` — maintained infrastructure, tooling, reference, portfolio, or operational support.
- `EXPERIMENTAL` — active research/prototype work whose claims remain explicitly bounded by evidence.
- `INCUBATING` — a real but not-yet-mature project identity.
- `HISTORICAL` — superseded or predecessor work retained for provenance.
- `EXTERNAL_REFERENCE` — imported, fork-derived, upstream, benchmark, or dependency-study code retained for a concrete reason.
- `ARCHIVE_CANDIDATE` — verified inactive/test/obsolete repository proposed for archival after dependency checks.
- `ARCHIVED` — GitHub-archived repository retained read-only for history.

Review status is separate from lifecycle:

- `VERIFIED` — lifecycle and responsibility are supported by current evidence.
- `PENDING_REVIEW` — lifecycle remains intentionally unresolved pending repository-local review.
- `CONFLICTED` — evidence sources disagree and the conflict is preserved rather than guessed through.

## Verified classifications

### Active core

| Repository | Product/system | Separate responsibility |
|---|---|---|
| `DGAF-Framework` | DGAF | Owns DGAF governance, evidence, authorization, provenance, and governed experimental-control framework. |
| `Orbit-Driftwatch` | Orbit-Driftwatch | Owns the public observable multi-agent reasoning and claim-to-evidence showcase. |
| `Intellectro` | **Collabration** | Owns the governed human+AI social product and its application-specific governance, provenance, persistence, and social interaction contracts. |

`Intellectro` remains the current repository/provider identifier. **Collabration** is the canonical human-facing product identity. A repository/provider rename is a separate migration event.

### Active supporting

| Repository | Responsibility |
|---|---|
| `ndrorchestration` | Owns account-level portfolio navigation and lifecycle classification, not project-local implementation truth. |
| `agent-control-plane` | Owns the reusable experimental execution-control kernel for capability dispatch, policy decisions, cooperative budgets, and run-scoped provenance. |

### Experimental

| Repository | Responsibility |
|---|---|
| `Meshsense` | Owns the independent companion-layer failure-mode compensation experiment around RuView. |
| `orbit-everyday` | Owns Orbit's local-first, privacy-oriented interpretation and UX research track. |

### Archived

| Repository | Reason |
|---|---|
| `gold-star-qa-framework` | GitHub reports the repository archived; it is retained as historical Gold Star QA provenance. |

## Pending repository review

The following repositories are present in the live owner census but are intentionally **not yet assigned a lifecycle**. Their current registry records use `PENDING_REVIEW` rather than inferring status from name, size, age, or conceptual similarity.

### Governance, evaluation, and application repositories

`Driftwatch`, `sentinel-governance`, `Amethyst-Governance-Eval-Stack`, `junior-apogee-app`, `resumeapex-eval`, `aoga-dashboard`, `pptl-governance-dashboard`, `dgaf-ops`, `Gold-star-standards`, `ai-governance-frameworks`.

### Prompt, portfolio, and support repositories

`ai-prompt-systems-portfolio`, `ai-prompt-engineering-portfolio`, `AI-Prompt-Engineer`, `prompt-optimization-library`, `.github`, `career-positioning`, `automation-scripts`, `chat-archives`, `entrepreneur-hub`.

### Research and creative repositories

`phi-calculus-app`, `AHG-Zeta-Pell-Autonomous-Lattice`, `Morse-Orchestration`, `Acoustic-mesh`, `3d-visualization-hub`, `Agentic-Iteration-Metaconcert-Yaml-AIMY-`, `DGAF-Google-AIStudio`, `SP1`, `aetherwake-jrpg`, `lily-contracts`.

### External/imported-looking and ambiguous repositories

`unsloth`, `GatorEducator__gatorgrader`, `deliverymanager__cordova-plugin-media-capture`, `drydart__flutter_android`, `Soroban-Eas__soroban-sas`, `eliezerkirubi-sys__quadcopter-rl-control`, `fabastrunck__cli`, `__forktest_1787727107`, `api`, `cli`.

Naming alone is not treated as proof of fork/upstream provenance or inactivity. The external/reference and archive pass must verify origin, active purpose, dependency use, unique material, and open work before changing those classifications.

## Separate-repository rule

An active repository should be able to complete this sentence clearly:

> **This repository exists separately because it owns _[specific responsibility]_ and no other repository owns that responsibility.**

Repositories that cannot pass this test are candidates for supporting, historical, incubating, consolidation, or archive review. Classification does not require deleting history or merging unrelated code.

## Archive criteria

A repository may move from `ARCHIVE_CANDIDATE` to `ARCHIVED` only after verifying all of the following:

1. it is not the canonical source for an active project;
2. no active mutable deployment, workflow, package, documentation contract, or dependency requires continued development there;
3. useful unique material is preserved or linked;
4. open work is adjudicated or explicitly retained as historical provenance;
5. upstream/external attribution remains intact where applicable; and
6. GitHub archive state is read back after the mutation before the registry is changed to `ARCHIVED`.

No repository is archived merely to make the profile look cleaner.

## Relationship semantics

Relationships such as `SUPPORTS`, `DERIVED_FROM`, `HISTORICAL_PREDECESSOR_OF`, `SHOWCASE_OF`, `EXPERIMENTS_WITH`, and `EXTERNAL_REFERENCE_FOR` are descriptive edges only. They do not transfer implementation status, runtime verification, empirical evidence, security assurance, scientific results, or authorization.

## Public portfolio rule

The GitHub profile is a curated projection, not the complete inventory. It should emphasize a small set of current authored work and link here for lifecycle detail. External/reference repositories, archive candidates, and unresolved repositories remain discoverable without being presented as equivalent current portfolio projects.

## Next review sequence

1. verify remaining authored governance/control repositories;
2. identify the canonical prompt/evaluation portfolio and classify duplicative containers;
3. verify research, creative, and private support repositories;
4. verify imported/reference provenance and ambiguous test repositories;
5. apply minimal repository-local boundary documentation;
6. archive only candidates that satisfy every approved predicate;
7. synchronize DGAF and workspace projections without creating a competing source of truth.

The machine-readable registry remains the canonical account-level lifecycle classification surface. This document is its human-readable companion.