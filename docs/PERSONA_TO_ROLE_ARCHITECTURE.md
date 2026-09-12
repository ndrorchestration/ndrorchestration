# Persona-to-Role Architecture — Current Ecosystem Policy

**Status:** Current-facing architecture policy  
**Date:** 2026-09-12  
**Parent migration controller:** `ndrorchestration/DGAF-Framework#671`  
**Canonical design:** DGAF PR #672, `docs/superpowers/specs/2026-09-12-persona-to-role-architecture-migration-design.md`

## Current rule

Named agents/personas are not primitive architectural units.

Current systems bind executable behavior and authority to functional **roles, capabilities, policies, contracts, and stable IDs**. Named personas may remain as optional presentation or historical lineage, but presentation identity must not determine system semantics or authority.

```text
Capability
  -> Role Contract
    -> Role Instance / Executor
      -> Optional Persona / Presentation
```

## How to interpret this repository

Existing files such as:

- `docs/agent-amethyst-instantiation.md`
- `docs/agent-colleen-instantiation.md`
- `docs/agent-reciprocity-instantiation.md`
- `docs/agent-roster.md`
- `docs/agent-activation-order.md`
- historical logs and classification records

are valuable **historical/design-lineage source material**. They are not automatically current executable architecture merely because they describe named agents as active or authoritative at the time they were written.

Do not destructively rewrite historical records. Current role interpretation must be supplied through explicit lineage mappings and role/capability registries.

## Migration classification

Before changing any named-agent reference, classify it as one of:

1. **Functional dependency (FD)** — replace with canonical role/capability ID.
2. **Persona/presentation (PP)** — retain only behind an optional presentation mapping.
3. **Fixture/demo identity (FX)** — use a neutral fixture unless identity itself is under test.
4. **Historical/provenance identity (HP)** — preserve exactly and link forward through lineage metadata.
5. **Undefined/conflicting (UN)** — do not migrate until its functional contract is specified/adjudicated.

## Current-facing documentation rule

New documentation should prefer functional terminology such as:

- governance orchestration
- continuity & provenance coordination
- evidence integrity & verification
- security & policy boundary enforcement
- uncertainty/risk escalation
- research & synthesis
- coordination & fairness
- knowledge retrieval & archival
- independent audit/challenge
- artifact execution/materialization
- communication/notification

These are role families, not automatic replacements for individual historical personas. Actual mappings must come from code/spec evidence.

## Authority rule

No authority transfers solely because a persona is renamed or mapped.

Every legacy named-actor permission must have an equivalent role-based permission with the same action, resource, conditions, timing, and independence constraints unless an intentional change is separately reviewed.

## Persona behavior rule

If a persona contains behavior-changing prompts, heuristics, routing, memory behavior, or decision logic, that logic is not presentation. Extract it into an explicit architectural object such as an execution profile, behavior policy, prompt strategy, or interaction policy.

## Historical evidence rule

Historical records keep their original actor identity. Do not rewrite event-time evidence to use later role names. A versioned lineage map may state how a historical identity relates to a current role.

## Compatibility and retirement

Compatibility aliases remain until every active consumer has migrated and cross-repository equivalence verification passes. Alias retirement is evidence-based, not calendar-based.

## Scope boundary

This policy changes architecture interpretation and future implementation direction only. It does not establish scientific evidence, independent verification, authorization, efficacy, production readiness, compliance, safety, or empirical N for any project.
