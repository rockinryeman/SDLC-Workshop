"""
Live demo: run the DMS against scripted scenarios and watch it decide.

Usage:  python simulate.py            (all scenarios)
        python simulate.py drowsy     (one scenario by name)

Each scenario is a sequence of sensor frames (one per ~0.5 s). The DMS processes
them in order and we print the state + response at each step — so the room can
SEE the car notice the driver and escalate.
"""

import sys
from dms import DMS, Frame, State, Response

# console colors (fall back to plain text if the terminal doesn't support them)
C = {"reset": "\033[0m", "green": "\033[92m", "yellow": "\033[93m",
     "red": "\033[91m", "gray": "\033[90m", "bold": "\033[1m", "cyan": "\033[96m"}

RESP_COLOR = {
    Response.NONE: "green",
    Response.ALERT: "yellow",
    Response.WARNING: "yellow",
    Response.SAFE_STOP_ASSIST: "red",
    Response.EMERGENCY_PROTOCOL: "red",
}


def frames(spec):
    """spec: list of (eye_closure, gaze_off_road, confidence, driver_ack) at 0.5s steps."""
    return [Frame(t=i * 0.5, eye_closure=e, gaze_off_road=g, confidence=c, driver_ack=a)
            for i, (e, g, c, a) in enumerate(spec)]


# ---- Scenarios (map to the workshop's test cases TC-001..006) --------------

SCENARIOS = {
    # TC-004 negative case: attentive driver glancing at mirrors -> NO alarm (DMS-004)
    "attentive": frames([
        (0.1, False, 0.95, False), (0.1, True, 0.95, False), (0.1, False, 0.95, False),
        (0.1, False, 0.95, False), (0.1, True, 0.95, False), (0.1, False, 0.95, False),
    ]),

    # TC-001 / DMS-001: drowsiness onset -> alert -> warning -> safe-stop -> emergency
    "drowsy": frames([
        (0.2, False, 0.95, False), (0.85, False, 0.95, False), (0.9, False, 0.95, False),
    ] + [(0.95, False, 0.95, False)] * 18),

    # DMS-003: driver recovers after the first alert -> de-escalate, no emergency
    "recovers": frames([
        (0.9, False, 0.95, False), (0.95, False, 0.95, False), (0.95, False, 0.95, False),
        (0.95, False, 0.95, False), (0.95, False, 0.95, False), (0.1, False, 0.95, True),
        (0.1, False, 0.95, False), (0.1, False, 0.95, False),
    ]),

    # TC-002 / DMS-002: distraction (eyes off road) -> distraction alert
    "distracted": frames([
        (0.1, False, 0.95, False), (0.1, True, 0.95, False), (0.1, True, 0.95, False),
        (0.1, True, 0.95, False), (0.1, True, 0.95, False), (0.1, True, 0.95, False),
    ]),

    # TC-003 edge case: sunglasses / low confidence -> UNKNOWN, no false alarm (DMS-004)
    "sunglasses": frames([
        (0.9, False, 0.35, False), (0.95, False, 0.30, False), (0.95, False, 0.32, False),
        (0.95, False, 0.31, False), (0.95, False, 0.33, False), (0.95, False, 0.30, False),
    ]),
}


def color(txt, name):
    return f"{C.get(name, '')}{txt}{C['reset']}"


def run_scenario(name):
    print(color(f"\n=== Scenario: {name} ===", "bold"))
    print(color(f"{'t (s)':>6}  {'eye':>4} {'gaze':>5} {'conf':>5}   {'STATE':<11} {'RESPONSE':<18} note", "gray"))
    dms = DMS()
    for f, d in zip(SCENARIOS[name], dms.run(SCENARIOS[name])):
        gaze = "off" if f.gaze_off_road else "road"
        line = (f"{d.t:>6.1f}  {f.eye_closure:>4.2f} {gaze:>5} {f.confidence:>5.2f}   "
                f"{d.state.value:<11} {d.response.value:<18} {d.note}")
        print(color(line, RESP_COLOR.get(d.response, "gray")))
    # summary
    worst = max((d.response for d in dms.log), key=lambda r: list(Response).index(r))
    print(color(f"  -> peak response: {worst.value}", "cyan"))


if __name__ == "__main__":
    which = sys.argv[1:] or list(SCENARIOS.keys())
    for name in which:
        if name in SCENARIOS:
            run_scenario(name)
        else:
            print(f"unknown scenario '{name}'. options: {', '.join(SCENARIOS)}")
    print()
