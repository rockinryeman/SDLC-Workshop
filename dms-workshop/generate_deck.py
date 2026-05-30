#!/usr/bin/env python3
"""Generate the branded AI-Powered Product Development (DMS) slide deck.
Run with: /tmp/pptxvenv/bin/python generate_deck.py
Brand: Industrial DevOps Now — teal #256E8E, dark #174C63, light #3288AD, gold #F0A500."""

from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR, MSO_AUTO_SIZE
from pptx.enum.shapes import MSO_SHAPE

# ---------- brand ----------
TEAL  = RGBColor(0x25, 0x6E, 0x8E)
TEALD = RGBColor(0x17, 0x4C, 0x63)
TEALL = RGBColor(0x32, 0x88, 0xAD)
GOLD  = RGBColor(0xF0, 0xA5, 0x00)
INK   = RGBColor(0x1B, 0x1B, 0x1B)
GRAY  = RGBColor(0x59, 0x59, 0x59)
LIGHT = RGBColor(0xF7, 0xF7, 0xF7)
LINE  = RGBColor(0xE2, 0xE2, 0xE2)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)
SUB   = RGBColor(0xD8, 0xE6, 0xF7)
FONT  = "Arial"

tTEALD = (0x17, 0x4C, 0x63)
tTEALL = (0x32, 0x88, 0xAD)
def lerp(a, b, t):
    return RGBColor(int(a[0]+(b[0]-a[0])*t), int(a[1]+(b[1]-a[1])*t), int(a[2]+(b[2]-a[2])*t))
def shades(n):
    return [lerp(tTEALD, tTEALL, i/(max(n-1,1))) for i in range(n)]

prs = Presentation()
prs.slide_width = Inches(13.333)
prs.slide_height = Inches(7.5)
BLANK = prs.slide_layouts[6]
SW, SH = 13.333, 7.5

def slide():
    return prs.slides.add_slide(BLANK)

def shape(s, kind, x, y, w, h, fill=None, line=None, line_w=None):
    sp = s.shapes.add_shape(kind, Inches(x), Inches(y), Inches(w), Inches(h))
    sp.shadow.inherit = False
    if fill is None:
        sp.fill.background()
    else:
        sp.fill.solid(); sp.fill.fore_color.rgb = fill
    if line is None:
        sp.line.fill.background()
    else:
        sp.line.color.rgb = line
        sp.line.width = Pt(line_w or 1)
    return sp

def settext(sp, text, size, color, bold=False, align=PP_ALIGN.LEFT,
            anchor=MSO_ANCHOR.MIDDLE, font=FONT, italic=False):
    tf = sp.text_frame
    tf.word_wrap = True
    tf.auto_size = MSO_AUTO_SIZE.NONE
    tf.vertical_anchor = anchor
    for i, ln in enumerate(text.split("\n")):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.alignment = align
        r = p.add_run(); r.text = ln
        f = r.font
        f.size = Pt(size); f.bold = bold; f.italic = italic
        f.name = font; f.color.rgb = color
    return sp

def textbox(s, x, y, w, h, text, size, color, bold=False, align=PP_ALIGN.LEFT,
            anchor=MSO_ANCHOR.TOP, font=FONT, italic=False):
    tb = s.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    settext(tb, text, size, color, bold, align, anchor, font, italic)
    return tb

def bg(s, color):
    shape(s, MSO_SHAPE.RECTANGLE, -0.1, -0.1, SW + 0.2, SH + 0.2, fill=color)

def footer(s, n):
    shape(s, MSO_SHAPE.RECTANGLE, 0.7, 7.04, 11.93, 0.015, fill=LINE)
    textbox(s, 0.7, 7.08, 7, 0.3, "Industrial DevOps Now  ·  AI-Powered Product Development", 9, GRAY)
    textbox(s, 4.8, 7.08, 4, 0.3, "Mentimeter: menti.com", 9, GRAY, align=PP_ALIGN.CENTER)
    textbox(s, 11.0, 7.08, 1.63, 0.3, str(n), 9, GRAY, align=PP_ALIGN.RIGHT, bold=True)

def accent(s):
    shape(s, MSO_SHAPE.RECTANGLE, 0, 0, 0.16, 7.5, fill=TEAL)

def header(s, title, kicker=None):
    accent(s)
    y = 0.62
    if kicker:
        textbox(s, 0.7, 0.5, 11.5, 0.3, kicker.upper(), 12, GOLD, bold=True)
        y = 0.92
    textbox(s, 0.7, y, 11.9, 0.9, title, 30, TEAL, bold=True)
    shape(s, MSO_SHAPE.RECTANGLE, 0.72, y + 0.82, 1.1, 0.045, fill=GOLD)
    return y + 1.15

