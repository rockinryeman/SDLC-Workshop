# Prompt 3 · Architecture / Design

## INPUT (prompt)
> Using the approved requirements, create a concise architecture description: system context (text) ·
> major components (sensors, perception/AI, decision logic, HMI, vehicle interface) · interfaces & data
> flows · failure modes · safety · privacy/cyber.

## OUTPUT (AI result)
- **Context:** In-cabin sensors → **DMS ECU** → vehicle systems (HMI, braking/lane-keep, eCall);
  cloud touched only for signed model updates (satisfies REQ-NF-04).
- **Components:** Sensors (camera, IR) · Perception/AI (on-device ML + confidence score) · Decision
  Logic (state classifier + escalation timer) · HMI (haptic/audio/visual) · Vehicle Interface
  (safe-stop assist, eCall) · Event Logger.
- **Data flows:** frames → Perception → `(state, confidence)` → Decision Logic → response command →
  HMI/Vehicle; all events → Logger (REQ-F-06).
- **Failure modes:** sensor occlusion → degrade to UNKNOWN (REQ-F-04); low confidence → hold; comms
  loss → local-only operation; false positive → confidence gating.
- **Safety:** confidence-threshold gating (REQ-F-04); fail-operational; driver override; emergency path
  independent of cloud (REQ-F-05).
- **Privacy/cyber:** on-device inference (REQ-NF-04); signed/rollback-able OTA (REQ-NF-06); encrypted
  local logs.

## 🔗 Chain check
"Using the approved requirements" — each component maps to REQ-F/NF IDs. **Requirements → Architecture:
connected.**

**Ask the room:** *Where could this go wrong, and how does it stay safe?*
