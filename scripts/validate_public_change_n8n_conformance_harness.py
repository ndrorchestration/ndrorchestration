#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

P = Path("automation/n8n/public-change-propagation-conformance-harness.v1.json")

ALLOWED_TYPES = {
    "n8n-nodes-base.manualTrigger",
    "n8n-nodes-base.code",
}
FORBIDDEN_SNIPPETS = (
    "fetch(",
    "require(",
    "process.env",
    "$http",
    "$request",
    "axios",
    "credentials",
)


def fail(message: str) -> None:
    raise SystemExit(f"PUBLIC_CHANGE_N8N_HARNESS_INVALID: {message}")


def main() -> None:
    d = json.loads(P.read_text(encoding="utf-8"))

    if d.get("id") != "publicChangeConformance001":
        fail("unexpected workflow id")

    if d.get("active") is not False:
        fail("workflow must remain active=false")

    meta = d.get("meta", {})
    if meta.get("harness_schema") != "NDR_PUBLIC_CHANGE_PROPAGATION_N8N_CONFORMANCE_HARNESS_V1":
        fail("unexpected harness_schema")
    if meta.get("import_compatibility") != "UNVERIFIED_UNTIL_LOCAL_RUNTIME_AVAILABLE":
        fail("import compatibility must remain unverified")
    if meta.get("mutation_authority") != "NONE":
        fail("mutation authority widened")
    if meta.get("network_authority") != "NONE":
        fail("network authority widened")

    nodes = d.get("nodes", [])
    if not nodes:
        fail("no nodes")
    node_types = {n.get("type") for n in nodes}
    if not node_types.issubset(ALLOWED_TYPES):
        fail("forbidden node type present")

    for node in nodes:
        if node.get("credentials"):
            fail("credentials must not be embedded")
        if node.get("type") == "n8n-nodes-base.code":
            code = node.get("parameters", {}).get("jsCode", "")
            for snippet in FORBIDDEN_SNIPPETS:
                if snippet in code:
                    fail(f"forbidden code capability: {snippet}")
            for required in (
                "INERT_CONFORMANCE_ONLY",
                "NOT_DEPLOYED",
                "promotion_eligible: false",
                "NONE_DEPLOYMENT_EVIDENCE_ONLY",
                "NDR_PUBLIC_CHANGE_RUNTIME_EVIDENCE_RECEIPT_V1",
            ):
                if required not in code:
                    fail(f"required inert binding missing: {required}")

    serialized = json.dumps(d)
    for forbidden_type in (
        "n8n-nodes-base.httpRequest",
        "n8n-nodes-base.notion",
        "n8n-nodes-base.webhook",
        "n8n-nodes-base.executeCommand",
        "n8n-nodes-base.ssh",
    ):
        if forbidden_type in serialized:
            fail(f"forbidden runtime-capability node: {forbidden_type}")

    print("PUBLIC_CHANGE_N8N_CONFORMANCE_HARNESS_VALID")


if __name__ == "__main__":
    main()