def run_pill(s, text):
    p = shape(s, MSO_SHAPE.ROUNDED_RECTANGLE, 9.9, 0.62, 2.73, 0.55, fill=GOLD)
    settext(p, "▶  " + text, 13, INK, bold=True, align=PP_ALIGN.CENTER)

def flow(s, items, x, y, total_w, h, fill_list=None, tcolor=WHITE, fsize=12):
    n = len(items); gap = 0.28
    bw = (total_w - gap * (n - 1)) / n
    cur = x
    for i, it in enumerate(items):
        col = fill_list[i] if fill_list else TEAL
        b = shape(s, MSO_SHAPE.ROUNDED_RECTANGLE, cur, y, bw, h, fill=col)
        settext(b, it, fsize, tcolor, bold=True, align=PP_ALIGN.CENTER)
        if i < n - 1:
            shape(s, MSO_SHAPE.RIGHT_ARROW, cur + bw + 0.03, y + h/2 - 0.11, gap - 0.06, 0.22, fill=GOLD)
        cur += bw + gap

def corner_circles(s):
    shape(s, MSO_SHAPE.OVAL, 11.1, -2.3, 5.6, 5.6, fill=TEAL)
    shape(s, MSO_SHAPE.OVAL, 12.1, 3.9, 4.6, 4.6, fill=TEALL)

# ---------- content slide ----------
def content(n, title, body, kicker=None, pill=None):
    s = slide()
    cy = header(s, title, kicker)
    if pill:
        run_pill(s, pill)
    textbox(s, 0.7, cy, 11.6, 1.6, body, 20, INK)
    footer(s, n)
    return s

# ---------- divider slide ----------
def divider(n, kicker, title, subtitle, badge=None):
    s = slide()
    bg(s, TEALD)
    corner_circles(s)
    textbox(s, 0.8, 0.6, 9, 0.4, "INDUSTRIAL DEVOPS NOW", 14, WHITE, bold=True)
    if badge:
        b = shape(s, MSO_SHAPE.ROUNDED_RECTANGLE, 0.8, 1.7, 3.7, 0.55, fill=GOLD)
        settext(b, badge, 14, INK, bold=True, align=PP_ALIGN.CENTER)
    if kicker:
        textbox(s, 0.82, 2.55, 9, 0.35, kicker.upper(), 13, GOLD, bold=True)
    shape(s, MSO_SHAPE.RECTANGLE, 0.85, 3.0, 1.6, 0.06, fill=GOLD)
    textbox(s, 0.8, 3.2, 10.0, 1.8, title, 40, WHITE, bold=True)
    textbox(s, 0.8, 4.9, 9.3, 1.4, subtitle, 20, SUB)
    textbox(s, 0.8, 7.05, 2, 0.3, str(n), 10, SUB, bold=True)
    return s

# ---------- menti slide ----------
def menti(n, pollno, kind, question):
    s = slide()
    bg(s, LIGHT)
    accent(s)
    b = shape(s, MSO_SHAPE.ROUNDED_RECTANGLE, 0.7, 0.75, 4.0, 0.6, fill=GOLD)
    settext(b, "▶  MENTIMETER  ·  POLL " + str(pollno), 14, INK, bold=True, align=PP_ALIGN.CENTER)
    textbox(s, 0.72, 1.65, 11, 0.4, kind.upper(), 13, GRAY, bold=True)
    textbox(s, 0.7, 2.4, 8.7, 2.6, question, 30, TEAL, bold=True)
    qr = shape(s, MSO_SHAPE.RECTANGLE, 10.1, 2.5, 2.3, 2.3, fill=WHITE, line=TEAL, line_w=1.5)
    settext(qr, "QR\njoin code", 13, GRAY, align=PP_ALIGN.CENTER)
    textbox(s, 0.7, 5.3, 9, 0.6, "Join at menti.com — enter the code shown on screen.", 16, INK)
    footer(s, n)
    return s

# =================== BUILD ===================

# 1 — Title
s = slide()
bg(s, TEALD)
corner_circles(s)
textbox(s, 0.85, 0.7, 9, 0.4, "INDUSTRIAL DEVOPS NOW", 15, WHITE, bold=True)
shape(s, MSO_SHAPE.RECTANGLE, 0.9, 2.45, 1.7, 0.07, fill=GOLD)
textbox(s, 0.85, 2.65, 9.8, 2.0, "AI-Powered Product Development", 46, WHITE, bold=True)
textbox(s, 0.85, 4.55, 8.8, 1.3,
        "Building Better Automotive Products with Smaller, Faster, Cross-Functional Teams", 22, SUB)
