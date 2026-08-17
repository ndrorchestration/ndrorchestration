# ASIS-AR Source Recovery Record

**Date:** 2026-08-17
**Status:** OPEN — canonical Android source not exposed

## Search performed

The connected GitHub account was enumerated for the owner `ndrorchestration`. Repository names currently exposed include `Acoustic-mesh`, `ndrorchestration`, `3d-visualization-hub`, `Meshsense`, and other portfolio/system repositories. No separately named repository matching `ASIS-AR`, `ASIS_AR`, `ASIS-Android`, or an equivalent Galaxy S24 Android application was exposed.

Repository/file searches were also performed for `ASIS-AR`, `Android`, and `S24`. No canonical Android implementation was returned through the connected GitHub search surface. `Acoustic-mesh` was specifically checked for `ASIS-AR` and Android markers without finding a matching Android source implementation.

## Interpretation

This is a **source-recovery / connector-visibility finding**, not evidence that the source never existed or has been deleted.

Historical Notion architecture records identify ASIS-AR as the Galaxy S24 implementation of the ASIS architecture. The implementation boundary therefore remains provisional until the actual source artifact is recovered.

## Do not do

- Do not create a competing ASIS-AR repository solely to close the recovery gap.
- Do not claim S24-1 implementation exists based on specification documents.
- Do not mark S24-1 PASS from emulator/static analysis.

## Required next evidence

Recover the canonical Android project from one of:

1. an existing GitHub repository/branch not currently exposed by the connector;
2. a historical repository/archive/ZIP;
3. the user's local Android Studio project;
4. another authoritative source artifact.

Once recovered, identify package/application IDs, Gradle structure, min/target SDK, current sensor APIs, and existing ASIS spatial components before integrating `S24_SENSOR_INVENTORY_SERVICE.md`.
