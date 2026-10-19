# Erdős #742 — n=25 Candidate Independent Review Checkpoint

**Date:** 2026-09-15  
**Review state:** PARTIAL REVIEW / NO BLOCKING DEFECT FOUND IN CHECKED SUBSET / OVERALL CLAIM NOT VERIFIED  
**Purpose:** Redirect the original novelty pilot into independent verification after a same-day priority collision.

## Review object

Public candidate repository:

- `paullenz/MurtySimon742`
- repository head observed during this review: `66a2c41a7389e07c4bfaf29fde914cc9b046c7bb` (2026-09-15 10:32:31Z)

The proof object is pinned by the repository's own reviewer-v2 manifest rather than by a moving `main` branch:

- claim: `e(G) <= 156, equality exactly K(12,13)` at `n=25`
- `N25_Reviewer_Manuscript_v2.md` SHA-256: `0c7334aa3f3d3179726765f30da578ef3b35d84a238a85c0a373f9f84918c2d5`
- `N25_Verification_Companion_v2.md` SHA-256: `cfa24af8fad8a4a28f15f2fcaca0b2673802bb4151bcbfa82313d6041eff4d58`
- reviewer-v2 manifest states `external_review_complete: false`

This checkpoint does not accept the candidate merely because its repository workflows or internal audits are green.

## Independently checked in this pass

### 1. Delta=13 witness-deficit arithmetic

The manuscript sets `T = 325 - 2e(G)` and derives

`e(G) <= C(h,2) + h(25-h) + o(o-1)`, with `2h+o <= T`.

Substituting the largest allowed `o=T-2h` reproduces the manuscript table exactly:

| h | e=157 (T=11) | e=156 (T=13) |
|---:|---:|---:|
| 0 | 110 | 156 |
| 1 | 96 | 134 |
| 2 | 89 | 119 |
| 3 | 89 | 111 |
| 4 | 96 | 110 |
| 5 | 110 | 116 |
| 6 | impossible | 129 |

This independently confirms the finite arithmetic in that step.

The equality continuation is also internally coherent on direct rederivation: at 156 edges the table forces `h=0,o=13`; all witnesses then lie in the 13-vertex `O` set. The bound

`156 <= |D[O]| + 2|S[O]| <= e(G[O]) + 2(C(13,2)-e(G[O])) = 156-e(G[O])`

forces `e(G[O])=0`; each O vertex has degree 12 and therefore is adjacent to all 12 vertices outside O, yielding exactly `K(12,13)`.

**Checkpoint status:** SUPPORTED BY INDEPENDENT REDERIVATION. This is not a formal proof audit of every premise used to define the witness classes.

### 2. Complement ledger arithmetic

For `M=300-e(G)`, `a=24-Delta`, `b=Delta`,

`L=M-a-C(b,2)` and `t=C(a,2)-L`.

Independent recomputation exactly matches all six manuscript rows:

| e(G) | Delta | a | b | L | t |
|---:|---:|---:|---:|---:|---:|
| 157 | 14 | 10 | 14 | 42 | 3 |
| 156 | 14 | 10 | 14 | 43 | 2 |
| 157 | 15 | 9 | 15 | 29 | 7 |
| 156 | 15 | 9 | 15 | 30 | 6 |
| 157 | 16 | 8 | 16 | 15 | 13 |
| 156 | 16 | 8 | 16 | 16 | 12 |

The identities

- `e(C)+r=L`,
- `e(F)=r+t`,
- `sum d_i=2(r+t)`,
- `sum rho_b=r`, and
- `Q>=r+2t`

follow from the stated selected-edge convention, edge partition, and minimum-degree condition, provided the complement/quasi-edge setup used by the manuscript is valid.

**Checkpoint status:** ARITHMETIC VERIFIED; GRAPH-THEORETIC PRECONDITIONS STILL REQUIRE SOURCE/LEMMA AUDIT.

### 3. Section 5 residual-activity lemma

The manuscript argues that no `B` vertex can have residual degree zero when `t>0`.

A direct rederivation finds the core counting internally consistent under its selected-edge convention:

- if `rho_b=0`, every A-neighbour of b is selected;
- their B-exception labels are distinct because selection is indexed by missing unordered B-pairs;
- an F-edge between S=N_A(b) and T=A\S would leave a non-exception A vertex undominated by a selected edge, so there are no F edges across S,T;
- every F-edge inside S forces two distinct residual A-B edges;
- every F-edge inside T forces one distinct residual A-B edge whose exception lies in A, so it cannot itself be selected;
- these two forced families have A-endpoints in disjoint sets S and T.

Hence `r >= 2e(F[S])+e(F[T]) = e(F)+e(F[S]) >= r+t`, contradicting `t>0`.

**Checkpoint status:** NO BLOCKING DEFECT FOUND IN FIRST-PASS REDERIVATION. The upstream complement criticality/quasi-edge theorem and uniqueness semantics remain separate dependencies to verify from primary sources.

## Not yet independently verified

These are the current proof-critical review obligations, in order:

1. **Published complement reductions.** Verify exact hypotheses, exceptional cases, parity/diameter-three handling, and numerical specialization of the Dailly–Foucaud–Hansberg and Haynes–Henning–van der Merwe–Yeo inputs.
2. **Quasi-edge construction and uniqueness.** Re-derive the complement 3-total-domination-edge-critical implications used to create selected edges and unique exceptions.
3. **Section 6 small-k injections.** Check every distinctness claim and the `b <= r-m` injection, including k=0/1 formulas and all endpoint-disjointness assumptions.
4. **Section 7 selected-pair/source-cap inequalities.** Verify `ell_j` pair-capacity bound, closure inequalities, repeated-value treatment, and source-cap monotonicity.
5. **Section 8 finite relaxation completeness.** Confirm that every actual graph satisfying the prior lemmas maps into an enumerated state; retaining nongraphical states is safe only if no graphical state is omitted.
6. **Section 9 subset-capacity inequality.** Re-derive equation (9.1), verify its source caps are valid upper bounds, and verify the claimed complete coverage of all surviving labelled columns.
7. **Fan-free m>=158 reduction.** Reproduce the outer-state enumerator independently or derive an alternate checker; do not rely only on the project's same-assistant implementation agreement.
8. **Equality chain outside Delta=13.** Independently reproduce the Delta=14 equality-column coverage and verify Delta=15/16 exclusion at 156 edges.
9. **Artifact provenance.** Recompute reviewer-v2 hashes and, where computational claims are proof-critical, independently execute or reimplement the relevant verifier against pinned input artifacts.
10. **External mathematical review boundary.** Even a complete local replay would remain independent computational evidence, not community acceptance or an official resolution of Erdős #742.

## Review strategy

The highest-value order is **lemmas before computation**. If any necessary graph-theoretic implication in steps 1–4 fails, expensive replay of the finite scans has little value. If those implications survive, independently implement the smallest checker that reconstructs only the proof-critical necessary-condition state space rather than copying the candidate repository's code.

The original LeanSMS baseline reproduction remains useful as calibration of the separate verified graph-generation stack, but the discovered candidate proof changes the n=25 purpose from novelty search to cross-verification.

## Current decision

- **Novel n=25 attack:** COLLISION / HOLD.
- **LeanSMS baseline reproduction:** AUTHORIZED AS REPRODUCTION ONLY when a capable runtime is available.
- **Independent review of public n=25 candidate:** AUTHORIZED.
- **Candidate n=25 theorem:** NOT VERIFIED.
- **Global Murty–Simon / Erdős #742 resolution:** NOT ESTABLISHED.
