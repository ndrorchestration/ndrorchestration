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
