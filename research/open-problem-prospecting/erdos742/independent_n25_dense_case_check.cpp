#include <algorithm>
#include <functional>
#include <iostream>
#include <numeric>
#include <stdexcept>
#include <vector>

using std::vector;
using i64 = long long;

// Independent reviewer for the remaining dense/equality n=25 cases.
// Derived from the reviewer-v2 manuscript equations rather than candidate
// scanner source. This checks the finite numerical layer only.

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

static bool eq72_ok(const vector<int>& d, const vector<int>& rho) {
  const int md = *std::max_element(d.begin(), d.end());
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
  return true;
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
      labels.resize(q);
      if (threshold_matching(labels, suppliers, p) >= q) caps[s] = q;
    }
  }
  return caps;
}

static bool outer_ok(const vector<int>& d, const vector<int>& rho, int r,
                     int t) {
  if (!eq72_ok(d, rho)) return false;
  const vector<int> caps = base_caps(d, rho);
  if (std::accumulate(caps.begin(), caps.end(), 0) < r + 2 * t)
    return false;

  const int md = *std::max_element(d.begin(), d.end());
  const int b = static_cast<int>(rho.size());
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

  const int a = static_cast<int>(d.size());
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

static bool pre_hall_column_ok(const vector<int>& d, const vector<int>& rho,
                               const vector<int>& R) {
  const int a = static_cast<int>(d.size());
  const int b = static_cast<int>(rho.size());
  int qmin = 0;
  for (int i = 0; i < a; ++i) qmin += std::max(0, d[i] - R[i]);
  vector<int> caps(b);
  for (int s = 0; s < b; ++s) caps[s] = cap_with_R(d, rho, R, s);
  if (std::accumulate(caps.begin(), caps.end(), 0) < qmin) return false;

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
  return std::accumulate(refined.begin(), refined.end(), 0) >= qmin;
}

static i64 enumerate_R_count(const vector<int>& d, const vector<int>& rho,
                             int r, i64& pre_hall) {
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
      if (pre_hall_column_ok(d, rho, R)) ++pre_hall;
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

struct Counts {
  i64 raw = 0;
  i64 outerpass = 0;
  i64 columns = 0;
  i64 pre_hall = 0;
};

static Counts delta14_e157() {
  constexpr int a = 10, b = 14, L = 42, t = 3;
  Counts out;
  for (int k = 2; k <= 5; ++k) {
    const int D = a - 1 - k;
    const int rmax = L - (a * k + 1) / 2;
    for (int r = b; r <= rmax; ++r) {
      const auto ds = partitions(a, 2 * (r + t), 0, D, true);
      const auto rhos = partitions(b, r, 1, a, false);
      out.raw += static_cast<i64>(ds.size()) * rhos.size();
      for (const auto& d : ds)
        for (const auto& rho : rhos) {
          if (!outer_ok(d, rho, r, t)) continue;
          ++out.outerpass;
          out.columns += enumerate_R_count(d, rho, r, out.pre_hall);
        }
    }
  }
  return out;
}

static void delta15_check(int e, i64 expected_raw) {
  constexpr int a = 9, b = 15;
  const int M = 300 - e;
  const int L = M - a - b * (b - 1) / 2;
  const int t = a * (a - 1) / 2 - L;
  i64 raw = 0, survivors = 0;
  for (int k = 2; k <= 3; ++k) {
    const int D = a - 1 - k;
    const int rmax = L - (a * k + 1) / 2;
    for (int r = b; r <= rmax; ++r) {
      const auto ds = partitions(a, 2 * (r + t), 0, D, true);
      const auto rhos = partitions(b, r, 1, a, false);
      raw += static_cast<i64>(ds.size()) * rhos.size();
      for (const auto& d : ds)
        for (const auto& rho : rhos)
          if (eq72_ok(d, rho)) ++survivors;
    }
  }
  std::cout << "d15.e" << e << ".raw = " << raw << "\n";
  std::cout << "d15.e" << e << ".eq72_survivors = " << survivors << "\n";
  if (raw != expected_raw || survivors != 0)
    throw std::runtime_error("delta15 count mismatch");
}

static void expect(const char* name, i64 actual, i64 wanted) {
  std::cout << name << " = " << actual << " (expected " << wanted << ")\n";
  if (actual != wanted) throw std::runtime_error(name);
}

int main() {
  const Counts d14 = delta14_e157();
  expect("d14.e157.raw", d14.raw, 59264);
  expect("d14.e157.outerpass", d14.outerpass, 31);
  expect("d14.e157.labelled_columns", d14.columns, 1480);
  expect("d14.e157.pre_hall_survivors", d14.pre_hall, 0);

  delta15_check(157, 108);
  delta15_check(156, 211);

  // Delta=16, e=157: Section 5 gives r>=b=16, while e(C)+r=L=15.
  expect("d16.e157.ledger_survivors", 0, 0);

  // Delta=16, e=156: r=16 and e(C)=0 force k=0. Equation (6.3)
  // would require 16 <= 16-C(7,2) = -5.
  const int rhs = 16 - 7 * 6 / 2;
  expect("d16.e156.small_k_rhs", rhs, -5);
  if (16 <= rhs) throw std::runtime_error("delta16 e156 should be impossible");

  std::cout << "PASS: independent dense/equality n=25 counts reproduce reviewer-v2 claims.\n";
  return 0;
}
