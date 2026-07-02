# Workspace Maintenance Protocol
**Version:** 1.0-stub | **Date:** 2026-07-02 | **Maintainer:** ndrorchestration  
**Status:** STUB — consolidates maintenance rules currently distributed across MASTER PORTFOLIO INVENTORY (Drive) and README  
**Canonical SOP for:** monthly review cycle, update triggers, cross-platform sync

> ⚠️ This file is a stub. Populate by pulling from MASTER PORTFOLIO INVENTORY v1.8 (Drive) Section IV — Perpetual Verification Protocol.

---

## Review Cadence

| Cadence | Action | Owner |
|---|---|---|
| **Monthly** (1st of month) | Full artifact audit — check all 5 domains, update classification index | ndrorchestration |
| **Weekly** | Check GitHub repos exist, no orphaned branches | ndrorchestration |
| **Per-session** | Update logs/, bump version on any modified doc | Session agent |
| **Quarterly** | Deep verification of Drive folder ↔ GitHub path mirror alignment | ndrorchestration |

---

## Update Triggers

This repository and `docs/master-classification-index.md` MUST be updated when:

- [ ] New repository created (either account)
- [ ] New framework or persona document created
- [ ] Major revision to any existing document
- [ ] New Perplexity Space created or archived
- [ ] Drive folder structure changes
- [ ] Agent roster changes (agent added, promoted, deprecated)
- [ ] Cross-account routing changes (`Flickerflash` ↔ `ndrorchestration`)

---

## Cross-Platform Sync Checklist

When making any substantive update:

```
□ GitHub: commit to correct repo + correct path (not root dump)
□ Drive: mirror folder name matches GitHub path schema
□ Classification Index: artifact entry updated (domain / visibility / status)
□ Master Portfolio Inventory (Drive): Section V pointer still valid
□ README: nav table still accurate
□ Logs: session log entry created in logs/
```

---

## Drive ↔ GitHub Path Mirror Standard

| Drive Folder | GitHub Equivalent Path |
|---|---|
| `Agent-Frameworks/Orchestration/` | `portfolio/frameworks/` |
| `Evaluation-Tools/` | `portfolio/rubrics/` |
| `Visualizations/Architecture/` | `portfolio/visualizations/` |
| `Mathematical-Models/` | `portfolio/math-models/` |
| `Resume/Career/` | `portfolio/resume/` |
| `[03] SYSTEM_GOVERNANCE/` | `docs/` |

> Mirror standard is **canonical**. Drive folders must be renamed to match GitHub paths, not the inverse.

---

## TODO — Populate

- [ ] Pull full verification protocol from Drive: MASTER PORTFOLIO INVENTORY v1.8, Section IV
- [ ] Add automated reminder setup instructions (Perplexity Tasks / calendar)
- [ ] Document backup protocol (Drive → GitHub export schedule)
- [ ] Add escalation path for unresolvable drift

---

*Stub created: 2026-07-02 by Amethyst | ndrorchestration*
