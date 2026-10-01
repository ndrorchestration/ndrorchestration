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
VALIDATOR = REPO_ROOT / "scripts" / "validate_public_change_propagation_deployment_gate.py"
BASE = json.loads(
    (REPO_ROOT / "docs" / "public-change-propagation-deployment-gate.v1.json").read_text(encoding="utf-8")
)


class PublicChangePropagationDeploymentGateNegativeTests(unittest.TestCase):
    def run_validator(self, gate: dict) -> subprocess.CompletedProcess[str]:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "docs").mkdir()
            (root / "docs" / "public-change-propagation-deployment-gate.v1.json").write_text(
                json.dumps(gate, indent=2) + "\n",
                encoding="utf-8",
            )
            return subprocess.run(
                [sys.executable, str(VALIDATOR)],
                cwd=root,
                text=True,
                capture_output=True,
                check=False,
            )

    def assert_rejected(self, gate: dict, needle: str) -> None:
        result = self.run_validator(gate)
        self.assertNotEqual(result.returncode, 0, result.stdout)
        self.assertIn(needle, result.stderr)

    def test_current_gate_passes(self) -> None:
        result = self.run_validator(copy.deepcopy(BASE))
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("PUBLIC_CHANGE_PROPAGATION_DEPLOYMENT_GATE_VALID", result.stdout)

    def test_premature_deployed_state_is_rejected(self) -> None:
        gate = copy.deepcopy(BASE)
        gate["current_state"] = "DEPLOYED_BOUNDED"
        self.assert_rejected(gate, "current_state must remain NOT_DEPLOYED")

    def test_promotable_state_cannot_be_widened(self) -> None:
        gate = copy.deepcopy(BASE)
        gate["promotable_state"] = "DEPLOYED"
        self.assert_rejected(gate, "unexpected promotable_state")

    def test_runtime_identity_evidence_cannot_be_removed(self) -> None:
        gate = copy.deepcopy(BASE)
        gate["required_evidence"].remove("runtime_identity")
        self.assert_rejected(gate, "required_evidence changed")

    def test_adapter_surface_evidence_cannot_be_removed(self) -> None:
        gate = copy.deepcopy(BASE)
        gate["required_evidence"].remove("adapter_surface")
        self.assert_rejected(gate, "required_evidence changed")

    def test_portable_vector_results_cannot_be_removed(self) -> None:
        gate = copy.deepcopy(BASE)
        gate["required_evidence"].remove("portable_vector_results")
        self.assert_rejected(gate, "required_evidence changed")

    def test_read_before_write_evidence_cannot_be_removed(self) -> None:
        gate = copy.deepcopy(BASE)
        gate["required_evidence"].remove("read_before_write_evidence")
        self.assert_rejected(gate, "required_evidence changed")

    def test_receipt_digest_cannot_be_removed(self) -> None:
        gate = copy.deepcopy(BASE)
        gate["required_evidence"].remove("runtime_receipt_digest")
        self.assert_rejected(gate, "required_evidence changed")

    def test_all_vectors_rule_cannot_be_removed(self) -> None:
        gate = copy.deepcopy(BASE)
        gate["promotion_rules"].remove(
            "Every portable conformance vector must pass on the actual runtime implementation."
        )
        self.assert_rejected(gate, "promotion rules weakened")

    def test_happy_path_shortcut_cannot_be_removed(self) -> None:
        gate = copy.deepcopy(BASE)
        gate["promotion_rules"].remove(
            "A successful connection, workflow import, workflow activation, or single happy-path run is insufficient for promotion."
        )
        self.assert_rejected(gate, "promotion rules weakened")

    def test_connected_implies_deployed_inference_cannot_be_removed(self) -> None:
        gate = copy.deepcopy(BASE)
        gate["forbidden_inferences"].remove("CONNECTED implies DEPLOYED")
        self.assert_rejected(gate, "forbidden inference missing")

    def test_conformant_implies_validated_inference_cannot_be_removed(self) -> None:
        gate = copy.deepcopy(BASE)
        gate["forbidden_inferences"].remove("CONFORMANT implies VALIDATED")
        self.assert_rejected(gate, "forbidden inference missing")

    def test_high_assurance_inference_cannot_be_removed(self) -> None:
        gate = copy.deepcopy(BASE)
        gate["forbidden_inferences"].remove("DEPLOYED_BOUNDED implies HIGH_ASSURANCE")
        self.assert_rejected(gate, "forbidden inference missing")

    def test_independent_validation_inference_cannot_be_removed(self) -> None:
        gate = copy.deepcopy(BASE)
        gate["forbidden_inferences"].remove(
            "DEPLOYED_BOUNDED implies INDEPENDENT_VALIDATION"
        )
        self.assert_rejected(gate, "forbidden inference missing")


if __name__ == "__main__":
    unittest.main()
