# Ecosystem Repository Lifecycle Architecture

**Status:** DESIGN APPROVED IN CHAT / WRITTEN SPEC AWAITING FINAL REVIEW  
**Date:** 2026-09-16  
**Scope:** `ndrorchestration` GitHub account and its documentation projections  
**Canonical design home:** `ndrorchestration/ndrorchestration` profile repository

## 1. Purpose

The `ndrorchestration` account contains flagship systems, research programs, products, supporting tools, creative work, historical projects, imported repositories, and short-lived experiments. Those categories are not yet represented consistently, so unrelated or superseded repositories can appear equivalent to active authored work.

This design establishes one account-level repository lifecycle and relationship model without making DGAF, Notion, or any other individual project authoritative over unrelated repositories.

Every retained repository should answer three questions clearly:

1. **Why does this repository exist separately?**
2. **What lifecycle state is it currently in?**
3. **What evidence or authority does it own, and what does it explicitly not inherit from other repositories?**

The goal is clarity and provenance, not reducing repository count for appearance alone.

## 2. Authority model

### 2.1 Project-local authority

Each repository remains authoritative for its own source code, tests/CI, project-specific evidence, release/deployment contracts, and project-specific governance or authorization state where applicable.

No account-level lifecycle classification transfers validation, scientific evidence, security claims, production readiness, authorization, or governance authority between repositories.

### 2.2 Account-level lifecycle authority

The `ndrorchestration/ndrorchestration` profile repository owns the **account-level lifecycle map** and public navigation model. It may classify a repository as active, experimental, historical, external, incubating, or an archive candidate, but it does not override project-local implementation or evidence records.

### 2.3 DGAF boundary

`DGAF-Framework` may maintain a bounded projection for repositories that participate in DGAF-related governance, evaluation, or historical lineage. It must not become the canonical account-wide inventory and must not imply DGAF authority over unrelated product, creative, career, or external-reference repositories.

### 2.4 Workspace projections

Notion, Google Drive, dashboards, generated reports, and portfolio pages are projections or coordination surfaces. They point back to the appropriate repository or runtime provider for authoritative implementation/runtime facts.

## 3. Lifecycle vocabulary

Every repository that completes classification receives exactly one primary lifecycle state.

### `ACTIVE_CORE`

A current flagship or strategically important system with a unique responsibility, active development or evidence maintenance, and a clear reason to exist separately.

### `ACTIVE_SUPPORTING`

Maintained supporting infrastructure, reusable tooling, reference material, profile infrastructure, or career-support material. It supports active work but is not itself a flagship system.

### `EXPERIMENTAL`

An active prototype, research track, mathematical investigation, hardware/sensing experiment, or exploratory application. Implementation may be substantial, but claims remain bounded by available evidence.

### `INCUBATING`

A real project idea or scaffold whose identity is not yet mature enough to present as a current system. It needs a concrete purpose and path forward or later reclassification.

### `HISTORICAL`

A superseded or predecessor project retained because provenance, concepts, artifacts, or chronology remain useful. It is not a current implementation or authority surface.

### `EXTERNAL_REFERENCE`

Imported, fork-derived, upstream, dependency-study, benchmark, or third-party code retained for a specific reference or experimentation purpose. It must not be presented as original authored work unless substantial derivative work is documented separately.

### `ARCHIVE_CANDIDATE`

A verified inactive, disposable-test, obsolete integration, superseded placeholder, or no-longer-needed external repository proposed for GitHub archival. Classification alone does not archive the repository.

### `ARCHIVED`

A repository whose GitHub archive state is established. History remains preserved and read-only.

### Classification review status

Lifecycle and review status are separate. Before a lifecycle is accepted, the registry may use:

- `classification_status: VERIFIED`
- `classification_status: PENDING_REVIEW`
- `classification_status: CONFLICTED`

A pending or conflicted repository receives no invented lifecycle merely to complete the census.

## 4. Separate-repository test

A repository should remain an independent long-term repository only when this sentence can be completed clearly:

> **This repository exists separately because it owns _[specific responsibility]_ and no other repository owns that responsibility.**

A repository that cannot pass this test should be evaluated for consolidation, historical classification, incubation, or archival.

Clear examples already include:

- DGAF — governance/evidence/authorization research framework;
- Agent Control Plane — reusable execution-control kernel;
- Collabration — governed human+AI social product;
- Orbit-Driftwatch — observable multi-agent systems showcase;
- Orbit Everyday — local-first interpretation/UX research track;
- MeshSense — companion-layer failure-mode compensation experiment;
- Aetherwake — independent creative/game project.

