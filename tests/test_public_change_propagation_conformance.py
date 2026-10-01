#!/usr/bin/env python3
from __future__ import annotations

import copy
import importlib.util
import json
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = REPO_ROOT / "scripts" / "simulate_public_change_propagation.py"
FIXTURES = REPO_ROOT / "tests" / "fixtures" / "public-change-propagation-conformance.v1.json"

spec = importlib.util.spec_from_file_location("prop_ref", MODULE_PATH)
mod = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(mod)

VECTORS = json.loads(FIXTURES.read_text(encoding="utf-8"))


class PublicChangePropagationConformanceTests(unittest.TestCase):
    def test_fixture_schema(self) -> None:
        self.assertEqual(
            VECTORS["schema_version"],
            "NDR_PUBLIC_CHANGE_PROPAGATION_CONFORMANCE_V1",
        )
        self.assertGreaterEqual(len(VECTORS["cases"]), 7)

    def test_reference_matches_all_portable_vectors(self) -> None:
        for case in VECTORS["cases"]:
            with self.subTest(case=case["id"]):
                original = copy.deepcopy(case["snapshot"])
                state, receipt = mod.propagate(
                    copy.deepcopy(case["snapshot"]),
                    copy.deepcopy(case["event"]),
                )
                expect = case["expect"]

                self.assertEqual(receipt["result"], expect["result"])

                if "authority_effect" in expect:
                    self.assertEqual(
                        receipt["authority_effect"],
                        expect["authority_effect"],
                    )

                for asset_id, expected in expect.get("asset_state", {}).items():
                    actual = state["assets"][asset_id]
                    self.assertEqual(actual["release_gate"], expected["release_gate"])
                    self.assertEqual(
                        actual["reconciliation_status"],
                        expected["reconciliation_status"],
                    )

                for endpoint_id, expected in expect.get("endpoint_state", {}).items():
                    actual = state["endpoints"][endpoint_id]
                    self.assertEqual(actual["release_gate"], expected["release_gate"])
                    self.assertEqual(actual["copy_state"], expected["copy_state"])

                if expect.get("no_state_change"):
                    self.assertEqual(state, original)

                if "error_contains" in expect:
                    self.assertTrue(
                        any(expect["error_contains"] in error for error in receipt["errors"]),
                        receipt["errors"],
                    )

    def test_vectors_never_expect_stronger_state(self) -> None:
        for case in VECTORS["cases"]:
            with self.subTest(case=case["id"]):
                for expected in case["expect"].get("asset_state", {}).values():
                    self.assertNotEqual(expected.get("release_gate"), "Pass")
                    self.assertNotEqual(expected.get("reconciliation_status"), "Done")
                for expected in case["expect"].get("endpoint_state", {}).values():
                    self.assertNotEqual(expected.get("release_gate"), "Pass")


if __name__ == "__main__":
    unittest.main()
