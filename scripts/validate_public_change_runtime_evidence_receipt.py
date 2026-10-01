#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

SCHEMA_PATH = Path("docs/public-change-runtime-evidence-receipt.v1.json")


def fail(msg: str) -> None:
    raise SystemExit(f"PUBLIC_CHANGE_RUNTIME_EVIDENCE_RECEIPT_INVALID: {msg}")


def canonical_digest(receipt: dict) -> str:
    body = {k: v for k, v in receipt.items() if k != "receipt_digest"}
    encoded = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def validate(receipt: dict, schema: dict) -> None:
    if receipt.get("receipt_schema_version") != schema["schema_version"]:
        fail("unexpected receipt_schema_version")

    missing = [f for f in schema["required_fields"] if f not in receipt or receipt[f] in ("", None)]
    if missing:
        fail("missing required fields: " + ", ".join(missing))

    enums = schema["enums"]
    check_fields = [
        "portable_vector_results",
        "read_before_write",
        "post_write_readback",
        "block_preservation",
        "pass_done_prohibition",
        "idempotency",
        "missing_relation_behavior",
        "unknown_trigger_behavior",
        "receipt_schema_validation",
    ]
    for field in check_fields:
        if receipt[field] not in enums["check"]:
            fail(f"invalid {field}")

    if receipt["operator_review"] not in enums["operator_review"]:
        fail("invalid operator_review")
    if receipt["overall_result"] not in enums["overall_result"]:
        fail("invalid overall_result")
    if receipt["authority_effect"] not in enums["authority_effect"]:
        fail("invalid authority_effect")

    digest = receipt.get("receipt_digest")
    if not digest:
        fail("missing receipt_digest")
    if digest != canonical_digest(receipt):
        fail("receipt_digest mismatch")

    requirements = schema["promotion_requirements"]
    promotable = all(receipt.get(k) == v for k, v in requirements.items())
    if receipt.get("promotion_eligible") is True and not promotable:
        fail("promotion_eligible true without satisfying promotion requirements")
    if receipt.get("promotion_eligible") not in (True, False):
        fail("promotion_eligible must be boolean")


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit("usage: validate_public_change_runtime_evidence_receipt.py RECEIPT_JSON")
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    receipt = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    validate(receipt, schema)
    print("PUBLIC_CHANGE_RUNTIME_EVIDENCE_RECEIPT_VALID")


if __name__ == "__main__":
    main()
