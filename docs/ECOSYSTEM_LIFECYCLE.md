# Ndr Repository Lifecycle Map

**Status:** ACTIVE ACCOUNT-LEVEL CLASSIFICATION  
**Authority scope:** `ACCOUNT_LEVEL_LIFECYCLE_ONLY`  
**Machine-readable source:** [`../ecosystem/repository-lifecycle.json`](../ecosystem/repository-lifecycle.json)  
**Reviewed:** 2026-09-24

## Authority boundary

This document classifies how repositories relate to the `ndrorchestration` account. It does **not** override repository-local source code, tests, CI, evidence, runtime facts, governance state, scientific state, security claims, or authorization.

Project repositories remain authoritative for their own implementation and evidence. Runtime providers remain authoritative for runtime facts. DGAF may maintain a bounded DGAF-related projection, but it is not the canonical account-wide repository inventory. Cross-repository relationships are descriptive only and never transfer validation or authority.

## Current census

The current connected GitHub owner census contains **48 repositories**:

- **47 `VERIFIED`** lifecycle classifications;
- **1 `PENDING_REVIEW`** classification;
- **0 `CONFLICTED`** classifications;
- **5 `ARCHIVE_CANDIDATE`** repositories awaiting the final archive gate; and
- **1 already `ARCHIVED`** repository.

A verified lifecycle means the account-level role is supported by current repository-local documentation and/or GitHub metadata. It does not mean production readiness, scientific validation, security certification, or authorization.

## Lifecycle vocabulary

- `ACTIVE_CORE` — current flagship or strategically important system with a unique responsibility.
- `ACTIVE_SUPPORTING` — maintained infrastructure, tooling, reference, portfolio, or operational support.
- `EXPERIMENTAL` — active research/prototype work whose claims remain explicitly bounded by evidence.
- `INCUBATING` — a real but not-yet-mature project identity.
- `HISTORICAL` — superseded or predecessor work retained for provenance.
- `EXTERNAL_REFERENCE` — imported/fork-derived code retained for a concrete active reference purpose.
- `ARCHIVE_CANDIDATE` — verified inactive/test/obsolete repository proposed for archival after dependency checks.
- `ARCHIVED` — GitHub-archived repository retained read-only for history.

Review status is separate from lifecycle: `VERIFIED`, `PENDING_REVIEW`, or `CONFLICTED`.

## Active core

| Repository | Product/system | Separate responsibility |
|---|---|---|
| `DGAF-Framework` | DGAF | Governance, evidence, authorization, provenance, and governed experimental controls. |
| `Orbit-Driftwatch` | Orbit-Driftwatch | Observable multi-agent reasoning and claim-audit showcase. |
| `Collabration` | **Collabration** | Governed human+AI social product. |

`Collabration` is the current repository and canonical human-facing product identity. Historical artifacts, deployment/provider records, and immutable provenance may retain the former `Intellectro` identifier where that identity was recorded at event time; those historical identifiers do not redefine the current repository name.

## Active supporting

`Gold-star-standards`, `ai-prompt-systems-portfolio`, `.github`, `career-positioning`, `automation-scripts`, `ndrorchestration`, `entrepreneur-hub`, `dgaf-ops`, and `agent-control-plane`.

These repositories support current work but are not interchangeable authorities. For example, the profile repository owns account-level lifecycle/navigation only, and `dgaf-ops` does not own DGAF scientific or authorization state.

## Experimental

`ai-governance-frameworks`, `3d-visualization-hub`, `junior-apogee-app` / **AI Evaluation Workbench**, `phi-calculus-app`, `sentinel-governance`, `resumeapex-eval`, `Driftwatch`, `Amethyst-Governance-Eval-Stack`, `Acoustic-mesh`, `aoga-dashboard`, `pptl-governance-dashboard`, `AHG-Zeta-Pell-Autonomous-Lattice`, `Meshsense`, `orbit-everyday`, and `Morse-Orchestration`.

`EXPERIMENTAL` means the project is a current research/prototype track with bounded claims. It does not mean the work is invalid or abandoned.

## Historical

- `AI-Prompt-Engineer` — earlier private prompt-engineering portfolio archive.
- `ai-prompt-engineering-portfolio` — v1 private portfolio predecessor.
- `prompt-optimization-library` — v0 prompt-optimization baseline archive.
- `chat-archives` — conversation/protocol/research provenance archive.
- `api` — dated generic API evidence-status record without an active implementation surface in that repository.

The current public prompt-systems portfolio is `ai-prompt-systems-portfolio`; the older prompt repositories remain useful lineage rather than competing current portfolios.

