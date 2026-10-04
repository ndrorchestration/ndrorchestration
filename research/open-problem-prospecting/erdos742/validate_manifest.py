from __future__ import annotations

import argparse
import json
from pathlib import Path

from harness import FRONTIER_DELTAS, FRONTIER_EDGES, FRONTIER_N, PINNED_COMMIT, PINNED_LEAN, sha256_file

ALLOWED_EVIDENCE = {
    "DEFINED",
    "GENERATED",
    "SOLVER_UNSAT",
    "SOLVER_SAT",
    "LRAT_VERIFIED",
    "LEAN_VERIFIED",
    "BRANCH_VERIFIED",
    "NOT_REFUTED_WITHIN_BUDGET",
    "NO_RESULT",
}


def validate_manifest(manifest_path: Path) -> list[str]:
    path = Path(manifest_path)
    errors: list[str] = []
    try:
        manifest = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        return [f"manifest parse failure: {exc}"]

    if manifest.get("schema_version") != 1:
        errors.append("schema_version must be 1")
    upstream = manifest.get("upstream", {})
    if upstream.get("commit") != PINNED_COMMIT:
        errors.append("upstream commit does not match pinned LeanSMS commit")
    if upstream.get("lean_toolchain") != PINNED_LEAN:
        errors.append("Lean toolchain does not match pinned value")

    mode = manifest.get("mode")
    params = manifest.get("parameters", {})
    evidence = manifest.get("evidence_state")
    if evidence not in ALLOWED_EVIDENCE:
        errors.append("unknown evidence_state")

    run = manifest.get("run", {})
    if run.get("timed_out") is True and evidence not in {"NOT_REFUTED_WITHIN_BUDGET", "NO_RESULT"}:
        errors.append("timeout cannot carry a verified/solver result evidence state")
    if evidence in {"LRAT_VERIFIED", "LEAN_VERIFIED", "BRANCH_VERIFIED"} and run.get("lrat_verified") is not True:
        errors.append("verified evidence requires lrat_verified=true")
    if evidence in {"LEAN_VERIFIED", "BRANCH_VERIFIED"} and run.get("lean_verified") is not True:
        errors.append("Lean/branch verified evidence requires lean_verified=true")
    if evidence in {"LRAT_VERIFIED", "LEAN_VERIFIED", "BRANCH_VERIFIED"} and run.get("solver_exit") != 20:
        errors.append("verified UNSAT evidence requires solver_exit=20")

    if mode == "frontier":
        if params.get("n") != FRONTIER_N:
            errors.append(f"frontier n must equal {FRONTIER_N}")
        if params.get("edges") != FRONTIER_EDGES:
            errors.append(f"frontier edges must equal {FRONTIER_EDGES}")
        if params.get("delta") not in FRONTIER_DELTAS:
            errors.append(f"frontier delta must be one of {list(FRONTIER_DELTAS)}")
        if evidence == "BRANCH_VERIFIED" and manifest.get("collision_audit") != "COMPLETE":
            errors.append("BRANCH_VERIFIED requires COMPLETE collision audit")
        if evidence == "BRANCH_VERIFIED" and manifest.get("formal_encoding_ready") is not True:
            errors.append("BRANCH_VERIFIED requires formal encoding readiness")
        expected_command = [
            "lake", "exe", "murty-simon-frontier-generate",
            str(FRONTIER_N), str(FRONTIER_EDGES), str(params.get("delta"))
        ]
        if evidence == "BRANCH_VERIFIED" and manifest.get("command") != expected_command:
            errors.append("BRANCH_VERIFIED command is not bound to manifest frontier parameters")
    elif mode == "baseline":
        if params.get("edges") is not None or params.get("delta") is not None:
            errors.append("baseline manifest must not bind frontier edges/delta")
    else:
        errors.append("mode must be baseline or frontier")

    artifacts = manifest.get("artifacts")
    if not isinstance(artifacts, list) or not artifacts:
        errors.append("at least one artifact is required")
    else:
        for idx, record in enumerate(artifacts):
            try:
                artifact = Path(record["path"])
                expected_hash = record["sha256"]
                expected_size = record["size_bytes"]
            except Exception:
                errors.append(f"artifact[{idx}] record is incomplete")
                continue
            if not artifact.is_file():
                errors.append(f"artifact[{idx}] missing: {artifact}")
                continue
            if artifact.stat().st_size != expected_size:
                errors.append(f"artifact[{idx}] size mismatch: {artifact}")
            actual_hash = sha256_file(artifact)
            if actual_hash != expected_hash:
                errors.append(f"artifact[{idx}] sha256 mismatch: {artifact}")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate an Erdős #742 pilot manifest fail-closed.")
    parser.add_argument("manifest", type=Path)
    args = parser.parse_args()
    errors = validate_manifest(args.manifest)
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("VALID")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
