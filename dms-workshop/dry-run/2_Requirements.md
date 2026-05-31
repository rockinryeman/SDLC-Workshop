# Prompt 2 · Requirements

## INPUT (prompt)
> You are a senior automotive systems engineer. Using the Planning outputs (stakeholders, customer
> needs, business objectives, success metrics, prioritized outcomes), produce a requirements
> specification for the DMS: functional · non-functional (latency, accuracy, privacy) · constraints &
> assumptions · acceptance criteria. Trace each requirement back to a stakeholder need or business
> objective from Planning.

## OUTPUT (AI result)
**Functional**
- REQ-F-01 Detect drowsiness within 2 s of sustained eye-closure/head-nod. *(→ CN-1, BO-1)*
- REQ-F-02 Detect distraction (eyes off road > 1.5 s). *(→ CN-1, BO-1)*
- REQ-F-03 Escalate response: advisory → active → emergency. *(→ Outcome 3)*
- REQ-F-04 Suppress alerts when attentive or low-confidence. *(→ CN-2, SM-2)*
- REQ-F-05 Trigger emergency protocol if unresponsive to escalation. *(→ Outcome 3)*
- REQ-F-06 Log every detection/response event. *(→ liability, traceability)*

**Non-functional**
- REQ-NF-01 Detection latency < 2 s. *(→ SM-3)*
- REQ-NF-02 Drowsiness accuracy ≥ 95%. *(→ SM-1)*
- REQ-NF-03 False-alarm rate < 1 / 8 h. *(→ SM-2, CN-2)*
- REQ-NF-04 On-device processing; no raw video leaves the vehicle. *(→ CN-3, Outcome 4)*
- REQ-NF-05 Equal performance across demographics & lighting. *(→ Risk: bias)*
- REQ-NF-06 Model is OTA-updatable. *(→ Assumption: OTA)*

**Constraints / assumptions:** existing camera+IR; automotive-grade ECU compute budget; UNECE R79
interaction for any steering/braking assist.

**Acceptance criteria (samples):** drowsy event flagged ≤ 2 s in HIL test (REQ-F-01/NF-01); false-alarm
rate < 1/8 h over a 40-h drive set (REQ-NF-03); 0 raw frames egress in network capture (REQ-NF-04).

## 🔗 Chain check
Every requirement carries a *(→ …)* link to a Planning need/objective/metric — and it does **not**
re-derive stakeholder needs (Planning owns those). **Planning → Requirements: connected.**

**Ask the room:** *What's missing? What would you challenge?*
