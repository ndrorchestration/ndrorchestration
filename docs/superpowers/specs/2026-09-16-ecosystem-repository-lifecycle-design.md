# Ecosystem Repository Lifecycle Architecture

**Status:** APPROVED DESIGN / IMPLEMENTATION NOT STARTED  
**Date:** 2026-09-16  
**Scope:** `ndrorchestration` GitHub account and its documentation projections  
**Canonical design home:** `ndrorchestration/ndrorchestration` profile repository

## 1. Purpose

The `ndrorchestration` account contains flagship systems, research programs, product applications, supporting tools, creative work, historical projects, imported repositories, and short-lived experiments. The current account does not consistently distinguish those categories, which can make unrelated or superseded repositories appear equivalent to active authored work.

This design establishes one account-level repository lifecycle and relationship model without making DGAF, Notion, or any other individual project the authority over unrelated repositories.

The objective is not to reduce the number of repositories for appearance alone. The objective is to make every retained repository answer three questions clearly:

1. **Why does this repository exist separately?**
2. **What lifecycle state is it currently in?**
3. **What evidence or authority does it own, and what does it explicitly not inherit from other repositories?**

## 2. Authority model

### 2.1 Project-local authority

Each repository remains authoritative for its own:

- source code and implementation state;
- repository-local tests and CI;
- project-specific evidence and limitations;
- project-specific release/deployment contracts;
- project-specific governance and authorization state, where applicable.

No account-level lifecycle classification transfers validation, scientific evidence, security claims, production readiness, authorization, or governance authority between repositories.

### 2.2 Account-level lifecycle authority

The `ndrorchestration/ndrorchestration` profile repository owns the **account-level lifecycle map** and public navigation model. It may state that a repository is active, experimental, historical, external, incubating, or an archive candidate, but it does not override project-local implementation or evidence records.

### 2.3 DGAF registry boundary

`DGAF-Framework` may maintain a bounded ecosystem projection for repositories that participate in DGAF-related governance, evaluation, or historical lineage. That projection must not become the canonical account-wide inventory and must not imply DGAF authority over unrelated product, creative, career, or external-reference repositories.

### 2.4 Notion and other workspace projections

Notion, Google Drive, dashboards, generated reports, and portfolio pages are projections or coordination surfaces. They must point back to the appropriate repository or runtime provider for authoritative implementation/runtime facts.

## 3. Lifecycle vocabulary

Every repository considered part of the managed ecosystem receives exactly one primary lifecycle state.

### `ACTIVE_CORE`

A current flagship or strategically important system with a unique responsibility, active development or active evidence maintenance, and a clear reason to exist separately.

### `ACTIVE_SUPPORTING`

A maintained supporting repository such as reusable tooling, reference material, operational infrastructure, profile infrastructure, or career-support material. It supports active work but is not itself a flagship system.

### `EXPERIMENTAL`

An active prototype, research track, mathematical investigation, hardware/sensing experiment, or exploratory application. Its implementation may be substantial, but its claims remain explicitly bounded by available evidence.

### `INCUBATING`

A real project idea or scaffold whose identity is not yet mature enough to present as a current system. Incubating repositories require either a concrete purpose statement and development path or later reclassification.

### `HISTORICAL`

A superseded or predecessor project retained because its provenance, concepts, artifacts, or chronology remain useful. Historical repositories are not current implementation or authority surfaces.

### `EXTERNAL_REFERENCE`

Imported, fork-derived, upstream, dependency-study, benchmark, or third-party code retained for a specific reference or experimentation purpose. These repositories must not be presented as original authored projects unless substantial derivative work is documented separately.

### `ARCHIVE_CANDIDATE`

A verified inactive, disposable-test, obsolete integration, superseded placeholder, or no-longer-needed external repository proposed for GitHub archival. Classification does not itself archive the repository.

### `ARCHIVED`

A repository whose GitHub archive state is established. History remains preserved and read-only.

## 4. Separate-repository test

A repository should remain an independent long-term repository only when this sentence can be completed clearly:

> **This repository exists separately because it owns _[specific responsibility]_ and no other repository owns that responsibility.**

A repository that cannot pass this test should be evaluated for consolidation, historical classification, incubation, or archival.

Examples of valid distinct responsibilities include:

- DGAF: governance/evidence/authorization research framework;
- Agent Control Plane: reusable execution-control kernel;
- Collabration: governed human+AI social product;
- Orbit-Driftwatch: observable multi-agent systems showcase;
- Orbit Everyday: local-first interpretation/UX research track;
- MeshSense: companion-layer failure-mode compensation experiment;
- Aetherwake: independent creative/game project.

## 5. Relationship model

Cross-repository relationships are descriptive, not authoritative. The account-level map may use relationship labels such as:

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

The following families guide implementation. Exact repository classifications will be recorded in the lifecycle registry after repository-local verification.

### 6.1 Flagship governance and control

Likely `ACTIVE_CORE` or `ACTIVE_SUPPORTING`:

- `DGAF-Framework`
- `dgaf-ops`
- `agent-control-plane`
- `sentinel-governance`

### 6.2 Evaluation and observability

Likely `ACTIVE_CORE`, `ACTIVE_SUPPORTING`, `EXPERIMENTAL`, or `HISTORICAL` depending on repository-local evidence:

- `Driftwatch`
- `Orbit-Driftwatch`
- `junior-apogee-app`
- `resumeapex-eval`
- `Amethyst-Governance-Eval-Stack`

### 6.3 Human-facing products and UX

- `Intellectro` repository / canonical product identity **Collabration**
- `orbit-everyday`
- `aoga-dashboard`
- `pptl-governance-dashboard`

The historical provider/repository identifier `Intellectro` may remain operational until provider and provenance dependencies are deliberately migrated. Product identity is Collabration.

### 6.4 Experimental research

- `phi-calculus-app`
- `AHG-Zeta-Pell-Autonomous-Lattice`
- `Morse-Orchestration`
- `Meshsense`
- `Acoustic-mesh`
- `3d-visualization-hub`

Experimental classification must not be interpreted as invalid work; it means implementation and hypotheses are intentionally distinguished from established empirical conclusions.

### 6.5 Portfolio and career support

- `ndrorchestration`
- `ai-prompt-systems-portfolio`
- `ai-governance-frameworks`
- `prompt-optimization-library`
- `ai-prompt-engineering-portfolio`
- `AI-Prompt-Engineer`
- `career-positioning`
- `automation-scripts`

The implementation pass should identify one canonical public prompt/evaluation portfolio and downgrade duplicative portfolio containers to supporting or historical status rather than presenting all of them as equivalent current products.

### 6.6 Creative work

- `aetherwake-jrpg`
- `SP1`

Creative projects do not need to inherit the AI-governance taxonomy beyond ordinary lifecycle/provenance labeling.

### 6.7 External/reference and imported repositories

Examples include:

- `unsloth`
- `GatorEducator__gatorgrader`
- `deliverymanager__cordova-plugin-media-capture`
- `drydart__flutter_android`
- `Soroban-Eas__soroban-sas`
- `eliezerkirubi-sys__quadcopter-rl-control`
- similarly named imported/fork-style repositories

The default policy is:

1. retain and label `EXTERNAL_REFERENCE` when there is an active, documented reason to keep the repository;
2. classify as `ARCHIVE_CANDIDATE` when the repository is no longer actively useful;
3. preserve upstream attribution and fork/import provenance;
4. do not count these repositories as original portfolio projects.

### 6.8 Disposable/test/ambiguous repositories

Examples requiring explicit adjudication include:

- `__forktest_1787727107`
- `api`
- `cli`
- `DGAF-Google-AIStudio`
- other effectively empty or narrowly temporary integration repositories

These should default to `INCUBATING` only when a real future purpose is documented; otherwise they become `ARCHIVE_CANDIDATE` after verification.

## 7. Canonical lifecycle record

Implementation will create a machine-readable lifecycle registry in the profile repository. Each entry should minimally contain:

```yaml
repository: ndrorchestration/example
product_name: Example
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

Additional optional fields may include:

- `historical_names`
- `upstream_repository`
- `replacement_repository`
- `runtime_providers`
- `portfolio_visibility`
- `archive_reason`
- `next_review_due`

The registry is an account-level classification map, not an implementation SSoT.

## 8. Documentation contract for active repositories

Every repository classified `ACTIVE_CORE`, `ACTIVE_SUPPORTING`, or `EXPERIMENTAL` should eventually expose, directly or through a concise linked status document:

1. **Purpose** — what the repository owns.
2. **Separate-repository reason** — why that responsibility belongs here rather than elsewhere.
3. **Current lifecycle/status** — implementation maturity and current activity.
4. **Evidence boundary** — what is and is not established.
5. **Relationship boundary** — which other repositories it interacts with and what does not transfer.
6. **Provenance/origin** — authored, collaborative, imported, or fork-derived.

This contract should be implemented with minimal edits when a repository already communicates these points well.

## 9. Profile/navigation design

The public profile should not display an exhaustive inventory as if all repositories have equal weight. It should present:

1. a small featured set of flagship work;
2. grouped secondary work by responsibility/family;
3. a link to the canonical lifecycle map for the complete inventory;
4. explicit wording that the profile is a curated projection rather than a project-local source of truth.

The Collabration product name should replace Intellectro in human-facing profile copy while retaining the current repository URL until the repository/provider rename is separately executed.

## 10. Archive policy

Archival is non-destructive and preserves repository history. A repository becomes eligible for archival only when the implementation pass verifies that:

- it is not the current canonical source for an active project;
- no active deployment, workflow, package, or documentation contract relies on mutable development in that repository;
- any useful unique material has been preserved or linked;
- open work has been adjudicated or explicitly left as historical provenance;
- upstream/external provenance is retained where applicable;
- the account-level lifecycle registry records the reason.

Deletion is outside the scope of this design.

## 11. Implementation sequence

### Phase 1 — Canonical lifecycle map

- inventory all accessible repositories;
- classify origin and lifecycle;
- record the separate-repository responsibility sentence;
- identify uncertain classifications rather than guessing;
- create the account-level machine-readable registry and human-readable companion.

### Phase 2 — Public navigation

- update the profile README to use the canonical project names and family structure;
- make Collabration the displayed product identity;
- expose the complete lifecycle map through a secondary link rather than cluttering the primary profile;
- keep claims bounded to repository-local evidence.

### Phase 3 — High-value repository boundaries

Prioritize repositories that are public, employer-facing, easily confused with another project, or currently under-classified. Update their README/status documentation with minimal boundary wording rather than unnecessary rewrites.

### Phase 4 — Consolidation and historical labeling

- identify duplicative prompt/portfolio repositories;
- preserve unique material before changing status;
- mark superseded projects historical where appropriate;
- avoid destructive history rewrites.

### Phase 5 — External/reference cleanup and archival

- verify active reasons for imported/fork repositories;
- label retained external references;
- archive verified inactive/test/obsolete repositories;
- never archive uncertain repositories solely for aesthetic cleanup.

### Phase 6 — Projection synchronization

After account-level classifications are accepted:

- update DGAF's bounded ecosystem projection only for relevant DGAF-associated repositories;
- synchronize Notion/workspace ecosystem records;
- reconcile portfolio/project registries without creating a competing SSoT;
- record negative findings and unresolved classifications.

## 12. Safety and evidence rules

The cleanup must preserve the following invariants:

- no project gains validation because another project is validated;
- no lifecycle label implies production readiness, security certification, scientific efficacy, or authorization;
- no historical repository is silently rewritten as though its old evidence applied to a successor;
- no imported repository is represented as original authored work;
- no repository is archived while its role or dependency status is uncertain;
- no secrets, private runtime credentials, or custody material are introduced into documentation;
- repository renames are separate migration events with provider/deployment/provenance checks.

## 13. Success criteria

The redesign is complete when:

1. every retained repository has an account-level lifecycle classification or an explicit unresolved state;
2. every current authored project has a distinct responsibility sentence;
3. public profile/navigation emphasizes a small set of flagship work rather than an undifferentiated inventory;
4. duplicative portfolio/research lineage is labeled or consolidated without losing provenance;
5. external/imported repositories are visibly distinguished from authored work;
6. archive candidates are verified before archival and archived repos retain history;
7. DGAF, Notion, and other ecosystem projections align with the account-level map without becoming competing authorities;
8. no scientific, production, authorization, or security claim is strengthened merely by the reorganization.

## 14. Explicit non-goals

This redesign does not:

- delete repositories;
- rewrite Git history;
- automatically rename repositories or providers;
- merge application code across projects solely to reduce repository count;
- establish production readiness or empirical efficacy;
- change DGAF scientific or authorization state;
- make the profile repository authoritative for project-local implementation or runtime truth.