## Incubating

- `Agentic-Iteration-Metaconcert-Yaml-AIMY-` — experiment scaffold whose current purpose is not yet sufficiently documented for a stronger lifecycle.
- `SP1` — game-project home whose current identity and implementation are still minimally documented.
- `aetherwake-jrpg` — private pre-alpha **Aetherwake — The Last Solarpunk Airship** track with a playable vertical slice and active standalone Windows preview packaging; retained as incubating while the game and delivery path mature.
- `coherence-control-benchmark` — private AI evaluation/orchestration-control benchmark prototype; provisionally `INCUBATING` with `PENDING_REVIEW` because repository metadata establishes the intended identity while the README/package presentation layer remains unreconciled starter scaffolding.

## Archive candidates

The following have passed classification review as archive candidates but **have not yet been archived by this lifecycle record**:

- `cli` — only a minimal Go “Hello, Bounty Hunter!” stub and no established current ecosystem responsibility.
- `__forktest_1787727107` — disposable fork test of `octocat/Hello-World`; no operational account references found outside lifecycle-cleanup documentation.
- `DGAF-Google-AIStudio` — generic AI Studio scaffold; no established current DGAF implementation responsibility or account references outside this cleanup.
- `unsloth` — upstream-derived Unsloth snapshot with no local authored branch or active account dependency found; preserve Apache-2.0/upstream provenance.
- `Soroban-Eas__soroban-sas` — contribution-attempt fork whose upstream issue is completed and whose account PRs are closed unmerged; no separate active account responsibility found.

Archival still requires the final dependency/open-work/readback gate. `ARCHIVE_CANDIDATE` is not equivalent to `ARCHIVED`.

## Archived

- `gold-star-qa-framework` — GitHub archived state is already established; retained for historical Gold Star QA provenance.

## External/reference forks

The following fork-derived repositories have a concrete retained contribution/reference purpose. Upstream remains canonical, and these forks are not counted as original authored portfolio projects:

| Repository | Verified upstream/source | Retention evidence |
|---|---|---|
| `fabastrunck__cli` | `fabastrunck/cli` | Account PR #2 remains open; retain until the open contribution is adjudicated. |
| `deliverymanager__cordova-plugin-media-capture` | `apache/cordova-plugin-media-capture` source lineage | Funded issue #1 and account PR #2 remain open. |
| `drydart__flutter_android` | `drydart/flutter_android` | Funded issue #1 and account PR #17 remain open. |
| `GatorEducator__gatorgrader` | `GatorEducator/gatorgrader` | Account PRs #290/#291 remain open. |
| `eliezerkirubi-sys__quadcopter-rl-control` | `eliezerkirubi-sys/quadcopter-rl-control` | Account PRs #24/#25/#26 remain open. |
| `lily-contracts` | `Lilly-Protocol/lily-contracts` | Account PR #166 was merged on 2026-09-02; retain as successful upstream-contribution provenance/reference. |

Fork provenance and contribution history establish origin and a bounded retention reason only; they do not transfer upstream authority or make these repositories original portfolio projects.

## Remaining pending review

- `coherence-control-benchmark` — `PENDING_REVIEW`. Foundation PR #1 now reconciles the intended identity, restores the missing React/Express entrypoints, adds explicit experimental-status/evidence-boundary documentation, CI, and cross-platform runtime scripts. However, `foundation-ci` has twice failed before runner allocation (`runner_id=0`, zero steps executed), so fresh-checkout install, typecheck, and build remain **NOT VERIFIED**. Keep the repository out of the public portfolio and do not strengthen its lifecycle until executable verification completes and the accepted foundation reaches `main`.

New ambiguity must be recorded explicitly rather than inferred into an existing lifecycle.

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

## Public portfolio rule

The GitHub profile is a curated projection, not the complete inventory. It emphasizes a small set of current authored work and links here for lifecycle detail. External/reference repositories, archive candidates, historical work, and unresolved repositories remain discoverable without being presented as equivalent current portfolio projects.

## Next reconciliation work

1. complete executable verification for `coherence-control-benchmark` foundation PR #1, then reconcile the accepted foundation on `main` before lifecycle promotion;
2. adjudicate retained open upstream contribution PRs before any related archive decision;
3. execute archival only for candidates satisfying every archive predicate and verify `archived=true` by readback;
4. continue correcting stale account/repository authority language where found;
5. synchronize DGAF and workspace projections after canonical lifecycle changes without creating competing sources of truth.

The machine-readable registry remains the canonical account-level lifecycle classification surface. This document is its human-readable companion.