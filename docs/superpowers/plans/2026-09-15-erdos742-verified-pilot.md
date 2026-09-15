# Erdős #742 Verified Proof-Certificate Pilot Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a fail-closed provenance/orchestration harness around pinned LeanSMS reproduction, stage the n=14 verified-extension test, and specify—but do not authorize—the n=25 e=157, Δ∈{13..17} frontier branches.

**Architecture:** Keep LeanSMS as the mathematical trust anchor and add a thin Python wrapper that never reimplements graph mathematics. The wrapper binds commands, parameters, artifacts, hashes, environment metadata, collision-audit state, and evidence classifications into deterministic manifests; a validator independently rechecks those manifests. Frontier commands remain gated until formal branch-specific Lean encoding work and same-day collision audit are complete.

**Tech Stack:** Python 3.11+ standard library, pytest, JSON Schema-like explicit validation in Python, SHA-256, GitHub Actions for wrapper tests; upstream LeanSMS pinned at commit `8fa708e4c8a00a8951dadc5c0f68863d057fcfab`, Lean `v4.24.0-rc1`, LRAT/SMS/Lean for later external execution.

**Spec:** `docs/superpowers/specs/2026-09-15-erdos742-verified-pilot-design.md`

## Global Constraints

- Upstream LeanSMS commit MUST equal `8fa708e4c8a00a8951dadc5c0f68863d057fcfab` unless a later reviewed update explicitly supersedes it.
- Lean toolchain MUST equal `leanprover/lean4:v4.24.0-rc1` for the pinned reproduction lane.
- The wrapper MUST NOT classify solver exit code 20 alone as `LEAN_VERIFIED`.
- Timeout/resource exhaustion MUST classify as `NOT_REFUTED_WITHIN_BUDGET`.
- n=25 frontier execution MUST remain fail-closed unless `formal_encoding_ready=true` and `collision_audit=COMPLETE`.
- One verified Δ branch MUST NOT be promoted beyond that exact branch.
- Local wrapper tests are provenance/orchestration tests only; they MUST NOT be described as mathematical verification.

---

## File Structure

- `research/open-problem-prospecting/erdos742/README.md` — operator-facing pilot state and evidence boundaries.
- `research/open-problem-prospecting/erdos742/pilot_config.json` — pinned upstream/toolchain, baseline ladder, frontier parameters, budgets.
- `research/open-problem-prospecting/erdos742/harness.py` — command construction, gate checks, manifest generation, artifact hashing.
- `research/open-problem-prospecting/erdos742/validate_manifest.py` — independent fail-closed manifest validation CLI.
- `research/open-problem-prospecting/erdos742/collision_audit_template.json` — same-day audit checklist/state contract.
- `research/open-problem-prospecting/erdos742/frontier_contract.json` — exact n=25 branch claim ceilings and authorization prerequisites.
- `research/open-problem-prospecting/erdos742/tests/test_harness.py` — wrapper behavior tests.
- `research/open-problem-prospecting/erdos742/tests/test_manifest_validation.py` — tamper/gate tests.
- `.github/workflows/erdos742-wrapper-tests.yml` — deterministic wrapper CI; no frontier solver run.

---

### Task 1: Pin configuration and evidence vocabulary

**Files:**
- Create: `research/open-problem-prospecting/erdos742/pilot_config.json`
- Create: `research/open-problem-prospecting/erdos742/frontier_contract.json`
- Test: `research/open-problem-prospecting/erdos742/tests/test_harness.py`

**Interfaces:**
- Consumes: approved design constants.
- Produces: `load_config(path) -> dict`, fixed frontier branch set, evidence labels.

- [ ] **Step 1: Write failing config tests**

```python
from pathlib import Path
from harness import load_config

ROOT = Path(__file__).resolve().parents[1]

def test_pinned_upstream_identity():
    cfg = load_config(ROOT / "pilot_config.json")
    assert cfg["leansms"]["commit"] == "8fa708e4c8a00a8951dadc5c0f68863d057fcfab"
    assert cfg["leansms"]["lean_toolchain"] == "leanprover/lean4:v4.24.0-rc1"


def test_frontier_branch_set_is_exact():
    cfg = load_config(ROOT / "pilot_config.json")
    assert cfg["frontier"] == {"n": 25, "edges": 157, "deltas": [13, 14, 15, 16, 17]}
```

