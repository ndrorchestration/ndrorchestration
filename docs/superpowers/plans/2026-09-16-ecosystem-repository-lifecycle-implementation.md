# Ecosystem Repository Lifecycle Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Establish a validated account-level repository lifecycle map, align public navigation and high-value repository boundaries to it, and archive only repositories whose inactive/obsolete status is verified.

**Architecture:** The `ndrorchestration/ndrorchestration` profile repository owns the account-level lifecycle classification only. Project repositories remain authoritative for their own implementation/evidence; DGAF and Notion remain bounded projections. A machine-readable JSON registry is validated by a stdlib Python checker and unit tests, with a human-readable lifecycle companion and curated profile README downstream from that registry.

**Tech Stack:** GitHub repositories/API, JSON, Python 3 stdlib, `unittest`, Markdown.

**Spec:** `docs/superpowers/specs/2026-09-16-ecosystem-repository-lifecycle-design.md`

## Global Constraints

- Every classified repository has exactly one lifecycle from `ACTIVE_CORE`, `ACTIVE_SUPPORTING`, `EXPERIMENTAL`, `INCUBATING`, `HISTORICAL`, `EXTERNAL_REFERENCE`, `ARCHIVE_CANDIDATE`, or `ARCHIVED`.
- Review status is separate: `VERIFIED`, `PENDING_REVIEW`, or `CONFLICTED`.
- No account-level classification transfers project-local validation, scientific evidence, security claims, production readiness, authorization, or governance authority.
- No imported/fork-derived repository is represented as original authored work without separately documented derivative evidence.
- No repository is archived while role/dependency status is uncertain.
- Repository renames are separate migration events and are outside this implementation unless separately approved.
- No repository deletion or Git-history rewriting.
- Collabration is the canonical product name; `Intellectro` remains a historical/provider/repository identifier until a separate rename migration.
- DGAF scientific/authorization state is unaffected by this work.

---

### Task 1: Create the canonical lifecycle registry and validator

**Files:**
- Create: `ecosystem/repository-lifecycle.json`
- Create: `scripts/validate_repository_lifecycle.py`
- Create: `tests/test_repository_lifecycle.py`

**Interfaces:**
- Consumes: the live GitHub repository census and approved lifecycle spec.
- Produces: a machine-readable account-level classification registry and `validate_registry(path) -> list[str]` validator used by later tasks.

- [ ] **Step 1: Write the failing validator tests**

Create `tests/test_repository_lifecycle.py` using `unittest`. Cover: valid registry; duplicate repository; invalid lifecycle; invalid review status; `VERIFIED` entry missing responsibility; `EXTERNAL_REFERENCE` missing origin/upstream note; `ARCHIVED` entry whose GitHub archived flag is false in recorded metadata; and a pending entry that is allowed to have lifecycle `null`.

- [ ] **Step 2: Run the tests and verify RED**

Run:

```bash
python -m unittest tests/test_repository_lifecycle.py -v
```

Expected: import/file-not-found failure because the validator and registry do not yet exist.

- [ ] **Step 3: Implement the minimal validator**

Create `scripts/validate_repository_lifecycle.py` with only Python stdlib. Expose:

```python
ALLOWED_LIFECYCLES = {
    "ACTIVE_CORE", "ACTIVE_SUPPORTING", "EXPERIMENTAL", "INCUBATING",
    "HISTORICAL", "EXTERNAL_REFERENCE", "ARCHIVE_CANDIDATE", "ARCHIVED",
}
ALLOWED_REVIEW_STATUSES = {"VERIFIED", "PENDING_REVIEW", "CONFLICTED"}

def validate_registry(path: str) -> list[str]:
    ...
```

The CLI exits `0` when no violations exist and `1` otherwise, printing deterministic one-line violations.

- [ ] **Step 4: Seed the registry from the live GitHub census**

Create `ecosystem/repository-lifecycle.json` with top-level fields:

```json
{
  "schema_version": "1.0.0",
  "generated_at": "2026-09-16",
  "authority_scope": "ACCOUNT_LEVEL_LIFECYCLE_ONLY",
  "repositories": []
}
```

Include every repository returned by the live `ndrorchestration` owner census. Record `repository`, `product_name`, `visibility`, `github_archived`, `origin`, `review_status`, `lifecycle`, `responsibility`, `canonical_project_source`, `relationships`, `current_claim_boundary`, `reviewed_at`, and `notes`.

