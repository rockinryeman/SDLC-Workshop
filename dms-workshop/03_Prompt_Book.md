# Prompt Book — Live DMS Exercise (synced to the deck)

Six phases, matching the LAAD deck's breadcrumb steps (Architecture/Design carries two prompts):

> **Planning → Requirements → Architecture/Design → Implementation → Verification → Deployment**

**How to run it:** fresh chat, prompts in order (each builds on the last). Rhythm: **paste → read
output aloud → ask the room → move on.** Don't perfect anything; momentum is the point.

> **Run on a frontier model (e.g. Claude Opus)** for the live exercise — it produces the cleanest,
> most honest output and the lowest-severity worst case. Even so, the chain is not defect-free: see
> [PROMPT_PACK_EVAL.md](PROMPT_PACK_EVAL.md). A strong move is to let the room **play skeptic** and hunt
> the emergency-logic / traceability hole — more credible than presenting a "perfect" chain.

> **Prime the chat once (before Prompt 1):** *"We're running a live workshop. Open every stage with a
> ≤5-line summary box (key decisions + open risks); cap prose, at most two tables per stage, no ASCII
> diagrams, ASCII characters only. This is a single-pass design exercise: you have run no tests and have
> no field data, so never present measured results as fact — mark anything unproven as ASSUMPTION or
> PENDING. Cite a regulation only with its real acceptance criterion; any number you choose yourself must
> be tagged SELF-IMPOSED DESIGN TARGET and never attributed to a named regulation (EU GSR / Regulation
> 2019/2144 ADDW+DDAW is the binding mandate; Euro NCAP is a voluntary rating). If unsure of a standard's
> ID, write STANDARD-REF-TBD rather than guessing."*

---

## Phase 1 · Planning  — Prompt 1
```text
You are a cross-functional automotive product team. Analyze the Driver Monitoring System concept and
generate: Stakeholders · Business Objectives · Customer Needs · Risks · Assumptions · Success Metrics ·
Prioritized Outcomes. Enumerate the safety-critical scenarios the system must handle as explicit
customer needs, including: (a) sustained drowsiness, (b) eyes-off-road distraction, and (c) the driver
becoming UNRESPONSIVE after escalation.
```
**Ask the room:** *What's the plan? What's missing?*

## Phase 2 · Requirements  — Prompt 2
```text
You are a senior automotive systems engineer. Using the Planning outputs (stakeholders, customer
needs, business objectives, success metrics, prioritized outcomes), produce a requirements
specification for the Driver Monitoring System (DMS):
- Functional requirements
- Non-functional requirements (latency, accuracy, privacy)
- Constraints & assumptions
- Acceptance criteria
Pin these targets (flag any deviation as DEVIATION with rationale): drowsiness detect-to-alert <2s;
distraction (eyes-off-road) detect-to-alert <1.5s as a SEPARATE requirement; true-positive rate >=95%;
false alarms <1 per 8h driving. Include a requirement for escalation: alert -> strong warning ->
safe-stop assist -> emergency protocol when the driver does not respond.
End with a fully RENDERED traceability table (do not merely assert "no orphans") mapping every
requirement backward to a stakeholder need and forward to the test case that will verify it. Every
safety-critical action (terminal safe-stop misfire, eCall, demographic-bias-before-release, event
logging) must have its OWN acceptance criterion AND its OWN negative/misfire test case.
```
**Ask the room:** *What's missing? What would you challenge?*

## Phase 3 · Architecture / Design  — Prompt 3
```text
Using the approved requirements, create a concise architecture description:
System context diagram (in text) · Major components: sensors, perception/AI, decision logic, HMI,
vehicle interface · Interfaces & data flows · Failure modes · Safety considerations · Privacy &
cybersecurity considerations
Specify the vehicle interface for the terminal safe action (safe-stop assist / emergency call). If you
scope it out, add an explicit DESCOPED-WITH-RISK note — do not silently make this alert-only. State
your ASIL assignment as an ASSUMPTION pending a HARA, and keep it consistent across the document.
```
**Ask the room:** *Where could this go wrong, and how does it stay safe?*

