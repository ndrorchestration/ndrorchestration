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
VALIDATOR = REPO_ROOT / "scripts" / "validate_public_change_propagation_adapter.py"
BASE = json.loads(
    (REPO_ROOT / "docs" / "public-change-propagation-adapter.v1.json").read_text(encoding="utf-8")
)


class PublicChangePropagationAdapterNegativeTests(unittest.TestCase):
    def run_validator(self, adapter: dict) -> subprocess.CompletedProcess[str]:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "docs").mkdir()
            (root / "docs" / "public-change-propagation-adapter.v1.json").write_text(
                json.dumps(adapter, indent=2) + "\n",
                encoding="utf-8",
            )
            return subprocess.run(
                [sys.executable, str(VALIDATOR)],
                cwd=root,
                text=True,
                capture_output=True,
                check=False,
            )

    def assert_rejected(self, adapter: dict, needle: str) -> None:
        result = self.run_validator(adapter)
        self.assertNotEqual(result.returncode, 0, result.stdout)
        self.assertIn(needle, result.stderr)

    def test_current_adapter_passes(self) -> None:
        result = self.run_validator(copy.deepcopy(BASE))
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("PUBLIC_CHANGE_PROPAGATION_ADAPTER_VALID", result.stdout)

    def test_canonical_data_source_remap_is_rejected(self) -> None:
        adapter = copy.deepcopy(BASE)
        adapter["source_systems"]["canonical_registry"]["data_source"] = "collection://wrong"
        self.assert_rejected(adapter, "canonical_registry data_source changed")

    def test_asset_data_source_remap_is_rejected(self) -> None:
        adapter = copy.deepcopy(BASE)
        adapter["source_systems"]["external_asset_registry"]["data_source"] = "collection://wrong"
        self.assert_rejected(adapter, "external_asset_registry data_source changed")

    def test_endpoint_data_source_remap_is_rejected(self) -> None:
        adapter = copy.deepcopy(BASE)
        adapter["source_systems"]["public_surface_manifest"]["data_source"] = "collection://wrong"
        self.assert_rejected(adapter, "public_surface_manifest data_source changed")

    def test_read_before_write_step_cannot_be_removed(self) -> None:
        adapter = copy.deepcopy(BASE)
        adapter["execution_protocol"].remove("Read and snapshot each affected asset before mutation.")
        self.assert_rejected(adapter, "required execution protocol steps missing")

    def test_post_write_readback_cannot_be_removed(self) -> None:
        adapter = copy.deepcopy(BASE)
        adapter["execution_protocol"].remove("Re-read mutated records and compare against intended post-state.")
        self.assert_rejected(adapter, "required execution protocol steps missing")

    def test_block_preservation_cannot_be_removed(self) -> None:
        adapter = copy.deepcopy(BASE)
        adapter["mutation_preconditions"].remove("Any target already in Block remains Block.")
        self.assert_rejected(adapter, "required mutation precondition missing")

    def test_pass_done_prohibition_cannot_be_removed(self) -> None:
        adapter = copy.deepcopy(BASE)
        adapter["mutation_preconditions"].remove("No target may transition to Pass or Done.")
        self.assert_rejected(adapter, "required mutation precondition missing")

    def test_receipt_extension_cannot_drop_observed_post_state(self) -> None:
        adapter = copy.deepcopy(BASE)
        adapter["receipt_extension"]["additional_required_fields"].remove("observed_post_state")
        self.assert_rejected(adapter, "receipt extension fields changed")

    def test_false_deployment_is_rejected(self) -> None:
        adapter = copy.deepcopy(BASE)
        adapter["deployment"]["status"] = "DEPLOYED"
        self.assert_rejected(adapter, "adapter must remain NOT_DEPLOYED")


if __name__ == "__main__":
    unittest.main()
