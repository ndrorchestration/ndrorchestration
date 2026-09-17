import json
import tempfile
import unittest
from pathlib import Path

from scripts.validate_repository_lifecycle import validate_registry


class RepositoryLifecycleValidatorTests(unittest.TestCase):
    def write_registry(self, payload):
        temp_dir = tempfile.TemporaryDirectory()
        self.addCleanup(temp_dir.cleanup)
        path = Path(temp_dir.name) / "registry.json"
        path.write_text(json.dumps(payload), encoding="utf-8")
        return path

    def base_registry(self):
        return {
            "schema_version": "1.0.0",
            "generated_at": "2026-09-16",
            "authority_scope": "ACCOUNT_LEVEL_LIFECYCLE_ONLY",
            "repositories": [
                {
                    "repository": "ndrorchestration/example",
                    "product_name": "Example",
                    "visibility": "public",
                    "github_archived": False,
                    "origin": "authored",
                    "review_status": "VERIFIED",
                    "lifecycle": "ACTIVE_CORE",
                    "responsibility": "Owns one bounded example responsibility.",
                    "canonical_project_source": "https://github.com/ndrorchestration/example",
                    "relationships": [],
                    "current_claim_boundary": "Project-local evidence only.",
                    "reviewed_at": "2026-09-16",
                    "notes": None,
                }
            ],
        }

    def test_valid_registry_has_no_violations(self):
        path = self.write_registry(self.base_registry())
        self.assertEqual(validate_registry(str(path)), [])

    def test_duplicate_repository_is_rejected(self):
        payload = self.base_registry()
        payload["repositories"].append(dict(payload["repositories"][0]))
        path = self.write_registry(payload)
        violations = validate_registry(str(path))
        self.assertTrue(any("duplicate repository" in item for item in violations))

    def test_invalid_lifecycle_is_rejected(self):
        payload = self.base_registry()
        payload["repositories"][0]["lifecycle"] = "CURRENT"
        path = self.write_registry(payload)
        violations = validate_registry(str(path))
        self.assertTrue(any("invalid lifecycle" in item for item in violations))

    def test_invalid_review_status_is_rejected(self):
        payload = self.base_registry()
        payload["repositories"][0]["review_status"] = "DONE"
        path = self.write_registry(payload)
        violations = validate_registry(str(path))
        self.assertTrue(any("invalid review_status" in item for item in violations))

    def test_verified_entry_requires_responsibility(self):
        payload = self.base_registry()
        payload["repositories"][0]["responsibility"] = ""
        path = self.write_registry(payload)
        violations = validate_registry(str(path))
        self.assertTrue(any("VERIFIED entry requires responsibility" in item for item in violations))

    def test_external_reference_requires_external_origin_and_upstream_context(self):
        payload = self.base_registry()
        entry = payload["repositories"][0]
        entry["lifecycle"] = "EXTERNAL_REFERENCE"
        entry["origin"] = "authored"
        entry["notes"] = None
        path = self.write_registry(payload)
        violations = validate_registry(str(path))
        self.assertTrue(any("EXTERNAL_REFERENCE requires external origin" in item for item in violations))
        self.assertTrue(any("EXTERNAL_REFERENCE requires upstream context" in item for item in violations))

    def test_archived_lifecycle_requires_github_archived_true(self):
        payload = self.base_registry()
        payload["repositories"][0]["lifecycle"] = "ARCHIVED"
        payload["repositories"][0]["github_archived"] = False
        path = self.write_registry(payload)
        violations = validate_registry(str(path))
        self.assertTrue(any("ARCHIVED requires github_archived=true" in item for item in violations))

    def test_pending_review_may_leave_lifecycle_unresolved(self):
        payload = self.base_registry()
        entry = payload["repositories"][0]
        entry["review_status"] = "PENDING_REVIEW"
        entry["lifecycle"] = None
        entry["responsibility"] = None
        path = self.write_registry(payload)
        self.assertEqual(validate_registry(str(path)), [])


if __name__ == "__main__":
    unittest.main()
