#!/usr/bin/env python3
from __future__ import annotations

import copy
import hashlib
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
VALIDATOR = REPO_ROOT / "scripts" / "validate_public_change_runtime_evidence_receipt.py"
SCHEMA = json.loads(
    (REPO_ROOT / "docs" / "public-change-runtime-evidence-receipt.v1.json").read_text(encoding="utf-8")
)


def digest(receipt: dict) -> str:
    body = {k: v for k, v in receipt.items() if k != "receipt_digest"}
    encoded = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def valid_receipt() -> dict:
    r = {
        "receipt_schema_version": "NDR_PUBLIC_CHANGE_RUNTIME_EVIDENCE_RECEIPT_V1",
        "generated_at": "2026-10-01T22:00:00Z",
        "runtime_identity": "neontic/local-n8n",
        "runtime_version": "2.40.7",
        "workflow_hash": "a" * 64,
        "contract_schema_version": "NDR_PUBLIC_CHANGE_PROPAGATION_CONTRACT_V1",
        "adapter_schema_version": "NDR_PUBLIC_CHANGE_PROPAGATION_ADAPTER_V1",
        "conformance_schema_version": "NDR_PUBLIC_CHANGE_PROPAGATION_CONFORMANCE_V1",
        "adapter_surface": "LIVE_NOTION",
        "portable_vector_results": "PASS",
        "read_before_write": "PASS",
        "post_write_readback": "PASS",
        "block_preservation": "PASS",
        "pass_done_prohibition": "PASS",
        "idempotency": "PASS",
        "missing_relation_behavior": "PASS",
        "unknown_trigger_behavior": "PASS",
        "receipt_schema_validation": "PASS",
        "operator_review": "PASS",
        "overall_result": "PASS",
        "authority_effect": "NONE_DEPLOYMENT_EVIDENCE_ONLY",
        "promotion_eligible": True,
    }
    r["receipt_digest"] = digest(r)
    return r


class RuntimeEvidenceReceiptTests(unittest.TestCase):
    def run_validator(self, receipt: dict) -> subprocess.CompletedProcess[str]:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "docs").mkdir()
            (root / "docs" / "public-change-runtime-evidence-receipt.v1.json").write_text(
                json.dumps(SCHEMA, indent=2) + "\n",
                encoding="utf-8",
            )
            p = root / "receipt.json"
            p.write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
            return subprocess.run(
                [sys.executable, str(VALIDATOR), str(p)],
                cwd=root,
                text=True,
                capture_output=True,
                check=False,
            )

    def test_valid_promotable_receipt_passes(self) -> None:
        result = self.run_validator(valid_receipt())
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_tampered_receipt_fails_digest(self) -> None:
        r = valid_receipt()
        r["runtime_version"] = "tampered"
        result = self.run_validator(r)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("receipt_digest mismatch", result.stderr)

    def test_missing_runtime_identity_fails(self) -> None:
        r = valid_receipt()
        r["runtime_identity"] = ""
        r["receipt_digest"] = digest(r)
        result = self.run_validator(r)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("missing required fields", result.stderr)

    def test_invalid_authority_effect_fails(self) -> None:
        r = valid_receipt()
        r["authority_effect"] = "AUTHORIZED"
        r["receipt_digest"] = digest(r)
        result = self.run_validator(r)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("invalid authority_effect", result.stderr)

    def test_false_promotion_eligibility_fails(self) -> None:
        r = valid_receipt()
        r["portable_vector_results"] = "FAIL"
        r["receipt_digest"] = digest(r)
        result = self.run_validator(r)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("promotion_eligible true", result.stderr)

    def test_shadow_adapter_cannot_be_promotable(self) -> None:
        r = valid_receipt()
        r["adapter_surface"] = "SHADOW_ONLY"
        r["receipt_digest"] = digest(r)
        result = self.run_validator(r)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("promotion_eligible true", result.stderr)

    def test_nonpromotable_receipt_can_still_be_valid(self) -> None:
        r = valid_receipt()
        r["operator_review"] = "NOT_RUN"
        r["adapter_surface"] = "SHADOW_ONLY"
        r["promotion_eligible"] = False
        r["receipt_digest"] = digest(r)
        result = self.run_validator(r)
        self.assertEqual(result.returncode, 0, result.stderr)


if __name__ == "__main__":
    unittest.main()
