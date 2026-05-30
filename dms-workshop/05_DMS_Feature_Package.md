# DMS Feature Package — Worked Example ("Answer Key")

**Use this to prep.** This is roughly what the live AI exercise should produce. Read it before
you facilitate so you know what "good" looks like and can steer the room if the live output drifts.
*Not a spec to ship — a teaching reference.*

**Feature:** Driver Monitoring System — Drowsiness & Distraction Detection

---

## 1. Business Problem
Detect when a driver becomes drowsy, distracted, or medically impaired, and respond in time to
prevent an incident — improving safety and customer trust while minimizing annoying false alarms.

## 2. Stakeholder Needs
- **Drivers** want to feel protected without being constantly nagged.
- **Safety engineers** require compliance with functional-safety and active-safety standards.
- **Regulators** increasingly require driver-attention monitoring (e.g., EU GSR).
- **Product managers** want measurable safety improvement and high customer trust.
- **Privacy/legal** require that in-cabin sensing protects driver data.
- **Test teams** require objective, repeatable acceptance criteria.

## 3. Functional Requirements
- **DMS-001:** Detect driver drowsiness within 2 seconds of onset of sustained eye-closure/head-nod.
- **DMS-002:** Detect driver distraction (eyes off road) within 1.5 seconds.
- **DMS-003:** Escalate response based on severity: alert → strong warning → safe-stop assist.
- **DMS-004:** Suppress alerts when a confident "attentive" state is detected (limit false alarms).
- **DMS-005:** Detect potential medical emergency (no response to escalating alerts) and initiate
  emergency protocol.
- **DMS-006:** Log all detection and response events for diagnostics and audit.

## 4. Non-Functional Requirements
- Detection-to-alert latency < 2 s.
- ≥ 95% true-positive detection of drowsiness in validation conditions.
- False-alarm rate < 1 per 8 hours of driving.
- Operates across lighting conditions, sunglasses, varied face types (no demographic bias).
- In-cabin image data processed on-device; no raw video leaves the vehicle by default.
- Support OTA update of detection models.

## 5. High-Level Architecture
```
In-cabin Camera + IR Sensors
        ↓
Perception / AI Model  (eye state, head pose, gaze)
        ↓
State Assessment + Confidence  (drowsy / distracted / attentive / unknown)
        ↓
Decision & Escalation Logic
        ↓
┌───────────────┬────────────────────┐
HMI (alerts)    Vehicle Interface     Event Logger
(visual/audio/  (safe-stop assist,    (diagnostics,
 haptic)         emergency call)       audit trail)
```

## 6. Textual SysML v2 Example
```
package DriverMonitoringSystem {
    requirement DMS_001;          // detect drowsiness in time
    requirement DMS_004;          // suppress false alarms

    action DetectDriverState;     // from sensor data → state
    action AssessConfidence;      // how sure are we?
    action SelectResponse;        // alert / warn / assist
    action TriggerResponse;       // act via HMI / vehicle

    flow CabinSensorData;
    flow DriverStateEstimate;
    flow ResponseCommand;
}
```

## 7. Test Cases
- **TC-001:** Simulate sustained eye closure → expect drowsiness alert within 2 s.
- **TC-002:** Driver looks at phone 2 s → expect distraction alert within 1.5 s.
- **TC-003:** Driver wearing sunglasses in bright light → detection still functions (edge case).
- **TC-004:** Attentive driver glancing at mirrors → **no** false alarm (negative case).
- **TC-005:** No response to escalating alerts → emergency protocol triggers.
- **TC-006:** Verify every detection/response event is logged.

## 8. Traceability Matrix
| Requirement | Verified by |
|---|---|
| DMS-001 | TC-001 |
| DMS-002 | TC-002 |
| DMS-003 | TC-001, TC-002, TC-005 |
| DMS-004 | TC-003, TC-004 |
| DMS-005 | TC-005 |
| DMS-006 | TC-006 |

## 9. Implementation Pseudocode
```
loop every frame:
    state, confidence = perception_model(cabin_sensor_data)
    if confidence < threshold:
        state = "unknown"          # don't act on low confidence
    if state in ("drowsy", "distracted"):
        severity = escalate(state, duration)
        trigger_response(severity)  # alert → warn → assist
        if severity == "no_response":
            initiate_emergency_protocol()
    log_event(state, confidence, response)
```

## 10. Deployment Strategy
- Deploy detection model via **OTA** update.
- **Pilot** with internal/employee fleet first; shadow-mode (detect-but-don't-act) before going live.
- **Monitor:** detection accuracy, false-alarm rate, driver override/annoyance signals.
- **Rollback** if false-alarm rate or missed-detection rate exceeds thresholds.
- **Success criteria:** measurable drowsiness-event reduction with false alarms under target.

---

## Where humans stay in the loop (say this to the room)
- Setting the **confidence threshold** — too low nags people, too high misses danger. A judgment call.
- Deciding **how aggressive** the safe-stop assist should be.
- Owning **accountability** when the system is wrong — AI assists; people remain responsible.
- Validating there's **no demographic bias** in detection before release.
