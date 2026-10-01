#!/usr/bin/env python3
from __future__ import annotations
import json
from pathlib import Path

P=Path("docs/public-change-propagation-deployment-gate.v1.json")

def fail(msg:str)->None:
    raise SystemExit(f"PUBLIC_CHANGE_PROPAGATION_DEPLOYMENT_GATE_INVALID: {msg}")

def main()->None:
    d=json.loads(P.read_text(encoding="utf-8"))
    if d.get("schema_version")!="NDR_PUBLIC_CHANGE_PROPAGATION_DEPLOYMENT_GATE_V1":
        fail("unexpected schema_version")
    if d.get("current_state")!="NOT_DEPLOYED":
        fail("current_state must remain NOT_DEPLOYED absent runtime evidence")
    if d.get("promotable_state")!="DEPLOYED_BOUNDED":
        fail("unexpected promotable_state")
    req=set(d.get("required_evidence",[]))
    needed={
        "runtime_identity","workflow_export_or_definition_hash","adapter_schema_version",
        "contract_schema_version","conformance_schema_version","exact_runtime_version",
        "execution_timestamp","portable_vector_results","adapter_surface","read_before_write_evidence",
        "post_write_readback_evidence","block_preservation_evidence",
        "pass_done_prohibition_evidence","idempotency_evidence",
        "missing_relation_partial_evidence","unknown_trigger_blocked_evidence",
        "receipt_schema_validation","runtime_receipt_digest","operator_or_agent_review"
    }
    if req!=needed:
        fail("required_evidence changed")
    rules=set(d.get("promotion_rules",[]))
    required_rules={
        "All required evidence fields must be present and nonempty.",
        "Every portable conformance vector must pass on the actual runtime implementation.",
        "No covered case may produce Pass or Done promotion.",
        "Any missing, stale, ambiguous, or conflicting evidence keeps state NOT_DEPLOYED.",
        "A successful connection, workflow import, workflow activation, or single happy-path run is insufficient for promotion.",
        "Deployment promotion requires adapter_surface=LIVE_NOTION; SHADOW_ONLY evidence is non-promotable."
    }
    if not required_rules.issubset(rules):
        fail("promotion rules weakened")
    forb=set(d.get("forbidden_inferences",[]))
    for needed_forbidden in {
        "CONNECTED implies DEPLOYED",
        "ACTIVE implies CONFORMANT",
        "CONFORMANT implies VALIDATED",
        "DEPLOYED_BOUNDED implies HIGH_ASSURANCE",
        "DEPLOYED_BOUNDED implies INDEPENDENT_VALIDATION"
    }:
        if needed_forbidden not in forb:
            fail("forbidden inference missing")
    print("PUBLIC_CHANGE_PROPAGATION_DEPLOYMENT_GATE_VALID")

if __name__=="__main__":
    main()