### …still Phase 3 (Architecture / Design) · Model the System — Prompt 4
```text
Using the architecture, generate a simple SysML v2 textual model:
· Requirements · Actions / functions — including DetectDriverState, AssessConfidence, SelectResponse,
  TriggerResponse, and an emergency/escalation action · Interfaces / flows · Major system elements
A satisfy-link is INVALID unless its target element appears as the source or sink of at least one
declared data flow — do not bind the terminal-safety requirement to an action that isn't wired into
the pipeline. Focus on readability, not tool-specific correctness.
```
**Ask the room:** *What should we watch for?*

## Phase 4 · Implementation  — Prompt 5
```text
Using the architecture and the SysML model, generate:
- High-level implementation approach
- Pseudocode for the detect-assess-respond loop
- Logic flow & data processing steps
- Assumptions
FAIL-SAFE RULES (apply exactly):
(1) Sustained UNKNOWN/low-confidence must itself escalate on its own timeout — never silently continue.
(2) Escalation may reset only after N CONSECUTIVE confirmed-attentive frames (hysteresis), never one frame.
(3) The emergency protocol must fire on driver non-response REGARDLESS of confidence and INDEPENDENT of
    whether safe-stop succeeds.
(4) Include a driver-cancelable abort window before any terminal action, traced to a test case.
State your detect-to-alert time and confirm your detection window (e.g. PERCLOS / multi-frame) fits
inside the latency budget. Explain how the solution satisfies the requirements.
```
**Ask the room:** *Idea to logic — with no separate dev-team handoff.*
> **Optional "show it run":** instead of pseudocode, ask for **runnable Python** and execute it
> live. See [09_Code_Simulation_Prompts.md](09_Code_Simulation_Prompts.md) and [`simulation/`](simulation/).

## Phase 5 · Verification  — Prompt 6
```text
This is a single-pass DESIGN review — you have executed NO tests, so do not report measured metrics as
fact. Generate test cases from the acceptance criteria (including the attentive-driver negative case =
no false alarm, the distraction-timing case, and the no-response emergency case), then review the
proposed implementation. For each acceptance criterion give a verdict — but for any SAFETY-CRITICAL or
IRREVERSIBLE action (safe-stop, eCall, full escalation) you may NOT use the word PASS while no test has
run; use REVIEWED-NO-DEFECT-FOUND or UNVERIFIED-PENDING-TEST, and re-trace that verdict against the
actual implementation logic, flagging any path where the code would not fire. Then list:
- Potential defects
- Risks (false alarms, missed detections)
- Recommended improvements
```
**Ask the room:** *Where does human expertise have to make the final call?*
> **Optional "tests that run":** ask for **pytest** and run it live (green/red), traceable to the
> requirements. See [09_Code_Simulation_Prompts.md](09_Code_Simulation_Prompts.md) and [`simulation/`](simulation/).

## Phase 6 · Deployment  — Prompt 7
```text
Using the verified implementation, create the deployment plan:
- OTA deployment plan & rollback strategy
- Monitoring metrics (accuracy, false-alarm rate, driver trust) — mapped back to the Success
  Metrics from Planning
- Release notes
- Customer impact assessment
- Success criteria after deployment
Include a SHADOW MODE (detect-but-don't-act) phase as gate 0, validated against labeled events before
any alert reaches a driver. Rollback thresholds must be NO LOOSER than the acceptance criteria they
trace to, and include a success criterion for the emergency-response path. You have NO measured data:
every metric or dashboard value must be an ILLUSTRATIVE/SYNTHETIC placeholder (e.g. <TP_RATE_PENDING>) —
never state a fleet size, accuracy %, or crash-reduction figure as observed.
```
**Ask the room:** *We just reached a deployment plan — how many teams would this normally take?*

---

## Facilitator discussion questions (use after the exercise)
- What surprised you about the output?
- What would you challenge or review before trusting it?
- Where would human expertise still be required?
- How many teams would traditionally be involved in producing all of this?
- What handoffs did we just eliminate?
- It's a safety system — what changes for you that AI helped build it?
