#!/usr/bin/env python3
"""Adversarial tests for the public-surface manifest validator."""

from __future__ import annotations

import copy
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
VALIDATOR = REPO_ROOT / "scripts" / "validate_public_surface_manifest.py"
BASE_MANIFEST = json.loads(
    (REPO_ROOT / "docs" / "public-surface-manifest.v1.json").read_text(encoding="utf-8")
)


class PublicSurfaceManifestNegativeTests(unittest.TestCase):
    def run_validator(self, manifest: dict) -> subprocess.CompletedProcess[str]:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "docs").mkdir()
            (root / "dashboard" / "pages").mkdir(parents=True)
            (root / "README.md").write_bytes((REPO_ROOT / "README.md").read_bytes())
            (root / "dashboard" / "pages" / "index.tsx").write_bytes(
                (REPO_ROOT / "dashboard" / "pages" / "index.tsx").read_bytes()
            )
            (root / "docs" / "public-surface-manifest.v1.json").write_text(
                json.dumps(manifest, indent=2) + "\n",
                encoding="utf-8",
            )
            return subprocess.run(
                [sys.executable, str(VALIDATOR)],
                cwd=root,
                text=True,
                capture_output=True,
                check=False,
            )

    def assert_rejected(self, manifest: dict, needle: str) -> None:
        result = self.run_validator(manifest)
        self.assertNotEqual(result.returncode, 0, result.stdout)
        self.assertIn(needle, result.stderr)

    def test_current_manifest_passes(self) -> None:
        result = self.run_validator(copy.deepcopy(BASE_MANIFEST))
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("PUBLIC_SURFACE_MANIFEST_VALID", result.stdout)

    def test_duplicate_surface_id_fails_closed(self) -> None:
        manifest = copy.deepcopy(BASE_MANIFEST)
        manifest["surfaces"][1]["id"] = manifest["surfaces"][0]["id"]
        self.assert_rejected(manifest, "duplicate surface id")

    def test_duplicate_public_url_fails_closed(self) -> None:
        manifest = copy.deepcopy(BASE_MANIFEST)
        manifest["surfaces"][1]["url"] = manifest["surfaces"][0]["url"]
        self.assert_rejected(manifest, "duplicate public URL")

    def test_pass_cannot_hide_uninspectable_copy(self) -> None:
        manifest = copy.deepcopy(BASE_MANIFEST)
        linkedin = next(s for s in manifest["surfaces"] if s["id"] == "linkedin.profile")
        linkedin["release_gate"] = "PASS"
        self.assert_rejected(manifest, "PASS requires RECONCILED copy_state")

    def test_pass_requires_verified_public_reachability(self) -> None:
        manifest = copy.deepcopy(BASE_MANIFEST)
        portfolio = next(s for s in manifest["surfaces"] if s["id"] == "portfolio.home")
        portfolio["reachability"] = "UNVERIFIED"
        self.assert_rejected(manifest, "PASS requires VERIFIED_PUBLIC reachability")

    def test_weakened_scientific_n_ceiling_fails_closed(self) -> None:
        manifest = copy.deepcopy(BASE_MANIFEST)
        manifest["invariant_claims"]["SCIENTIFIC_N_INCREMENT"] = 1
        self.assert_rejected(manifest, "invariant_claims changed from the fail-closed baseline")

    def test_independent_validation_cannot_be_promoted(self) -> None:
        manifest = copy.deepcopy(BASE_MANIFEST)
        manifest["invariant_claims"]["INDEPENDENT_VALIDATION"] = "ESTABLISHED"
        self.assert_rejected(manifest, "invariant_claims changed from the fail-closed baseline")

    def test_high_assurance_cannot_be_promoted(self) -> None:
        manifest = copy.deepcopy(BASE_MANIFEST)
        manifest["invariant_claims"]["HIGH_ASSURANCE"] = "AUTHORIZED"
        self.assert_rejected(manifest, "invariant_claims changed from the fail-closed baseline")

    def test_tektite_current_and_accepted_proof_identity_cannot_collapse(self) -> None:
        manifest = copy.deepcopy(BASE_MANIFEST)
        tektite = next(
            s for s in manifest["surfaces"] if s["id"] == "tektite.bounded_demo"
        )
        tektite["source_version"]["current_git_commit"] = tektite["source_version"][
            "accepted_proof_source_sha"
        ]
        self.assert_rejected(
            manifest,
            "current Tektite deployment identity must remain distinct from accepted proof source identity",
        )

    def test_tektite_verifier_identity_cannot_drift(self) -> None:
        manifest = copy.deepcopy(BASE_MANIFEST)
        tektite = next(
            s for s in manifest["surfaces"] if s["id"] == "tektite.bounded_demo"
        )
        tektite["source_version"]["verifier_result"] = "PASS"
        self.assert_rejected(manifest, "unexpected accepted Tektite proof verifier result")

    def test_empty_refresh_triggers_fail_closed(self) -> None:
        manifest = copy.deepcopy(BASE_MANIFEST)
        manifest["surfaces"][0]["refresh_triggers"] = []
        self.assert_rejected(manifest, "refresh_triggers must be a non-empty list")

    def test_repository_owned_source_blob_drift_fails_closed(self) -> None:
        manifest = copy.deepcopy(BASE_MANIFEST)
        portfolio = next(s for s in manifest["surfaces"] if s["id"] == "portfolio.home")
        portfolio["local_source"]["git_blob_sha"] = "0" * 40
        self.assert_rejected(manifest, "local_source drift")


if __name__ == "__main__":
    unittest.main()
