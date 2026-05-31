# Dry-Run Transcript — DMS Live Exercise

A captured test run of the full 6-phase / 7-prompt chain. Each phase shows the **INPUT** (the prompt
pasted) and the **OUTPUT** (what the AI produced), plus a **🔗 Chain check** confirming it consumed
the prior step's artifacts. Artifact IDs (REQ-F-01, TC-01, …) make the digital thread visible.

> Priming line used first: *"We're running a live workshop. Keep each answer concise and skimmable —
> bullets over prose."*

---

## Phase 1 · Planning — Prompt 1

**INPUT:**
> You are a cross-functional automotive product team. Analyze the Driver Monitoring System concept and
> generate: Stakeholders · Business Objectives · Customer Needs · Risks · Assumptions · Success Metrics ·
> Prioritized Outcomes.

**OUTPUT:**
- **Stakeholders:** drivers; OEM product management; safety engineers; regulators (Euro NCAP, EU GSR);
  legal/liability; privacy office; fleet customers.
- **Business Objectives:** (BO-1) meet EU GSR driver-attention mandate; (BO-2) improve NCAP safety
  rating; (BO-3) reduce fatigue/distraction incidents; (BO-4) limit brand & liability exposure.
- **Customer Needs:** (CN-1) be protected when drowsy/distracted; (CN-2) not be nagged by false
  alarms; (CN-3) keep in-cabin data private; (CN-4) work in varied lighting / with sunglasses.
- **Risks:** false alarms erode trust; missed detection → safety/liability; demographic/lighting bias;
  privacy backlash; missing the regulatory deadline.
- **Assumptions:** in-cabin camera + IR present; on-device compute available; OTA update capability;
  fixed regulatory timeline.
- **Success Metrics:** (SM-1) ≥95% drowsiness-detection accuracy; (SM-2) <1 false alarm / 8 h driving;
  (SM-3) detection latency <2 s; (SM-4) zero critical missed-detection events in pilot.
- **Prioritized Outcomes:** 1) regulatory-compliant drowsy/distracted detection · 2) low false-alarm
  rate · 3) medical-emergency escalation · 4) privacy-by-design.

🔗 *Starts the thread — defines the objectives & metrics every later step traces back to.*

---

## Phase 2 · Requirements — Prompt 2

**INPUT:**
> You are a senior automotive systems engineer. Using the Planning outputs (stakeholders, customer
> needs, business objectives, success metrics, prioritized outcomes), produce a requirements
> specification for the DMS: functional · non-functional (latency, accuracy, privacy) · constraints &
> assumptions · acceptance criteria. Trace each requirement back to a stakeholder need or business
> objective from Planning.

**OUTPUT:**
- **Functional**
  - REQ-F-01 Detect drowsiness within 2 s of sustained eye-closure/head-nod. *(→ CN-1, BO-1)*
  - REQ-F-02 Detect distraction (eyes off road > 1.5 s). *(→ CN-1, BO-1)*
  - REQ-F-03 Escalate response: advisory → active → emergency. *(→ Outcome 3)*
  - REQ-F-04 Suppress alerts when attentive or low-confidence. *(→ CN-2, SM-2)*
  - REQ-F-05 Trigger emergency protocol if unresponsive to escalation. *(→ Outcome 3)*
  - REQ-F-06 Log every detection/response event. *(→ liability, traceability)*
- **Non-functional**
  - REQ-NF-01 Detection latency < 2 s. *(→ SM-3)*
  - REQ-NF-02 Drowsiness accuracy ≥ 95%. *(→ SM-1)*
  - REQ-NF-03 False-alarm rate < 1 / 8 h. *(→ SM-2, CN-2)*
  - REQ-NF-04 On-device processing; no raw video leaves the vehicle. *(→ CN-3, Outcome 4)*
  - REQ-NF-05 Equal performance across demographics & lighting. *(→ Risk: bias)*
  - REQ-NF-06 Model is OTA-updatable. *(→ Assumption: OTA)*
- **Constraints/assumptions:** existing camera+IR; automotive-grade ECU compute budget; UNECE R79
  interaction for any steering/braking assist.
- **Acceptance criteria (samples):** drowsy event flagged ≤ 2 s in HIL test (REQ-F-01/NF-01);
  false-alarm rate measured < 1/8 h over a 40-h drive set (REQ-NF-03); 0 raw frames egress in network
  capture (REQ-NF-04).

🔗 **Chain check:** every requirement carries a *(→ …)* link to a Planning need/objective/metric; no
stakeholder-need re-derivation. **Planning → Requirements: connected.**

---

## Phase 3 · Architecture / Design — Prompt 3

**INPUT:**
> Using the approved requirements, create a concise architecture description: system context (text) ·
> major components (sensors, perception/AI, decision logic, HMI, vehicle interface) · interfaces & data
> flows · failure modes · safety · privacy/cyber.

**OUTPUT:**
- **Context:** In-cabin sensors → **DMS ECU** → vehicle systems (HMI, braking/lane-keep, eCall);
  cloud touched only for signed model updates (satisfies REQ-NF-04).
- **Components:** Sensors (camera, IR) · Perception/AI (on-device ML + confidence score) · Decision
  Logic (state classifier + escalation timer) · HMI (haptic/audio/visual) · Vehicle Interface
  (safe-stop assist, eCall) · Event Logger.
- **Data flows:** frames → Perception → `(state, confidence)` → Decision Logic → response command →
  HMI/Vehicle; all events → Logger (REQ-F-06).
- **Failure modes:** sensor occlusion → degrade to UNKNOWN (REQ-F-04); low confidence → hold; comms
  loss → local-only operation; false positive → confidence gating.
