# Prompt 1 · Planning

## INPUT (prompt)
> You are a cross-functional automotive product team. Analyze the Driver Monitoring System concept and
> generate: Stakeholders · Business Objectives · Customer Needs · Risks · Assumptions · Success Metrics ·
> Prioritized Outcomes.

*(Prime the chat once first: "We're running a live workshop. Keep each answer concise and skimmable —
bullets over prose.")*

## OUTPUT (AI result)
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

## 🔗 Chain check
Starts the thread — defines the **objectives (BO)**, **needs (CN)**, and **metrics (SM)** that every
later step traces back to.

**Ask the room:** *What's the plan? What's missing?*
