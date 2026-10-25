# Erdős #742 — n=25 Candidate Bridge Audit Pass 3

**Date:** 2026-09-15  
**State:** PUBLISHED REDUCTIONS SOURCE-CHECKED / SECTIONS 4–7 REDERIVED / NO BLOCKING DEFECT FOUND / OVERALL CANDIDATE STILL NOT VERIFIED

## Scope

This pass audits the graph-theoretic bridge that feeds the independently reproduced finite relaxation. It is intentionally separate from Pass 2's numerical replay.

Primary published inputs checked:

1. T. W. Haynes, M. A. Henning, L. C. van der Merwe, A. Yeo, *A maximum degree theorem for diameter-2-critical graphs*, Central European Journal of Mathematics 12 (2014), 1882–1889, DOI `10.2478/s11533-014-0449-3`.
2. A. Dailly, F. Foucaud, A. Hansberg, *Strengthening the Murty–Simon conjecture on diameter 2 critical graphs*, Discrete Mathematics 342 (2019), 3142–3159, DOI `10.1016/j.disc.2019.06.023`.

## Published reductions

### D2C complement correspondence

The 2014 paper states:

- Theorem 3.1: a diameter-2-critical graph has complement that is either `3_t`-critical or `4_t`-supercritical, under the paper's non-star/no-isolated-complement convention.
- Theorem 3.2: a `4_t`-supercritical graph is exactly the disjoint union of two nontrivial cliques.
- Observation 3.4: for a missing edge `uv` in a `3_t`-critical graph, either `{u,v}` dominates, or (after swapping endpoints if needed) there is an edge `uw` that dominates every vertex except `v`; the paper writes `uw -> v`.
- Theorem 3.6(a): if a `3_t`-critical graph of order `n` has minimum degree `delta <= 0.3n`, then its size is strictly greater than `ceil(n(n-2)/4)`.

The manuscript's use is consistent:

- A non-star D2C graph has no universal vertex, so its complement has no isolated vertex and the correspondence applies.
- If the complement were `4_t`-supercritical, the original graph would be complete bipartite; the non-bipartite branch therefore has a `3_t`-critical complement.
- At `n=25`, `Delta(G) >= 17` gives `delta(H)=24-Delta(G) <= 7 <= 0.3*25`. Theorem 3.6(a) then gives `e(H)>144`, hence `e(H)>=145` and `e(G)<=155`. Therefore an `e(G)>=156` case indeed has `Delta(G)<=16`.

**Disposition:** SOURCE STATEMENTS AND NUMERICAL SPECIALIZATION CHECKED.

### Dominating-edge exclusion

The 2019 paper's Theorem 4 states that a non-bipartite D2C graph with a dominating edge, other than the six-vertex graph `H5`, has at most `floor(n^2/4)-2` edges.

At `n=25` this is `156-2=154`. Therefore any order-25 non-bipartite graph under review with 156 or more edges has no dominating edge. The `H5` exception is irrelevant by order.

**Disposition:** SOURCE STATEMENT AND ORDER-25 SPECIALIZATION CHECKED.

## Quasi-edge bridge

Let `H` be the `3_t`-critical complement, choose a minimum-degree vertex `v`, set `A=N_H(v)` and `B=V(H)\N_H[v]`.

For every missing unordered pair `{b,w}` inside `H[B]`, the pair cannot dominate `v`. Observation 3.4 therefore yields, after swapping `b,w` if required, an edge `bi -> w`. Because `b` does not dominate `v`, the auxiliary endpoint `i` must dominate `v`, hence `i in A`. The edge is therefore cross-part.

The exception `w` is unique: `bi` dominates `H-w`, while both `b` and `i` miss `w`. Choosing exactly one such representative for each missing unordered B-pair gives the manuscript's selected-edge convention.

A selected edge cannot represent two distinct missing B-pairs because the edge has a unique B-exception. Opposite orientations of one missing pair also do not collide because exactly one representative is designated for that unordered pair.

**Disposition:** REDERIVED; NO COLLISION DEFECT FOUND.

## Residual ledger

With `M=e(H)`, `a=|A|`, `b=|B|`, `C=H[A]`, `F=overline{C}`, selected cross-edge count `Q`, and residual cross-edge count `r`:

- selected cross-edges plus existing B-edges equal `C(b,2)`;
- therefore `M = a + e(C) + C(b,2) + r`;
- hence `e(C)+r=L := M-a-C(b,2)`;
- `e(F)=C(a,2)-e(C)=r+t`, where `t=C(a,2)-L`;
- `sum d_i=2(r+t)` and `sum rho_b=r`.

Minimum degree `a` in `H` gives `d_B(i)>=d_i` for each `i in A`, hence total selected degree `Q>=r+2t`.

**Disposition:** REDERIVED.

## Section 5 residual activity

Assuming a B-vertex has residual degree zero:

- all of its A-neighbours are selected and have distinct B-exceptions;
- an F-edge crossing `S=N_A(b)` to `T=A\S` would contradict domination by a selected edge, so no F-edge crosses `S,T`;
- every F-edge inside `S` forces two distinct residual cross-edges;
- every F-edge inside `T` forces one distinct residual cross-edge, whose A-exception prevents it from being selected;
- the two forced families are disjoint by their A-endpoints.

Thus `r >= 2e(F[S])+e(F[T]) = e(F)+e(F[S]) >= r+t`, contradicting `t>0`.

Therefore every B-vertex is residual-active and `r>=b`.

**Disposition:** REDERIVED; DISTINCTNESS CHECKED.

## Section 6 small-k injections

For a minimum-C-degree vertex `x`, `Y=N_C(x)`, `X=A\({x} union Y)`:

- a missing pair in `X` misses `x`;
- any B-auxiliary quasi-edge is residual because its exception lies in A;
- each B endpoint used by such a quasi-edge forces a separate residual `xz` edge;
- every unused B vertex has a residual incident edge by Section 5;
- these give `b <= r-m` for the number `m` of B-auxiliary edges.

For `k=0`, all missing X-pairs require B auxiliaries, yielding

`b <= L - C(a-1,2)`.

For `k=1`, at most `s=e_C(y,X)` missing X-pairs can use the unique A auxiliary `y`, yielding

`b <= L - 1 - C(a-2,2)`.

These are exactly the inequalities used both in the equality scan and the independently reproduced Fan-free upper-range domain reduction.

**Disposition:** REDERIVED; INJECTION/DISTINCTNESS ARGUMENT CHECKED.

## Section 7 selected-edge inequalities

For a selected edge `bi -> w`, every F-neighbour `u` of `i` must be adjacent to `b`. Charging residual `bu` edges to `b`, and selected `bu` edges through their distinct supplements to residual `uw` edges, yields

`d_i <= rho_b + rho_w`.

Charging the latter family instead to distinct residual `i w_u` edges gives

`d_i <= rho_b + R_i`.

Because `b` is adjacent to `i` and every F-neighbour of `i`, and its A-degree is `rho_b+q_b`, one also gets

`d_i <= rho_b + q_b - 1`, and trivially `q_b+rho_b<=a`.

For `S_j={i:d_i>=j}`, minimum degree forces at least

`ell_j = sum_{i in S_j} d_i - sum_b min(rho_b,|S_j|)`

selected incidences into `S_j`. Each selected incidence injects into a distinct missing unordered B-pair whose residual-degree sum is at least `j`. This gives equation (7.2).

The later source-cap, h-index, supplement-cap, and subset-capacity tests are valid relaxations of these inequalities: they use upper bounds on feasible selected incidences and therefore can safely reject a numerical state only when even the relaxation lacks sufficient capacity.

**Disposition:** REDERIVED; NO DIRECTION-OF-INEQUALITY ERROR FOUND.

## Combined state after Passes 1–3

The following surfaces now have independent support:

- published order-25 external reductions;
- complement/quasi-edge selected-edge bridge;
- complement ledger;
- Sections 5–7 hand mathematics;
- Delta=13 arithmetic/equality continuation;
- complete Delta=14, e=156 finite relaxation including (9.1);
- complete order-25 Fan-free `m>=158` finite outer reduction.

No blocking defect has been found in this checked chain.

## Evidence ceiling

This is still **not an independent human peer review**, and it is not a formal proof in a proof assistant. The candidate's release object/hash provenance should still be independently rebound, and the remaining order-25 assembly should be checked as a single end-to-end argument rather than inferred from individually clean components.

Current classification:

- **Public n=25 candidate:** STRONGLY CORROBORATED / NOT VERIFIED.
- **n=25 novelty lane in this project:** COLLISION_HOLD.
- **Global Murty-Simon / Erdős #742:** NOT ESTABLISHED AS SOLVED.