- **Safety:** confidence threshold gating (REQ-F-04); fail-operational; driver override; emergency
  path independent of cloud (REQ-F-05).
- **Privacy/cyber:** on-device inference (REQ-NF-04); signed/rollback-able OTA (REQ-NF-06); encrypted
  local logs.

🔗 **Chain check:** "Using the approved requirements" — components map to REQ-F/NF IDs. **Requirements
→ Architecture: connected.**

---

## Phase 3 · Model the System — Prompt 4

**INPUT:**
> Using the architecture, generate a simple SysML v2 textual model: requirements · actions
> (DetectDrowsiness, AssessConfidence, TriggerResponse) · interfaces/flows · major system elements.
> Focus on readability.

**OUTPUT:**
```
package DriverMonitoringSystem {
  requirement REQ_F_01;        // detect drowsiness in time
  requirement REQ_F_04;        // suppress false alarms

  part sensors;  part perception;  part decisionLogic;  part hmi;  part vehicleIf;

  action DetectDriverState  { in CabinFrames;  out StateEstimate; }
  action AssessConfidence   { in StateEstimate; out GatedState; }   // satisfies REQ_F_04
  action TriggerResponse    { in GatedState;   out ResponseCommand; } // satisfies REQ_F_03

  flow CabinFrames    from sensors to perception;
  flow StateEstimate  from perception to decisionLogic;
  flow ResponseCommand from decisionLogic to hmi, vehicleIf;
}
```

🔗 **Chain check:** parts mirror the architecture components; actions `satisfy` REQ IDs. **Architecture
→ Model: connected.**

---

## Phase 4 · Implementation — Prompt 5

**INPUT:**
> Using the architecture and the SysML model, generate: high-level implementation approach · pseudocode
> for the detect-assess-respond loop · logic flow & data processing steps · assumptions. Explain how it
> satisfies the requirements.

**OUTPUT:**
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

🔗 **Chain check:** explicitly "Using the architecture and the SysML model"; pseudocode mirrors the
`DetectDriverState → AssessConfidence → TriggerResponse` actions. **Model → Implementation: connected.**

---

## Phase 5 · Verification — Prompt 6

**INPUT:**
> Generate test cases from the acceptance criteria, then review the proposed implementation. Identify:
> requirements satisfied · which test cases pass · potential defects · risks · recommended
> improvements. Provide a pass/fail assessment.

**OUTPUT:**
- **Test cases (from acceptance criteria):**
  - TC-01 sustained eye-closure → drowsy alert ≤ 2 s *(REQ-F-01/NF-01)*
  - TC-02 eyes off road 2 s → distraction alert *(REQ-F-02)*
  - TC-03 sunglasses/low light → no false alarm, state UNKNOWN *(REQ-F-04/NF-05)*
  - TC-04 attentive glances → no alarm *(REQ-F-04/NF-03)*
  - TC-05 no response to escalation → emergency protocol *(REQ-F-05)*
  - TC-06 every event logged *(REQ-F-06)*
- **Review:** REQ-F-01..06 satisfied by the loop; TC-01..06 would pass against the pseudocode.
- **Potential defects:** escalation timing not specified for *intermittent* drowsiness; THRESHOLD value
  unset; no debounce on rapid state flips.
- **Risks:** false-alarm rate (SM-2) unproven until tuned; bias (REQ-NF-05) needs a representative
  validation set.
- **Improvements:** add hysteresis/debounce; define numeric thresholds & escalation windows; add a
  bias test matrix.
- **Assessment:** **PASS with conditions** — logic is requirement-complete; tune thresholds and add
  debounce before fleet release.

🔗 **Chain check:** test cases are *generated here* (no longer dangling) and trace to REQ IDs; review is
against the Phase-4 implementation. **Implementation → Verification: connected.**

---

## Phase 6 · Deployment — Prompt 7

**INPUT:**
> Using the verified implementation, create the deployment plan: OTA & rollback · monitoring metrics
> mapped back to the Success Metrics from Planning · release notes · customer impact · success criteria.

**OUTPUT:**
- **OTA rollout:** shadow-mode → 1% → 10% → 100%, each gate held on live metrics.
- **Rollback:** auto-revert if false-alarm rate breaches SM-2 within 48 h.
- **Monitoring → Planning Success Metrics:**
  - detection accuracy → **SM-1 (≥95%)**
  - false-alarm rate → **SM-2 (<1/8 h)**
  - alert latency → **SM-3 (<2 s)**
  - missed-detection events → **SM-4 (zero critical)**
  - + driver override / trust signal
- **Release notes:** new DMS drowsy/distracted detection + emergency escalation; on-device, privacy-safe.
- **Customer impact:** improved safety; expect occasional advisory alerts; no data leaves the vehicle.
- **Success criteria (30 days):** SM-1–SM-4 all met in-field before exiting staged rollout.

🔗 **Chain check:** "Using the verified implementation"; every monitoring metric maps to a Planning
**SM-#**, closing the loop back to Phase 1. **Verification → Deployment → Planning: loop closed.**

---

## Dry-run verdict
✅ **The digital thread is continuous end-to-end.** Planning's objectives/metrics flow into
requirements (traced IDs) → architecture → model → implementation → verification (tests generated &
traced) → deployment (metrics mapped back to Planning). Every "🔗 Chain check" passed.

**Watch-items for the live run** (surfaced by the dry run, good discussion fodder):
- Numeric **thresholds** (confidence, escalation windows) are a human judgment call — set them live.
- **Bias validation** (REQ-NF-05) needs a representative data set — name it as a real gate.
- Add **debounce/hysteresis** to avoid alert flicker — a natural "what would you change?" moment.
