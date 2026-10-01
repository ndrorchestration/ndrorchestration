#!/usr/bin/env python3
from __future__ import annotations

import copy
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
VALIDATOR = REPO_ROOT / "scripts" / "validate_public_change_propagation_contract.py"
BASE = json.loads(
    (REPO_ROOT / "docs" / "public-change-propagation-contract.v1.json").read_text(encoding="utf-8")
)


class PublicChangePropagationContractNegativeTests(unittest.TestCase):
    def run_validator(self, contract: dict) -> subprocess.CompletedProcess[str]:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "docs").mkdir()
            (root / "docs" / "public-change-propagation-contract.v1.json").write_text(
                json.dumps(contract, indent=2) + "\n",
                encoding="utf-8",
            )
            return subprocess.run(
                [sys.executable, str(VALIDATOR)],
                cwd=root,
                text=True,
                capture_output=True,
                check=False,
            )

    def assert_rejected(self, contract: dict, needle: str) -> None:
        result = self.run_validator(contract)
        self.assertNotEqual(result.returncode, 0, result.stdout)
        self.assertIn(needle, result.stderr)

    def test_current_contract_passes(self) -> None:
        result = self.run_validator(copy.deepcopy(BASE))
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("PUBLIC_CHANGE_PROPAGATION_CONTRACT_VALID", result.stdout)

    def test_asset_auto_pass_is_rejected(self) -> None:
        contract = copy.deepcopy(BASE)
        contract["allowed_mutations"]["governed_asset"]["Release Gate"] = "Pass"
        self.assert_rejected(contract, "governed_asset allowed mutations changed")

    def test_endpoint_auto_pass_is_rejected(self) -> None:
        contract = copy.deepcopy(BASE)
        contract["allowed_mutations"]["public_surface_endpoint"]["Release Gate"] = "Pass"
        self.assert_rejected(contract, "public_surface_endpoint allowed mutations changed")

    def test_asset_reconciliation_done_is_rejected(self) -> None:
        contract = copy.deepcopy(BASE)
        contract["allowed_mutations"]["governed_asset"]["Reconciliation Status"] = "Done"
        self.assert_rejected(contract, "governed_asset allowed mutations changed")

    def test_claim_ceiling_protection_cannot_be_removed(self) -> None:
        contract = copy.deepcopy(BASE)
        contract["prohibited_mutations"].remove("Claim Ceiling")
        self.assert_rejected(contract, "required prohibited mutations missing")

    def test_independent_validation_protection_cannot_be_removed(self) -> None:
        contract = copy.deepcopy(BASE)
        contract["prohibited_mutations"].remove("independent validation state")
        self.assert_rejected(contract, "required prohibited mutations missing")

    def test_high_assurance_protection_cannot_be_removed(self) -> None:
        contract = copy.deepcopy(BASE)
        contract["prohibited_mutations"].remove("High-Assurance authorization")
        self.assert_rejected(contract, "required prohibited mutations missing")

    def test_receipt_authority_effect_cannot_be_strengthened(self) -> None:
        contract = copy.deepcopy(BASE)
        contract["audit_receipt"]["authority_effect"] = "AUTHORIZED"
        self.assert_rejected(contract, "receipt authority_effect changed")

    def test_receipt_schema_cannot_drop_prior_state(self) -> None:
        contract = copy.deepcopy(BASE)
        contract["audit_receipt"]["required_fields"].remove("prior_state")
        self.assert_rejected(contract, "receipt required_fields changed")

    def test_review_to_pass_transition_is_rejected(self) -> None:
        contract = copy.deepcopy(BASE)
        contract["state_machine"]["asset"]["forbidden"] = [
            ["Block", "Review"],
            ["Block", "Pass"],
        ]
        self.assert_rejected(contract, "asset forbidden transitions changed")

    def test_false_runtime_deployment_claim_is_rejected(self) -> None:
        contract = copy.deepcopy(BASE)
        contract["deployment"]["status"] = "DEPLOYED"
        self.assert_rejected(contract, "contract must remain NOT_DEPLOYED")


if __name__ == "__main__":
    unittest.main()
