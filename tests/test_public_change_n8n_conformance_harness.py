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
VALIDATOR = REPO_ROOT / "scripts" / "validate_public_change_n8n_conformance_harness.py"
BASE = json.loads(
    (REPO_ROOT / "automation" / "n8n" / "public-change-propagation-conformance-harness.v1.json").read_text(encoding="utf-8")
)


class PublicChangeN8nHarnessNegativeTests(unittest.TestCase):
    def run_validator(self, workflow: dict) -> subprocess.CompletedProcess[str]:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            p = root / "automation" / "n8n"
            p.mkdir(parents=True)
            (p / "public-change-propagation-conformance-harness.v1.json").write_text(
                json.dumps(workflow, indent=2) + "\n",
                encoding="utf-8",
            )
            return subprocess.run(
                [sys.executable, str(VALIDATOR)],
                cwd=root,
                text=True,
                capture_output=True,
                check=False,
            )

    def assert_rejected(self, workflow: dict, needle: str) -> None:
        result = self.run_validator(workflow)
        self.assertNotEqual(result.returncode, 0, result.stdout)
        self.assertIn(needle, result.stderr)

    def test_current_harness_passes(self) -> None:
        result = self.run_validator(copy.deepcopy(BASE))
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_missing_or_changed_workflow_id_is_rejected(self) -> None:
        w = copy.deepcopy(BASE)
        w["id"] = "wrong"
        self.assert_rejected(w, "unexpected workflow id")

    def test_activation_is_rejected(self) -> None:
        w = copy.deepcopy(BASE)
        w["active"] = True
        self.assert_rejected(w, "workflow must remain active=false")

    def test_network_authority_is_rejected(self) -> None:
        w = copy.deepcopy(BASE)
        w["meta"]["network_authority"] = "READ"
        self.assert_rejected(w, "network authority widened")

    def test_mutation_authority_is_rejected(self) -> None:
        w = copy.deepcopy(BASE)
        w["meta"]["mutation_authority"] = "WRITE"
        self.assert_rejected(w, "mutation authority widened")

    def test_http_node_is_rejected(self) -> None:
        w = copy.deepcopy(BASE)
        w["nodes"].append({
            "parameters": {},
            "id": "bad",
            "name": "HTTP",
            "type": "n8n-nodes-base.httpRequest",
            "typeVersion": 4,
            "position": [520, 0],
        })
        self.assert_rejected(w, "forbidden node type present")

    def test_embedded_credentials_are_rejected(self) -> None:
        w = copy.deepcopy(BASE)
        w["nodes"][1]["credentials"] = {"notionApi": {"id": "x", "name": "x"}}
        self.assert_rejected(w, "credentials must not be embedded")

    def test_fetch_in_code_is_rejected(self) -> None:
        w = copy.deepcopy(BASE)
        w["nodes"][1]["parameters"]["jsCode"] += "\nfetch('https://example.com');"
        self.assert_rejected(w, "forbidden code capability")

    def test_false_deployed_binding_is_rejected(self) -> None:
        w = copy.deepcopy(BASE)
        code = w["nodes"][1]["parameters"]["jsCode"]
        w["nodes"][1]["parameters"]["jsCode"] = code.replace("NOT_DEPLOYED", "DEPLOYED_BOUNDED")
        self.assert_rejected(w, "required inert binding missing")

    def test_false_promotion_eligibility_is_rejected(self) -> None:
        w = copy.deepcopy(BASE)
        code = w["nodes"][1]["parameters"]["jsCode"]
        w["nodes"][1]["parameters"]["jsCode"] = code.replace(
            "promotion_eligible: false", "promotion_eligible: true"
        )
        self.assert_rejected(w, "required inert binding missing")


if __name__ == "__main__":
    unittest.main()
