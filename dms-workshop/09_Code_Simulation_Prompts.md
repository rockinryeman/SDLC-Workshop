# Code & Simulation Prompts — making the build runnable

Detailed prompts for the **Develop** and **Test** phases so the room sees **real, running software**,
not just generated text. Use them in a tool that can **execute code** (ChatGPT Code Interpreter /
Advanced Data Analysis, Claude with code execution, or a local Jupyter notebook). A working
**reference** lives in [`simulation/`](simulation/) — fall back to it if live generation wobbles.

> Where these fit: they are the fuller versions of Prompt Book **Phase 4 (Develop)** and
> **Phase 5 (Test)**.

---

## Develop — real, runnable Python
```
Turn the implementation into runnable Python (no external libraries). Provide a DMS class with:
- an enum of driver states (attentive, drowsy, distracted, unknown, emergency)
- an enum of responses (none, alert, warning, safe-stop assist, emergency protocol)
- a process(frame) method that takes per-frame sensor input (eye_closure 0–1, gaze_off_road bool,
  confidence 0–1) and returns the state + response
- detection rules: sustained eye closure -> drowsy; sustained gaze off road -> distracted;
  confidence below a threshold -> unknown (no action); escalate response the longer the driver
  stays impaired; emergency if impairment persists with no acknowledgment
- an event log
Make it clean and readable. Then show the code.
```
**Say:** "Notice — that's not pseudocode anymore. It runs."

## Develop → run the simulation (the moment it comes alive)
```
Write a short script that runs the DMS against a few scripted scenarios — an attentive driver, a
drowsy driver whose eyes close and stay closed, a distracted driver, and a sunglasses/low-confidence
case. Step through time and print the state and response at each step so we can watch it escalate.
Run it and show the output.
```
**Say:** "There it is — the car noticing the drowsy driver and escalating to a safe stop. That's the
feature from our opening story, running."

## Test — tests made real
```
Write pytest tests that verify the requirements:
- DMS-001 detects drowsiness and alerts
- DMS-002 detects distraction
- DMS-003 escalates alert -> warning -> safe-stop
- DMS-004 no false alarm when attentive; holds on low confidence
- DMS-005 emergency protocol when unresponsive
- DMS-006 logs every event
Run the tests and show green/red.
```
**Say:** "Verification just stopped being a paragraph — it's evidence, and it traces straight back to
our requirements."

## Optional — Interactive UI (let the room drive it)
```
Build a small Streamlit app with sliders for eye closure, gaze off road, perception confidence, and
how long the condition is held — plus sidebar sliders for the tuning thresholds (confidence
threshold, drowsy/warn/safe-stop/emergency timings). Show the resulting state and response, colored
by severity, and a timeline. Then run it.
```
**Say:** "Watch what happens when I lower the confidence threshold — false alarms appear. *That* is a
human judgment call, not the AI's."

---

## Facilitator notes
- **Have the reference ready.** Open `simulation/` and confirm `python3 simulate.py drowsy` and
  `pytest -v` work *before* the session. If live generation stalls, run these instead — same payoff.
- **Time:** these add ~6–10 min. If short on time, do Step 5 + 5b and skip the live pytest (or vice
  versa). The simulation (5b) is the one to protect — it's the visual "wow."
- **Tie it back:** the simulation closes the loop on the opening drowsy-driver story and makes the
  "humans in the loop" slide concrete (the tuning thresholds are the human decisions).
