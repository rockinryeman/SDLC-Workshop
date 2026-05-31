"""
Interactive Driver Monitoring System — let the room "drive" the DMS.

Run:  streamlit run app.py    (install first:  pip install streamlit)

Move the sensor sliders to make the driver drowsy or distracted and watch the
system escalate ALERT -> WARNING -> SAFE-STOP -> EMERGENCY. The sidebar exposes
the *tuning knobs* — the human-judgment decisions we talk about in the workshop
(e.g. drop the confidence threshold and watch false alarms appear).
"""

import streamlit as st
from dms import DMS, Frame, Response

st.set_page_config(page_title="Driver Monitoring System — Live", layout="centered")

st.markdown("<h2 style='color:#256E8E;margin-bottom:0'>Driver Monitoring System — Live</h2>",
            unsafe_allow_html=True)
st.caption("Industrial DevOps Now · AI-Powered Product Development workshop")

# ---- sidebar: the human-judgment tuning knobs ----
st.sidebar.header("Tuning (human judgment)")
conf_thr = st.sidebar.slider("Confidence threshold", 0.0, 1.0, 0.6, 0.05,
                             help="Below this, the system holds and does NOT act (limits false alarms).")
drowsy_s = st.sidebar.slider("Drowsy after (s)", 0.5, 4.0, 2.0, 0.5)
warn_s = st.sidebar.slider("Warn after (s)", 0.5, 4.0, 2.0, 0.5)
safestop_s = st.sidebar.slider("Safe-stop after (s)", 1.0, 8.0, 4.0, 0.5)
emerg_s = st.sidebar.slider("Emergency after (s)", 2.0, 10.0, 6.0, 0.5)

# ---- main: live sensor inputs ----
c1, c2 = st.columns(2)
eye = c1.slider("Eye closure  (0 open · 1 shut)", 0.0, 1.0, 0.2, 0.05)
conf = c1.slider("Perception confidence", 0.0, 1.0, 0.9, 0.05)
gaze = c2.checkbox("Eyes off road")
dur = c2.slider("Hold this condition for (s)", 0.5, 12.0, 6.0, 0.5)

dms = DMS(confidence_threshold=conf_thr, drowsy_seconds=drowsy_s, warn_after=warn_s,
          safestop_after=safestop_s, emergency_after=emerg_s)
n = max(1, int(dur / 0.5))
decisions = [dms.process(Frame(i * 0.5, eye, gaze, conf, False)) for i in range(n)]
final = decisions[-1]

COLORS = {
    Response.NONE: "#1e8e3e",
    Response.ALERT: "#f0a500",
    Response.WARNING: "#e8710a",
    Response.SAFE_STOP_ASSIST: "#d93025",
    Response.EMERGENCY_PROTOCOL: "#a50e0e",
}

st.markdown(
    f"<div style='padding:20px;border-radius:12px;background:{COLORS[final.response]};"
    f"color:white;font-size:1.5rem;font-weight:800;text-align:center;margin:14px 0'>"
    f"{final.state.value} &nbsp;→&nbsp; {final.response.value.replace('_', ' ').upper()}</div>",
    unsafe_allow_html=True,
)
if final.note:
    st.caption("➜ " + final.note)

st.subheader("Decision timeline")
st.dataframe(
    [{"t (s)": d.t, "state": d.state.value, "response": d.response.value, "note": d.note}
     for d in decisions],
    use_container_width=True, hide_index=True,
)

st.info("Try it: set **Eye closure = 0.95** and **Hold = 10s** to watch a drowsy driver escalate "
        "to an emergency — then drop the **Confidence threshold** in the sidebar and see what changes.")