- [ ] **Step 2: Run tests and verify they fail before files/functions exist**

Run: `pytest research/open-problem-prospecting/erdos742/tests/test_harness.py -q`  
Expected: import/file failure.

- [ ] **Step 3: Add minimal config loader and JSON contracts**

`load_config` must parse JSON and reject a non-object top level:

```python
def load_config(path: Path) -> dict:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError("config root must be an object")
    return data
```

- [ ] **Step 4: Re-run tests**

Expected: PASS.

- [ ] **Step 5: Commit**

```bash
git add research/open-problem-prospecting/erdos742
git commit -m "feat: pin Erdos 742 pilot configuration"
```

### Task 2: Implement fail-closed execution gates and command construction

**Files:**
- Modify: `research/open-problem-prospecting/erdos742/harness.py`
- Modify: `research/open-problem-prospecting/erdos742/tests/test_harness.py`

**Interfaces:**
- Consumes: pilot config and collision-audit object.
- Produces: `build_baseline_command(n) -> list[str]`, `authorize_frontier(config, audit, formal_encoding_ready) -> tuple[bool,str]`, `build_frontier_probe(delta, ...)` only after authorization.

- [ ] **Step 1: Add failing tests**

```python
def test_baseline_command_is_exact():
    assert build_baseline_command(13) == ["lake", "exe", "murty-simon-generate", "13"]


def test_frontier_denied_without_complete_audit():
    ok, reason = authorize_frontier(CONFIG, {"status": "INCOMPLETE"}, True)
    assert ok is False
    assert "collision audit" in reason.lower()


def test_frontier_denied_without_formal_encoding():
    ok, reason = authorize_frontier(CONFIG, {"status": "COMPLETE"}, False)
    assert ok is False
    assert "formal" in reason.lower()
```

- [ ] **Step 2: Verify failures**

Run the targeted tests and confirm missing functions fail.

- [ ] **Step 3: Implement minimal gate logic**

The frontier gate returns true only if both prerequisites are explicit. `build_frontier_probe` must raise `PermissionError` when the gate is closed. It must never silently downgrade to the general `murty-simon-generate` command because that command does not encode exact e=157/Δ=d semantics.

- [ ] **Step 4: Re-run tests**

Expected: PASS.

- [ ] **Step 5: Commit**

```bash
git add research/open-problem-prospecting/erdos742/harness.py research/open-problem-prospecting/erdos742/tests/test_harness.py
git commit -m "feat: enforce Erdos 742 frontier gates"
```

### Task 3: Add deterministic manifests and artifact hashing

**Files:**
- Modify: `research/open-problem-prospecting/erdos742/harness.py`
- Create: `research/open-problem-prospecting/erdos742/tests/test_manifest_validation.py`

**Interfaces:**
- Produces: `sha256_file(path) -> str`, `build_manifest(...) -> dict`, `classify_run(...) -> str`.

- [ ] **Step 1: Add failing hash/classification tests**

```python
def test_sha256_is_content_bound(tmp_path):
    p = tmp_path / "a.cnf"
    p.write_text("p cnf 1 1\n1 0\n", encoding="utf-8")
    assert sha256_file(p) == hashlib.sha256(p.read_bytes()).hexdigest()


def test_timeout_never_becomes_unsat():
    assert classify_run(timed_out=True, solver_exit=None, lrat_verified=False, lean_verified=False) == "NOT_REFUTED_WITHIN_BUDGET"


def test_solver_unsat_without_lrat_is_not_verified():
    assert classify_run(False, 20, False, False) == "SOLVER_UNSAT"
```

- [ ] **Step 2: Verify failures**.

- [ ] **Step 3: Implement minimal hashing/manifest/classification**.

Manifest artifact entries are `{path, sha256, size_bytes}` and parameters include exact `mode`, `n`, optional `edges`, optional `delta`.

- [ ] **Step 4: Re-run tests**.

- [ ] **Step 5: Commit**.

