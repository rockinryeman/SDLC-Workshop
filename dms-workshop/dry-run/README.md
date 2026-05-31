# Dry Run — DMS Live Exercise (one file per prompt)

A captured test run of the 6-phase / 7-prompt chain. Each file has the **INPUT** (prompt), the
**OUTPUT** (AI result), and a **🔗 Chain check** confirming it consumed the prior step's artifacts.
Traceable IDs (`BO`, `CN`, `SM`, `REQ-F`, `REQ-NF`, `TC`) make the digital thread visible.

| Phase | File |
|-------|------|
| 1 · Planning | [1_Planning.md](1_Planning.md) |
| 2 · Requirements | [2_Requirements.md](2_Requirements.md) |
| 3 · Architecture / Design | [3_Architecture_Design.md](3_Architecture_Design.md) |
| 3 · Model the System | [4_Model.md](4_Model.md) |
| 4 · Implementation | [5_Implementation.md](5_Implementation.md) |
| 5 · Verification | [6_Verification.md](6_Verification.md) |
| 6 · Deployment | [7_Deployment.md](7_Deployment.md) |

## Verdict: ✅ the digital thread is continuous
Planning's objectives/metrics flow into requirements (traced IDs) → architecture → model →
implementation → verification (tests generated & traced) → deployment (metrics mapped back to
Planning). Every chain check passed.

## Watch-items surfaced by the dry run (good live discussion fuel)
1. **Numeric thresholds** (confidence, escalation windows) are a human judgment call — set them live.
2. **Bias validation** (REQ-NF-05) needs a named, representative data set — call it out as a real gate.
3. Add **debounce / hysteresis** to avoid alert flicker — a natural "what would you change?" moment.

> Doubles as a **backup answer key**: if the live AI wobbles, show these outputs instead.
