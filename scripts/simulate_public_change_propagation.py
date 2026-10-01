#!/usr/bin/env python3
"""Reference implementation for bounded public change propagation.

This is a pure, local state transformer for contract conformance testing.
It does not call Notion, n8n, Vercel, GitHub, or any external runtime.
"""

from __future__ import annotations

import copy
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from uuid import uuid4

CONTRACT_PATH = Path("docs/public-change-propagation-contract.v1.json")


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def load_contract() -> dict:
    return json.loads(CONTRACT_PATH.read_text(encoding="utf-8"))


def propagate(snapshot: dict, event: dict, *, contract: dict | None = None) -> tuple[dict, dict]:
    contract = contract or load_contract()
    state = copy.deepcopy(snapshot)

    canonical_id = event.get("canonical_message_id")
    trigger_class = event.get("trigger_class")
    trigger_source_version = event.get("trigger_source_version", "")

    receipt = {
        "schema": contract["audit_receipt"]["schema"],
        "receipt_id": str(uuid4()),
        "generated_at": now_iso(),
        "triggering_canonical_message_id": canonical_id,
        "trigger_class": trigger_class,
        "trigger_source_version": trigger_source_version,
        "affected_assets": [],
        "affected_endpoints": [],
        "prior_state": {"assets": {}, "endpoints": {}},
        "new_state": {"assets": {}, "endpoints": {}},
        "result": "PASS",
        "authority_effect": contract["audit_receipt"]["authority_effect"],
        "errors": [],
    }

    valid_triggers = set(contract["trigger"]["material_change_classes"])
    if trigger_class not in valid_triggers:
        receipt["result"] = "BLOCKED"
        receipt["errors"].append(f"unknown trigger_class: {trigger_class}")
        return state, receipt

    canonical = state.get("canonical_messages", {}).get(canonical_id)
    if canonical is None:
        receipt["result"] = "BLOCKED"
        receipt["errors"].append(f"canonical message not found: {canonical_id}")
        return state, receipt

    matched_assets = []
    for asset_id, asset in state.get("assets", {}).items():
        sources = set(asset.get("canonical_sources", []))
        triggers = set(asset.get("refresh_triggers", []))
        if canonical_id in sources and trigger_class in triggers:
            matched_assets.append(asset_id)

    if not matched_assets:
        receipt["result"] = "PARTIAL"
        receipt["errors"].append("no governed assets matched canonical source + refresh trigger")
        return state, receipt

    for asset_id in matched_assets:
        asset = state["assets"][asset_id]
        receipt["affected_assets"].append(asset_id)
        receipt["prior_state"]["assets"][asset_id] = {
            "release_gate": asset.get("release_gate"),
            "reconciliation_status": asset.get("reconciliation_status"),
        }

        if asset.get("release_gate") == "Block":
            receipt["new_state"]["assets"][asset_id] = copy.deepcopy(
                receipt["prior_state"]["assets"][asset_id]
            )
            receipt["errors"].append(f"{asset_id}: blocked asset preserved")
            receipt["result"] = "PARTIAL"
        else:
            asset["release_gate"] = "Review"
            asset["reconciliation_status"] = "In progress"
            receipt["new_state"]["assets"][asset_id] = {
                "release_gate": asset["release_gate"],
                "reconciliation_status": asset["reconciliation_status"],
            }

        endpoint_ids = asset.get("public_surface_endpoints")
        if not endpoint_ids:
            receipt["errors"].append(f"{asset_id}: missing public_surface_endpoints relation")
            receipt["result"] = "PARTIAL"
            continue

        for endpoint_id in endpoint_ids:
            endpoint = state.get("endpoints", {}).get(endpoint_id)
            if endpoint is None:
                receipt["errors"].append(f"{asset_id}: endpoint not found: {endpoint_id}")
                receipt["result"] = "PARTIAL"
                continue

            if endpoint_id not in receipt["affected_endpoints"]:
                receipt["affected_endpoints"].append(endpoint_id)
                receipt["prior_state"]["endpoints"][endpoint_id] = {
                    "release_gate": endpoint.get("release_gate"),
                    "copy_state": endpoint.get("copy_state"),
                }

            if endpoint.get("release_gate") == "Block":
                receipt["new_state"]["endpoints"][endpoint_id] = copy.deepcopy(
                    receipt["prior_state"]["endpoints"][endpoint_id]
                )
                receipt["errors"].append(f"{endpoint_id}: blocked endpoint preserved")
                receipt["result"] = "PARTIAL"
            else:
                endpoint["release_gate"] = "Review"
                endpoint["copy_state"] = "Review Needed"
                receipt["new_state"]["endpoints"][endpoint_id] = {
                    "release_gate": endpoint["release_gate"],
                    "copy_state": endpoint["copy_state"],
                }

    return state, receipt


def main() -> None:
    if len(sys.argv) != 3:
        raise SystemExit(
            "usage: simulate_public_change_propagation.py SNAPSHOT_JSON EVENT_JSON"
        )
    snapshot = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    event = json.loads(Path(sys.argv[2]).read_text(encoding="utf-8"))
    state, receipt = propagate(snapshot, event)
    print(json.dumps({"state": state, "receipt": receipt}, indent=2))


if __name__ == "__main__":
    main()
