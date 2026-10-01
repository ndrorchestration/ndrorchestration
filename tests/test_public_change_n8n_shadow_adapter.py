#!/usr/bin/env python3
from __future__ import annotations
import copy,json,subprocess,sys,tempfile,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
VALIDATOR=ROOT/"scripts"/"validate_public_change_n8n_shadow_adapter.py"
BASE=json.loads((ROOT/"automation"/"n8n"/"public-change-propagation-shadow-adapter.v1.json").read_text(encoding="utf-8"))
class Tests(unittest.TestCase):
 def runv(self,w):
  with tempfile.TemporaryDirectory() as tmp:
   root=Path(tmp); p=root/"automation"/"n8n"; p.mkdir(parents=True)
   (p/"public-change-propagation-shadow-adapter.v1.json").write_text(json.dumps(w,indent=2)+"\n",encoding="utf-8")
   return subprocess.run([sys.executable,str(VALIDATOR)],cwd=root,text=True,capture_output=True,check=False)
 def reject(self,w,s):
  r=self.runv(w); self.assertNotEqual(r.returncode,0); self.assertIn(s,r.stderr)
 def test_current_passes(self): self.assertEqual(self.runv(copy.deepcopy(BASE)).returncode,0)
 def test_activation_rejected(self):
  w=copy.deepcopy(BASE); w["active"]=True; self.reject(w,"active=false")
 def test_live_surface_rejected(self):
  w=copy.deepcopy(BASE); w["meta"]["adapter_surface"]="LIVE_NOTION"; self.reject(w,"adapter surface changed")
 def test_network_rejected(self):
  w=copy.deepcopy(BASE); w["meta"]["network_authority"]="READ"; self.reject(w,"network authority widened")
 def test_mutation_rejected(self):
  w=copy.deepcopy(BASE); w["meta"]["mutation_authority"]="WRITE"; self.reject(w,"mutation authority widened")
 def test_credentials_rejected(self):
  w=copy.deepcopy(BASE); w["nodes"][1]["credentials"]={"x":{"id":"x"}}; self.reject(w,"credentials forbidden")
 def test_fetch_rejected(self):
  w=copy.deepcopy(BASE); w["nodes"][1]["parameters"]["jsCode"]+="\nfetch('https://example.com')"; self.reject(w,"forbidden code capability")
 def test_promotion_rejected(self):
  w=copy.deepcopy(BASE); w["nodes"][1]["parameters"]["jsCode"]=w["nodes"][1]["parameters"]["jsCode"].replace("promotion_eligible:false","promotion_eligible:true"); self.reject(w,"required shadow marker missing")
if __name__=="__main__": unittest.main()
