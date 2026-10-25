#include <algorithm>
#include <array>
#include <bit>
#include <cstdint>
#include <iostream>
#include <stdexcept>
#include <unordered_set>
#include <vector>

using U64 = std::uint64_t;

struct Key {
    std::array<std::uint8_t, 8> sets{};
    std::uint8_t len = 0;
    bool operator==(const Key& other) const {
        return len == other.len && sets == other.sets;
    }
};

struct KeyHash {
    std::size_t operator()(const Key& k) const noexcept {
        U64 h = 1469598103934665603ULL;
        h ^= k.len;
        h *= 1099511628211ULL;
        for (int i = 0; i < k.len; ++i) {
            h ^= k.sets[i];
            h *= 1099511628211ULL;
        }
        return static_cast<std::size_t>(h);
    }
};

struct Counts {
    U64 seen = 0;
    U64 states = 0;
    U64 transitions = 0;
    bool found = false;
    bool complete = false;
    std::vector<int> witness;
};

static bool rank_allowed(int set_mask, unsigned rank_mask) {
    return (rank_mask >> std::popcount(static_cast<unsigned>(set_mask))) & 1U;
}

static Counts exhaust(unsigned rank_mask, int target) {
    std::vector<int> allowed;
    for (int x = 0; x < 256; ++x)
        if (rank_allowed(x, rank_mask)) allowed.push_back(x);

    std::unordered_set<Key, KeyHash> seen;
    seen.reserve(300000);
    Key empty;
    seen.insert(empty);
    std::vector<Key> frontier{empty};
    Counts out;

    for (int round = 0; round < target && !frontier.empty(); ++round) {
        std::vector<Key> next;
        for (const Key& family : frontier) {
            ++out.states;
            for (int x : allowed) {
                bool present = false;
                for (int i = 0; i < family.len; ++i)
                    if (family.sets[i] == x) present = true;
                if (present) continue;

                ++out.transitions;
                std::vector<int> closure;
                closure.reserve(17);
                for (int i = 0; i < family.len; ++i)
                    closure.push_back(family.sets[i]);
                closure.push_back(x);

                bool valid = true;
                for (int i = 0; i < family.len; ++i) {
                    const int u = x | family.sets[i];
                    if (!rank_allowed(u, rank_mask)) {
                        valid = false;
                        break;
                    }
                    closure.push_back(u);
                }
                if (!valid) continue;

                std::sort(closure.begin(), closure.end());
                closure.erase(std::unique(closure.begin(), closure.end()), closure.end());
                if (static_cast<int>(closure.size()) >= target) {
                    out.found = true;
                    out.witness = closure;
                    out.seen = seen.size();
                    return out;
                }

                Key child;
                child.len = static_cast<std::uint8_t>(closure.size());
                for (int i = 0; i < child.len; ++i)
                    child.sets[i] = static_cast<std::uint8_t>(closure[i]);
                if (seen.insert(child).second)
                    next.push_back(child);
            }
        }
        frontier.swap(next);
    }

    out.seen = seen.size();
    out.complete = frontier.empty();
    return out;
}

static void expect(const char* name, U64 actual, U64 expected) {
    std::cout << name << "=" << actual << " expected=" << expected << "\n";
    if (actual != expected)
        throw std::runtime_error(std::string("mismatch: ") + name);
}

int main() {
    // Red ranks {0,2,3,6,8}; blue ranks {1,4,5,7}.
    constexpr unsigned red = 333;
    constexpr unsigned blue = 178;

    const Counts r9 = exhaust(red, 9);
    const Counts b9 = exhaust(blue, 9);
    if (r9.found || b9.found || !r9.complete || !b9.complete)
        throw std::runtime_error("size-9 closure exhaustion failed");
    expect("red.seen", r9.seen, 71138);
    expect("red.states", r9.states, 71138);
    expect("red.transitions", r9.transitions, 7738539);
    expect("blue.seen", b9.seen, 164391);
    expect("blue.states", b9.states, 164391);
    expect("blue.transitions", b9.transitions, 22461940);

    // Positive controls: both colour classes really do admit an 8-set family.
    const Counts r8 = exhaust(red, 8);
    const Counts b8 = exhaust(blue, 8);
    if (!r8.found || !b8.found)
        throw std::runtime_error("positive control for size 8 failed");

    std::cout << "red8_witness=";
    for (int x : r8.witness) std::cout << x << ',';
    std::cout << "\nblue8_witness=";
    for (int x : b8.witness) std::cout << x << ',';
    std::cout << "\nF(8) upper-colouring verification PASS: no monochromatic union-closed family has size >=9.\n";
    return 0;
}