Use `PENDING_REVIEW` + `lifecycle: null` rather than guessing when repository-local evidence has not yet been checked.

- [ ] **Step 5: Assign high-confidence classifications only**

Initial `VERIFIED` classifications may include repositories already supported by current project-local documentation and/or unambiguous GitHub metadata, including the profile repo, DGAF, Collabration/Intellectro, Agent Control Plane, Orbit-Driftwatch, Orbit Everyday, MeshSense, archived Gold Star QA, and obvious imported/reference naming when upstream/reference provenance is established. Keep uncertain repositories pending.

- [ ] **Step 6: Run registry validation GREEN**

Run:

```bash
python scripts/validate_repository_lifecycle.py ecosystem/repository-lifecycle.json
python -m unittest tests/test_repository_lifecycle.py -v
```

Expected: both PASS.

- [ ] **Step 7: Commit**

```bash
git add ecosystem/repository-lifecycle.json scripts/validate_repository_lifecycle.py tests/test_repository_lifecycle.py
git commit -m "feat(ecosystem): add validated repository lifecycle registry"
```

### Task 2: Create the human-readable lifecycle companion

**Files:**
- Create: `docs/ECOSYSTEM_LIFECYCLE.md`
- Modify: `docs/ECOSYSTEM_INVENTORY.md`

**Interfaces:**
- Consumes: `ecosystem/repository-lifecycle.json`.
- Produces: human-readable lifecycle vocabulary, family map, unresolved queue, and explicit statement that the legacy inventory is a historical/secondary projection.

- [ ] **Step 1: Draft the lifecycle companion from the registry**

Include: authority boundary; lifecycle definitions; current verified classifications grouped by lifecycle/family; pending classifications; external/reference handling; archive criteria; relationship semantics; and a link to the machine-readable registry.

- [ ] **Step 2: Reconcile the legacy inventory**

At the top of `docs/ECOSYSTEM_INVENTORY.md`, add a short notice that `ecosystem/repository-lifecycle.json` is canonical for account-level lifecycle classification and that `ECOSYSTEM_INVENTORY.md` is a human/history projection that must not override project-local truth.

- [ ] **Step 3: Validate references**

Check that every repository named in `docs/ECOSYSTEM_LIFECYCLE.md` exists in the JSON registry and that no lifecycle term outside the approved vocabulary appears as a current classification.

- [ ] **Step 4: Commit**

```bash
git add docs/ECOSYSTEM_LIFECYCLE.md docs/ECOSYSTEM_INVENTORY.md
git commit -m "docs(ecosystem): publish lifecycle map and authority boundary"
```

### Task 3: Reconcile the public profile navigation

**Files:**
- Modify: `README.md`

**Interfaces:**
- Consumes: verified lifecycle classifications and project-local README evidence.
- Produces: curated employer/public navigation that points to the full lifecycle map without presenting every repository as equivalent.

- [ ] **Step 1: Preserve the existing professional positioning and featured-work structure**

Do not expand the profile into a complete inventory.

- [ ] **Step 2: Replace human-facing `Intellectro` product wording with `Collabration`**

Retain the repository URL and add a concise historical-identifier note where needed. Do not claim the repository/provider rename has occurred.

- [ ] **Step 3: Add an ecosystem-navigation section**

Group secondary work into concise families such as governance/control, evaluation/observability, experimental research, and supporting portfolio work. Link `docs/ECOSYSTEM_LIFECYCLE.md` as the complete lifecycle map.

- [ ] **Step 4: Keep external/reference and archive candidates off the featured portfolio surface**

They remain discoverable through GitHub and the lifecycle map but are not presented as original current projects.

- [ ] **Step 5: Verify claims against project-local sources**

Re-read at minimum DGAF, Collabration, Orbit-Driftwatch, Agent Control Plane, Orbit Everyday, and MeshSense before changing their profile summaries.

- [ ] **Step 6: Commit**

```bash
git add README.md
git commit -m "docs(profile): align portfolio navigation with lifecycle map"
```

### Task 4: Verify and classify the remaining authored repositories

**Files:**
- Modify: `ecosystem/repository-lifecycle.json`
- Modify: `docs/ECOSYSTEM_LIFECYCLE.md`

