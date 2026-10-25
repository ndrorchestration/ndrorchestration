// Independent reviewer implementation for the public n=25 Murty-Simon candidate.
//
// Derived from the reviewer manuscript's stated necessary conditions, not from
// the candidate repository's scanner source.  This program verifies only the
// finite numerical relaxation.  It does not prove the upstream graph-theoretic
// lemmas and does not establish Erdős #742 globally.

#include <algorithm>
#include <functional>
#include <iostream>
#include <numeric>
#include <stdexcept>
#include <vector>

using std::vector;
using i64 = long long;

static vector<vector<int>> partitions(int n, int total, int lo, int hi,
                                      bool require_max = false) {
  vector<vector<int>> out;
  vector<int> v(n);
  std::function<void(int, int, int)> rec = [&](int pos, int rem, int minv) {
    if (pos == n) {
      if (rem == 0 && (!require_max || v[n - 1] == hi)) out.push_back(v);
      return;
    }
    const int left = n - pos - 1;
    for (int x = minv; x <= std::min(hi, rem); ++x) {
      const int rem2 = rem - x;
      if (rem2 < left * x) break;
      if (rem2 > left * hi) continue;
      v[pos] = x;
      rec(pos + 1, rem2, x);
    }
  };
  rec(0, total, lo);
  return out;
}

static i64 pair_capacity(const vector<int>& rho, int j) {
  i64 count = 0;
  for (int x = 0; x < static_cast<int>(rho.size()); ++x)
    for (int y = x + 1; y < static_cast<int>(rho.size()); ++y)
      if (rho[x] + rho[y] >= j) ++count;
  return count;
}

static int threshold_matching(vector<int> labels, vector<int> suppliers,
                              int source_rho) {
  std::sort(labels.begin(), labels.end());
  std::sort(suppliers.begin(), suppliers.end());
  int i = 0, j = 0, matched = 0;
  while (i < static_cast<int>(labels.size()) &&
         j < static_cast<int>(suppliers.size())) {
    if (labels[i] <= source_rho + suppliers[j]) {
      ++matched;
      ++i;
      ++j;
    } else {
      ++j;
    }
  }
  return matched;
}

static vector<int> base_caps(const vector<int>& d, const vector<int>& rho) {
  const int a = static_cast<int>(d.size());
  const int b = static_cast<int>(rho.size());
  vector<int> caps(b, 0);
  for (int s = 0; s < b; ++s) {
    const int p = rho[s];
    vector<int> suppliers;
    for (int w = 0; w < b; ++w)
      if (w != s) suppliers.push_back(rho[w]);
    for (int q = 1; q <= a - p; ++q) {
      vector<int> labels;
      for (int x : d)
        if (x <= p + q - 1) labels.push_back(x);
      if (static_cast<int>(labels.size()) < q) continue;
      std::sort(labels.begin(), labels.end());
      labels.resize(q);  // easiest q labels give a safe upper bound
      if (threshold_matching(labels, suppliers, p) >= q) caps[s] = q;
    }
  }
  return caps;
}

static bool outer_ok(const vector<int>& d, const vector<int>& rho, int r,
                     int t) {
  const int a = static_cast<int>(d.size());
  const int b = static_cast<int>(rho.size());
  const int md = *std::max_element(d.begin(), d.end());

  // Equation (7.2): selected-pair threshold capacity.
  for (int j = 1; j <= md; ++j) {
    int sj = 0, sumd = 0;
    for (int x : d)
      if (x >= j) {
        ++sj;
        sumd += x;
      }
    i64 residual_supply = 0;
    for (int p : rho) residual_supply += std::min(p, sj);
    const i64 ell = std::max<i64>(0, sumd - residual_supply);
    if (ell > pair_capacity(rho, j)) return false;
  }

  const vector<int> caps = base_caps(d, rho);
  if (std::accumulate(caps.begin(), caps.end(), 0) < r + 2 * t)
    return false;

  // Reapply the source/supplier matching upper bound inside each S_j.
  for (int j = 1; j <= md; ++j) {
    int sj = 0, sumd = 0;
    for (int x : d)
      if (x >= j) {
        ++sj;
        sumd += x;
      }
    i64 residual_supply = 0;
    for (int p : rho) residual_supply += std::min(p, sj);
    const int ell = static_cast<int>(std::max<i64>(0, sumd - residual_supply));

    int source_total = 0;
    for (int s = 0; s < b; ++s) {
      const int p = rho[s];
      vector<int> labels, suppliers;
      for (int x : d)
        if (x >= j && x <= p + caps[s] - 1) labels.push_back(x);
      for (int w = 0; w < b; ++w)
        if (w != s) suppliers.push_back(rho[w]);
      source_total +=
          std::min(caps[s], threshold_matching(labels, suppliers, p));
    }
    if (source_total < ell) return false;
  }

  // Residual-column h-index lower bound.
  int h = 0;
  for (int j = 1; j <= a; ++j) {
    int count = 0;
    for (int p : rho)
      if (p >= j) ++count;
    if (count >= j) h = j;
  }
  int lb = 0;
  for (int x : d) lb += std::max(0, x - h);
  return lb <= r;
}

