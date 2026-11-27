"""Offline transition regressions; no live network or production mutations."""
import unittest
from pathlib import Path

from profile_transition_contract import (
    blob_sha, check_profile, PROFILE_URL, RAW_URL, LEGACY_BLOB,
    LEGACY_MARKERS, CANDIDATE_MARKERS, PRIOR_PROFILE_BLOB, PRIOR_PROFILE_MARKERS,
)


class ProfileTransitionTests(unittest.TestCase):
    def setUp(self):
        self.candidate = Path("README.md").read_bytes()
        self.legacy = Path("README.archive.2026-11-26.md").read_bytes()
        self.surface = {
            "url": PROFILE_URL, "release_gate": "REVIEW",
            "local_source": {"path": "README.md", "git_blob_sha": blob_sha(self.candidate)},
        }
        self.rendered = (200, PROFILE_URL, " ".join(LEGACY_MARKERS))
        self.raw = (200, RAW_URL, self.legacy)

    def check(self, candidate=None, event="pull_request", ref="refs/pull/85/merge", rendered=None, raw=None, base_blob=LEGACY_BLOB):
        return check_profile(self.surface, self.candidate if candidate is None else candidate,
                             event, ref, self.rendered if rendered is None else rendered,
                             self.raw if raw is None else raw, base_blob=base_blob)

    def test_exact_archived_legacy(self):
        self.assertEqual(blob_sha(self.legacy), LEGACY_BLOB)
        result = self.check()
        self.assertEqual(result["result"], "PASS")
        self.assertEqual(result["candidate_contract"], "PASS")
        self.assertFalse(result["publication_authorized"])

    def test_main_candidate(self):
        result = self.check(event="schedule", ref="refs/heads/main",
                            rendered=(200, PROFILE_URL, " ".join(CANDIDATE_MARKERS)),
                            raw=(200, RAW_URL, self.candidate))
        self.assertEqual(result["result"], "PASS")

    def test_unchanged_post_cutover_pr(self):
        result = self.check(base_blob=blob_sha(self.candidate),
                            rendered=(200, PROFILE_URL, " ".join(CANDIDATE_MARKERS)),
                            raw=(200, RAW_URL, self.candidate))
        self.assertEqual(result["result"], "PASS")

    def test_qualified_successor_required(self):
        body = self.candidate.replace(b"Proposed successor identity", b"Current official identity")
        self.surface["local_source"]["git_blob_sha"] = blob_sha(body)
        self.assertEqual(self.check(candidate=body)["candidate_contract"], "FAIL")

    def test_prior_profile_requires_exact_public_blob_and_review(self):
        # Exact previous blob is required; candidate bytes must not impersonate it.
        result = self.check(base_blob=PRIOR_PROFILE_BLOB,
                            rendered=(200, PROFILE_URL, " ".join(PRIOR_PROFILE_MARKERS)),
                            raw=(200, RAW_URL, self.candidate))
        self.assertEqual(result["mode"], "PR_EXISTING_TEN_PROJECT_PROFILE")
        self.assertEqual(result["expected_public_blob"], PRIOR_PROFILE_BLOB)
        self.assertEqual(result["result"], "FAIL")
        self.surface["release_gate"] = "PASS"
        self.assertIn("PR transition requires REVIEW gate", self.check(base_blob=PRIOR_PROFILE_BLOB)["errors"])

    def test_unknown_or_missing_pr_base(self):
        for base in (None, "0" * 40):
            self.assertEqual(self.check(base_blob=base)["result"], "FAIL")

    def test_candidate_not_yet_published(self):
        self.assertEqual(self.check(raw=(200, RAW_URL, self.candidate))["result"], "FAIL")

    def test_legacy_not_current_after_cutover(self):
        self.assertEqual(self.check(event="schedule", ref="refs/heads/main")["result"], "FAIL")

    def test_wrong_candidate_blob(self):
        self.assertEqual(self.check(candidate=self.candidate + b"\n")["candidate_contract"], "FAIL")

    def test_wrong_order_even_if_rebound(self):
        body = self.candidate.replace(b"### 01 ", b"### 02 ", 1)
        self.surface["local_source"]["git_blob_sha"] = blob_sha(body)
        self.assertEqual(self.check(candidate=body)["candidate_contract"], "FAIL")

    def test_missing_heading_even_if_rebound(self):
        body = self.candidate.replace(b"Five flagship projects", b"Featured work")
        self.surface["local_source"]["git_blob_sha"] = blob_sha(body)
        self.assertEqual(self.check(candidate=body)["candidate_contract"], "FAIL")

    def test_rendered_503(self):
        self.assertEqual(self.check(rendered=(503, PROFILE_URL, self.rendered[2]))["result"], "FAIL")

    def test_rendered_markers_missing(self):
        self.assertEqual(self.check(rendered=(200, PROFILE_URL, ""))["result"], "FAIL")

    def test_rendered_redirect(self):
        self.assertEqual(self.check(rendered=(200, PROFILE_URL + "?changed", self.rendered[2]))["result"], "FAIL")

    def test_raw_503(self):
        self.assertEqual(self.check(raw=(503, RAW_URL, self.legacy))["result"], "FAIL")

    def test_raw_redirect(self):
        self.assertEqual(self.check(raw=(200, RAW_URL + "?changed", self.legacy))["result"], "FAIL")

    def test_raw_unknown_blob(self):
        self.assertEqual(self.check(raw=(200, RAW_URL, self.legacy + b"\n"))["result"], "FAIL")

    def test_non_main_dispatch(self):
        self.assertEqual(self.check(event="workflow_dispatch", ref="refs/heads/other")["result"], "FAIL")

    def test_unknown_context(self):
        self.assertEqual(self.check(event="", ref="")["result"], "FAIL")

    def test_pr_gate_not_promoted(self):
        self.surface["release_gate"] = "PASS"
        self.assertEqual(self.check()["result"], "FAIL")


if __name__ == "__main__":
    unittest.main()
