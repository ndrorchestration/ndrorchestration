# Erdős #742 — n=25 Independent Review Pass 2

**Date:** 2026-09-15  
**State:** FINITE RELAXATION REPRODUCED / NO BLOCKING DEFECT FOUND IN CHECKED NUMERICAL LAYER / OVERALL CANDIDATE NOT VERIFIED  
**Review object:** `paullenz/MurtySimon742`, reviewer-v2 claim `e(G) <= 156, equality exactly K(12,13)` at `n=25`.

## Method

A new C++ checker was written from the equations and necessary conditions stated in the reviewer-v2 manuscript. It does **not** execute or copy the candidate repository's enumeration programs.

Reviewer implementation:

`research/open-problem-prospecting/erdos742/independent_n25_relaxation_check.cpp`

The implementation independently constructs:

- nondecreasing `d` degree multisets for the complement-of-`C` relaxation;
- positive nondecreasing residual-degree multisets `rho`;
- equation (7.2) pair-capacity tests;
- source/supplier matching upper bounds;
- the residual-column h-index lower bound;
- every labelled residual column `R` required by the manuscript relaxation;
- the simultaneous supplement-cap refinement; and
- equation (9.1) over every nonempty subset of `A`.

For the Fan-free `m >= 158` layer it separately applies the manuscript's explicit `k=0,1` inequalities before enumerating the complete remaining finite domain.

## Equality band: Delta=14, e(G)=156

### k=1 boundary

Independent output:

| Quantity | Independent count | Reviewer-v2 count |
|---|---:|---:|
| Raw outer states | 401,543 | 401,543 |
| Labelled residual columns | 3,252,212 | 3,252,212 |
| Outer states containing pre-(9.1) survivors | 130 | 130 |
| Pre-(9.1) surviving columns | 1,788 | 1,788 |
| Columns rejected by (9.1) | 1,788 | 1,788 |
| Columns surviving (9.1) | 0 | 0 |

### k=2,...,5

Independent output:

| Quantity | Independent count | Reviewer-v2 count |
|---|---:|---:|
| Raw outer states | 82,452 | 82,452 |
| Labelled residual columns | 188,520 | 188,520 |
| Outer states containing pre-(9.1) survivors | 28 | 28 |
| Pre-(9.1) surviving columns | 171 | 171 |
| Columns rejected by (9.1) | 171 | 171 |
| Columns surviving (9.1) | 0 | 0 |

**Disposition:** the complete numerical relaxation described for the `Delta=14, e=156` equality case is independently reproduced at the count and final-survivor levels.

## Fan-free upper range m>=158

For `n=25`, the manuscript reduces the larger edge-count domain to `Delta in {14,15,16}` and uses its small-`k` inequalities before the outer finite scan.

Independent output:

| Delta | Complete remaining outer domain | Independent survivors | Reviewer-v2 domain/survivors |
|---:|---:|---:|---:|
| 14 | 128,666 | 0 | 128,666 / 0 |
| 15 | 88 | 0 | 88 / 0 |
| 16 | 0 | 0 | 0 / 0 |

The domain counts are themselves independently reconstructed from the allowed `(m,k,r,d,rho)` ranges after applying the manuscript's equations (6.3) and (6.4) to `k=0,1`.

**Disposition:** the reviewer-v2 order-25 Fan-free finite arithmetic is independently reproduced.

## What this strengthens

This pass materially reduces the risk that the candidate's fixed-order result is an artifact of one enumeration implementation. Together with Pass 1, the checked surface now includes:

- Delta=13 witness-deficit arithmetic and equality continuation;
- the six complement-ledger rows;
- Section 5 residual-activity counting;
- Section 6 small-`k` band reductions;
- Section 7 selected-edge/pair-capacity inequalities at the implemented numerical level;
- the complete Delta=14 equality relaxation, including the 1,959 total pre-(9.1) surviving columns and their elimination by (9.1); and
- the complete Fan-free `m>=158` order-25 finite outer domain.

## Evidence ceiling

This result is **independent computational corroboration of the manuscript's finite relaxation**, not an independent proof of all graph-theoretic premises.

It does not by itself establish that every actual diameter-2-critical graph maps into the relaxation unless the upstream complement/quasi-edge lemmas, selected-edge convention, injections, and source-capacity inequalities are all correct under the manuscript's hypotheses.

It also does not establish the global Murty-Simon conjecture or an official resolution of Erdős #742.

## Remaining review obligations

1. Complete a theorem-level audit of the complement/total-domination correspondence and every exceptional case used at order 25.
2. Finish a line-by-line proof audit of the quasi-edge construction, uniqueness/selection semantics, and Section 6/7 injections rather than relying only on successful numerical reproduction.
3. Recompute the reviewer-v2 release hashes from independently fetched bytes and bind this review to immutable candidate objects rather than moving `main`.
4. If practical, obtain genuinely independent human mathematical review of the graph-theoretic bridge. Same-model checking plus an independent implementation is stronger evidence, but it is not community review.
5. Keep the original novelty lane on `COLLISION_HOLD`; use this work only as independent verification/reproduction.

## Automated reproduction

A separate GitHub Actions workflow compiles and runs this checker:

`.github/workflows/erdos742-n25-independent-review.yml`

The executable exits nonzero if any expected reviewer-v2 count differs or if any finite-relaxation survivor remains where the checked claim expects zero.
