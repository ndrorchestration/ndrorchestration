#!/usr/bin/env python3
from __future__ import annotations
import json
from pathlib import Path

P = Path("docs/public-change-propagation-adapter.v1.json")

def fail(msg: str) -> None:
    raise SystemExit(f"PUBLIC_CHANGE_PROPAGATION_ADAPTER_INVALID: {msg}")

def main() -> None:
    d=json.loads(P.read_text(encoding="utf-8"))
    if d.get("schema_version")!="NDR_PUBLIC_CHANGE_PROPAGATION_ADAPTER_V1":
        fail("unexpected schema_version")
    if d.get("deployment",{}).get("status")!="NOT_DEPLOYED":
        fail("adapter must remain NOT_DEPLOYED until runtime evidence exists")
    src=d.get("source_systems",{})
    expected={
      "canonical_registry":"collection://d6b116f3-19de-410e-b11f-3828d273d938",
      "external_asset_registry":"collection://c81c3f9b-bbc7-48ac-bc7f-bd2a9625c2b8",
      "public_surface_manifest":"collection://02334462-afea-472c-b244-b7700bb7e726"
    }
    for k,v in expected.items():
        if src.get(k,{}).get("data_source")!=v:
            fail(f"{k} data_source changed")
    protocol=set(d.get("execution_protocol",[]))
    required_snippets=[
      "Read and snapshot each affected asset before mutation.",
      "Read and snapshot each endpoint before mutation.",
      "Re-read mutated records and compare against intended post-state.",
      "Stop. Never auto-promote Review or Block."
    ]
    if not set(required_snippets).issubset(protocol):
        fail("required execution protocol steps missing")
    pre=set(d.get("mutation_preconditions",[]))
    for req in [
      "Prior state must be captured before writes.",
      "Any target already in Block remains Block.",
      "No target may transition to Pass or Done."
    ]:
        if req not in pre:
            fail("required mutation precondition missing")
    ext=d.get("receipt_extension",{})
    if ext.get("base_schema")!="NDR_PUBLIC_CHANGE_PROPAGATION_RECEIPT_V1":
        fail("receipt base schema changed")
    fields=set(ext.get("additional_required_fields",[]))
    needed={"adapter_schema_version","canonical_record_url","asset_record_urls","endpoint_record_urls","observed_post_state","write_conflicts"}
    if fields!=needed:
        fail("receipt extension fields changed")
    print("PUBLIC_CHANGE_PROPAGATION_ADAPTER_VALID")

if __name__=="__main__":
    main()
