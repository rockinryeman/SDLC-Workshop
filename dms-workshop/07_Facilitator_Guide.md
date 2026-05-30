# Facilitator Guide — DMS Workshop

The thing you hold while running it. Timings, what to say, what to do, and how to recover when
things wander. Pairs with the Slide Deck (06) and Prompt Book (03).

**Total:** 90 min · **Audience:** mixed, leaning non-technical · **Tone:** human first, technical second.

---

## Before you start (prep checklist)
- [ ] Read the **Scenario Brief (01)** and **Feature Package (05)** so you know what "good" looks like.
- [ ] Open the AI tool in a fresh chat; paste the priming line: *"We're running a live workshop.
      Keep each answer concise and skimmable — bullets over prose."*
- [ ] Build the 5 **Mentimeter** polls (04); test the join code on your phone.
- [ ] Have the **Prompt Book (03)** open in a separate window for fast copy-paste.
- [ ] Decide your **scope dial** default (full system vs. fatigue-only) — see Scenario Brief.

---

## 0–10 min · Why development is slow  *(Slides 1–6)*

**Say (the hook):** "It's late, a driver's been on the highway for hours, their eyes start to
droop and they drift toward the line. Could the car notice — and help? Building that one feature
today takes many teams and many months. Today we'll do it as one small team, in minutes."

**Do:** Slide 3 — state the four objectives plainly.

**▶ Poll #1 (Slide 4):** launch it, give 60–90 s, react to the top answer live ("Testing — no
surprise, that's where a lot of rework lands").

**Say (land it):** "Specialization exists for good reasons — risk, compliance, expertise. But
every handoff is a delay and a chance for something to get lost."

**Recovery:** if the room is quiet, call on the poll result directly — it gives shy rooms a safe entry.

## 10–20 min · AI and team transformation  *(Slides 7–10)*

**▶ Poll #2 (Slide 7, word cloud):** "What slows delivery the most?" Read 3–4 words aloud as they
appear. This becomes the room's own language — reuse their words for the rest of the session.

**Say:** "AI doesn't replace the specialist. It makes their expertise available *at the moment
you need it* — so a small team can do what used to need six."

**Do:** Slide 10 — set up the exercise: "We're about to *be* that small team, for a Driver
Monitoring System."

## 20–55 min · Live DMS exercise  ⭐  *(Slides 11–19, Prompt Book)*

This is the heart. **Protect this time.** Rhythm for each step:
**paste prompt → read output aloud → ask the room → move on.** Don't perfect anything.

| Min | Slide | Action |
|-----|-------|--------|
| 20–24 | 11–12 | Set the scene: the DMS scenario + customer need |
| 24–29 | 13 | **Prompt 1 — Requirements.** Ask: *"What's missing?"* |
| 29–34 | 14 | **Prompt 2 — Architecture.** Ask: *"Where could this go wrong, how stay safe?"* |
| 34–38 | 15 | **Prompt 3 — SysML model.** Non-tech framing: *"a structured way to write the design down."* |
| 38–43 | 16 | **Prompt 4 — Tests + traceability.** Ask: *"Which test must pass before shipping?"* |
| 43–45 | 17 | **▶ Poll #3 (Midpoint).** Energy reset. |
| 45–51 | 18 | **Prompts 5–6 — Implementation + verification.** Ask: *"Where must a human decide?"* |
| 51–55 | 19 | **Prompt 7 — Deployment.** Ask: *"How many teams would this normally take?"* |

**Recovery — if AI output is weak/odd:** that's a *teaching moment*, not a failure. Say: "See —
this is exactly why we review. What would you change?" Then move on. Don't re-prompt repeatedly.

**Recovery — if running long:** skip the SysML step (15/Prompt 3) or collapse 5–6 into a single
read. Never skip Deployment — the "we reached a release plan" payoff matters.

## 55–70 min · Traceability & digital engineering  *(Slide 20)*

**Do:** Scroll back through the chat and literally point: "Need → here. Requirement → here. Test →
here. Code → here. Deploy → here. It's all connected."

**Say:** "The small team didn't just move fast — it left a connected, auditable trail. In a safety
system, that traceability is everything."

## 70–85 min · Future-state team design  *(Slides 21–24)*

**Do:** Slide 21 — contrast months-of-handoffs vs. hours-with-one-team.

**Say (Slide 22, important for credibility):** "Notice where humans stayed in charge: setting the
confidence threshold, deciding how aggressive the safe-stop is, checking for bias, owning the
outcome. AI assisted. People remained accountable."

**▶ Poll #4 (Slide 23, ranking):** "Where would you pilot AI first?" — moves the room from
"interesting" to "where do *we* start?"

**Say:** "The future team is outcome-oriented — and specialists shift toward governance, standards,
reviews, and the hard exceptions."

## 85–90 min · Takeaways & close  *(Slides 25–26)*

**Say:** "Three things to take with you: smaller teams, faster learning, better outcomes — with
humans accountable throughout."

**▶ Poll #5 (Slide 26, closing):** "What's the biggest opportunity?" Capture the result.

**Close (callback to the hook):** "We just took a feature that protects a tired driver — from idea
to deployment plan — as one small team, in minutes. Now imagine this across your whole portfolio.
That's the opportunity." → Open Q&A.

---

## Quick-reference: facilitator questions (from Prompt Book)
- What surprised you about the output?
- What would you challenge before trusting it?
- Where would human expertise still be required?
- How many teams would this traditionally involve?
- What handoffs did we just eliminate?
- It's a safety system — what changes for you that AI helped design it?

## If you only remember three things
1. **Keep it human** — the drowsy-driver story carries a non-technical room.
2. **Protect the live exercise** — it's the proof; everything else is framing.
3. **Always return to accountability** — execs need to hear humans stay responsible.
