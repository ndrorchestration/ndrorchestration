#!/usr/bin/env python3
from __future__ import annotations

import copy
import importlib.util
import json
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = REPO_ROOT / "scripts" / "simulate_public_change_propagation.py"

spec = importlib.util.spec_from_file_location("prop_ref", MODULE_PATH)
mod = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(mod)

BASE = {
    "canonical_messages": {
        "canonical.dgaf": {"id": "canonical.dgaf"}
    },
    "assets": {
        "asset.dgaf": {
            "canonical_sources": ["canonical.dgaf"],
            "refresh_triggers": ["CANONICAL_CLAIM_CHANGED"],
            "release_gate": "Pass",
            "reconciliation_status": "Done",
            "public_surface_endpoints": ["endpoint.dgaf"],
        }
    },
    "endpoints": {
        "endpoint.dgaf": {
            "release_gate": "Pass",
            "copy_state": "Reconciled",
        }
    },
}

EVENT = {
    "canonical_message_id": "canonical.dgaf",
    "trigger_class": "CANONICAL_CLAIM_CHANGED",
    "trigger_source_version": "example-v2",
}


class PublicChangePropagationReferenceTests(unittest.TestCase):
    def test_pass_moves_only_to_review(self) -> None:
        state, receipt = mod.propagate(copy.deepcopy(BASE), copy.deepcopy(EVENT))
        self.assertEqual(receipt["result"], "PASS")
        self.assertEqual(state["assets"]["asset.dgaf"]["release_gate"], "Review")
        self.assertEqual(
            state["assets"]["asset.dgaf"]["reconciliation_status"], "In progress"
        )
        self.assertEqual(state["endpoints"]["endpoint.dgaf"]["release_gate"], "Review")
        self.assertEqual(
            state["endpoints"]["endpoint.dgaf"]["copy_state"], "Review Needed"
        )
        self.assertEqual(receipt["authority_effect"], "NONE_RECONCILIATION_ONLY")

    def test_idempotent_review_state(self) -> None:
        once, receipt1 = mod.propagate(copy.deepcopy(BASE), copy.deepcopy(EVENT))
        twice, receipt2 = mod.propagate(once, copy.deepcopy(EVENT))
        self.assertEqual(receipt1["result"], "PASS")
        self.assertEqual(receipt2["result"], "PASS")
        self.assertEqual(once, twice)

    def test_blocked_asset_is_never_weakened(self) -> None:
        snapshot = copy.deepcopy(BASE)
        snapshot["assets"]["asset.dgaf"]["release_gate"] = "Block"
        snapshot["assets"]["asset.dgaf"]["reconciliation_status"] = "In progress"
        state, receipt = mod.propagate(snapshot, copy.deepcopy(EVENT))
        self.assertEqual(state["assets"]["asset.dgaf"]["release_gate"], "Block")
        self.assertEqual(receipt["result"], "PARTIAL")

    def test_blocked_endpoint_is_never_weakened(self) -> None:
        snapshot = copy.deepcopy(BASE)
        snapshot["endpoints"]["endpoint.dgaf"]["release_gate"] = "Block"
        snapshot["endpoints"]["endpoint.dgaf"]["copy_state"] = "Review Needed"
        state, receipt = mod.propagate(snapshot, copy.deepcopy(EVENT))
        self.assertEqual(state["endpoints"]["endpoint.dgaf"]["release_gate"], "Block")
        self.assertEqual(receipt["result"], "PARTIAL")

    def test_missing_endpoint_relation_is_partial(self) -> None:
        snapshot = copy.deepcopy(BASE)
        snapshot["assets"]["asset.dgaf"]["public_surface_endpoints"] = []
        state, receipt = mod.propagate(snapshot, copy.deepcopy(EVENT))
        self.assertEqual(receipt["result"], "PARTIAL")
        self.assertIn("missing public_surface_endpoints relation", receipt["errors"][0])
        self.assertEqual(state["assets"]["asset.dgaf"]["release_gate"], "Review")

    def test_missing_endpoint_record_is_partial(self) -> None:
        snapshot = copy.deepcopy(BASE)
        del snapshot["endpoints"]["endpoint.dgaf"]
        _, receipt = mod.propagate(snapshot, copy.deepcopy(EVENT))
        self.assertEqual(receipt["result"], "PARTIAL")
        self.assertTrue(any("endpoint not found" in e for e in receipt["errors"]))

    def test_unknown_canonical_is_blocked_and_noop(self) -> None:
        event = copy.deepcopy(EVENT)
        event["canonical_message_id"] = "canonical.missing"
        state, receipt = mod.propagate(copy.deepcopy(BASE), event)
        self.assertEqual(receipt["result"], "BLOCKED")
        self.assertEqual(state, BASE)

    def test_unknown_trigger_is_blocked_and_noop(self) -> None:
        event = copy.deepcopy(EVENT)
        event["trigger_class"] = "UNAUTHORIZED_CHANGE"
        state, receipt = mod.propagate(copy.deepcopy(BASE), event)
        self.assertEqual(receipt["result"], "BLOCKED")
        self.assertEqual(state, BASE)

    def test_unmatched_refresh_trigger_is_partial_and_noop(self) -> None:
        event = copy.deepcopy(EVENT)
        event["trigger_class"] = "SOURCE_AUTHORITY_CHANGED"
        state, receipt = mod.propagate(copy.deepcopy(BASE), event)
        self.assertEqual(receipt["result"], "PARTIAL")
        self.assertEqual(state, BASE)

    def test_receipt_contains_required_contract_fields(self) -> None:
        _, receipt = mod.propagate(copy.deepcopy(BASE), copy.deepcopy(EVENT))
        contract = json.loads(
            (REPO_ROOT / "docs" / "public-change-propagation-contract.v1.json").read_text(
                encoding="utf-8"
            )
        )
        self.assertTrue(set(contract["audit_receipt"]["required_fields"]).issubset(receipt))


if __name__ == "__main__":
    unittest.main()