### Task 4: Implement independent manifest validator

**Files:**
- Create: `research/open-problem-prospecting/erdos742/validate_manifest.py`
- Modify: `research/open-problem-prospecting/erdos742/tests/test_manifest_validation.py`

**Interfaces:**
- Produces: `validate_manifest(manifest_path: Path) -> list[str]`; empty list means valid.

- [ ] **Step 1: Add tamper tests**

Create a synthetic artifact, build a manifest, mutate the artifact, then assert validation returns a hash mismatch. Add a test that a frontier manifest with `collision_audit != COMPLETE` cannot carry `BRANCH_VERIFIED`.

- [ ] **Step 2: Verify failures**.

- [ ] **Step 3: Implement validator**

The validator must check required metadata, pinned commit, artifact existence, size, SHA-256, parameter binding, and evidence/gate consistency.

- [ ] **Step 4: Re-run tests**.

- [ ] **Step 5: Commit**.

### Task 5: Add collision-audit contract

**Files:**
- Create: `research/open-problem-prospecting/erdos742/collision_audit_template.json`
- Modify: `research/open-problem-prospecting/erdos742/tests/test_harness.py`

**Interfaces:**
- Produces: `audit_is_complete(audit: dict) -> tuple[bool,list[str]]`.

- [ ] **Step 1: Add failing audit tests** asserting every required source class must be marked checked and canonical-source inaccessibility forces `INCOMPLETE`.
- [ ] **Step 2: Verify failures**.
- [ ] **Step 3: Implement exact source checklist:** canonical page, discussion/forum, arXiv/math.CO, GitHub, Zenodo/artifacts, recent papers/preprints.
- [ ] **Step 4: Re-run tests**.
- [ ] **Step 5: Commit**.

### Task 6: Add operator runbook and evidence ceilings

**Files:**
- Create: `research/open-problem-prospecting/erdos742/README.md`

**Interfaces:** Human-facing only.

- [ ] **Step 1: Document exact baseline commands**

```bash
lake exe murty-simon-generate 9
lake exe murty-simon-generate 13
lake exe murty-simon-generate 14
```

State explicitly that n=14 is staged but not verified in this repository until a retained manifest says so.

- [ ] **Step 2: Document artifact expectations**: base CNF, symmetry JSON, extended CNF, LRAT, logs, theorem source where applicable, manifest.
- [ ] **Step 3: Document n=25 prohibition**: no generic command is presented as a valid frontier command until the branch-specific Lean `EncodingSpec` exists and its proof obligations close.
- [ ] **Step 4: Commit**.

### Task 7: Add wrapper-only CI

**Files:**
- Create: `.github/workflows/erdos742-wrapper-tests.yml`

**Interfaces:** GitHub Actions runs only Python wrapper tests.

- [ ] **Step 1: Add workflow** using Python 3.12, install pytest, run `pytest research/open-problem-prospecting/erdos742/tests -q`.
- [ ] **Step 2: Ensure workflow name clearly says `Erdos 742 Wrapper Tests (No Solver)`**.
- [ ] **Step 3: Commit**.

### Task 8: Verify branch and open draft PR

**Files:** No new implementation files.

- [ ] **Step 1: Run all wrapper tests locally or via CI**.
- [ ] **Step 2: Confirm no test or document claims n=13/n=14 was executed in the current environment**.
- [ ] **Step 3: Confirm `frontier_contract.json` remains `NOT_AUTHORIZED`**.
- [ ] **Step 4: Open a draft PR with the evidence boundary and current environment limitation**.
- [ ] **Step 5: Update Notion with branch, PR, files, test evidence, and the exact next external execution command**.

## Plan self-review

- **Spec coverage:** trust anchor, evidence vocabulary, baseline ladder, n=25 exact semantics, collision audit, resource limits, hashing, validation, CI, and fail-closed frontier gate are each mapped to a task.
- **Placeholder scan:** no TBD/TODO implementation placeholders remain; frontier mathematical encoding is deliberately defined as a later authorization prerequisite rather than implied implemented work.
- **Type consistency:** config/audit/manifest interfaces use JSON dictionaries and Path objects consistently; evidence labels are fixed strings.
