"""
Driver Monitoring System (DMS) — reference detect-assess-respond logic.

A small, dependency-free model of the DMS the workshop builds live. It mirrors the
requirements in 05_DMS_Feature_Package.md:

  DMS-001  detect drowsiness within ~2 s of sustained eye-closure / head-nod
  DMS-002  detect distraction (eyes off road) within ~1.5 s
  DMS-003  escalate response: ALERT -> WARNING -> SAFE_STOP_ASSIST
  DMS-004  suppress alerts when confidently attentive (limit false alarms)
  DMS-005  detect a possible medical emergency (no response to escalation)
  DMS-006  log every detection / response event

This module is imported by simulate.py (console demo), test_dms.py (pytest) and
app.py (Streamlit UI). Keep it pure and readable — it's a teaching artifact.
"""

from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional


# ---- States and responses -------------------------------------------------

class State(str, Enum):
    ATTENTIVE = "ATTENTIVE"
    DROWSY = "DROWSY"
    DISTRACTED = "DISTRACTED"
    UNKNOWN = "UNKNOWN"          # low confidence — do NOT act (DMS-004)
    EMERGENCY = "EMERGENCY"      # impaired and unresponsive (DMS-005)


class Response(str, Enum):
    NONE = "none"
    ALERT = "alert"                       # gentle chime / icon
    WARNING = "warning"                   # stronger aud: + haptic
    SAFE_STOP_ASSIST = "safe_stop_assist" # begin assisted slow-down
    EMERGENCY_PROTOCOL = "emergency_protocol"  # call for help


@dataclass
class Frame:
    """One time-step of sensor input."""
    t: float                    # seconds since start
    eye_closure: float          # 0.0 (open) .. 1.0 (fully closed)
    gaze_off_road: bool         # eyes off the forward road
    confidence: float           # perception confidence 0.0 .. 1.0
    driver_ack: bool = False    # did the driver respond/recover this frame?


@dataclass
class Decision:
    t: float
    state: State
    confidence: float
    response: Response
    note: str = ""


# ---- The system -----------------------------------------------------------

@dataclass
class DMS:
    # tunable thresholds (the "human judgment" knobs we talk about in the room)
    confidence_threshold: float = 0.6     # below this -> UNKNOWN, no action (DMS-004)
    drowsy_eye_closure: float = 0.8       # eyes >= 80% closed counts as drooping
    drowsy_seconds: float = 2.0           # sustained this long -> drowsy (DMS-001)
    distract_seconds: float = 1.5         # eyes off road this long -> distracted (DMS-002)
    warn_after: float = 2.0               # seconds in alert before escalating to warning
    safestop_after: float = 4.0           # seconds impaired before safe-stop assist
    emergency_after: float = 6.0          # seconds unresponsive before emergency (DMS-005)

    # internal timers / state
    _eye_closed_since: Optional[float] = None
    _gaze_off_since: Optional[float] = None
    _impaired_since: Optional[float] = None
    log: List[Decision] = field(default_factory=list)

    def _classify(self, f: Frame) -> State:
        # DMS-004: never act on low-confidence perception
        if f.confidence < self.confidence_threshold:
            self._eye_closed_since = None
            self._gaze_off_since = None
            return State.UNKNOWN

        # track sustained eye closure
        if f.eye_closure >= self.drowsy_eye_closure:
            if self._eye_closed_since is None:
                self._eye_closed_since = f.t
        else:
            self._eye_closed_since = None

        # track sustained gaze off road
        if f.gaze_off_road:
            if self._gaze_off_since is None:
                self._gaze_off_since = f.t
        else:
            self._gaze_off_since = None

        drowsy = (self._eye_closed_since is not None
                  and f.t - self._eye_closed_since >= self.drowsy_seconds)
        distracted = (self._gaze_off_since is not None
                      and f.t - self._gaze_off_since >= self.distract_seconds)

        if drowsy:
            return State.DROWSY
        if distracted:
            return State.DISTRACTED
        return State.ATTENTIVE

    def process(self, f: Frame) -> Decision:
        """Process one frame and return the decision (also appended to the log)."""
        state = self._classify(f)

        # a confident, attentive driver (or an acknowledgment) clears the impaired timer
        if state in (State.ATTENTIVE, State.UNKNOWN) or f.driver_ack:
            self._impaired_since = None
            response = Response.NONE
            note = "driver acknowledged" if f.driver_ack else ""
            if state == State.UNKNOWN:
                note = "low confidence — holding (no false alarm)"
            decision = Decision(f.t, state, f.confidence, response, note)
            self.log.append(decision)
            return decision

        # impaired (drowsy/distracted): escalate based on how long it has persisted (DMS-003)
        if self._impaired_since is None:
            self._impaired_since = f.t
        elapsed = f.t - self._impaired_since

        if elapsed >= self.emergency_after:
            state = State.EMERGENCY
            response = Response.EMERGENCY_PROTOCOL
            note = "no response to escalation — emergency protocol"
        elif elapsed >= self.safestop_after:
            response = Response.SAFE_STOP_ASSIST
            note = "escalated: safe-stop assist"
        elif elapsed >= self.warn_after:
            response = Response.WARNING
            note = "escalated: warning"
        else:
            response = Response.ALERT
            note = "first alert"

        decision = Decision(f.t, state, f.confidence, response, note)
        self.log.append(decision)
        return decision

    def run(self, frames: List[Frame]) -> List[Decision]:
        return [self.process(f) for f in frames]
