# Ndr Repository Lifecycle Map

**Status:** ACTIVE ACCOUNT-LEVEL CLASSIFICATION  
**Authority scope:** `ACCOUNT_LEVEL_LIFECYCLE_ONLY`  
**Machine-readable source:** [`../ecosystem/repository-lifecycle.json`](../ecosystem/repository-lifecycle.json)  
**Reviewed:** 2026-09-16

## Authority boundary

This document classifies how repositories relate to the `ndrorchestration` account. It does **not** override repository-local source code, tests, CI, evidence, runtime facts, governance state, scientific state, security claims, or authorization.

Project repositories remain authoritative for their own implementation and evidence. Runtime providers remain authoritative for runtime facts. DGAF may maintain a bounded DGAF-related projection, but it is not the canonical account-wide repository inventory. Cross-repository relationships are descriptive only and never transfer validation or authority.

## Current census

The current connected GitHub owner census contains **47 repositories**:

- **38 `VERIFIED`** lifecycle classifications;
- **9 `PENDING_REVIEW`** classifications;
- **0 `CONFLICTED`** classifications;
- **3 `ARCHIVE_CANDIDATE`** repositories awaiting the final archive gate; and
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
| `Intellectro` | **Collabration** | Governed human+AI social product. |

`Intellectro` remains the repository/provider identifier. **Collabration** is the canonical human-facing product identity. A repository/provider rename is a separate migration event.

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

## Archive candidates

The following have passed classification review as archive candidates but **have not yet been archived by this lifecycle record**:

- `cli` — only a minimal Go “Hello, Bounty Hunter!” stub and no established current ecosystem responsibility.
- `__forktest_1787727107` — disposable fork test of `octocat/Hello-World`; no operational account references found outside lifecycle-cleanup documentation.
- `DGAF-Google-AIStudio` — generic AI Studio scaffold; no established current DGAF implementation responsibility or account references outside this cleanup.

Archival still requires the final dependency/open-work/readback gate. `ARCHIVE_CANDIDATE` is not equivalent to `ARCHIVED`.

## Archived

- `gold-star-qa-framework` — GitHub archived state is already established; retained for historical Gold Star QA provenance.

## Verified fork provenance, retention still unresolved

GitHub metadata verifies these as fork-derived repositories, but their active retention purpose has not yet been adjudicated. They therefore remain `PENDING_REVIEW` rather than being promoted automatically to `EXTERNAL_REFERENCE` or `ARCHIVE_CANDIDATE`:

| Repository | Verified upstream/source |
|---|---|
| `unsloth` | `unslothai/unsloth` |
| `GatorEducator__gatorgrader` | `GatorEducator/gatorgrader` |
| `deliverymanager__cordova-plugin-media-capture` | `apache/cordova-plugin-media-capture` source lineage |
| `drydart__flutter_android` | `drydart/flutter_android` |
| `Soroban-Eas__soroban-sas` | `Soroban-Eas/soroban-sas` |
| `eliezerkirubi-sys__quadcopter-rl-control` | `eliezerkirubi-sys/quadcopter-rl-control` |
| `fabastrunck__cli` | `fabastrunck/cli` |
| `lily-contracts` | `Lilly-Protocol/lily-contracts` |

Fork provenance establishes origin, not an active reason to retain the fork.

## Remaining pending review

One authored repository remains intentionally unresolved in addition to the eight fork-retention decisions above:

- `aetherwake-jrpg` — substantial game source and a technical specification exist, and GitHub confirms this is a new non-fork repository created on 2026-09-16; however, no current README/lifecycle statement exists. Implementation volume alone is not being used to infer the intended long-term lifecycle.

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

1. resolve the eight fork-retention decisions;
2. establish `aetherwake-jrpg`'s project-local lifecycle statement;
3. continue correcting stale account/repository authority language where found;
4. execute archival only for candidates satisfying every archive predicate;
5. synchronize DGAF and workspace projections without creating competing sources of truth.

The machine-readable registry remains the canonical account-level lifecycle classification surface. This document is its human-readable companion.