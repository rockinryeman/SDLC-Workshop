# DMS Simulation — runnable reference

A small, dependency-light Driver Monitoring System you can **run live** in the workshop so the
room sees the software actually work — not just generated text. Use it as a **backup** if live
code-generation wobbles, or run it directly.

## Files
| File | What it is |
|------|-----------|
| `dms.py` | Core detect-assess-respond logic (the DMS state machine). Pure Python, no deps. |
| `simulate.py` | Console demo — runs scripted scenarios and prints each decision. |
| `test_dms.py` | `pytest` suite mapped to requirements DMS-001…006 (live green/red). |
| `app.py` | Interactive **Streamlit** UI — sliders to "drive" the DMS. |
| `requirements.txt` | `streamlit`, `pytest` |

## Run it

**1. The console simulation** (no install needed):
```bash
cd simulation
python3 simulate.py            # all scenarios
python3 simulate.py drowsy     # just the drowsy-driver escalation
```
Scenarios: `attentive` · `drowsy` · `recovers` · `distracted` · `sunglasses`

**2. The live tests** (verification, made real):
```bash
pip install pytest
pytest -v
```

**3. The interactive UI**:
```bash
pip install streamlit
streamlit run app.py
```
Move **Eye closure → 0.95**, **Hold → 10s** to watch a drowsy driver escalate ALERT → WARNING →
SAFE-STOP → EMERGENCY. Then drop the **Confidence threshold** in the sidebar to show false alarms
appearing — the "human judgment" point.

## How it maps to the workshop
- **Step 5 (Implementation)** → `dms.py` is what "real, runnable code" looks like.
- **Step 5b (Simulation)** → `simulate.py` / `app.py` — the room sees it run.
- **Step 6 (Verification)** → `pytest` turns the test cases into live green/red, traceable to
  DMS-001…006.

See `../09_Code_Simulation_Prompts.md` for the prompts to generate all of this live.