static int cap_with_R(const vector<int>& d, const vector<int>& rho,
                      const vector<int>& R, int s) {
  const int a = static_cast<int>(d.size());
  const int b = static_cast<int>(rho.size());
  const int p = rho[s];
  vector<int> suppliers;
  for (int w = 0; w < b; ++w)
    if (w != s) suppliers.push_back(rho[w]);

  int best = 0;
  for (int q = 1; q <= a - p; ++q) {
    vector<int> labels;
    for (int i = 0; i < a; ++i)
      if (d[i] <= p + q - 1 && d[i] <= p + R[i]) labels.push_back(d[i]);
    if (threshold_matching(labels, suppliers, p) >= q) best = q;
  }
  return best;
}

// 0 = rejected before (9.1), 1 = rejected by (9.1), 2 = survives (9.1).
static int column_status(const vector<int>& d, const vector<int>& rho,
                         const vector<int>& R) {
  const int a = static_cast<int>(d.size());
  const int b = static_cast<int>(rho.size());

  int qmin = 0;
  for (int i = 0; i < a; ++i) qmin += std::max(0, d[i] - R[i]);

  vector<int> caps(b, 0);
  for (int s = 0; s < b; ++s) caps[s] = cap_with_R(d, rho, R, s);
  if (std::accumulate(caps.begin(), caps.end(), 0) < qmin) return 0;

  // Simultaneous supplement-cap refinement from Section 8.
  vector<int> refined = caps;
  for (int s = 0; s < b; ++s) {
    int best = 0;
    for (int q = 0; q <= caps[s]; ++q) {
      int suppliers = 0;
      for (int w = 0; w < b; ++w)
        if (w != s && rho[w] + caps[w] >= q - 1) ++suppliers;
      if (suppliers >= q) best = q;
    }
    refined[s] = best;
  }
  if (std::accumulate(refined.begin(), refined.end(), 0) < qmin) return 0;

  // Equation (9.1), checked over every nonempty subset of A.
  for (int mask = 1; mask < (1 << a); ++mask) {
    int demand = 0;
    for (int i = 0; i < a; ++i)
      if ((mask >> i) & 1) demand += std::max(0, d[i] - R[i]);

    int capacity = 0;
    for (int s = 0; s < b; ++s) {
      int eligible = 0;
      for (int i = 0; i < a; ++i) {
        if (!((mask >> i) & 1)) continue;
        if (d[i] <= rho[s] + refined[s] - 1 &&
            d[i] <= rho[s] + R[i])
          ++eligible;
      }
      capacity += std::min(refined[s], eligible);
    }
    if (demand > capacity) return 1;
  }
  return 2;
}

struct EqualityCounts {
  i64 raw_outer = 0;
  i64 labelled_columns = 0;
  i64 pre_hall_survivors = 0;
  i64 survivor_outer_states = 0;
  i64 hall_killed = 0;
  i64 hall_survivors = 0;
};

static i64 enumerate_R(const vector<int>& d, const vector<int>& rho, int r,
                       i64& pre_hall, i64& hall_killed, i64& hall_survivors) {
  const int a = static_cast<int>(d.size());
  const int b = static_cast<int>(rho.size());
  int h = 0;
  for (int j = 1; j <= a; ++j) {
    int count = 0;
    for (int p : rho)
      if (p >= j) ++count;
    if (count >= j) h = j;
  }

  vector<int> lo(a), R(a);
  int minsum = 0;
  for (int i = 0; i < a; ++i) {
    lo[i] = std::max(0, d[i] - h);
    minsum += lo[i];
  }
  if (minsum > r) return 0;

  i64 total = 0;
  std::function<void(int, int)> rec = [&](int pos, int rem) {
    if (pos == a) {
      if (rem != 0) return;
      ++total;
      const int status = column_status(d, rho, R);
      if (status) {
        ++pre_hall;
        if (status == 1)
          ++hall_killed;
        else
          ++hall_survivors;
      }
      return;
    }
    int minrest = 0;
    for (int j = pos + 1; j < a; ++j) minrest += lo[j];
    const int maxrest = (a - pos - 1) * b;
    const int low = std::max(lo[pos], rem - maxrest);
    const int high = std::min(b, rem - minrest);
    for (int x = low; x <= high; ++x) {
      R[pos] = x;
      rec(pos + 1, rem - x);
    }
  };
  rec(0, r);
  return total;
}