**Interfaces:**
- Consumes: each repository's live metadata, README/status docs, archived flag, and recent purpose evidence.
- Produces: `VERIFIED` lifecycle classifications or explicit `CONFLICTED`/`PENDING_REVIEW` records.

- [ ] **Step 1: Review governance/control repositories**

Verify `dgaf-ops`, `sentinel-governance`, `aoga-dashboard`, `pptl-governance-dashboard`, `Amethyst-Governance-Eval-Stack`, and `Gold-star-standards` against their own current docs before classification.

- [ ] **Step 2: Review evaluation/portfolio repositories**

Verify `Driftwatch`, `junior-apogee-app`, `resumeapex-eval`, `ai-prompt-systems-portfolio`, `ai-prompt-engineering-portfolio`, `AI-Prompt-Engineer`, and `prompt-optimization-library` and identify the canonical public prompt/evaluation portfolio.

- [ ] **Step 3: Review research/creative repositories**

Verify `phi-calculus-app`, `AHG-Zeta-Pell-Autonomous-Lattice`, `Morse-Orchestration`, `Acoustic-mesh`, `3d-visualization-hub`, `aetherwake-jrpg`, `SP1`, and `Agentic-Iteration-Metaconcert-Yaml-AIMY-`.

- [ ] **Step 4: Review supporting/private repositories**

Verify `career-positioning`, `automation-scripts`, `chat-archives`, `entrepreneur-hub`, and `DGAF-Google-AIStudio`.

- [ ] **Step 5: Run validation**

```bash
python scripts/validate_repository_lifecycle.py ecosystem/repository-lifecycle.json
python -m unittest tests/test_repository_lifecycle.py -v
```

Expected: PASS; unresolved entries are explicit rather than guessed.

- [ ] **Step 6: Commit**

```bash
git add ecosystem/repository-lifecycle.json docs/ECOSYSTEM_LIFECYCLE.md
git commit -m "docs(ecosystem): verify authored repository lifecycle states"
```

### Task 5: Verify imported/reference repositories and archive candidates

**Files:**
- Modify: `ecosystem/repository-lifecycle.json`
- Modify: `docs/ECOSYSTEM_LIFECYCLE.md`

**Interfaces:**
- Consumes: GitHub fork/upstream metadata where available, README attribution, repository activity/purpose, dependency references, and archive criteria.
- Produces: explicit `EXTERNAL_REFERENCE`, `ARCHIVE_CANDIDATE`, `INCUBATING`, or `CONFLICTED` classifications.

- [ ] **Step 1: Verify imported/reference provenance**

Review `unsloth`, `GatorEducator__gatorgrader`, `deliverymanager__cordova-plugin-media-capture`, `drydart__flutter_android`, `Soroban-Eas__soroban-sas`, `eliezerkirubi-sys__quadcopter-rl-control`, `fabastrunck__cli`, and any similarly imported names returned by the live census.

- [ ] **Step 2: Verify disposable/ambiguous candidates**

Review `__forktest_1787727107`, `api`, and `cli` for active dependencies, unique material, deployments, workflows, packages, and documentation references.

- [ ] **Step 3: Record archive candidates without archiving uncertain repositories**

Only mark `ARCHIVE_CANDIDATE` when all approved archive predicates are satisfied. Otherwise use `PENDING_REVIEW` or `CONFLICTED`.

- [ ] **Step 4: Validate and commit**

Run the same validator/test suite and commit the registry/doc update.

### Task 6: Apply minimal repository-local boundary documentation

**Files:**
- Modify only repository-local `README.md` or status documents that lack the approved six-part documentation contract.

**Interfaces:**
- Consumes: accepted lifecycle registry classifications.
- Produces: concise local purpose, separate-repository reason, lifecycle/status, evidence boundary, relationship boundary, and provenance/origin statements.

- [ ] **Step 1: Prioritize public/employer-facing ambiguity**

Start with repositories whose identity is easy to confuse with another project: Driftwatch, Sentinel, Junior Apogee, Phi-Calculus, Acoustic Mesh, 3D Visualization Hub, AI Governance Frameworks, and any current public portfolio container.

- [ ] **Step 2: Avoid rewriting repos that already satisfy the contract**

