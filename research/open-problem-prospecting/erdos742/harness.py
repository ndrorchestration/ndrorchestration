from __future__ import annotations

import hashlib
import json
import os
import platform
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable

PINNED_COMMIT = "8fa708e4c8a00a8951dadc5c0f68863d057fcfab"
PINNED_LEAN = "leanprover/lean4:v4.24.0-rc1"
FRONTIER_N = 25
FRONTIER_EDGES = 157
FRONTIER_DELTAS = (13, 14, 15, 16, 17)
REQUIRED_AUDIT_SOURCES = (
    "canonical_page",
    "discussion_forum",
    "arxiv_math_co",
    "github",
    "zenodo_artifacts",
    "recent_papers_preprints",
)


def load_config(path: Path) -> dict:
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError("config root must be an object")
    return data


def build_baseline_command(n: int) -> list[str]:
    if n < 3:
        raise ValueError("n must be >= 3")
    return ["lake", "exe", "murty-simon-generate", str(n)]


def audit_is_complete(audit: dict) -> tuple[bool, list[str]]:
    missing: list[str] = []
    if audit.get("status") != "COMPLETE":
        missing.append("status:not_COMPLETE")
    sources = audit.get("sources")
    if not isinstance(sources, dict):
        return False, missing + ["sources:missing"]
    for name in REQUIRED_AUDIT_SOURCES:
        entry = sources.get(name)
        if not isinstance(entry, dict) or entry.get("checked") is not True:
            missing.append(f"{name}:unchecked")
            continue
        if name == "canonical_page" and entry.get("accessible") is not True:
            missing.append("canonical_page:inaccessible")
    return len(missing) == 0, missing


def authorize_frontier(config: dict, audit: dict, formal_encoding_ready: bool) -> tuple[bool, str]:
    if formal_encoding_ready is not True:
        return False, "Formal branch encoding and proof obligations are not ready"
    complete, missing = audit_is_complete(audit)
    if not complete:
        return False, "Collision audit is incomplete: " + ", ".join(missing)
    frontier = config.get("frontier")
    if frontier != {"n": FRONTIER_N, "edges": FRONTIER_EDGES, "deltas": list(FRONTIER_DELTAS)}:
        return False, "Frontier parameter contract does not match pinned claim"
    leansms = config.get("leansms", {})
    if leansms.get("commit") != PINNED_COMMIT or leansms.get("lean_toolchain") != PINNED_LEAN:
        return False, "Pinned LeanSMS identity does not match approved trust anchor"
    return True, "AUTHORIZED_BY_LOCAL_GATE"


def build_frontier_probe(config: dict, delta: int, audit: dict, formal_encoding_ready: bool) -> list[str]:
    ok, reason = authorize_frontier(config, audit, formal_encoding_ready)
    if not ok:
        raise PermissionError(reason)
    if delta not in FRONTIER_DELTAS:
        raise ValueError(f"delta must be one of {list(FRONTIER_DELTAS)}")
    # Deliberately names a future branch-specific executable. We do not fall back
    # to the general generator because it lacks exact e=157 / Delta=d semantics.
    return ["lake", "exe", "murty-simon-frontier-generate", str(FRONTIER_N), str(FRONTIER_EDGES), str(delta)]


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with Path(path).open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def classify_run(*, timed_out: bool, solver_exit: int | None, lrat_verified: bool, lean_verified: bool) -> str:
    if timed_out:
        return "NOT_REFUTED_WITHIN_BUDGET"
    if solver_exit == 10:
        return "SOLVER_SAT"
    if solver_exit != 20:
        return "NO_RESULT"
    if lean_verified and lrat_verified:
        return "LEAN_VERIFIED"
    if lrat_verified:
        return "LRAT_VERIFIED"
    return "SOLVER_UNSAT"


def _artifact_record(path: Path) -> dict:
    p = Path(path).resolve()
    return {"path": str(p), "sha256": sha256_file(p), "size_bytes": p.stat().st_size}


def build_manifest(
    *,
    mode: str,
    n: int,
    edges: int | None,
    delta: int | None,
    artifacts: Iterable[Path],
    collision_audit: str,
    evidence_state: str,
    command: list[str],
    solver_exit: int | None,
    timed_out: bool,
    lrat_verified: bool,
    lean_verified: bool,
    formal_encoding_ready: bool | None = None,
) -> dict:
    if mode not in {"baseline", "frontier"}:
        raise ValueError("mode must be baseline or frontier")
    now = datetime.now(timezone.utc).isoformat()
    return {
        "schema_version": 1,
        "project": "erdos742-verified-pilot",
        "created_at_utc": now,
        "mode": mode,
        "parameters": {"n": n, "edges": edges, "delta": delta},
        "command": command,
        "upstream": {
            "repository": "https://github.com/leansolving/leansms",
            "commit": PINNED_COMMIT,
            "lean_toolchain": PINNED_LEAN,
        },
        "environment": {
            "python": sys.version.split()[0],
            "platform": platform.platform(),
            "machine": platform.machine(),
            "cpu_count": os.cpu_count(),
        },
        "run": {
            "solver_exit": solver_exit,
            "timed_out": timed_out,
            "lrat_verified": lrat_verified,
            "lean_verified": lean_verified,
            "derived_classification": classify_run(
                timed_out=timed_out,
                solver_exit=solver_exit,
                lrat_verified=lrat_verified,
                lean_verified=lean_verified,
            ),
        },
        "collision_audit": collision_audit,
        "formal_encoding_ready": formal_encoding_ready,
        "evidence_state": evidence_state,
        "artifacts": [_artifact_record(Path(p)) for p in artifacts],
        "claim_ceiling": (
            "Baseline reproduction only; no frontier novelty claim."
            if mode == "baseline"
            else "Exact branch only; one branch does not exhaust n=25 and n=25 does not by itself prove the global conjecture."
        ),
    }
