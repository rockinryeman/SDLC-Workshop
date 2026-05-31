"""
Runnable verification for the DMS — pytest tests mapped to the requirements.

Run live in the workshop:  pytest -v
Green/red here is the "verification" step made real, traceable to DMS-001..006.
"""

from dms import DMS, Frame, State, Response


def drive(dms, spec):
    """spec: list of (eye_closure, gaze_off_road, confidence, driver_ack) at 0.5s steps."""
    decisions = []
    for i, (e, g, c, a) in enumerate(spec):
        decisions.append(dms.process(Frame(i * 0.5, e, g, c, a)))
    return decisions


def peak(decisions):
    return max((d.response for d in decisions), key=lambda r: list(Response).index(r))


# DMS-001 — detect drowsiness from sustained eye closure, and alert
def test_dms_001_detects_drowsiness():
    d = drive(DMS(), [(0.95, False, 0.95, False)] * 8)
    assert any(x.state == State.DROWSY for x in d)
    assert peak(d) != Response.NONE


# DMS-002 — detect distraction (eyes off road)
def test_dms_002_detects_distraction():
    d = drive(DMS(), [(0.1, True, 0.95, False)] * 6)
    assert any(x.state == State.DISTRACTED for x in d)


# DMS-003 — escalate alert -> warning -> safe-stop as impairment persists
def test_dms_003_escalates():
    d = drive(DMS(), [(0.95, False, 0.95, False)] * 16)
    seq = [x.response for x in d]
    assert Response.ALERT in seq
    assert Response.WARNING in seq
    assert Response.SAFE_STOP_ASSIST in seq


# DMS-004 — suppress alerts when confidently attentive (no false alarm)
def test_dms_004_no_false_alarm_when_attentive():
    d = drive(DMS(), [(0.1, False, 0.95, False)] * 8)
    assert all(x.response == Response.NONE for x in d)


# DMS-004 — low confidence (e.g. sunglasses) -> UNKNOWN, never acts
def test_dms_004_low_confidence_holds():
    d = drive(DMS(), [(0.95, False, 0.30, False)] * 8)
    assert all(x.state == State.UNKNOWN for x in d)
    assert all(x.response == Response.NONE for x in d)


# DMS-005 — no response to escalation -> emergency protocol
def test_dms_005_emergency_when_unresponsive():
    d = drive(DMS(), [(0.95, False, 0.95, False)] * 20)
    assert any(x.state == State.EMERGENCY for x in d)
    assert peak(d) == Response.EMERGENCY_PROTOCOL


# DMS-003 — driver who recovers after an alert does NOT reach emergency
def test_driver_recovery_deescalates():
    spec = [(0.95, False, 0.95, False)] * 5 + [(0.1, False, 0.95, True)] + [(0.1, False, 0.95, False)] * 4
    d = drive(DMS(), spec)
    assert peak(d) in (Response.ALERT, Response.WARNING)
    assert not any(x.state == State.EMERGENCY for x in d)


# DMS-006 — every frame is logged
def test_dms_006_logs_events():
    dms = DMS()
    drive(dms, [(0.5, False, 0.9, False)] * 5)
    assert len(dms.log) == 5