## 5. Relationship model

Cross-repository relationships are descriptive, not authoritative. The account-level map may use labels such as:

- `FLAGSHIP_OF`
- `SUPPORTS`
- `DERIVED_FROM`
- `HISTORICAL_PREDECESSOR_OF`
- `SHOWCASE_OF`
- `EXPERIMENTS_WITH`
- `EXTERNAL_REFERENCE_FOR`
- `PROVIDER_OR_RUNTIME_COMPANION_TO`

A relationship edge never transfers evidence or authority.

## 6. Initial repository families

These families guide implementation. Exact lifecycle assignments are recorded only after repository-local verification.

### Flagship governance and control

Likely active core/supporting:

- `DGAF-Framework`
- `dgaf-ops`
- `agent-control-plane`
- `sentinel-governance`

### Evaluation and observability

- `Driftwatch`
- `Orbit-Driftwatch`
- `junior-apogee-app`
- `resumeapex-eval`
- `Amethyst-Governance-Eval-Stack`

### Human-facing products and UX

- `Intellectro` repository / canonical product identity **Collabration**
- `orbit-everyday`
- `aoga-dashboard`
- `pptl-governance-dashboard`

The historical provider/repository identifier `Intellectro` may remain operational until provider and provenance dependencies are deliberately migrated. Product identity is Collabration.

### Experimental research

- `phi-calculus-app`
- `AHG-Zeta-Pell-Autonomous-Lattice`
- `Morse-Orchestration`
- `Meshsense`
- `Acoustic-mesh`
- `3d-visualization-hub`

Experimental classification distinguishes implementation/hypothesis from established empirical conclusions; it is not a dismissal of the work.

### Portfolio and career support

- `ndrorchestration`
- `ai-prompt-systems-portfolio`
- `ai-governance-frameworks`
- `prompt-optimization-library`
- `ai-prompt-engineering-portfolio`
- `AI-Prompt-Engineer`
- `career-positioning`
- `automation-scripts`

The implementation pass should identify one canonical public prompt/evaluation portfolio and downgrade duplicative containers to supporting or historical status rather than presenting them as equivalent products.

### Creative work

- `aetherwake-jrpg`
- `SP1`

Creative projects do not need to inherit the AI-governance taxonomy beyond ordinary lifecycle/provenance labeling.

### External/reference and imported repositories

Examples include:

- `unsloth`
- `GatorEducator__gatorgrader`
- `deliverymanager__cordova-plugin-media-capture`
- `drydart__flutter_android`
- `Soroban-Eas__soroban-sas`
- `eliezerkirubi-sys__quadcopter-rl-control`
- similarly named imported/fork-style repositories

Default policy:

1. retain and label `EXTERNAL_REFERENCE` when there is an active, documented reason to keep the repository;
2. classify as `ARCHIVE_CANDIDATE` when it is no longer actively useful;
3. preserve upstream attribution and fork/import provenance;
4. do not count these repositories as original portfolio projects.

### Disposable/test/ambiguous repositories

Examples requiring explicit adjudication:

- `__forktest_1787727107`
- `api`
- `cli`
- `DGAF-Google-AIStudio`
- other effectively empty or narrowly temporary integration repositories

These receive `INCUBATING` only when a real future purpose is documented; otherwise they become `ARCHIVE_CANDIDATE` after verification.

## 7. Canonical lifecycle record

Implementation will create a machine-readable lifecycle registry in the profile repository. Each record should minimally contain:

```yaml
repository: ndrorchestration/example
product_name: Example
classification_status: VERIFIED
lifecycle: ACTIVE_CORE
visibility: public
origin: authored
responsibility: "Owns ..."
canonical_project_source: "https://github.com/ndrorchestration/example"
relationships: []
current_claim_boundary: "Project-local evidence only"
reviewed_at: 2026-09-16
notes: null
```

For an unresolved repository, `classification_status` may be `PENDING_REVIEW` or `CONFLICTED` and `lifecycle` remains null until evidence supports a classification.

Recommended `origin` values are `authored`, `collaborative`, `imported`, `forked`, and `unknown_pending_review`.

Optional fields may include `historical_names`, `upstream_repository`, `replacement_repository`, `runtime_providers`, `portfolio_visibility`, `archive_reason`, and `next_review_due`.

