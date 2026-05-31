# Prompt Book — Live DMS Exercise (6 SDLC phases)

Walk the **Driver Monitoring System** through the lifecycle, live, as one small team. Phases align
to the framework in [10_AI_Across_SDLC.md](10_AI_Across_SDLC.md):

> **Plan → Analyze → Design → Develop → Test → Deploy**

**How to run it:** fresh chat, prompts in order (each builds on the last). For **Develop** and
**Test**, use a tool that can **run code** (Code Interpreter / Claude / Jupyter) — or fall back to
the runnable reference in [`simulation/`](simulation/). Rhythm: **paste → read output → ask the room
→ move on.** Don't perfect anything; momentum is the point.

> **Prime the chat once (before Phase 1):** *"We're running a live workshop. Keep each answer
> concise and skimmable — bullets over prose."*

---

## Phase 1 · Plan
```
You are a senior automotive systems engineer. We are launching a Driver Monitoring System (DMS)
that detects when a driver is drowsy, distracted, or experiencing a medical emergency, and responds
appropriately. Give:
- The product vision (one paragraph)
- Key stakeholder needs
- A short capability roadmap (MVP -> later)
- Top risks and constraints
```
**Ask the room:** *Does this capture the real goal? What's missing?*

## Phase 2 · Analyze
```
Turn those needs into a requirements specification:
- Functional requirements
- Non-functional requirements (latency, accuracy, privacy)
- Assumptions
- Acceptance criteria
Flag any gaps or NEW requirements you discover along the way.
```
**Ask the room:** *What would you challenge? What did it surface that we'd have missed?*

## Phase 3 · Design
```
Using the requirements, create the design:
- System context (described in text)
- Major components: sensors, perception/AI, decision logic, HMI, vehicle interface
- Interfaces and data flows
- Failure modes, safety, and privacy/cybersecurity considerations
Then express it as a simple SysML v2 textual model (requirements, actions, flows) that traces back
to the requirements. Favor readability over tool-specific correctness.
```
**Ask the room:** *Where could this go wrong — and how does the system stay safe?*

## Phase 4 · Develop
```
Turn the design into runnable Python (no external libraries):
- enums for driver state (attentive, drowsy, distracted, unknown, emergency) and response
  (none, alert, warning, safe-stop assist, emergency protocol)
- a DMS class with a process(frame) method implementing detect-assess-respond: sustained eye
  closure -> drowsy; sustained gaze off road -> distracted; low confidence -> unknown (no action);
  escalate the longer the driver stays impaired; emergency if unresponsive
- an event log
Show the code, then run it on one sample frame.
```
**Ask the room:** *That's real code — notice we got here with no separate dev-team handoff.*
*(Backup: [`simulation/dms.py`](simulation/dms.py).)*

## Phase 5 · Test
```
Write pytest tests that verify the requirements: detect drowsiness, detect distraction, escalate
alert -> warning -> safe-stop, suppress false alarms when attentive / low-confidence, trigger
emergency when unresponsive, and log events. Run them and show green/red.

Then run the logic against scripted scenarios — attentive, drowsy, distracted, sunglasses
(low confidence) — and print the state + response at each step.
```
**Ask the room:** *Verification just became evidence. Which test must pass before we ship?*
*(Backup: [`simulation/test_dms.py`](simulation/test_dms.py) and [`simulate.py`](simulation/simulate.py).)*

## Phase 6 · Deploy
```
Create the deployment plan:
- OTA deployment plan and rollback strategy
- Monitoring metrics (detection accuracy, false-alarm rate, driver-trust signals)
- Release notes
- Customer impact assessment
- Success criteria after deployment
```
**Ask the room:** *We went from idea to deployable as one team. How many teams would this normally take?*

---

## Facilitator discussion questions (use after the exercise)
- What surprised you about the output?
- What would you challenge or review before trusting it?
- Where would human expertise still be required?
- How many teams would traditionally be involved in producing all of this?
- What handoffs did we just eliminate?
- It's a safety system — what changes for you that AI helped design *and run* it?
