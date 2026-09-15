#!/usr/bin/env python3

RANK = [x.bit_count() for x in range(256)]


def allowed(x, rank_mask):
    return bool((rank_mask >> RANK[x]) & 1)


def exhaust(rank_mask, target):
    allowed_sets = [x for x in range(256) if allowed(x, rank_mask)]
    seen = {()}
    frontier = [()]
    states = 0
    transitions = 0

    for _ in range(target):
        nxt = []
        for family in frontier:
            states += 1
            fs = set(family)
            for x in allowed_sets:
                if x in fs:
                    continue
                transitions += 1
                closure = fs | {x}
                ok = True
                for y in family:
                    u = x | y
                    if not allowed(u, rank_mask):
                        ok = False
                        break
                    closure.add(u)
                if not ok:
                    continue
                if len(closure) >= target:
                    return {
                        "found": True,
                        "complete": False,
                        "seen": len(seen),
                        "states": states,
                        "transitions": transitions,
                        "witness": tuple(sorted(closure)),
                    }
                child = tuple(sorted(closure))
                if child not in seen:
                    seen.add(child)
                    nxt.append(child)
        frontier = nxt
        if not frontier:
            return {
                "found": False,
                "complete": True,
                "seen": len(seen),
                "states": states,
                "transitions": transitions,
                "witness": None,
            }

    return {
        "found": False,
        "complete": not frontier,
        "seen": len(seen),
        "states": states,
        "transitions": transitions,
        "witness": None,
    }


def main():
    red = 333   # ranks {0,2,3,6,8}
    blue = 178  # ranks {1,4,5,7}

    r9 = exhaust(red, 9)
    b9 = exhaust(blue, 9)
    assert r9["complete"] and not r9["found"]
    assert b9["complete"] and not b9["found"]
    assert (r9["seen"], r9["states"], r9["transitions"]) == (71138, 71138, 7738539)
    assert (b9["seen"], b9["states"], b9["transitions"]) == (164391, 164391, 22461940)

    r8 = exhaust(red, 8)
    b8 = exhaust(blue, 8)
    assert r8["found"] and b8["found"]

    print("red", r9)
    print("blue", b9)
    print("red size-8 positive control", r8["witness"])
    print("blue size-8 positive control", b8["witness"])
    print("INDEPENDENT PYTHON F(8) UPPER-BOUND CHECK PASSED")


if __name__ == "__main__":
    main()
