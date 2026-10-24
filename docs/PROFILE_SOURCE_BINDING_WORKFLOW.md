# Profile README source-binding workflow

The ORBIT public-surface manifest binds `github.profile` to the exact Git blob SHA of the root README. This is a **freshness assertion**, not an assertion that profile copy is independently accepted.

When changing `README.md`, run from the repository root:

```bash
python3 scripts/sync_profile_source_blob.py --write
python3 scripts/sync_profile_source_blob.py
python3 scripts/validate_public_surface_manifest.py
python3 -m unittest tests/test_sync_profile_source_blob.py tests/test_public_surface_manifest.py
```

The default synchronizer mode is read-only, returns nonzero for mismatch, and prints the expected and actual SHA. `--write` changes only `github.profile.local_source.git_blob_sha`; it does not change the profile release gate, copy state, evidence claims, or other surfaces. Review the manifest diff alongside the README diff in the same pull request.

Do not skip the fail-closed validator, promote `REVIEW` to `PASS` merely because the hash matches, or infer production approval from a passing workflow. Recheck the exact PR head and run before requesting review.

Issue: [#78](https://github.com/ndrorchestration/ndrorchestration/issues/78). This change is a proposed deterministic helper; integration into contributor policy or CI should be decided in review.
