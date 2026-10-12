# Ndr Repository Lifecycle Map

**Status:** ACTIVE ACCOUNT-LEVEL CLASSIFICATION  
**Authority scope:** `ACCOUNT_LEVEL_LIFECYCLE_ONLY`  
**Machine-readable source:** [`../ecosystem/repository-lifecycle.json`](../ecosystem/repository-lifecycle.json)  
**Lifecycle classifications reviewed:** 2026-09-24  
**Connected owner census reconfirmed:** 2026-09-28

## Historical DGAF documentation overlay — 2026-09-28

- `ndrorchestration/DGAF-Framework` protected `main`: `728a5a5ba63e63952f7c3c717239bd4dbdcd92b5`.
- Primary current-facing repository state: `docs/CURRENT_STATE.md`, reconciled through merged PR #1116.
- Accepted architecture authority: PR #1089 architecture governance; PR #1041 is historical/superseded/unmerged.
- This overlay does not alter repository lifecycle classification or promote scientific, efficacy, independent-validation, runtime, or High-Assurance state.

## Capability navigation — 2026-10-12

**Scope:** the 27 repositories supplied for this reorganization. This is a navigation and responsibility mapping, not a fresh account census, dependency lockfile, completeness certification, or evidence promotion. Repository metadata and README identities were read on 2026-10-12; lifecycle labels below are retained from the existing account registry, whose review dates remain authoritative.

The supplied account URL is the profile entry point, not an additional repository. The concatenated chat-archives / ai-prompt-engineering-portfolio URL has been split into two entries. Private repositories are labeled; their links require access. No private artifact contents are reproduced here beyond existing account-level responsibility descriptions.

### Governance, evidence & authorization