static EqualityCounts equality_band(int k_lo, int k_hi) {
  constexpr int a = 10, b = 14, t = 2;
  EqualityCounts out;
  for (int k = k_lo; k <= k_hi; ++k) {
    const int D = a - 1 - k;
    const int rmax = 43 - 5 * k;
    for (int r = b; r <= rmax; ++r) {
      const auto ds = partitions(a, 2 * (r + t), 0, D, true);
      const auto rhos = partitions(b, r, 1, a, false);
      out.raw_outer += static_cast<i64>(ds.size()) * rhos.size();
      for (const auto& d : ds) {
        for (const auto& rho : rhos) {
          if (!outer_ok(d, rho, r, t)) continue;
          i64 pre = 0, killed = 0, survived = 0;
          out.labelled_columns += enumerate_R(d, rho, r, pre, killed, survived);
          out.pre_hall_survivors += pre;
          out.hall_killed += killed;
          out.hall_survivors += survived;
          if (pre > 0) ++out.survivor_outer_states;
        }
      }
    }
  }
  return out;
}

struct FanFreeCounts {
  i64 raw_after_small_k = 0;
  i64 survivors = 0;
};

static FanFreeCounts fan_free_delta(int Delta) {
  const int a = 24 - Delta;
  const int b = Delta;
  FanFreeCounts out;

  for (int m = 158; m <= (25 * Delta) / 2; ++m) {
    const int M = 300 - m;
    const int L = M - a - b * (b - 1) / 2;
    const int t = a * (a - 1) / 2 - L;

    // The manuscript's small-k inequalities (6.3),(6.4) exclude k=0,1
    // throughout these upper ranges.  Enumerate the remaining complete domain.
    for (int k = 2; k < a; ++k) {
      const int D = a - 1 - k;
      const int rmax = L - (a * k + 1) / 2;
      for (int r = b; r <= rmax; ++r) {
        const auto ds = partitions(a, 2 * (r + t), 0, D, true);
        const auto rhos = partitions(b, r, 1, a, false);
        out.raw_after_small_k += static_cast<i64>(ds.size()) * rhos.size();
        for (const auto& d : ds)
          for (const auto& rho : rhos)
            if (outer_ok(d, rho, r, t)) ++out.survivors;
      }
    }
  }
  return out;
}

static void expect(const char* name, i64 actual, i64 wanted) {
  std::cout << name << " = " << actual << " (expected " << wanted << ")\n";
  if (actual != wanted) throw std::runtime_error(std::string("count mismatch: ") + name);
}

int main() {
  const EqualityCounts k1 = equality_band(1, 1);
  expect("k1.raw_outer", k1.raw_outer, 401543);
  expect("k1.labelled_columns", k1.labelled_columns, 3252212);
  expect("k1.survivor_outer_states", k1.survivor_outer_states, 130);
  expect("k1.pre_hall_survivors", k1.pre_hall_survivors, 1788);
  expect("k1.hall_killed", k1.hall_killed, 1788);
  expect("k1.hall_survivors", k1.hall_survivors, 0);

  const EqualityCounts k2_5 = equality_band(2, 5);
  expect("k2_5.raw_outer", k2_5.raw_outer, 82452);
  expect("k2_5.labelled_columns", k2_5.labelled_columns, 188520);
  expect("k2_5.survivor_outer_states", k2_5.survivor_outer_states, 28);
  expect("k2_5.pre_hall_survivors", k2_5.pre_hall_survivors, 171);
  expect("k2_5.hall_killed", k2_5.hall_killed, 171);
  expect("k2_5.hall_survivors", k2_5.hall_survivors, 0);

  const FanFreeCounts d14 = fan_free_delta(14);
  const FanFreeCounts d15 = fan_free_delta(15);
  const FanFreeCounts d16 = fan_free_delta(16);
  expect("fanfree.d14.outer", d14.raw_after_small_k, 128666);
  expect("fanfree.d14.survivors", d14.survivors, 0);
  expect("fanfree.d15.outer", d15.raw_after_small_k, 88);
  expect("fanfree.d15.survivors", d15.survivors, 0);
  expect("fanfree.d16.outer", d16.raw_after_small_k, 0);
  expect("fanfree.d16.survivors", d16.survivors, 0);

  std::cout << "PASS: independent finite-relaxation counts reproduce the reviewer-v2 claims.\n";
  return 0;
}
