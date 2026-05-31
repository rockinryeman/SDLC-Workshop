# Prompt 6 · Verification

## INPUT (prompt)
> Generate test cases from the acceptance criteria, then review the proposed implementation. Identify:
> requirements satisfied · which test cases pass · potential defects · risks · recommended
> improvements. Provide a pass/fail assessment.

## OUTPUT (AI result)
**Test cases (generated from the acceptance criteria):**
- TC-01 sustained eye-closure → drowsy alert ≤ 2 s *(REQ-F-01 / NF-01)*
- TC-02 eyes off road 2 s → distraction alert *(REQ-F-02)*
- TC-03 sunglasses / low light → no false alarm, state UNKNOWN *(REQ-F-04 / NF-05)*
- TC-04 attentive glances → no alarm *(REQ-F-04 / NF-03)*
- TC-05 no response to escalation → emergency protocol *(REQ-F-05)*
- TC-06 every event logged *(REQ-F-06)*

**Review:**
- **Requirements satisfied:** REQ-F-01..06 by the loop.
- **Tests that pass:** TC-01..06 against the pseudocode.
- **Potential defects:** escalation timing unspecified for *intermittent* drowsiness; THRESHOLD value
  unset; no debounce on rapid state flips.
- **Risks:** false-alarm rate (SM-2) unproven until tuned; bias (REQ-NF-05) needs a representative
  validation set.
- **Improvements:** add hysteresis/debounce; define numeric thresholds & escalation windows; add a
  bias test matrix.
- **Assessment:** **PASS with conditions** — logic is requirement-complete; tune thresholds and add
  debounce before fleet release.

> **Optional "tests that run":** ask for **pytest** and run it live (green/red) — see
> [`../simulation/test_dms.py`](../simulation/test_dms.py).

## 🔗 Chain check
Test cases are **generated here** (no longer a dangling reference) and trace to REQ IDs; the review is
against the Phase-5 implementation. **Implementation → Verification: connected.**

**Ask the room:** *Where does human expertise have to make the final call?*
