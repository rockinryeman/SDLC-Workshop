# Prompt Book — Live DMS Exercise

**Purpose:** Guide the room through an AI-assisted automotive SDLC exercise for a **Driver
Monitoring System**. Each prompt builds on the previous output to demonstrate iterative,
single-team product development.

**How to run it:** Paste each prompt into the AI tool live on screen. Read the output aloud (or
have a participant do it). After each, ask the facilitator question before moving on. The goal is
to *show the journey*, not to produce a perfect artifact.

> **Tip:** Start a fresh chat, then feed these in order. Tell the AI once at the start:
> *"We're running a live workshop. Keep each answer concise and skimmable — bullets over prose."*

---

## Prompt 1 · Requirements Generation
```
You are a senior automotive systems engineer. We are designing a Driver Monitoring System (DMS)
that detects when a driver is drowsy, distracted, or experiencing a medical emergency, and
responds appropriately. Generate:
- Stakeholder needs
- Functional requirements
- Non-functional requirements (latency, accuracy, privacy)
- Constraints
- Assumptions
- Acceptance criteria
Format the output as a requirements specification.
```
**Ask the room:** *What's missing? What would you challenge?*

## Prompt 2 · Architecture & Design
```
Using the approved requirements, create a concise architecture description including:
- System context diagram (described in text)
- Major components (sensors, perception/AI, decision logic, HMI, vehicle interface)
- Interfaces and data flows
- Failure modes
- Safety considerations
- Privacy and cybersecurity considerations
```
**Ask the room:** *Where could this go wrong, and how would the system stay safe?*

## Prompt 3 · SysML v2 Text Model
```
Using the architecture, generate a simple SysML v2 textual model including:
- Requirements
- Actions/functions (e.g., DetectDrowsiness, AssessConfidence, TriggerResponse)
- Interfaces/flows
- Major system elements
Focus on readability, not tool-specific correctness.
```
**Ask the room (non-technical framing):** *This is just a structured way to write down the
design so both a person and a machine can read it — notice how it traces back to the requirements.*

## Prompt 4 · Test Development
```
Create:
- Verification strategy
- Functional test cases
- Edge case test cases (sunglasses, darkness, head turned, passenger interference)
- Negative test cases (false-positive drowsiness)
- A requirements-to-test traceability matrix
Include objective pass/fail criteria.
```
**Ask the room:** *Which of these tests would you most want to see pass before shipping?*

## Prompt 5 · Implementation Approach
```
Generate:
- High-level implementation approach
- Pseudocode for the detect-assess-respond loop
- Logic flow
- Data processing steps
- Assumptions
Explain how the solution satisfies the requirements.
```
**Ask the room:** *Notice we went from idea to logic without a separate dev team handoff.*

## Prompt 6 · Verification Review
```
Review the proposed implementation. Identify:
- Which requirements are satisfied
- Which tests would pass
- Potential defects
- Risks (especially false alarms and missed detections)
- Recommended improvements
Provide a pass/fail assessment.
```
**Ask the room:** *Where does human expertise still have to make the final call?*

## Prompt 7 · Deployment Planning
```
Create:
- OTA deployment plan
- Rollback strategy
- Monitoring metrics (detection accuracy, false-alarm rate, driver trust signals)
- Release notes
- Customer impact assessment
- Success criteria after deployment
```
**Ask the room:** *We just reached a deployment plan. How many teams would this normally take?*

---

## Facilitator discussion questions (use after the exercise)
- What surprised you about the output?
- What would you challenge or review before trusting it?
- Where would human expertise still be required?
- How many teams would traditionally be involved in producing all of this?
- What handoffs did we just eliminate?
- This is a safety system — what does it change for you that AI helped design it?