Collabration, Agent Control Plane, Orbit-Driftwatch, Orbit Everyday, and MeshSense already contain strong boundary language; make no cosmetic rewrite unless a concrete inconsistency is found.

- [ ] **Step 3: Add historical/supporting labels to superseded or duplicative containers**

For verified historical/supporting prompt/evaluation repositories, preserve unique content and add a clear pointer to the canonical current portfolio rather than deleting history.

- [ ] **Step 4: Validate each changed repository independently**

Use that repository's existing tests/CI where available; documentation-only changes must not be represented as implementation validation.

- [ ] **Step 5: Commit changes per repository**

Keep commits scoped so each repository can be reviewed or reverted independently.

### Task 7: Archive verified inactive repositories

**Files:**
- Modify: `ecosystem/repository-lifecycle.json`
- Modify: `docs/ECOSYSTEM_LIFECYCLE.md`
- Repository setting mutation: GitHub archive flag for verified candidates only.

**Interfaces:**
- Consumes: `ARCHIVE_CANDIDATE` entries that satisfy every archive predicate.
- Produces: GitHub-archived repositories and registry state `ARCHIVED` with recorded archive reason/date.

- [ ] **Step 1: Recheck every candidate immediately before archival**

Require: not canonical for an active project; no active mutable dependency/deployment/workflow/package contract; unique material preserved/linked; open work adjudicated or retained as history; provenance retained.

- [ ] **Step 2: Archive only verified candidates**

Do not archive `PENDING_REVIEW` or `CONFLICTED` entries.

- [ ] **Step 3: Read back GitHub metadata**

Confirm `archived=true` before changing registry lifecycle to `ARCHIVED`.

- [ ] **Step 4: Validate and commit account-level records**

Run validator/tests and record archive reason/date in the lifecycle map.

### Task 8: Synchronize bounded projections

**Files:**
- Modify as warranted: `DGAF-Framework/registry/ecosystem_registry.json`
- Modify as warranted: Notion/workspace ecosystem records
- Modify: profile lifecycle registry only when new evidence requires it

**Interfaces:**
- Consumes: accepted account-level lifecycle map.
- Produces: bounded projections that align without becoming alternate SSoTs.

- [ ] **Step 1: Update only DGAF-relevant entries in the DGAF projection**

Do not add unrelated creative/career/external repositories merely for account completeness.

- [ ] **Step 2: Preserve DGAF registry semantics**

Its projection must remain project/governance-scoped and must not imply cross-project authority.

- [ ] **Step 3: Synchronize workspace records**

Update Notion/other ecosystem documentation to point to the profile lifecycle registry for account-level classification and project-local sources for implementation/runtime truth.

- [ ] **Step 4: Record unresolved conflicts**

Do not force alignment by choosing whichever source is easiest to edit.

### Task 9: Final verification and hygiene report

**Files:**
- Create: `docs/ECOSYSTEM_LIFECYCLE_RECONCILIATION_2026-09-16.md`

**Interfaces:**
- Consumes: final registry, GitHub metadata, repo-local changes, archive readbacks, and projection synchronization results.
- Produces: evidence-bound completion report with verified classifications, unresolved entries, archived repos, consolidation decisions, and non-effects.

- [ ] **Step 1: Run the canonical validator/test suite**

```bash
python scripts/validate_repository_lifecycle.py ecosystem/repository-lifecycle.json
python -m unittest tests/test_repository_lifecycle.py -v
```

Expected: PASS.

- [ ] **Step 2: Compare registry coverage to the live repository census**

Every live repository must appear exactly once in the account-level registry. Newly discovered repositories may be `PENDING_REVIEW`; omission is not allowed.

- [ ] **Step 3: Verify archive readbacks and public-profile naming**

Confirm archived states from GitHub and confirm public profile human-facing product name is Collabration while repository URL remains historically `Intellectro` until a separate migration.

- [ ] **Step 4: Write the reconciliation report**

Separate verified facts, classification judgments, unresolved conflicts, archive actions, and future rename/consolidation candidates. State explicitly that no project-local scientific, production, security, or authorization state changed merely because of ecosystem reorganization.

- [ ] **Step 5: Commit**

```bash
git add docs/ECOSYSTEM_LIFECYCLE_RECONCILIATION_2026-09-16.md
git commit -m "docs(ecosystem): record lifecycle reconciliation evidence"
```
