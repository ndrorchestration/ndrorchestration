# Ecosystem Repository Lifecycle Reconciliation — 2026-09-16

## Scope

This reconciliation establishes an account-level lifecycle and navigation model for repositories owned by `ndrorchestration` without transferring project-local implementation, evidence, runtime, scientific, security, or authorization state between projects.

Canonical machine-readable classification:

- `ecosystem/repository-lifecycle.json`

Human-readable companion:

- `docs/ECOSYSTEM_LIFECYCLE.md`

Design and implementation records:

- `docs/superpowers/specs/2026-09-16-ecosystem-repository-lifecycle-design.md`
- `docs/superpowers/plans/2026-09-16-ecosystem-repository-lifecycle-implementation.md`

## Verified census

The connected GitHub owner census contains 47 repositories. The lifecycle registry represents all 47 exactly once.

Current classification state:

- 38 `VERIFIED`
- 9 `PENDING_REVIEW`
- 0 `CONFLICTED`
- 3 `ARCHIVE_CANDIDATE`
- 1 already `ARCHIVED`

The registry validator was developed test-first. The focused unit suite contains eight tests covering valid registries, duplicate rejection, lifecycle/review vocabulary, verified-entry responsibility requirements, external-origin requirements, archive-state consistency, and unresolved pending-review behavior. The focused suite passed 8/8 locally before the registry was admitted.

## Major corrections completed

### Account-level authority

The profile repository is now the designed canonical home for **account-level repository lifecycle classification and public navigation only**.

It is not authoritative for project-local source, test results, runtime facts, scientific state, security claims, or authorization.

DGAF remains authoritative only for its own DGAF/PDMAL project-local governance/evidence state. Notion, Google Drive, dashboards, and other workspace records remain projections or coordination surfaces.

### Public profile

The profile now:

- presents **Collabration** as the canonical human-facing product identity while retaining the `Intellectro` repository/provider identifier for provenance;
- keeps a deliberately small featured-project surface;
- groups secondary work by responsibility rather than presenting every repository as an equivalent current product; and
- links to the complete lifecycle map for account-wide classification.

### Prompt/portfolio lineage

Repository-local documentation supports the following separation:

- `ai-prompt-systems-portfolio` — current public prompt/evaluation portfolio (`ACTIVE_SUPPORTING`);
- `ai-prompt-engineering-portfolio` — v1 private predecessor (`HISTORICAL`);
- `AI-Prompt-Engineer` — earlier private predecessor (`HISTORICAL`);
- `prompt-optimization-library` — v0 baseline/methodology predecessor (`HISTORICAL`).

This removes the appearance that four repositories are competing current prompt products while preserving their provenance.

### Historical authority wording

Separate documentation corrections were prepared and merged in owning repositories:

- `ndrorchestration/.github` — removed the stale claim that Notion owns portfolio lifecycle/disposition and pointed account-level lifecycle authority to the profile registry while preserving project-local authority.
- `ndrorchestration/chat-archives` — removed current-sounding “Governed by Agent Amethyst” / DGAF-governance wording from the archive README and explicitly treated persona/governance terminology as historical provenance.

Archived records themselves were not rewritten.

## Fork and external provenance

GitHub metadata verified these repositories as fork-derived:

- `unsloth` → `unslothai/unsloth`
- `GatorEducator__gatorgrader` → `GatorEducator/gatorgrader`
- `deliverymanager__cordova-plugin-media-capture` → Apache Cordova media-capture source lineage
- `drydart__flutter_android` → `drydart/flutter_android`
- `Soroban-Eas__soroban-sas` → `Soroban-Eas/soroban-sas`
- `eliezerkirubi-sys__quadcopter-rl-control` → `eliezerkirubi-sys/quadcopter-rl-control`
- `fabastrunck__cli` → `fabastrunck/cli`
- `lily-contracts` → `Lilly-Protocol/lily-contracts`

Fork provenance is recorded separately from lifecycle. These remain `PENDING_REVIEW` until an active retention purpose or archive rationale is established; being a fork is not itself a reason to archive or retain.

## Archive candidates

Three repositories have sufficient evidence for `ARCHIVE_CANDIDATE` classification:

- `cli` — minimal Go stub with no established current ecosystem responsibility;
- `__forktest_1787727107` — disposable fork test of `octocat/Hello-World`, with no operational account references found outside cleanup records;
- `DGAF-Google-AIStudio` — generic AI Studio scaffold with no established current DGAF implementation responsibility or operational account references found outside cleanup records.

Issue #26 in the profile repository records the final archive gate.

The connected GitHub toolset does not expose a repository-settings mutation for the `archived` property. Therefore no repository has been falsely represented as archived. Each candidate remains `ARCHIVE_CANDIDATE` until an authorized archive action occurs and GitHub metadata is read back with `archived=true`.

## Existing archive

`gold-star-qa-framework` is already GitHub-archived and is classified `ARCHIVED` as historical Gold Star QA provenance.

## Remaining unresolved classifications

Nine repositories remain intentionally unresolved:

- eight fork-retention decisions listed above; and
- `aetherwake-jrpg`.

`aetherwake-jrpg` is a new private non-fork repository with substantial JavaScript source and a technical specification, but no current README/lifecycle statement. The reconciliation does not infer long-term lifecycle from implementation volume alone.

No unresolved repository was assigned a lifecycle merely to make the census appear complete.

## Evidence and authority non-effects

This reorganization does not:

- establish production readiness for any project;
- establish security certification or compliance;
- transfer empirical evidence between repositories;
- strengthen or weaken DGAF/PDMAL scientific results;
- authorize any experiment or primary analysis;
- change DGAF's fail-closed scientific state;
- make a historical or external repository first-party current work; or
- make the profile registry authoritative for project-local implementation/runtime truth.

For DGAF specifically, repository-lifecycle hygiene has **zero scientific or primary-analysis authorization effect**.

## Next controlled actions

1. Resolve the eight fork-retention decisions based on actual continuing use.
2. Add a project-local identity/lifecycle statement to `aetherwake-jrpg` before assigning its account lifecycle.
3. Execute the archive gate in issue #26 through a tool/account surface that can mutate repository settings, then read back `archived=true` before changing lifecycle records.
4. Synchronize the accepted account-level classifications into Notion/workspace projections without making those projections competing authorities.
5. Keep future repository additions fail-closed: add them as `PENDING_REVIEW` until origin, responsibility, and lifecycle are supported by evidence.
