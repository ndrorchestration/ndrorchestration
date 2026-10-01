#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

CONTRACT = Path("docs/public-change-propagation-contract.v1.json")

EXPECTED_ASSET = {
    "Reconciliation Status": "In progress",
    "Release Gate": "Review",
}
EXPECTED_ENDPOINT = {
    "Release Gate": "Review",
    "Copy State": "Review Needed",
}
REQUIRED_PROHIBITED = {
    "Evidence Ceiling",
    "Claim Ceiling",
    "Release Gate = Pass",
    "public copy rewrite",
    "independent validation state",
    "canonical efficacy state",
    "High-Assurance authorization",
    "production executor authority",
}
REQUIRED_RECEIPT_FIELDS = {
    "receipt_id",
    "generated_at",
    "triggering_canonical_message_id",
    "trigger_class",
    "trigger_source_version",
    "affected_assets",
    "affected_endpoints",
    "prior_state",
    "new_state",
    "result",
    "authority_effect",
    "errors",
}


def fail(message: str) -> None:
    raise SystemExit(f"PUBLIC_CHANGE_PROPAGATION_CONTRACT_INVALID: {message}")


def main() -> None:
    data = json.loads(CONTRACT.read_text(encoding="utf-8"))

    if data.get("schema_version") != "NDR_PUBLIC_CHANGE_PROPAGATION_CONTRACT_V1":
        fail("unexpected schema_version")

    note = data.get("authority_note", "")
    if "REVIEW" not in note or "cannot strengthen claims" not in note:
        fail("authority_note must preserve one-way fail-closed semantics")

    allowed = data.get("allowed_mutations", {})
    if allowed.get("governed_asset") != EXPECTED_ASSET:
        fail("governed_asset allowed mutations changed")
    if allowed.get("public_surface_endpoint") != EXPECTED_ENDPOINT:
        fail("public_surface_endpoint allowed mutations changed")

    prohibited = set(data.get("prohibited_mutations", []))
    if not REQUIRED_PROHIBITED.issubset(prohibited):
        fail("required prohibited mutations missing")

    receipt = data.get("audit_receipt", {})
    if receipt.get("schema") != "NDR_PUBLIC_CHANGE_PROPAGATION_RECEIPT_V1":
        fail("unexpected receipt schema")
    if set(receipt.get("required_fields", [])) != REQUIRED_RECEIPT_FIELDS:
        fail("receipt required_fields changed")
    if receipt.get("result_enum") != ["PASS", "PARTIAL", "BLOCKED"]:
        fail("receipt result_enum changed")
    if receipt.get("authority_effect") != "NONE_RECONCILIATION_ONLY":
        fail("receipt authority_effect changed")

    for layer in ("asset", "endpoint"):
        sm = data.get("state_machine", {}).get(layer, {})
        forbidden = {tuple(x) for x in sm.get("forbidden", [])}
        required_forbidden = {
            ("Review", "Pass"),
            ("Block", "Review"),
            ("Block", "Pass"),
        }
        if forbidden != required_forbidden:
            fail(f"{layer} forbidden transitions changed")

    deployment = data.get("deployment", {})
    if deployment.get("status") != "NOT_DEPLOYED":
        fail("contract must remain NOT_DEPLOYED until runtime evidence exists")

    print("PUBLIC_CHANGE_PROPAGATION_CONTRACT_VALID")


if __name__ == "__main__":
    main()
