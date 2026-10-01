#!/usr/bin/env python3
"""Fail-closed structural validator for docs/public-surface-manifest.v1.json.

This validates the manifest's own contract and invariant claim ceilings.
It does not verify live endpoint reachability or establish project authority.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from urllib.parse import urlparse

MANIFEST = Path("docs/public-surface-manifest.v1.json")

EXPECTED_INVARIANTS = {
    "SCIENTIFIC_N_INCREMENT": 0,
    "INDEPENDENT_VALIDATION": "NOT_ESTABLISHED",
    "CANONICAL_DGAF_EFFICACY": "NOT_ESTABLISHED",
    "HIGH_ASSURANCE": "NOT_AUTHORIZED",
    "LIVE_REPOSITORY_MUTATION": "NOT_AUTHORIZED",
    "ROLLBACK_EXECUTION": "NOT_AUTHORIZED",
    "PRODUCTION_EXECUTOR": "NOT_ESTABLISHED",
}

ALLOWED_REACHABILITY = {
    "VERIFIED_PUBLIC",
    "VERIFIED_AUTHENTICATED",
    "UNVERIFIED",
    "UNAVAILABLE",
}
ALLOWED_COPY_STATE = {"RECONCILED", "REVIEW_NEEDED", "NOT_INSPECTABLE"}
ALLOWED_RELEASE_GATE = {"PASS", "REVIEW", "BLOCK"}

REQUIRED_SURFACE_KEYS = {
    "id",
    "type",
    "url",
    "reachability",
    "copy_state",
    "release_gate",
    "canonical_dependencies",
    "verification_methods",
    "source_version",
    "last_verified",
    "refresh_triggers",
}


def fail(message: str) -> None:
    print(f"PUBLIC_SURFACE_MANIFEST_INVALID: {message}", file=sys.stderr)
    raise SystemExit(1)


def valid_https_url(value: str) -> bool:
    parsed = urlparse(value)
    return parsed.scheme == "https" and bool(parsed.netloc)


def main() -> None:
    if not MANIFEST.is_file():
        fail(f"missing manifest: {MANIFEST}")

    try:
        data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        fail(f"cannot parse JSON: {exc}")

    if data.get("schema_version") != "NDR_PUBLIC_SURFACE_MANIFEST_V1":
        fail("unexpected schema_version")

    authority_note = data.get("authority_note", "")
    required_note_terms = ("routing", "freshness", "does not establish")
    lower_note = authority_note.lower()
    if not all(term in lower_note for term in required_note_terms):
        fail("authority_note must preserve routing/freshness non-authority semantics")

    invariants = data.get("invariant_claims")
    if invariants != EXPECTED_INVARIANTS:
        fail(
            "invariant_claims changed from the fail-closed baseline: "
            f"expected {EXPECTED_INVARIANTS!r}, got {invariants!r}"
        )

    surfaces = data.get("surfaces")
    if not isinstance(surfaces, list) or not surfaces:
        fail("surfaces must be a non-empty list")

    ids: set[str] = set()
    urls: set[str] = set()

    for index, surface in enumerate(surfaces):
        label = f"surface[{index}]"
        if not isinstance(surface, dict):
            fail(f"{label} must be an object")

        missing = REQUIRED_SURFACE_KEYS - surface.keys()
        if missing:
            fail(f"{label} missing keys: {sorted(missing)}")

        surface_id = surface["id"]
        if not isinstance(surface_id, str) or not surface_id.strip():
            fail(f"{label}.id must be non-empty")
        if surface_id in ids:
            fail(f"duplicate surface id: {surface_id}")
        ids.add(surface_id)

        url = surface["url"]
        if not isinstance(url, str) or not valid_https_url(url):
            fail(f"{surface_id}.url must be an absolute https URL")
        if url in urls:
            fail(f"duplicate public URL: {url}")
        urls.add(url)

        reachability = surface["reachability"]
        copy_state = surface["copy_state"]
        release_gate = surface["release_gate"]

        if reachability not in ALLOWED_REACHABILITY:
            fail(f"{surface_id}.reachability invalid: {reachability}")
        if copy_state not in ALLOWED_COPY_STATE:
            fail(f"{surface_id}.copy_state invalid: {copy_state}")
        if release_gate not in ALLOWED_RELEASE_GATE:
            fail(f"{surface_id}.release_gate invalid: {release_gate}")

        for list_key in (
            "canonical_dependencies",
            "verification_methods",
            "refresh_triggers",
        ):
            value = surface[list_key]
            if not isinstance(value, list) or not value:
                fail(f"{surface_id}.{list_key} must be a non-empty list")
            if len(value) != len(set(value)):
                fail(f"{surface_id}.{list_key} contains duplicates")

        last_verified = surface["last_verified"]
        if not isinstance(last_verified, str) or len(last_verified) != 10:
            fail(f"{surface_id}.last_verified must be YYYY-MM-DD")

        if release_gate == "PASS":
            if reachability != "VERIFIED_PUBLIC":
                fail(f"{surface_id}: PASS requires VERIFIED_PUBLIC reachability")
            if copy_state != "RECONCILED":
                fail(f"{surface_id}: PASS requires RECONCILED copy_state")

        if copy_state == "NOT_INSPECTABLE" and release_gate == "PASS":
            fail(f"{surface_id}: NOT_INSPECTABLE cannot be PASS")

    tektite = next((x for x in surfaces if x["id"] == "tektite.bounded_demo"), None)
    if tektite is None:
        fail("required surface missing: tektite.bounded_demo")

    version = tektite.get("source_version")
    if not isinstance(version, dict):
        fail("tektite.bounded_demo.source_version must be an object")

    for key in (
        "current_git_commit",
        "accepted_proof_source_sha",
        "accepted_proof_deployment_id",
        "accepted_proof_artifact_id",
        "accepted_proof_sha256",
        "verifier_result",
    ):
        if not version.get(key):
            fail(f"tektite.bounded_demo.source_version missing {key}")

    if version["current_git_commit"] == version["accepted_proof_source_sha"]:
        fail("current Tektite deployment identity must remain distinct from accepted proof source identity")

    if version["verifier_result"] != "TEKTITE_PROOF_OF_OPERATION_V1=PASS":
        fail("unexpected accepted Tektite proof verifier result")

    print(
        "PUBLIC_SURFACE_MANIFEST_VALID: "
        f"{len(surfaces)} surfaces, "
        f"{sum(s['release_gate'] == 'PASS' for s in surfaces)} PASS, "
        f"{sum(s['release_gate'] == 'REVIEW' for s in surfaces)} REVIEW, "
        f"{sum(s['release_gate'] == 'BLOCK' for s in surfaces)} BLOCK"
    )


if __name__ == "__main__":
    main()
