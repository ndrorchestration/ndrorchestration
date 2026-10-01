#!/usr/bin/env python3
"""Verify externally observable public-surface reachability and stable markers.

This script checks only public HTTP behavior for explicitly machine-checkable
surfaces. It does not establish project authority, scientific validity,
independent validation, production assurance, or authorization state.
"""

from __future__ import annotations

import hashlib
import json
import os
import subprocess
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

MANIFEST = Path("docs/public-surface-manifest.v1.json")
OUT = Path("public-surface-live-check.json")
RECEIPT = Path("public-surface-live-check.sha256")

CHECKS = {
    "portfolio.home": {
        "markers": [
            "AI Systems Design",
            "Governed AI Systems",
            "Evaluation &amp; Evidence",
            "Public Explanation &amp; Reuse",
        ],
    },
    "github.profile": {
        "markers": [
            "AI Systems Design",
            "Tektite",
            "What did the system actually do",
        ],
    },
    "github.organization_profile": {
        "markers": [
            "evidence",
            "repository",
        ],
    },
    "dgaf.command_center": {
        "markers": [
            "DGAF",
            "Governance Command Center",
            "NOT AUTHORIZED",
        ],
    },
    "tektite.bounded_demo": {
        "markers": [
            "Tektite Demo",
            "CLAIM BOUNDARY",
            "REQUEST",
            "AUTHORITY",
        ],
    },
}

SKIPPED = {
    "linkedin.profile": "Public endpoint identity is verified, but automated content readback is intentionally excluded because LinkedIn blocks unauthenticated automation."
}


def fetch(url: str) -> tuple[int, str, str]:
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": "ndrorchestration-public-surface-verifier/1.0",
            "Accept": "text/html,application/xhtml+xml",
        },
        method="GET",
    )
    try:
        with urllib.request.urlopen(req, timeout=20) as response:
            body = response.read(2_000_000).decode("utf-8", errors="replace")
            final_url = response.geturl()
            return response.status, final_url, body
    except urllib.error.HTTPError as exc:
        body = exc.read(200_000).decode("utf-8", errors="replace")
        return exc.code, exc.geturl(), body


def source_head() -> str:
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "HEAD"],
            text=True,
            stderr=subprocess.DEVNULL,
        ).strip()
    except (OSError, subprocess.CalledProcessError):
        return "UNKNOWN"


def main() -> None:
    manifest_bytes = MANIFEST.read_bytes()
    manifest_sha256 = hashlib.sha256(manifest_bytes).hexdigest()
    data = json.loads(manifest_bytes.decode("utf-8"))
    by_id = {s["id"]: s for s in data["surfaces"]}

    results = []
    failures = []

    for surface_id, spec in CHECKS.items():
        surface = by_id.get(surface_id)
        if not surface:
            failures.append(f"missing machine-checkable surface: {surface_id}")
            continue

        status, final_url, body = fetch(surface["url"])
        missing = [marker for marker in spec["markers"] if marker.lower() not in body.lower()]
        ok = 200 <= status < 300 and not missing

        result = {
            "id": surface_id,
            "declared_url": surface["url"],
            "final_url": final_url,
            "http_status": status,
            "required_markers": spec["markers"],
            "missing_markers": missing,
            "result": "PASS" if ok else "FAIL",
        }
        results.append(result)

        if not ok:
            failures.append(
                f"{surface_id}: status={status}, missing_markers={missing!r}, final_url={final_url}"
            )

    for surface_id, reason in SKIPPED.items():
        if surface_id not in by_id:
            failures.append(f"missing skipped surface: {surface_id}")
            continue
        results.append(
            {
                "id": surface_id,
                "declared_url": by_id[surface_id]["url"],
                "result": "SKIPPED_BY_POLICY",
                "reason": reason,
            }
        )

    provenance = {
        "repository": os.environ.get("GITHUB_REPOSITORY", "ndrorchestration/ndrorchestration"),
        "source_head": source_head(),
        "github_event_sha": os.environ.get("GITHUB_SHA", "").strip(),
        "manifest_path": str(MANIFEST),
        "manifest_sha256": manifest_sha256,
        "workflow": os.environ.get("GITHUB_WORKFLOW", ""),
        "workflow_run_id": os.environ.get("GITHUB_RUN_ID", ""),
        "workflow_run_attempt": os.environ.get("GITHUB_RUN_ATTEMPT", ""),
        "workflow_ref": os.environ.get("GITHUB_WORKFLOW_REF", ""),
        "event_name": os.environ.get("GITHUB_EVENT_NAME", ""),
    }

    artifact = {
        "schema": "NDR_PUBLIC_SURFACE_LIVE_CHECK_V1",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "manifest_schema": data.get("schema_version"),
        "provenance": provenance,
        "scope": "public reachability and stable rendered markers only",
        "authority_note": "PASS does not establish technical, scientific, governance, runtime, validation, efficacy, security, or authorization truth.",
        "results": results,
        "summary": {
            "pass": sum(r["result"] == "PASS" for r in results),
            "fail": sum(r["result"] == "FAIL" for r in results),
            "skipped_by_policy": sum(r["result"] == "SKIPPED_BY_POLICY" for r in results),
        },
    }

    payload = (json.dumps(artifact, indent=2) + "\n").encode("utf-8")
    OUT.write_bytes(payload)
    receipt_sha256 = hashlib.sha256(payload).hexdigest()
    RECEIPT.write_text(
        f"{receipt_sha256}  {OUT.name}\n",
        encoding="utf-8",
    )

    print(payload.decode("utf-8"), end="")
    print(f"PUBLIC_SURFACE_LIVE_CHECK_RECEIPT_SHA256={receipt_sha256}")

    if failures:
        print("PUBLIC_SURFACE_LIVE_CHECK_FAILED", file=sys.stderr)
        for failure in failures:
            print(f"- {failure}", file=sys.stderr)
        raise SystemExit(1)

    print("PUBLIC_SURFACE_LIVE_CHECK_PASS")


if __name__ == "__main__":
    main()