| Repository | Responsibility | Retained lifecycle | Visibility / GitHub archive state |
| --- | --- | --- | --- |
| [DGAF-Framework](https://github.com/ndrorchestration/DGAF-Framework) | DGAF governance, evidence, authorization, provenance, and experiment-control framework. | ACTIVE_CORE | public |
| [ai-governance-frameworks](https://github.com/ndrorchestration/ai-governance-frameworks) | Experimental governance-framework mappings, templates, and research. | EXPERIMENTAL | public |

### Execution, operations & CI integrity

| Repository | Responsibility | Retained lifecycle | Visibility / GitHub archive state |
| --- | --- | --- | --- |
| [agent-control-plane](https://github.com/ndrorchestration/agent-control-plane) | Reusable experimental agent execution-control kernel. | ACTIVE_SUPPORTING | public |
| [sentinel-governance](https://github.com/ndrorchestration/sentinel-governance) | Experimental CI/CD integrity and reviewable repair-proposal operator. | EXPERIMENTAL | public |
| [automation-scripts](https://github.com/ndrorchestration/automation-scripts) | Reusable ecosystem maintenance and organization utilities. | ACTIVE_SUPPORTING | private |
| [dgaf-ops](https://github.com/ndrorchestration/dgaf-ops) | Private DGAF operational and historical working records. | ACTIVE_SUPPORTING | private |
| [.github](https://github.com/ndrorchestration/.github) | Shared account community-health defaults and evidence conventions. | ACTIVE_SUPPORTING | public |

### Evaluation, rubrics & drift

| Repository | Responsibility | Retained lifecycle | Visibility / GitHub archive state |
| --- | --- | --- | --- |
| [resumeapex-eval](https://github.com/ndrorchestration/resumeapex-eval) | Goldcanstaytoday protocol and reproducible evaluation harness. | EXPERIMENTAL | public |
| [junior-apogee-app](https://github.com/ndrorchestration/junior-apogee-app) | Experimental AI evaluation and QA workbench. | EXPERIMENTAL | public |
| [Driftwatch](https://github.com/ndrorchestration/Driftwatch) | Experimental drift-detection and evaluation track. | EXPERIMENTAL | public |
| [Amethyst-Governance-Eval-Stack](https://github.com/ndrorchestration/Amethyst-Governance-Eval-Stack) | Experimental multi-agent evaluation and orchestration framework. | EXPERIMENTAL | private |
| [Gold-star-standards](https://github.com/ndrorchestration/Gold-star-standards) | Current internal evaluation rubrics and project-defined standards. | ACTIVE_SUPPORTING | private |

### Dashboards & evidence projection

| Repository | Responsibility | Retained lifecycle | Visibility / GitHub archive state |
| --- | --- | --- | --- |
| [aoga-dashboard](https://github.com/ndrorchestration/aoga-dashboard) | Older experimental AOGA API/dashboard and runtime-evidence surface. | EXPERIMENTAL | private |
| [pptl-governance-dashboard](https://github.com/ndrorchestration/pptl-governance-dashboard) | Experimental PPTL/Herald dashboard and persistence prototype. | EXPERIMENTAL | private |

### Spatial, acoustic & mathematical research

| Repository | Responsibility | Retained lifecycle | Visibility / GitHub archive state |
| --- | --- | --- | --- |
| [3d-visualization-hub](https://github.com/ndrorchestration/3d-visualization-hub) | Experimental multidimensional visualization research surfaces. | EXPERIMENTAL | public |
| [Acoustic-mesh](https://github.com/ndrorchestration/Acoustic-mesh) | Experimental audio, signaling, and acoustic-mesh engineering track. | EXPERIMENTAL | public |
| [AHG-Zeta-Pell-Autonomous-Lattice](https://github.com/ndrorchestration/AHG-Zeta-Pell-Autonomous-Lattice) | Experimental AHG control-plane simulation and audit track. | EXPERIMENTAL | public |

### Prompt systems, portfolio & commercialization

| Repository | Responsibility | Retained lifecycle | Visibility / GitHub archive state |
| --- | --- | --- | --- |
| [ai-prompt-systems-portfolio](https://github.com/ndrorchestration/ai-prompt-systems-portfolio) | Current public prompt-systems and evaluation portfolio. | ACTIVE_SUPPORTING | public |
| [ndrorchestration](https://github.com/ndrorchestration/ndrorchestration) | Account portfolio navigation and lifecycle classification. | ACTIVE_SUPPORTING | public |
| [career-positioning](https://github.com/ndrorchestration/career-positioning) | Private career strategy and paid-opportunity evidence records. | ACTIVE_SUPPORTING | private |
| [entrepreneur-hub](https://github.com/ndrorchestration/entrepreneur-hub) | Commercialization and governance-template support track. | ACTIVE_SUPPORTING | public |

### Historical lineage & placeholders

| Repository | Responsibility | Retained lifecycle | Visibility / GitHub archive state |
| --- | --- | --- | --- |
| [AI-Prompt-Engineer](https://github.com/ndrorchestration/AI-Prompt-Engineer) | Historical private prompt-engineering portfolio archive. | HISTORICAL | private |
| [ai-prompt-engineering-portfolio](https://github.com/ndrorchestration/ai-prompt-engineering-portfolio) | Private v1 prompt-engineering portfolio archive. | HISTORICAL | private |
| [prompt-optimization-library](https://github.com/ndrorchestration/prompt-optimization-library) | Historical v0 prompt-optimization baseline and methodology archive. | HISTORICAL | private |
| [chat-archives](https://github.com/ndrorchestration/chat-archives) | Historical conversation, protocol, and research archive. | HISTORICAL | private |
| [gold-star-qa-framework](https://github.com/ndrorchestration/gold-star-qa-framework) | Historical Gold Star QA framework archive. | ARCHIVED | private · archived |
| [api](https://github.com/ndrorchestration/api) | Historical generic API evidence-status record. | HISTORICAL | private |

### Relationship and dependency boundaries

| From / consumer | Relationship | Source / owner | Evidence scope and remaining gate |
| --- | --- | --- | --- |
| Tektite | PROJECTS / EXPLAINS | DGAF state and ACP status | Human-facing representation; projection never authorizes execution or proves enforcement. Static replay is distinct from live integration. |
| DGAF ↔ ACP | PROPOSED_COMPOSITION / SEPARATE_OWNERS | DGAF adjudication; ACP admission and execution | [ACP handoff](https://github.com/ndrorchestration/agent-control-plane/blob/main/docs/ECOSYSTEM_HANDOFF.md) requires a reproducible integration artifact/test. No ecosystem-wide production integration is asserted. Execution receipts require fresh adjudication for follow-on effects. |
| ResumeApex / Driftwatch | MAPS_TO | [Common Evaluation Object Model](https://github.com/ndrorchestration/ai-prompt-systems-portfolio/blob/main/specs/common_evaluation_object_model_v0.md) | Shared evaluation vocabulary; local scoring remains local, evidence_transfer=false, authorization_effect=NONE. This is semantic interoperability, not a shared runtime dependency. |
| Sentinel | REQUIRES_FOR_CONFIGURED_OPERATION | GitHub webhook/App configuration and external orchestrator | [Local operator contract](https://github.com/ndrorchestration/sentinel-governance#current-operator-model); observe mode skips mutation, repair mode proposes a structurally gated PR. Correct repair still requires review and verification. |
| Prompt v0/v1 archives | PREDECESSOR_OF | ai-prompt-systems-portfolio | Historical lineage, not concurrent active portfolio authorities. AI-Prompt-Engineer remains historical too. |
| AOGA / PPTL dashboards | RELATED_PROJECTION_TRACK | Project-local contracts | Separate experimental dashboard responsibilities; code-level duplication and accepted integration are not established by grouping. |
| Acoustic / spatial / AHG research | CONCEPTUALLY_RELATED | Separate research repositories | Shared vocabulary or mathematical constants do not establish runtime dependency, detector efficacy, physical accuracy, or DGAF validity. |
| api / dgaf-ops / chat-archives | HISTORICAL_OR_OPERATIONAL_SUPPORT | Project-local owning repositories | api is not the shared ecosystem API; operations and archives do not own current scientific or authorization state. |

A runtime dependency requires an exact consumer/source binding, interface or package/version, reproducible composition test, and its own evidence boundary. A navigation link, common pattern, role name, or dashboard view is insufficient. Do not merge AOGA/PPTL/Tektite, Driftwatch/Orbit-Driftwatch, or the evaluation repositories merely because they share a capability group.

### Alignment with existing maps

The [Notion Capability Graph](https://app.notion.com/p/3ecf5bad238b8189966fc7c26463de86) owns workspace composition and discovery records; this account map owns GitHub navigation/lifecycle only. Its inspected record explicitly retains graph completeness as NOT ESTABLISHED and CGAP-12 as blocked. This update does not recount its nodes/edges or insert purportedly verified dependencies.

The [DGAF registry](https://github.com/ndrorchestration/DGAF-Framework/blob/main/registry/ecosystem_registry.json) is a bounded DGAF projection and explicitly marks its September 16 projection STALE. It must not supersede this account inventory or project-local current state. This reorganization does not refresh runtime identity or promote that registry's status.

Repository nodes and capabilities are different: Governed Repo, Evidence Gate, ClaimGraph, Assurance Profiles, CEP, and Tektite can be capabilities within owning repositories. Adding those names to a capability graph does not require creating or pretending there is a separate repository for each.

### Review and change receipt

- Before: profile navigation emphasized selected projects; this map classified lifecycle without grouping the supplied inventory by capability.
- After: all 27 supplied repositories have one primary navigation group, retained lifecycle, responsibility, visibility, and relationship boundaries.
- Supporting source: repository-lifecycle.json blob `15dfebf088e33185666499ce792a8a0fde4189ba`; live GitHub metadata and README reads on 2026-10-12. Lifecycle review dates were not reset.
- Common evaluation contract blob: `db1947f3060b6cbdfa2efecea8f72566f9e8bc9f`; ACP handoff blob: `6b1059a5f6c89b806174818a06cbf952123f4672`.
- Unchanged ceilings: SCIENTIFIC_N_INCREMENT=0; INDEPENDENT_VALIDATION=NOT_ESTABLISHED; CANONICAL_DGAF_EFFICACY=NOT_ESTABLISHED; HIGH_ASSURANCE=NOT_AUTHORIZED.
- Remaining audit work: exact package/import/workflow/runtime dependency census; accepted versus draft integration bindings; graph export and deterministic integrity analytics. None is represented as completed here.

## Authority boundary

This document classifies how repositories relate to the `ndrorchestration` account. It does **not** override repository-local source code, tests, CI, evidence, runtime facts, governance state, scientific state, security claims, or authorization.

Project repositories remain authoritative for their own implementation and evidence. Runtime providers remain authoritative for runtime facts. DGAF may maintain a bounded DGAF-related projection, but it is not the canonical account-wide repository inventory. Cross-repository relationships are descriptive only and never transfer validation or authority.

## Retained September census

The September connected GitHub owner census recorded **48 repositories** (historical count; not re-established by the scoped October 12 review):

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
- `coherence-control-benchmark` — private AI evaluation/orchestration-control benchmark prototype; `INCUBATING` with `PENDING_REVIEW`. The repository README now states the intended identity and evidence boundary; executable verification remains the promotion gate.

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

- `coherence-control-benchmark` — `PENDING_REVIEW`. The README now reconciles the intended identity and explicit evidence boundary on `main`. Fresh-checkout install, typecheck, build, and any benchmark-specific verification remain **NOT VERIFIED** for lifecycle promotion. Keep the repository out of the public portfolio until executable verification completes and the implementation/evidence surface is re-audited.

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