The registry is an account-level classification map, not an implementation SSoT.

## 8. Documentation contract for active repositories

Every `ACTIVE_CORE`, `ACTIVE_SUPPORTING`, or `EXPERIMENTAL` repository should eventually expose, directly or through a concise linked status document:

1. **Purpose** — what the repository owns.
2. **Separate-repository reason** — why that responsibility belongs here.
3. **Current lifecycle/status** — implementation maturity and current activity.
4. **Evidence boundary** — what is and is not established.
5. **Relationship boundary** — what interacts with it and what does not transfer.
6. **Provenance/origin** — authored, collaborative, imported, or fork-derived.

When a repository already communicates these points well, changes should be minimal rather than a rewrite.

## 9. Profile/navigation design

The public profile should not display an exhaustive inventory as if all repositories have equal weight. It should provide:

1. a small featured set of flagship work;
2. grouped secondary work by responsibility/family;
3. a link to the complete lifecycle map;
4. explicit wording that the profile is a curated projection rather than a project-local source of truth.

The human-facing profile should display **Collabration** while retaining the current `Intellectro` repository URL until repository/provider renaming is separately executed.

## 10. Archive policy

Archival is non-destructive and preserves repository history. A repository becomes eligible only after verification that:

- it is not the current canonical source for an active project;
- no active deployment, workflow, package, or documentation contract relies on mutable development there;
- useful unique material has been preserved or linked;
- open work has been adjudicated or explicitly retained as historical provenance;
- upstream/external provenance is retained where applicable;
- the lifecycle registry records the reason.

Deletion is outside scope.

## 11. Implementation sequence

### Phase 1 — Canonical lifecycle map

- inventory all accessible repositories;
- verify origin and lifecycle;
- record the separate-repository responsibility sentence;
- retain uncertain classifications as pending/conflicted rather than guessing;
- create machine-readable and human-readable account-level lifecycle records.

### Phase 2 — Public navigation

- update the profile README to canonical project names and family structure;
- make Collabration the displayed product identity;
- link the complete lifecycle map as secondary navigation;
- keep claims bounded to project-local evidence.

### Phase 3 — High-value repository boundaries

Prioritize public, employer-facing, easily confused, or under-classified repositories. Add minimal boundary wording rather than unnecessary rewrites.

### Phase 4 — Consolidation and historical labeling

- identify duplicative prompt/portfolio repositories;
- preserve unique material before any status change;
- mark superseded projects historical where appropriate;
- avoid destructive history rewrites.

### Phase 5 — External/reference cleanup and archival

- verify active reasons for imported/fork repositories;
- label retained external references;
- archive verified inactive/test/obsolete repositories;
- never archive uncertain repositories solely for aesthetic cleanup.

### Phase 6 — Projection synchronization

After account-level classifications are accepted:

- update DGAF's bounded projection only for DGAF-relevant repositories;
- synchronize Notion/workspace ecosystem records;
- reconcile portfolio/project registries without creating a competing SSoT;
- preserve negative findings and unresolved classifications.

## 12. Safety and evidence rules

The cleanup preserves these invariants:

- no project gains validation because another project is validated;
- no lifecycle label implies production readiness, security certification, scientific efficacy, or authorization;
- historical evidence does not silently transfer to a successor;
- imported repositories are not represented as original authored work;
- no repository is archived while role or dependency status is uncertain;
- no secrets, runtime credentials, or custody material enter documentation;
- repository/provider renames are separate migration events with dependency and provenance checks.

## 13. Success criteria

The redesign is complete when:

1. every retained repository has a verified lifecycle or an explicit `PENDING_REVIEW`/`CONFLICTED` classification status;
2. every current authored project has a distinct responsibility sentence;
3. public navigation emphasizes a small flagship set instead of an undifferentiated inventory;
4. duplicative portfolio/research lineage is labeled or consolidated without losing provenance;
5. external/imported repositories are visibly distinguished from authored work;
6. archive candidates are verified before archival and archived repos retain history;
7. DGAF, Notion, and other projections align with the account-level map without becoming competing authorities;
8. no scientific, production, authorization, or security claim is strengthened merely by reorganization.

## 14. Explicit non-goals

This redesign does not:

- delete repositories;
- rewrite Git history;
- automatically rename repositories or providers;
- merge application code solely to reduce repository count;
- establish production readiness or empirical efficacy;
- change DGAF scientific or authorization state;
- make the profile repository authoritative for project-local implementation or runtime truth.
