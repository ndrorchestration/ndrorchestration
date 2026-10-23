# GitHub profile pin candidates — evidence review (2026-10-23)

This is a **portfolio selection review**, not a security audit, CI attestation, production acceptance, or independent validation.

## Selection criteria

Each pin should give a new visitor (1) an accessible entry point, (2) concrete public implementation or inspectable artifact, (3) a distinct relevant skill signal, and (4) honest limitations. Repository visibility alone is not an endorsement of operational safety.

| Priority | Public repository | Inspected entry point | Portfolio role | Important boundary |
| --- | --- | --- | --- | --- |
| 1 | [DGAF-Framework](https://github.com/ndrorchestration/DGAF-Framework) | README and `docs/CURRENT_STATE.md` | Research architecture and evidence-bound authorization | Experimental; scientific efficacy and independent validation not established; release/admission gates remain separate |
| 2 | [resumeapex-eval](https://github.com/ndrorchestration/resumeapex-eval) | README and `eval/cli.py` | Runnable evaluation harness | Known-answer fixture verification is not model-performance evidence |
| 3 | [Orbit-Driftwatch](https://github.com/ndrorchestration/Orbit-Driftwatch) | README and `package.json` | Multi-agent observability | Deterministic control is not validated live hosted provider execution |
| 4 | [agent-control-plane](https://github.com/ndrorchestration/agent-control-plane) | README and `pyproject.toml` | Scoped execution and provenance | Local experimental control-plane primitives, not production security or orchestration |
| 5 | [ai-prompt-systems-portfolio](https://github.com/ndrorchestration/ai-prompt-systems-portfolio) | README and `specs/01_state_anchor_eval.yaml` | Prompt specification and evaluation design | Rubric/specification does not constitute an executed benchmark |
| 6 | [Collabration](https://github.com/ndrorchestration/Collabration) | README and `package.json` | Full-stack governed human/AI product | Alpha-stage implementation; runtime/security and persistence claims need separate verification |

## Observed commit candidates

The GitHub commit-search connector returned these first results when queried on 2026-10-23. They are *search results*, not established synchronized branch-head attestations:

- DGAF: `1a95b94332dffb404c5a3ce026d70781a8c10b90`
- ResumeApex: `4c9d4cfe8eae52bcac99c6d5f6a38d346a61a89f`
- Orbit-Driftwatch: `333271158f0e11a58dc83b5d1d8433c8999e89d7`
- ACP: `bd56a747686d775236bb78603bdaf2afc90733cb`
- Prompt portfolio: `0f56fb683f8be2f4599d66fc406f4c8123b5d17c`
- Collabration: `2cc00245e09ad39953253ce2b5df060ab34276aa`

The available connected workflow query only retrieves **pull-request-triggered workflow runs** for an individual commit and returned an empty list for each candidate. **This does not show that main-branch CI passed, failed, or never ran.** Do not promote these results into verification.

The DGAF current-state document displayed `last_verified: 2026-10-15` when inspected; that document's verification timestamp does not attest subsequent release or security activity.

## Recommendation

Keep the six suggested pins as a **portfolio composition**, contingent on future exact-head CI/security and usability checks. Keep Collabration as the replaceable sixth candidate depending on whether a given application is for product engineering or solely AI evaluation.

## Follow-up gates

1. Resolve each repository's actual protected/default branch head and retrieve complete current push/PR workflow conclusions.
2. Verify advertised clean-install tests on a pinned environment, without equating test execution with independent validation.
3. Review dependency advisories, license links, README entry points, and any publicly advertised demo.
4. Set GitHub pinned repositories manually through the account profile UI; this document is **not** evidence that pins were changed.

## Verification pass 1 addendum — 2026-10-23

Read-only GitHub commit-status inspection on the six commit-search candidates above returned **no legacy commit-status entries for five projects**. This must **not** be interpreted as a green GitHub Actions check suite. The workflow lookup available through the connected GitHub action is limited to pull-request-triggered runs and does not establish push/main results. Complete exact-head check-suite conclusions and current main-head identity remain **UNVERIFIED**.

For Collabration's candidate commit `2cc00245e09ad39953253ce2b5df060ab34276aa`, one legacy commit status was returned: **Vercel = failure**, target `https://vercel.com/ndrorchestration?upgradeToPro=build-rate-limit`. The target suggests a build-rate/capacity limitation; no job log or runtime evidence was obtained to prove the root cause. This is a deployment-status exception, **not** evidence that the app source is defective.

**Disposition:** Maintain six *provisional* pins, flag Collabration's deployment for separate investigation, and do not assert full CI verification or make release/governance changes. No workflows were rerun.

## Verification pass 2 — 2026-10-23: dependency and deployment inventory

Read-only manifest inspection produced the following **inventory**, not an audited dependency graph or security clearance:

- **DGAF-Framework:** root `pyproject.toml` declares a Python 3.12-compatible Vercel runtime with no root Python dependencies. Root `requirements.txt` explicitly notes deprecated Python API stubs and TypeScript Next.js handlers. These root files do **not** describe all CI/bootstrap lock dependencies; the Black advisory and signed bootstrap work remain separate release/security concerns.
- **resumeapex-eval:** `requirements.txt` uses minimum-only bounds `numpy>=1.24`, `pandas>=2.0`, `scipy>=1.10`, `pytest>=7.0`. Clean-environment reproducibility should use an accepted lock or constraints set rather than assuming future installs resolve identically.
- **Orbit-Driftwatch:** root Node package declares Node >=20 and scripts `npm test`, `npm run verify:deployment`, `npm run verify:live`; it advertises no root runtime dependencies. No such command was run in this pass.
- **agent-control-plane:** Python >=3.10 with setuptools >=68; optional cryptography range >=46,<52 and pinned tiktoken 0.14.0. No CVE conclusion can be inferred from a manifest alone.
- **ai-prompt-systems-portfolio:** root package.json is absent (404), consistent with a specification/artifact-oriented repository. This is not by itself a defect and should not be represented as an executable JavaScript package.
- **Collabration:** `apps/web/package.json` declares Next 16.3.4, React/React-DOM 19.2.8, Supabase SSR 0.12.7 and Supabase JS 2.116.0. This is a version inventory, **not** a vulnerability assertion.

The connected Vercel project search for `collabration` returned no project in the authenticated scope. The deployment display action was unavailable. Accordingly, the earlier GitHub legacy Vercel failure with a build-rate-limit URL remains an **unresolved deployment signal**, with root cause and current production status not independently established.

GitHub Actions push-branch/check-suite visibility was unavailable through the connected GitHub operations used. Public web access to GitHub Actions pages also failed. Do not infer CI conclusions from this absence. All six candidates remain **provisional**; no workflows were rerun or project files altered.
