# Burnout Rubric — Industry Translation

**NDR Internal Name:** Burnout Rubric (Friction Scale)
**Industry-Standard Name:** Human-in-Loop Escalation Gate
**Version:** 1.0 | **Date:** 2026-07-02
**Source:** NDR Orchestration Rubrics — Architectural Systems Governance V1.0

---

## Overview

The Burnout Rubric governs when an AI system operates autonomously versus when human review or intervention is required. It functions as a 5-level escalation threshold system — the primary governance mechanism for human-in-loop (HITL) decisions in NDR-based orchestration workflows.

In industry-standard terms, this maps to **human-in-loop escalation gates** used in AI evaluation platforms, annotation QA pipelines, and agentic system oversight protocols.

---

## Level Mapping

| NDR Level | NDR Class | NDR Protocol Description | NDR Action | Industry Translation | Use Case |
|---|---|---|---|---|---|
| L1–L2 | Maintenance | Low-complexity pattern matching or formatting | Silent Execution | Autonomous execution — no review needed | Routine annotation, formatting tasks, template fill |
| L3 | Refinement | Logic branching or minor workflow adjustments | Verify & Run | Soft flag — human spot-check recommended | Edge case annotation, ambiguous rubric application |
| L4 | Structural | Foundational shifts in goal or data architecture | Architect Sync | Hard flag — human review required before proceeding | Policy-breaking outputs, scope change, novel failure mode |
| L5 | Systemic | Volatility detected; system redesign required | Abort / Redesign | Escalation / halt — system-level intervention needed | Systematic hallucination, safety violation, alignment failure |

---

## Application to Eval Roles

When applying rubrics during AI annotation or evaluation tasks:
- **L1–L2 outputs:** Score and submit without escalation
- **L3 outputs:** Score, flag with reasoning note, submit for QA review
- **L4 outputs:** Do not score independently — escalate to senior reviewer or team lead
- **L5 outputs:** Halt task, document failure pattern, report to project manager

---

## Governance Alignment
- NIST AI RMF 600-1: Maps to GOVERN 1.1 (roles/responsibilities for human oversight)
- ISO 42001: Maps to Clause 8.4 (AI system operation with human oversight)
- Anthropic AUP / OpenAI Usage Policies: L5 = policy violation escalation path

---

## Formula Reference

Structural Integrity threshold formula (Platinum Mean):

```
S_i = T_c / 1.7747
```

Where S_i = Structural Integrity, T_c = total Contextual Tokens.
If density exceeds this ratio, apply Telescopic Lens Gate for semantic compression.

---

## Status
- NDR Burnout Score for this artifact: L2 (Maintenance — low complexity, direct translation)
- Portfolio Status: Polish → ready for public-facing use
