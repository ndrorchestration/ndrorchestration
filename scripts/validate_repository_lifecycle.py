#!/usr/bin/env python3
import json
import sys
from pathlib import Path

ALLOWED_LIFECYCLES = {
    "ACTIVE_CORE",
    "ACTIVE_SUPPORTING",
    "EXPERIMENTAL",
    "INCUBATING",
    "HISTORICAL",
    "EXTERNAL_REFERENCE",
    "ARCHIVE_CANDIDATE",
    "ARCHIVED",
}
ALLOWED_REVIEW_STATUSES = {"VERIFIED", "PENDING_REVIEW", "CONFLICTED"}
EXTERNAL_ORIGINS = {"external", "fork-derived", "upstream"}
REQUIRED_ENTRY_FIELDS = {
    "repository",
    "product_name",
    "visibility",
    "github_archived",
    "origin",
    "review_status",
    "lifecycle",
    "responsibility",
    "canonical_project_source",
    "relationships",
    "current_claim_boundary",
    "reviewed_at",
    "notes",
}


def _nonempty(value):
    return isinstance(value, str) and bool(value.strip())


def validate_registry(path: str) -> list[str]:
    violations: list[str] = []
    registry_path = Path(path)

    try:
        payload = json.loads(registry_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return [f"registry unreadable: {exc}"]

    if payload.get("schema_version") != "1.0.0":
        violations.append("schema_version must equal 1.0.0")
    if payload.get("authority_scope") != "ACCOUNT_LEVEL_LIFECYCLE_ONLY":
        violations.append("authority_scope must equal ACCOUNT_LEVEL_LIFECYCLE_ONLY")

    repositories = payload.get("repositories")
    if not isinstance(repositories, list):
        return violations + ["repositories must be a list"]

    seen: set[str] = set()
    for index, entry in enumerate(repositories):
        prefix = f"repositories[{index}]"
        if not isinstance(entry, dict):
            violations.append(f"{prefix}: entry must be an object")
            continue

        missing = sorted(REQUIRED_ENTRY_FIELDS - set(entry))
        if missing:
            violations.append(f"{prefix}: missing fields: {', '.join(missing)}")
            continue

        repository = entry.get("repository")
        if not _nonempty(repository):
            violations.append(f"{prefix}: repository must be a non-empty string")
        elif repository in seen:
            violations.append(f"{prefix}: duplicate repository: {repository}")
        else:
            seen.add(repository)

        review_status = entry.get("review_status")
        if review_status not in ALLOWED_REVIEW_STATUSES:
            violations.append(f"{prefix}: invalid review_status: {review_status}")

        lifecycle = entry.get("lifecycle")
        if lifecycle is not None and lifecycle not in ALLOWED_LIFECYCLES:
            violations.append(f"{prefix}: invalid lifecycle: {lifecycle}")

        if review_status == "VERIFIED":
            if lifecycle is None:
                violations.append(f"{prefix}: VERIFIED entry requires lifecycle")
            if not _nonempty(entry.get("responsibility")):
                violations.append(f"{prefix}: VERIFIED entry requires responsibility")
            if not _nonempty(entry.get("reviewed_at")):
                violations.append(f"{prefix}: VERIFIED entry requires reviewed_at")

        if lifecycle == "EXTERNAL_REFERENCE":
            if entry.get("origin") not in EXTERNAL_ORIGINS:
                violations.append(f"{prefix}: EXTERNAL_REFERENCE requires external origin")
            if not (_nonempty(entry.get("upstream_repository")) or _nonempty(entry.get("notes"))):
                violations.append(f"{prefix}: EXTERNAL_REFERENCE requires upstream context")

        if lifecycle == "ARCHIVED" and entry.get("github_archived") is not True:
            violations.append(f"{prefix}: ARCHIVED requires github_archived=true")

        if not isinstance(entry.get("relationships"), list):
            violations.append(f"{prefix}: relationships must be a list")

    return violations


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("usage: validate_repository_lifecycle.py <registry.json>")
        return 2

    violations = validate_registry(argv[1])
    for violation in violations:
        print(violation)
    return 1 if violations else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
