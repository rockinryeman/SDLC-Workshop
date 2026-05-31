# Prompt 5 · Implementation

## INPUT (prompt)
> Using the architecture and the SysML model, generate: high-level implementation approach · pseudocode
> for the detect-assess-respond loop · logic flow & data processing steps · assumptions. Explain how it
> satisfies the requirements.

## OUTPUT (AI result)
- **Approach:** per-frame state machine in the Decision Logic component; perception returns
  `(state, confidence)`; confidence gate before any action; escalation driven by how long impairment
  persists.
- **Pseudocode:**
```
loop every frame:
    state, confidence = perception(cabin_frame)        # AssessConfidence (REQ-F-04)
    if confidence < THRESHOLD:
        state = UNKNOWN                                # no action on low confidence
    if state in (DROWSY, DISTRACTED):
        severity = escalate(state, duration_impaired)  # advisory->active->emergency (REQ-F-03)
        trigger_response(severity)
        if severity == NO_RESPONSE:
            initiate_emergency_protocol()              # REQ-F-05
    log_event(state, confidence, response)             # REQ-F-06
```
- **Logic flow:** detect → assess confidence → (gate) → escalate → respond → log.
- **Assumptions:** perception runs ≥ 15 fps; thresholds tunable; clock available for durations.
- **Satisfies:** REQ-F-01/02 (detection), F-03 (escalation), F-04 (gating), F-05 (emergency),
  F-06 (logging); NF-01 latency via per-frame loop.

> **Optional "show it run":** ask for **runnable Python** instead of pseudocode and execute it — see
> [`../simulation/`](../simulation/) for a working reference.

## 🔗 Chain check
Explicitly "Using the architecture and the SysML model"; pseudocode mirrors the
`DetectDriverState → AssessConfidence → TriggerResponse` actions. **Model → Implementation: connected.**

**Ask the room:** *Idea to logic — with no separate dev-team handoff.*
