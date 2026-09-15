# Erdős #742 — n=25 End-to-End Independent Corroboration Checkpoint

**Date:** 2026-09-15  
**State:** ORDER-25 CANDIDATE STRONGLY CORROBORATED / NOT HUMAN-INDEPENDENTLY VERIFIED / GLOBAL ERDŐS #742 NOT ESTABLISHED AS SOLVED  
**Novelty posture:** `COLLISION_HOLD`

## Review object

Public candidate: `paullenz/MurtySimon742`, reviewer-v2 claim at order 25:

`e(G) <= 156`, with equality exactly `K(12,13)`.

This checkpoint combines the independently rederived graph-theoretic bridge with two independently written finite-review executables. It does not adopt the candidate's scanner implementation as evidence.

## Upper-bound chain at n=25

For a 25-vertex diameter-2-critical graph `G`:

1. **Bipartite branch.** A bipartite diameter-2 graph is complete bipartite. Therefore it has at most `12*13=156` edges.
2. **Delta <= 12.** Degree sum gives `2e(G) <= 25*12=300`, so `e(G)<=150`.
3. **Delta = 13.** The independently rederived witness-deficit inequality excludes `e(G)>=157`. At 156 it forces the complete bipartite equality structure.
4. **Delta = 14, e=157.** Independent dense-case checker reconstructs exactly `59,264` outer states. Thirty-one reach the residual-column stage, producing exactly `1,480` labelled columns; none survives the pre-Hall source-cap refinement.
5. **Delta = 14, e>=158.** Independent Fan-free checker reconstructs the complete remaining domain of `128,666` states after the manuscript's explicit small-k inequalities and leaves zero survivors.
6. **Delta = 15, e=157.** Independent checker reconstructs exactly `108` states; equation (7.2) eliminates all of them.
7. **Delta = 15, e>=158.** Independent Fan-free checker reconstructs exactly `88` remaining states and leaves zero survivors.
8. **Delta = 16, e=157.** Section 5 requires `r>=16`, while the ledger gives `r<=L=15`, so the case is impossible.
9. **Delta = 16, e>=158.** The independently reconstructed remaining Fan-free domain is empty.
10. **Delta >= 17.** The published complement maximum-degree theorem gives `e(G)<=155` after specialization to `n=25`.

These branches cover every possible maximum degree and every edge count above 156.

## Equality chain at e(G)=156

1. **Bipartite case.** Equality in the complete-bipartite bound is exactly `K(12,13)`.
2. **Delta <= 12.** Impossible by degree sum because 156 edges require degree sum 312.
3. **Delta = 13.** Independent witness-deficit/equality rederivation forces a 13-vertex independent set of degree 12 and therefore exactly `K(12,13)`.
4. **Delta = 14.** Independent equality checker reproduces the complete finite relaxation:
   - `k=1`: 401,543 outer states → 3,252,212 labelled columns → 1,788 pre-(9.1) survivors in 130 outer states → all 1,788 rejected by (9.1).
   - `k=2,...,5`: 82,452 outer states → 188,520 labelled columns → 171 pre-(9.1) survivors in 28 outer states → all 171 rejected by (9.1).
   - final survivors: 0.
5. **Delta = 15.** Independent checker reconstructs exactly `211` states; equation (7.2) eliminates all of them.
6. **Delta = 16.** The ledger forces `r=16` and `e(C)=0`, hence `k=0`; equation (6.3) would require `16 <= 16-C(7,2)=-5`, impossible.
7. **Delta >= 17.** Published complement maximum-degree theorem gives `e(G)<=155`.

Thus the checked argument leaves `K(12,13)` as the unique equality object at order 25.

## Independently checked graph bridge

The following manuscript inputs have been source-checked or rederived in Pass 3:

- D2C complement correspondence to `3_t`-critical / `4_t`-supercritical graphs;
- characterization of the `4_t`-supercritical complement case;
- the quasi-edge observation and unique-exception semantics;
- the published `delta(H)<=0.3n` maximum-degree input and its `n=25` specialization;
- the published dominating-edge exclusion and its `n=25` specialization;
- selected-edge convention and reverse-orientation collision prevention;
- complement residual ledger;
- Section 5 residual-activity injection;
- Section 6 small-k injection and formulas;
- Section 7 selected-edge inequalities and pair-capacity bound.

No blocking defect has been found in these checked steps.

## Durable executable evidence

Two reviewer executables now cover the finite numerical layers:

- `independent_n25_relaxation_check.cpp` — Delta=14 equality and Fan-free `m>=158` domains.
- `independent_n25_dense_case_check.cpp` — Delta=14 `e=157`, Delta=15 `e=156/157`, and Delta=16 contradictions.

Workflow:

`.github/workflows/erdos742-n25-independent-review.yml`

The workflow compiles both reviewers and fails if the expected count identities or zero-survivor claims change.

## What is now justified

**SUPPORTED / STRONGLY CORROBORATED:** the public reviewer-v2 fixed-order `n=25` claim has survived an independently implemented numerical replay and a separate source/lemma audit of the main graph-theoretic bridge.

## What is not justified

- Calling the result independently peer reviewed.
- Calling the candidate formally verified end-to-end.
- Claiming community acceptance.
- Claiming the global Murty-Simon conjecture or Erdős #742 solved.
- Claiming novelty for this project; priority collision remains in force.

The public candidate repository itself continues broader finite/general-n work and explicitly keeps external review open.

## Remaining highest-value gates

1. Rebind the reviewer-v2 release objects by independently recomputing their byte hashes and preserve immutable source identities.
2. Run the pinned LeanSMS reproduction baseline in an environment capable of cloning/executing the toolchain; keep it separate from this manuscript route.
3. Seek genuinely independent human mathematical review of the selected/residual bridge and the end-to-end order-25 assembly.
4. Keep PR #18 draft/unmerged while it functions as a review incubator rather than canonical mathematical authority.
5. For the broader open-problem prospecting program, begin the next candidate only under the same same-day collision and evidence-ceiling rules.
