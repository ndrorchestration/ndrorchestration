# Erdős #742 Verified Proof-Certificate Pilot

**State:** WRAPPER VERIFIED / LEANSMS RUNTIME NOT EXECUTED HERE / FRONTIER COLLISION HOLD

This directory is an incubator implementation surface for the bounded Erdős #742 / Murty–Simon proof-certificate pilot. The canonical research/scoping record remains in Notion. Nothing in this directory should be read as a proof of the global Murty–Simon conjecture.

## 2026-09-15 collision decision

The same-day audit found a public candidate fixed-order proof project (`paullenz/MurtySimon742`) that claims the full n=25 bound `e(G) <= 156` with equality `K(12,13)`, while explicitly leaving independent mathematical and computational review open. Separate public work (`edisonymy/erdos-lean-research`) already contains LRAT-backed exclusions for restricted order-25 symmetry classes.

Therefore the novelty lane is **COLLISION_HOLD**. The authorized direction is independent verification/reproduction, not a competing n=25 priority claim. This hold is encoded in `pilot_config.json`, `frontier_contract.json`, and `collision_audit_2026-09-15.json` and is enforced by `authorize_frontier`.

## Trust anchor

Pinned upstream:

- `leansolving/leansms`
- commit `8fa708e4c8a00a8951dadc5c0f68863d057fcfab`
- Lean `leanprover/lean4:v4.24.0-rc1`
- mathlib `v4.24.0-rc1`
- LRAT proof certificates
- SMS symmetry clauses verified in Lean
- final certificate checking in Lean

## What the wrapper does

The Python wrapper binds run parameters, exact commands, artifact hashes, toolchain identity, collision-audit state, formal-encoding readiness, and evidence classification into a manifest that can be independently revalidated.

It deliberately does **not** reimplement the graph mathematics. LeanSMS remains the mathematical verification layer.

## Baseline ladder

Run these only in an environment where the pinned LeanSMS checkout and SMS dependencies are installed:

```bash
lake exe murty-simon-generate 9
lake exe murty-simon-generate 13
lake exe murty-simon-generate 14
```

Interpretation:

- `n=9`: smoke test of the installed pipeline.
- `n=13`: reproduce the published 2026 end-to-end LeanSMS Murty–Simon baseline.
- `n=14`: first extension stress test. It is **not verified in this repository** unless a retained manifest and proof artifacts demonstrate that the run completed and checked successfully.

## Expected retained artifacts

For a successful LeanSMS generation run, retain at least:

- base CNF;
- symmetry-clause JSON;
- extended CNF;
- LRAT proof;
- complete command/stdout/stderr log;
- theorem source or theorem-instantiation source when produced;
- reproducibility manifest containing hashes and environment identity.

A missing or hash-mismatched required artifact fails validation closed.

## Evidence vocabulary

- `GENERATED`: artifacts were produced; no proof claim.
- `SOLVER_UNSAT`: solver exit status only; not a certified result.
- `LRAT_VERIFIED`: LRAT verifies against the exact extended CNF.
- `LEAN_VERIFIED`: the Lean verification layer closes over the retained result.
- `NOT_REFUTED_WITHIN_BUDGET`: timeout/resource ceiling; no mathematical conclusion.
- `BRANCH_VERIFIED`: reserved for an exact n=25/e=157/Delta=d branch after formal branch encoding and collision audit gates close.

## n=25 frontier is fail-closed

The currently scoped finite frontier is source-bound as:

- `n = 25`
- `e(G) = 157`
- `Delta(G) in {13,14,15,16,17}`

The generic upstream command `murty-simon-generate 25` is **not** a valid substitute for these branch contracts: upstream `encodeMurtySimon` searches the broader D2C/non-bipartite property with an edge lower bound, not exact `e=157` and exact `Delta=d`.

The wrapper therefore refuses to produce a frontier command unless:

1. a branch-specific formal encoding is explicitly marked ready;
2. the complete same-day collision audit passes;
3. exact frontier parameters and upstream identity match the pinned contract;
4. the recorded frontier status is explicitly changed to `READY_FOR_AUTHORIZATION` after review.

The emitted executable name `murty-simon-frontier-generate` is a future branch-specific interface. It is not claimed to exist upstream today. Do not create or run it until the Lean encoding and proof obligations are actually implemented and compiled.

## Collision audit

Before any novel frontier computation, the audit must cover:

- canonical Erdős problem status page;
- discussion/forum surface;
- arXiv/math.CO;
- GitHub;
- Zenodo/artifact repositories;
- recent papers/preprints.

The dated 2026-09-15 audit found a priority collision and the canonical Erdős page was also inaccessible to direct same-day fetch. The resulting state is `COLLISION_HOLD`; frontier novelty authorization remains closed.

## Resource ceilings

Initial operational ceilings are intentionally provisional:

- feasibility probe: at most 60 minutes wall-clock per Delta branch;
- first full branch: at most 24 hours wall-clock.

A timeout is recorded only as `NOT_REFUTED_WITHIN_BUDGET`.

## Wrapper tests

From the repository root:

```bash
pytest research/open-problem-prospecting/erdos742/tests -q
python -m py_compile \
  research/open-problem-prospecting/erdos742/harness.py \
  research/open-problem-prospecting/erdos742/validate_manifest.py
```

These tests validate provenance and fail-closed orchestration semantics. They are **not** mathematical verification of Erdős #742.

## Current execution limitation

The environment used to stage this branch could inspect GitHub through the connected GitHub integration but could not resolve `github.com` from its local execution container. Consequently the actual LeanSMS/SMS baseline reproduction is recorded as `NOT_EXECUTED` here. The next runtime step belongs in a suitable environment such as Codespaces or another system capable of installing and running the pinned dependencies.
