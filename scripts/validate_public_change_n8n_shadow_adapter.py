#!/usr/bin/env python3
from __future__ import annotations
import json
from pathlib import Path
P=Path("automation/n8n/public-change-propagation-shadow-adapter.v1.json")
ALLOWED={"n8n-nodes-base.manualTrigger","n8n-nodes-base.code"}
def fail(m): raise SystemExit("PUBLIC_CHANGE_N8N_SHADOW_ADAPTER_INVALID: "+m)
def main():
 d=json.loads(P.read_text(encoding="utf-8"))
 if d.get("id")!="publicChangeShadowAdapter001": fail("unexpected workflow id")
 if d.get("active") is not False: fail("workflow must remain active=false")
 m=d.get("meta",{})
 if m.get("adapter_surface")!="SHADOW_ONLY": fail("adapter surface changed")
 if m.get("mutation_authority")!="NONE": fail("mutation authority widened")
 if m.get("network_authority")!="NONE": fail("network authority widened")
 for n in d.get("nodes",[]):
  if n.get("type") not in ALLOWED: fail("forbidden node type")
  if n.get("credentials"): fail("credentials forbidden")
  if n.get("type")=="n8n-nodes-base.code":
   code=n.get("parameters",{}).get("jsCode","")
   for s in ("fetch(","require(","process.env","axios","$http","$request"):
    if s in code: fail("forbidden code capability: "+s)
   for s in ("SHADOW_ONLY","NOT_DEPLOYED","promotion_eligible:false","read_before_write:'PASS'","post_write_readback:'PASS'","write_conflict_detection:'PASS'","SHADOW_ADAPTER_CONFORMANCE_FAILED"):
    if s not in code: fail("required shadow marker missing: "+s)
 print("PUBLIC_CHANGE_N8N_SHADOW_ADAPTER_VALID")
if __name__=="__main__": main()
