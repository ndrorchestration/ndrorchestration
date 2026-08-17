# ASIS-AR — Galaxy S24 Sensor Inventory Service

## Purpose

Define the first implementation artifact for S24-1: a runtime sensor-inventory service that enumerates Android-exposed sensors on the target Galaxy S24, records hardware/API metadata, measures observed event rates during a bounded capture window, and emits a provenance-bearing manifest.

## S24-1 acceptance gate

S24-1 is **PASS** only when a physical Galaxy S24 execution produces:

1. a non-empty sensor inventory;
2. stable identifiers/type/vendor metadata for each observed sensor;
3. observed event timestamps and counts for selected continuous sensors;
4. computed event-rate statistics over the capture window;
5. a device/build/API provenance record;
6. a deterministic JSON manifest that can be hashed and archived.

A static specification or emulator result does not close S24-1.

## Initial sensor targets

Primary targets are the Android sensor framework families needed by ASIS:

- accelerometer
- gyroscope
- geomagnetic / magnetic-field sensor
- rotation vector
- gravity
- linear acceleration
- pressure
- light
- proximity
- Hall / vendor-specific magnetic sensor where exposed

Secondary platform channels are tracked separately:

- GNSS/location
- microphone/audio capture
- camera metadata and capture timing
- Wi-Fi metadata
- Bluetooth metadata

## Required manifest fields

For each enumerated sensor capture:

- sensor type
- sensor name
- vendor
- version
- maximum range
- resolution
- minimum delay
- reporting mode
- wake-up capability
- power information when exposed
- Android API level
- device/build identifier
- capture start/end timestamps
- event count
- observed event rate
- dropped/error count

## Capture design

The service should request the fastest practical rate supported by the device while respecting Android foreground/background restrictions and power/thermal constraints. It must record the requested rate separately from the observed rate.

Event timestamps should be retained exactly as provided by the Android sensor event API. Wall-clock timestamps may be added for provenance but must not replace the sensor event clock.

## Evidence boundary

This service validates **sensor availability and acquisition behavior**. It does not establish spatial reconstruction accuracy, acoustic measurement accuracy, sensor fusion quality, or ASIS capability.

Raw Wi-Fi CSI is explicitly outside this gate. Android Wi-Fi metadata availability is not evidence of raw CSI access.

## Planned implementation shape

```text
SensorManager
  -> enumerateSensors()
  -> select target sensors
  -> register listeners
  -> bounded capture window
  -> event counters + timestamp statistics
  -> manifest serialization
  -> SHA-256 evidence hash
```

## Next implementation step

Implement the Android/Kotlin service against the canonical ASIS-AR source repository once the source location is recovered. Do not create a new repository solely to satisfy this specification if the existing ASIS-AR source can be identified.