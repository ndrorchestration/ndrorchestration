import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from harness import build_manifest
from validate_manifest import validate_manifest


def _base_manifest(tmp_path: Path) -> Path:
    artifact = tmp_path / "proof_sms.lrat"
    artifact.write_text("1 0 0\n", encoding="utf-8")
    manifest = build_manifest(
        mode="baseline",
        n=13,
        edges=None,
        delta=None,
        artifacts=[artifact],
        collision_audit="NOT_REQUIRED",
        evidence_state="LRAT_VERIFIED",
        command=["lake", "exe", "murty-simon-generate", "13"],
        solver_exit=20,
        timed_out=False,
        lrat_verified=True,
        lean_verified=False,
    )
    path = tmp_path / "manifest.json"
    path.write_text(json.dumps(manifest, indent=2, sort_keys=True), encoding="utf-8")
    return path


def test_manifest_validates_when_artifacts_match(tmp_path):
    path = _base_manifest(tmp_path)
    assert validate_manifest(path) == []


def test_manifest_detects_artifact_tamper(tmp_path):
    path = _base_manifest(tmp_path)
    manifest = json.loads(path.read_text(encoding="utf-8"))
    artifact = Path(manifest["artifacts"][0]["path"])
    artifact.write_text("tampered\n", encoding="utf-8")
    errors = validate_manifest(path)
    assert any("sha256 mismatch" in e.lower() for e in errors)


def test_frontier_branch_verified_requires_complete_audit(tmp_path):
    artifact = tmp_path / "proof_sms.lrat"
    artifact.write_text("1 0 0\n", encoding="utf-8")
    manifest = build_manifest(
        mode="frontier",
        n=25,
        edges=157,
        delta=13,
        artifacts=[artifact],
        collision_audit="INCOMPLETE",
        evidence_state="BRANCH_VERIFIED",
        command=["placeholder-frontier-command"],
        solver_exit=20,
        timed_out=False,
        lrat_verified=True,
        lean_verified=True,
    )
    path = tmp_path / "manifest.json"
    path.write_text(json.dumps(manifest, indent=2, sort_keys=True), encoding="utf-8")
    errors = validate_manifest(path)
    assert any("collision audit" in e.lower() for e in errors)


def test_frontier_parameters_are_exact(tmp_path):
    artifact = tmp_path / "proof_sms.lrat"
    artifact.write_text("1 0 0\n", encoding="utf-8")
    manifest = build_manifest(
        mode="frontier",
        n=25,
        edges=157,
        delta=99,
        artifacts=[artifact],
        collision_audit="COMPLETE",
        evidence_state="LRAT_VERIFIED",
        command=["placeholder-frontier-command"],
        solver_exit=20,
        timed_out=False,
        lrat_verified=True,
        lean_verified=False,
    )
    path = tmp_path / "manifest.json"
    path.write_text(json.dumps(manifest, indent=2, sort_keys=True), encoding="utf-8")
    errors = validate_manifest(path)
    assert any("delta" in e.lower() for e in errors)


def test_branch_verified_requires_formal_encoding_ready(tmp_path):
    artifact = tmp_path / "proof_sms.lrat"
    artifact.write_text("1 0 0\n", encoding="utf-8")
    manifest = build_manifest(
        mode="frontier",
        n=25,
        edges=157,
        delta=13,
        artifacts=[artifact],
        collision_audit="COMPLETE",
        evidence_state="BRANCH_VERIFIED",
        command=["lake", "exe", "murty-simon-frontier-generate", "25", "157", "13"],
        solver_exit=20,
        timed_out=False,
        lrat_verified=True,
        lean_verified=True,
        formal_encoding_ready=False,
    )
    path = tmp_path / "manifest.json"
    path.write_text(json.dumps(manifest, indent=2, sort_keys=True), encoding="utf-8")
    errors = validate_manifest(path)
    assert any("formal encoding" in e.lower() for e in errors)


def test_frontier_verified_command_is_parameter_bound(tmp_path):
    artifact = tmp_path / "proof_sms.lrat"
    artifact.write_text("1 0 0\n", encoding="utf-8")
    manifest = build_manifest(
        mode="frontier",
        n=25,
        edges=157,
        delta=13,
        artifacts=[artifact],
        collision_audit="COMPLETE",
        evidence_state="BRANCH_VERIFIED",
        command=["lake", "exe", "murty-simon-frontier-generate", "25", "157", "14"],
        solver_exit=20,
        timed_out=False,
        lrat_verified=True,
        lean_verified=True,
        formal_encoding_ready=True,
    )
    path = tmp_path / "manifest.json"
    path.write_text(json.dumps(manifest, indent=2, sort_keys=True), encoding="utf-8")
    errors = validate_manifest(path)
    assert any("command" in e.lower() for e in errors)
