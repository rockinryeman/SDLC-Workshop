# Prompt Book — Live DMS Exercise (synced to the deck)

Six phases, matching the LAAD deck's breadcrumb steps (Architecture/Design carries two prompts):

> **Planning → Requirements → Architecture/Design → Implementation → Verification → Deployment**

**How to run it:** fresh chat, prompts in order (each builds on the last). Rhythm: **paste → read
output aloud → ask the room → move on.** Don't perfect anything; momentum is the point.

> **Prime the chat once (before Prompt 1):** *"We're running a live workshop. Keep each answer
> concise and skimmable — bullets over prose."*

---

## Phase 1 · Planning  — Prompt 1
```
You are a cross-functional automotive product team. Analyze the Driver Monitoring System concept and
generate: Stakeholders · Business Objectives · Customer Needs · Risks · Assumptions · Success Metrics ·
Prioritized Outcomes.
```
**Ask the room:** *What's the plan? What's missing?*

## Phase 2 · Requirements  — Prompt 2
```
You are a senior automotive systems engineer. Using the Planning outputs (stakeholders, customer
needs, business objectives, success metrics, prioritized outcomes), produce a requirements
specification for the Driver Monitoring System (DMS):
- Functional requirements
- Non-functional requirements (latency, accuracy, privacy)
- Constraints & assumptions
- Acceptance criteria
Trace each requirement back to a stakeholder need or business objective from Planning.
```
**Ask the room:** *What's missing? What would you challenge?*

## Phase 3 · Architecture / Design  — Prompt 3
```
Using the approved requirements, create a concise architecture description:
System context diagram (in text) · Major components: sensors, perception/AI, decision logic, HMI,
vehicle interface · Interfaces & data flows · Failure modes · Safety considerations · Privacy &
cybersecurity considerations
```
**Ask the room:** *Where could this go wrong, and how does it stay safe?*

### …still Phase 3 (Architecture / Design) · Model the System — Prompt 4
```
Using the architecture, generate a simple SysML v2 textual model:
· Requirements · Actions / functions (DetectDrowsiness, AssessConfidence, TriggerResponse) ·
Interfaces / flows · Major system elements
Focus on readability, not tool-specific correctness.
```
**Ask the room:** *What should we watch for?*

## Phase 4 · Implementation  — Prompt 5
```
Using the architecture and the SysML model, generate:
- High-level implementation approach
- Pseudocode for the detect-assess-respond loop
- Logic flow & data processing steps
- Assumptions
Explain how the solution satisfies the requirements.
```
**Ask the room:** *Idea to logic — with no separate dev-team handoff.*
> **Optional "show it run":** instead of pseudocode, ask for **runnable Python** and execute it
> live. See [09_Code_Simulation_Prompts.md](09_Code_Simulation_Prompts.md) and [`simulation/`](simulation/).

## Phase 5 · Verification  — Prompt 6
```
Generate test cases from the acceptance criteria, then review the proposed implementation. Identify:
- Which requirements are satisfied
- Which test cases pass
- Potential defects
- Risks (false alarms, missed detections)
- Recommended improvements
Provide a pass/fail assessment.
```
**Ask the room:** *Where does human expertise have to make the final call?*
> **Optional "tests that run":** ask for **pytest** and run it live (green/red), traceable to the
> requirements. See [09_Code_Simulation_Prompts.md](09_Code_Simulation_Prompts.md) and [`simulation/`](simulation/).

## Phase 6 · Deployment  — Prompt 7
```
Using the verified implementation, create the deployment plan:
- OTA deployment plan & rollback strategy
- Monitoring metrics (accuracy, false-alarm rate, driver trust) — mapped back to the Success
  Metrics from Planning
- Release notes
- Customer impact assessment
- Success criteria after deployment
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
