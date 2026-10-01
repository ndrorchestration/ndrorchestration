#!/usr/bin/env python3
from __future__ import annotations
import json
from pathlib import Path
P=Path("automation/n8n/public-change-propagation-vector-conformance.v1.json")
ALLOWED={"n8n-nodes-base.manualTrigger","n8n-nodes-base.code"}
def fail(m): raise SystemExit("PUBLIC_CHANGE_N8N_VECTOR_HARNESS_INVALID: "+m)
def main():
 d=json.loads(P.read_text(encoding="utf-8"))
 if d.get("id")!="publicChangeVectorConformance001": fail("unexpected workflow id")
 if d.get("active") is not False: fail("workflow must remain active=false")
 m=d.get("meta",{})
 if m.get("mutation_authority")!="NONE": fail("mutation authority widened")
 if m.get("network_authority")!="NONE": fail("network authority widened")
 if m.get("conformance_schema")!="NDR_PUBLIC_CHANGE_PROPAGATION_CONFORMANCE_V1": fail("conformance schema changed")
 for n in d.get("nodes",[]):
  if n.get("type") not in ALLOWED: fail("forbidden node type")
  if n.get("credentials"): fail("credentials forbidden")
  if n.get("type")=="n8n-nodes-base.code":
   code=n.get("parameters",{}).get("jsCode","")
   for s in ("fetch(","require(","process.env","axios","$http","$request"):
    if s in code: fail("forbidden code capability: "+s)
   for s in ("pass_to_review","idempotent_review","blocked_asset","blocked_endpoint","missing_relation","unknown_canonical","unknown_trigger","PORTABLE_VECTOR_CONFORMANCE_FAILED","NOT_DEPLOYED","NONE_DEPLOYMENT_EVIDENCE_ONLY"):
    if s not in code: fail("required conformance marker missing: "+s)
 print("PUBLIC_CHANGE_N8N_VECTOR_HARNESS_VALID")
if __name__=="__main__": main()
