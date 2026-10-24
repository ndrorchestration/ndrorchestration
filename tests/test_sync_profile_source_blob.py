"""Contract tests for the README -> public-surface manifest SHA synchronizer."""
import hashlib
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "sync_profile_source_blob.py"


class ProfileSourceBlobSyncTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        (self.root / "docs").mkdir()
        (self.root / "README.md").write_bytes(b"New profile copy\n")
        self.manifest = {
            "invariant_claims": {"HIGH_ASSURANCE": "NOT_AUTHORIZED"},
            "surfaces": [{"id": "github.profile", "copy_state": "REVIEW_NEEDED",
                          "release_gate": "REVIEW",
                          "local_source": {"path": "README.md", "git_blob_sha": "0" * 40}}],
        }
        self.save()

    def save(self):
        (self.root / "docs" / "public-surface-manifest.v1.json").write_text(
            json.dumps(self.manifest) + "\n", encoding="utf-8"
        )

    def run_sync(self, *args):
        return subprocess.run([sys.executable, str(SCRIPT), *args],
                              cwd=self.root, capture_output=True, text=True, check=False)

    def test_check_fails_closed_without_mutating(self):
        before = (self.root / "docs" / "public-surface-manifest.v1.json").read_bytes()
        result = self.run_sync()
        self.assertEqual(result.returncode, 1)
        self.assertIn("DRIFT", result.stdout)
        self.assertEqual(before, (self.root / "docs" / "public-surface-manifest.v1.json").read_bytes())

    def test_write_updates_only_exact_blob_binding(self):
        result = self.run_sync("--write")
        self.assertEqual(result.returncode, 0, result.stderr)
        after = json.loads((self.root / "docs" / "public-surface-manifest.v1.json").read_text())
        expected = hashlib.sha1(b"blob 17\0New profile copy\n").hexdigest()
        self.assertEqual(after["surfaces"][0]["local_source"]["git_blob_sha"], expected)
        self.assertEqual(after["surfaces"][0]["release_gate"], "REVIEW")
        self.assertEqual(after["surfaces"][0]["copy_state"], "REVIEW_NEEDED")
        self.assertEqual(after["invariant_claims"], self.manifest["invariant_claims"])
        self.assertEqual(self.run_sync().returncode, 0)

    def test_wrong_source_path_blocks_write(self):
        self.manifest["surfaces"][0]["local_source"]["path"] = "other.md"
        self.save()
        self.assertNotEqual(self.run_sync("--write").returncode, 0)

    def test_missing_profile_blocks_write(self):
        self.manifest["surfaces"] = []
        self.save()
        self.assertNotEqual(self.run_sync("--write").returncode, 0)


if __name__ == "__main__":
    unittest.main()
