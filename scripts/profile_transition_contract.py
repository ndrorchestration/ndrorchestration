"""Revision-aware profile transition checks. No release or authority promotion."""
import hashlib
import re
import urllib.error
import urllib.request

LEGACY_BLOB = "b094c7554084a572d0efb5dc6d52187e12fb7c66"
PROFILE_URL = "https://github.com/ndrorchestration/ndrorchestration/blob/main/README.md"
RAW_URL = "https://raw.githubusercontent.com/ndrorchestration/ndrorchestration/main/README.md"
LEGACY_MARKERS = ("Agentic Assurance", "Tektite", "What did the system actually do")
PROJECTS = (
    ("Dynamic Governance Agentic Formation (DGAF)", "DGAF-Framework"),
    ("Agent Control Plane (ACP)", "agent-control-plane"),
    ("To Sail the Starry Sky", "ToSailtheStarrySky-jrpg"),
    ("ResumeApex Career Assistance Evaluation Suite", "resumeapex-eval"),
    ("Collabration", "Collabration"),
    ("AI Evaluation Workbench", "junior-apogee-app"),
    ("Orbit-Driftwatch", "Orbit-Driftwatch"),
    ("MORSE", "Morse-Orchestration"),
    ("AI Prompt Systems Portfolio", "ai-prompt-systems-portfolio"),
    ("Sentinel Governance", "sentinel-governance"),
)
CANDIDATE_MARKERS = ("Five flagship projects", "Five additional selected projects") + tuple(p[0] for p in PROJECTS)


def blob_sha(body):
    return hashlib.sha1(f"blob {len(body)}\0".encode("ascii") + body).hexdigest()


def fetch_raw():
    request = urllib.request.Request(RAW_URL, headers={"Accept": "text/plain", "User-Agent": "ndrorchestration-profile-verifier/1.0", "Cache-Control": "no-cache"})
    try:
        with urllib.request.urlopen(request, timeout=20) as response:
            return response.status, response.geturl(), response.read(2_000_001)
    except urllib.error.HTTPError as exc:
        return exc.code, exc.geturl(), b""
    except OSError:
        return 0, RAW_URL, b""


def check_profile(surface, local_bytes, event, ref, rendered, raw, base_blob=None):
    """Return separate candidate and public-copy observations; never authorize publication."""
    errors = []
    local_blob = blob_sha(local_bytes)
    binding = surface.get("local_source", {})
    if binding.get("path") != "README.md" or binding.get("git_blob_sha") != local_blob:
        errors.append("candidate blob/path mismatch")
    expected_lines = [
        (f"### {i:02d} — " if i <= 5 else f"| **{i:02d} — ")
        + f"[{name}](https://github.com/ndrorchestration/{slug})"
        for i, (name, slug) in enumerate(PROJECTS, 1)
    ]
    try:
        lines = local_bytes.decode("utf-8").splitlines()
    except UnicodeDecodeError:
        lines = []
        errors.append("candidate is not UTF-8")
    actual_lines = [line for line in lines if re.match(r"^(?:### |\| \*\*)\d{2} — ", line)]
    if len(actual_lines) != 10 or any(
        line != expected if i < 5 else not line.startswith(expected + "** |")
        for i, (line, expected) in enumerate(zip(actual_lines, expected_lines))
    ):
        errors.append("candidate project heading/order mismatch")
    if not all(marker in "\n".join(lines) for marker in CANDIDATE_MARKERS):
        errors.append("candidate markers missing")
    candidate_ok = not errors

    if event == "pull_request":
        if base_blob == LEGACY_BLOB:
            mode, expected_blob, markers = "PR_EXISTING_PUBLIC", LEGACY_BLOB, LEGACY_MARKERS
            if surface.get("release_gate") != "REVIEW":
                errors.append("PR transition requires REVIEW gate")
        elif base_blob == local_blob:
            mode, expected_blob, markers = "PR_UNCHANGED_CURRENT_PROFILE", local_blob, CANDIDATE_MARKERS
        else:
            mode, expected_blob, markers = "PR_UNRECONCILED_BASE", "", ()
            errors.append("unexpected or missing PR base profile identity")
    elif event in ("schedule", "workflow_dispatch", "push") and ref == "refs/heads/main":
        mode, expected_blob, markers = "MAIN_CURRENT_PUBLIC", local_blob, CANDIDATE_MARKERS
    else:
        mode, expected_blob, markers = "INVALID_CONTEXT", "", ()
        errors.append("unsupported verification context")

    status, final_url, body = rendered
    raw_status, raw_final_url, raw_bytes = raw
    actual_raw_blob = blob_sha(raw_bytes)
    missing = [marker for marker in markers if marker.lower() not in body.lower()]
    if surface.get("url") != PROFILE_URL or final_url != PROFILE_URL or not 200 <= status < 300 or missing:
        errors.append("rendered public profile check failed")
    if raw_status != 200 or raw_final_url != RAW_URL or len(raw_bytes) > 2_000_000 or actual_raw_blob != expected_blob:
        errors.append("public raw README identity check failed")
    return {
        "id": "github.profile", "declared_url": surface.get("url"),
        "final_url": final_url, "http_status": status,
        "required_markers": list(markers), "missing_markers": missing,
        "candidate_blob": local_blob, "candidate_contract": "PASS" if candidate_ok else "FAIL",
        "mode": mode, "pr_base_blob": base_blob, "expected_public_blob": expected_blob, "observed_public_blob": actual_raw_blob,
        "raw_http_status": raw_status, "raw_final_url": raw_final_url,
        "errors": errors, "result": "FAIL" if errors else "PASS",
        "publication_authorized": False,
    }