textbox(s, 0.85, 6.5, 10, 0.5, "A 90-minute hands-on workshop", 15, GOLD, bold=True)

# 2 — Why we're here
content(2, "Why we're here",
        "A tired driver drifts toward the lane line. Could the car notice — and help?\n\n"
        "Today, building that one feature takes many teams and many months.",
        kicker="Act 1 · Why product development is slow")

# 3 — Objectives (chips)
s = slide()
cy = header(s, "Workshop objectives", "Act 1 · Why product development is slow")
chips = ["Smaller teams", "Faster iteration", "Better traceability", "Outcome-focused delivery"]
cx, cyy, cw, ch, gap = 0.7, cy + 0.3, 5.7, 1.3, 0.5
for i, c in enumerate(chips):
    x = cx + (i % 2) * (cw + gap)
    y = cyy + (i // 2) * (ch + gap)
    b = shape(s, MSO_SHAPE.ROUNDED_RECTANGLE, x, y, cw, ch, fill=LIGHT, line=LINE, line_w=1)
    settext(b, c, 22, TEAL, bold=True, align=PP_ALIGN.CENTER)
footer(s, 3)

# 4 — Poll 1
menti(4, 1, "Multiple choice",
      "Where does your organization spend the most engineering effort?")

# 5 — Automotive development today
content(5, "Automotive development today",
        "Specialized functions create handoffs, delays, and rework.",
        kicker="Act 1 · Why product development is slow")

# 6 — The cost of handoffs (chain)
s = slide()
cy = header(s, "The cost of handoffs", "Act 1 · Why product development is slow")
textbox(s, 0.7, cy, 11.6, 0.6, "Every handoff between specialized functions adds delay and a chance for rework.", 18, INK)
flow(s, ["Requirements", "Systems", "Architecture", "Development", "Test", "Release"],
     0.7, 3.7, 11.93, 1.05, fill_list=shades(6), fsize=12)
footer(s, 6)

# 7 — Poll 2
menti(7, 2, "Word cloud", "What slows product delivery the most today?")

# 8 — Why specialization exists
content(8, "Why specialization exists",
        "Risk reduction, compliance, and deep expertise — good reasons that no longer scale alone.",
        kicker="Act 2 · What AI changes")

# 9 — AI as capability amplification
content(9, "AI as capability amplification",
        "AI makes expertise available at the point of need — it augments specialists, not replaces them.",
        kicker="Act 2 · What AI changes")

# 10 — Future-state team (nodes)
s = slide()
cy = header(s, "Future-state team", "Act 2 · What AI changes")
textbox(s, 0.7, cy, 11.6, 0.6, "A small, cross-functional team does what used to need six.", 18, INK)
nodes = [("Product Owner", TEAL, WHITE), ("Engineers", TEAL, WHITE), ("AI Copilot", GOLD, INK)]
nx, ny, nw, nh = 1.1, 3.7, 3.2, 1.3
for i, (label, fill, tc) in enumerate(nodes):
    x = nx + i * (nw + 0.85)
    b = shape(s, MSO_SHAPE.ROUNDED_RECTANGLE, x, ny, nw, nh, fill=fill)
    settext(b, label, 20, tc, bold=True, align=PP_ALIGN.CENTER)
    if i < len(nodes) - 1:
        textbox(s, x + nw, ny, 0.85, nh, "+", 30, TEAL, bold=True, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
textbox(s, 0.7, 5.4, 11.6, 0.5, "One small, cross-functional product team.", 16, GRAY, italic=True)
footer(s, 10)

# 11 — Scenario divider
divider(11, "Act 3 · Live DMS exercise", "Driver Monitoring System",
        "Detect drowsy, distracted, or medical-emergency states — and respond safely.",
        badge="THE LIVE EXERCISE")

# 12 — Customer need
content(12, "Customer need",
        "Protect a tired or distracted driver — without constant false alarms.",
        kicker="Act 3 · Live DMS exercise")

# 13 — Step 1 Requirements
content(13, "Step 1 — Requirements",
        "Generate stakeholder needs, requirements, constraints, and acceptance criteria.",
        kicker="Act 3 · Live DMS exercise", pill="Run Prompt 1")

# 14 — Step 2 Architecture (flow)
s = slide()
cy = header(s, "Step 2 — Architecture", "Act 3 · Live DMS exercise")
run_pill(s, "Run Prompt 2")
textbox(s, 0.7, cy, 11.6, 0.6, "From sensing to a safe response — the system in one line.", 18, INK)
flow(s, ["Sensors\n(camera / IR)", "AI Perception", "Decision Logic", "HMI + Vehicle"],
     0.7, 3.7, 11.93, 1.2, fill_list=shades(4), fsize=14)
footer(s, 14)

# 15 — Step 3 Model
content(15, "Step 3 — Model (SysML v2)",
        "A structured, readable design that traces back to the requirements.",
        kicker="Act 3 · Live DMS exercise", pill="Run Prompt 3")

# 16 — Step 4 Tests
content(16, "Step 4 — Tests & traceability",
        "Functional, edge, and negative test cases — plus a requirements-to-test matrix.",
        kicker="Act 3 · Live DMS exercise", pill="Run Prompt 4")

# 17 — Poll 3
menti(17, 3, "Multiple choice", "Which SDLC activity benefited most from AI so far?")

# 18 — Step 5-6
content(18, "Step 5–6 — Implementation & verification",
        "Detect-assess-respond logic, then a pass/fail review against the requirements.",
        kicker="Act 3 · Live DMS exercise", pill="Run Prompts 5–6")

# 19 — Step 7 Deployment
content(19, "Step 7 — Deployment",
        "OTA rollout, shadow mode, monitoring, and rollback.",
        kicker="Act 3 · Live DMS exercise", pill="Run Prompt 7")

# 20 — Digital thread (flow)
s = slide()
cy = header(s, "The digital thread", "Act 4 · What just happened")
textbox(s, 0.7, cy, 11.6, 0.6, "One connected, auditable trail — created by a single team in minutes.", 18, INK)
flow(s, ["Need", "Requirement", "Design", "Test", "Code", "Deploy"],
     0.7, 3.7, 11.93, 1.05, fill_list=shades(6), fsize=13)
footer(s, 20)

# 21 — Timeline comparison (bars)
s = slide()
header(s, "Traditional vs. AI-enabled timeline", "Act 4 · What just happened")
# traditional
textbox(s, 0.7, 2.7, 2.6, 0.5, "Traditional", 16, TEAL, bold=True, anchor=MSO_ANCHOR.MIDDLE)
b1 = shape(s, MSO_SHAPE.ROUNDED_RECTANGLE, 3.3, 2.65, 9.0, 0.85, fill=TEAL)
settext(b1, "Months — sequential handoffs across teams", 15, WHITE, bold=True, align=PP_ALIGN.CENTER)
# ai-enabled
textbox(s, 0.7, 4.3, 2.6, 0.5, "AI-Enabled", 16, GOLD, bold=True, anchor=MSO_ANCHOR.MIDDLE)
b2 = shape(s, MSO_SHAPE.ROUNDED_RECTANGLE, 3.3, 4.25, 2.6, 0.85, fill=GOLD)
settext(b2, "Hours", 15, INK, bold=True, align=PP_ALIGN.CENTER)
textbox(s, 6.05, 4.3, 6, 0.7, "— one small team", 15, INK, anchor=MSO_ANCHOR.MIDDLE)
textbox(s, 0.7, 5.6, 11.6, 0.6, "Same rigor. A fraction of the calendar time.", 16, GRAY, italic=True)
footer(s, 21)

# 22 — Humans in the loop
content(22, "Where humans stayed in the loop",
        "Confidence thresholds · safety aggressiveness · bias checks · accountability.\n\n"
        "AI assisted. People decided.",
        kicker="Act 4 · What just happened")

# 23 — Poll 4
menti(23, 4, "Ranking", "Where would you pilot AI first?")

# 24 — Future operating model
content(24, "Future operating model",
        "Outcome-oriented product teams, with specialists providing governance, standards, "
        "reviews, and exception handling.",
        kicker="Act 5 · Future-state organization")

# 25 — Key takeaways (cards)
s = slide()
cy = header(s, "Key takeaways", "Act 5 · Future-state organization")
cards = ["Smaller teams", "Faster learning", "Better outcomes"]
cw, ch, gap = 3.7, 1.6, 0.45
cx = 0.7
for i, c in enumerate(cards):
    x = cx + i * (cw + gap)
    b = shape(s, MSO_SHAPE.ROUNDED_RECTANGLE, x, cy + 0.3, cw, ch, fill=shades(3)[i])
    settext(b, c, 22, WHITE, bold=True, align=PP_ALIGN.CENTER)
textbox(s, 0.7, cy + 2.3, 11.6, 0.6, "Humans remain accountable throughout.", 18, INK, bold=True)
footer(s, 25)

# 26 — Closing + Poll 5
divider(26, "Act 5 · Closing", "What is the biggest opportunity?",
        "Closing Mentimeter poll, then open Q&A.  Join at menti.com.",
        badge="▶ POLL 5  ·  Q&A")

out = "AI-Powered-Product-Development_DMS.pptx"
prs.save(out)
print("Saved", out, "with", len(prs.slides._sldIdLst), "slides")
