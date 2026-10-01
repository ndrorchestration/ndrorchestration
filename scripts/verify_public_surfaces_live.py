#!/usr/bin/env python3
"""Verify externally observable public-surface reachability and stable markers.

This script checks only public HTTP behavior for explicitly machine-checkable
surfaces. It does not establish project authority, scientific validity,
independent validation, production assurance, or authorization state.
"""

from __future__ import annotations

import json
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

MANIFEST = Path("docs/public-surface-manifest.v1.json")
OUT = Path("public-surface-live-check.json")

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


def main() -> None:
    data = json.loads(MANIFEST.read_text(encoding="utf-8"))
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

    artifact = {
        "schema": "NDR_PUBLIC_SURFACE_LIVE_CHECK_V1",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "manifest_schema": data.get("schema_version"),
        "scope": "public reachability and stable rendered markers only",
        "authority_note": "PASS does not establish technical, scientific, governance, runtime, validation, efficacy, security, or authorization truth.",
        "results": results,
        "summary": {
            "pass": sum(r["result"] == "PASS" for r in results),
            "fail": sum(r["result"] == "FAIL" for r in results),
            "skipped_by_policy": sum(r["result"] == "SKIPPED_BY_POLICY" for r in results),
        },
    }

    OUT.write_text(json.dumps(artifact, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(artifact, indent=2))

    if failures:
        print("PUBLIC_SURFACE_LIVE_CHECK_FAILED", file=sys.stderr)
        for failure in failures:
            print(f"- {failure}", file=sys.stderr)
        raise SystemExit(1)

    print("PUBLIC_SURFACE_LIVE_CHECK_PASS")


if __name__ == "__main__":
    main()
