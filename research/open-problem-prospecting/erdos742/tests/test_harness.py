import hashlib
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from harness import (
    audit_is_complete,
    authorize_frontier,
    build_baseline_command,
    build_frontier_probe,
    classify_run,
    load_config,
    sha256_file,
)

CONFIG_PATH = ROOT / "pilot_config.json"


def test_pinned_upstream_identity():
    cfg = load_config(CONFIG_PATH)
    assert cfg["leansms"]["commit"] == "8fa708e4c8a00a8951dadc5c0f68863d057fcfab"
    assert cfg["leansms"]["lean_toolchain"] == "leanprover/lean4:v4.24.0-rc1"


def test_frontier_branch_set_is_exact():
    cfg = load_config(CONFIG_PATH)
    assert cfg["frontier"] == {"n": 25, "edges": 157, "deltas": [13, 14, 15, 16, 17]}


def test_baseline_command_is_exact():
    assert build_baseline_command(13) == ["lake", "exe", "murty-simon-generate", "13"]


def test_frontier_denied_without_complete_audit():
    cfg = load_config(CONFIG_PATH)
    ok, reason = authorize_frontier(cfg, {"status": "INCOMPLETE"}, True)
    assert ok is False
    assert "collision audit" in reason.lower()


def test_frontier_denied_without_formal_encoding():
    cfg = load_config(CONFIG_PATH)
    ok, reason = authorize_frontier(cfg, {"status": "COMPLETE"}, False)
    assert ok is False
    assert "formal" in reason.lower()


def test_frontier_command_requires_gate():
    cfg = load_config(CONFIG_PATH)
    try:
        build_frontier_probe(cfg, delta=13, audit={"status": "INCOMPLETE"}, formal_encoding_ready=True)
    except PermissionError as exc:
        assert "collision audit" in str(exc).lower()
    else:
        raise AssertionError("frontier probe was built despite closed gate")


def test_sha256_is_content_bound(tmp_path):
    p = tmp_path / "a.cnf"
    p.write_text("p cnf 1 1\n1 0\n", encoding="utf-8")
    assert sha256_file(p) == hashlib.sha256(p.read_bytes()).hexdigest()


def test_timeout_never_becomes_unsat():
    assert classify_run(timed_out=True, solver_exit=None, lrat_verified=False, lean_verified=False) == "NOT_REFUTED_WITHIN_BUDGET"


def test_solver_unsat_without_lrat_is_not_verified():
    assert classify_run(timed_out=False, solver_exit=20, lrat_verified=False, lean_verified=False) == "SOLVER_UNSAT"


def test_lean_verified_requires_lrat_and_solver_unsat():
    assert classify_run(timed_out=False, solver_exit=20, lrat_verified=True, lean_verified=True) == "LEAN_VERIFIED"
    assert classify_run(timed_out=False, solver_exit=10, lrat_verified=True, lean_verified=True) != "LEAN_VERIFIED"


def test_audit_requires_all_source_classes():
    audit = {
        "status": "COMPLETE",
        "sources": {
            "canonical_page": {"checked": True, "accessible": True},
            "discussion_forum": {"checked": True, "accessible": True},
            "arxiv_math_co": {"checked": True, "accessible": True},
            "github": {"checked": True, "accessible": True},
            "zenodo_artifacts": {"checked": True, "accessible": True},
            "recent_papers_preprints": {"checked": True, "accessible": True},
        },
    }
    ok, missing = audit_is_complete(audit)
    assert ok is True
    assert missing == []


def test_inaccessible_canonical_source_forces_incomplete():
    audit = {
        "status": "COMPLETE",
        "sources": {
            "canonical_page": {"checked": True, "accessible": False},
            "discussion_forum": {"checked": True, "accessible": True},
            "arxiv_math_co": {"checked": True, "accessible": True},
            "github": {"checked": True, "accessible": True},
            "zenodo_artifacts": {"checked": True, "accessible": True},
            "recent_papers_preprints": {"checked": True, "accessible": True},
        },
    }
    ok, missing = audit_is_complete(audit)
    assert ok is False
    assert "canonical_page:inaccessible" in missing


def test_frontier_denied_when_audit_claims_complete_without_sources():
    cfg = load_config(CONFIG_PATH)
    ok, reason = authorize_frontier(cfg, {"status": "COMPLETE"}, True)
    assert ok is False
    assert "collision audit" in reason.lower()


def test_frontier_denied_while_collision_hold():
    cfg = load_config(CONFIG_PATH)
    cfg["frontier_default_status"] = "COLLISION_HOLD"
    audit = {
        "status": "COMPLETE",
        "sources": {
            "canonical_page": {"checked": True, "accessible": True},
            "discussion_forum": {"checked": True, "accessible": True},
            "arxiv_math_co": {"checked": True, "accessible": True},
            "github": {"checked": True, "accessible": True},
            "zenodo_artifacts": {"checked": True, "accessible": True},
            "recent_papers_preprints": {"checked": True, "accessible": True},
        },
    }
    ok, reason = authorize_frontier(cfg, audit, True)
    assert ok is False
    assert "hold" in reason.lower()
