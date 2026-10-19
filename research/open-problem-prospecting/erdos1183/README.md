# Erdős #1183 — bounded n=8 candidate checkpoint

**Date:** 2026-09-15  
**State:** CANDIDATE FINITE RESULT / COMPUTATION INDEPENDENTLY REPRODUCED / NOVELTY NOT CONFIRMED / GLOBAL PROBLEM OPEN  
**Scope:** exact value of the lattice-closed small case `f(8)` only.

## Exact statement used

For Erdős #1183, `f(n)` is the largest integer such that every 2-colouring of `2^[n]` contains a monochromatic family of at least `f(n)` sets that is closed under both union and intersection.

The public 2026-08-12 working report records

```text
f(1..7) = 1,2,2,3,3,4,4
F(1..7) = 1,2,2,3,4,5,7
```

and says the canonical page was then OPEN with zero claimed proofs and no current worker. That status check is historical, not a substitute for a same-day canonical worker check.

## Candidate result

The bounded computation here supports

```text
f(8) = 5.
```

### Lower bound

A maximal chain in `2^[8]` has 9 sets. Every 2-colouring colours at least 5 of them the same colour, and any subfamily of a chain is closed under union and intersection. Hence `f(8) >= 5`.

### Upper bound

Colour a subset red iff its cardinality is in

```text
{0,2,5,6}
```

and blue otherwise, i.e. blue ranks are

```text
{1,3,4,7,8}.
```

For each colour form the **pair-compatibility graph** whose vertices are sets of that colour and where distinct `A,B` are adjacent iff both `A union B` and `A intersection B` have the same colour.

Every monochromatic family closed under union and intersection is a clique in the corresponding compatibility graph. Therefore an exact clique-number upper bound is also an exact upper bound for the size of a monochromatic sublattice.

Two independently written exact maximum-clique implementations reproduce:

| colour | vertices | edges | clique number |
|---|---:|---:|---:|
| red | 113 | 1260 | 4 |
| blue | 143 | 2326 | 5 |

Thus this colouring contains no monochromatic union/intersection-closed family of size 6, so `f(8) <= 5`. Combined with the chain lower bound, the bounded conclusion is `f(8)=5`.

## Reproduction

C++ verifier:

```bash
g++ -O2 -std=c++20 f8_rank_clique_check.cpp -o /tmp/erdos1183-f8
/tmp/erdos1183-f8
```

Expected invariants:

```text
red vertices=113 edges=1260 omega=4
blue vertices=143 edges=2326 omega=5
```

Python verifier:

```bash
python f8_rank_clique_check.py
```

It independently reconstructs the graphs and performs a separate branch-and-bound maximum-clique search.

Locally verified source SHA-256 values before commit:

```text
62190aa9833b1bd48074824b755e51e88efecd0cfdd2ae97bc358462065857e8  f8_rank_clique_check.cpp
077b5975f18f351a5ff94cfc4f6974abedd37866fc67be6cb321f7c7c5746619  f8_rank_clique_check.py
```

## Collision / priority boundary

Searches on 2026-09-15 found no indexed public source stating `f(8)=5`, no hit for this rank colouring, and no post-March update in `QuanyuTang/erdos-problem-1183`. The August working report still stops at `n=7`.

However, the canonical Erdős Problems origin is not directly readable from this environment today, so the current worker / claimed-proof fields cannot be certified same-day. Therefore:

- mathematical finite result: **SUPPORTED BY TWO INDEPENDENT EXACT CHECKERS**;
- novelty / priority: **NOT CONFIRMED**;
- permission to present as a new solution or claim priority: **NOT GRANTED**;
- global Erdős #1183: **OPEN / NOT SOLVED BY THIS RESULT**.

## Next gates

1. Obtain a same-day canonical status + discussion-thread check for #1183.
2. Have a mathematically independent reviewer inspect the compatibility-graph reduction and exact clique search.
3. If no collision is found, preserve immutable artifacts and determine whether the finite extension is worth reporting to the tracker/authors.
4. Separately investigate `F(8)`; do not infer its value from the `f(8)` result.
