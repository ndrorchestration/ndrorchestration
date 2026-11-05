#!/usr/bin/env python3
"""Synchronize README's exact Git blob identity in the public-surface manifest.

Default mode is read-only and fails closed on drift. --write changes only the
github.profile.local_source.git_blob_sha field, never release/copy status.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

MANIFEST = Path("docs/public-surface-manifest.v1.json")
README = Path("README.md")


def git_blob_sha(body: bytes) -> str:
    return hashlib.sha1(f"blob {len(body)}\0".encode("ascii") + body).hexdigest()


def sync(write: bool = False) -> int:
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    profiles = [s for s in manifest["surfaces"] if s.get("id") == "github.profile"]
    if len(profiles) != 1 or profiles[0].get("local_source", {}).get("path") != "README.md":
        raise ValueError("expected exactly one github.profile README source binding")
    profile = profiles[0]
    actual = git_blob_sha(README.read_bytes())
    previous = profile["local_source"].get("git_blob_sha")
    if previous == actual:
        print("PROFILE_SOURCE_BLOB_SYNC=PASS")
        return 0
    if not write:
        print(f"PROFILE_SOURCE_BLOB_SYNC=DRIFT expected={previous} actual={actual}")
        return 1
    profile["local_source"]["git_blob_sha"] = actual
    MANIFEST.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(f"PROFILE_SOURCE_BLOB_SYNC=UPDATED {actual}; review gate unchanged")
    return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true", help="update only the README source blob binding")
    args = parser.parse_args()
    raise SystemExit(sync(write=args.write))
