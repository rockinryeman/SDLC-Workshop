# 90-Minute Workshop Plan — DMS Edition

**Theme:** GenAI enables smaller, cross-functional teams to design better automotive products
faster — without losing engineering rigor.

**Scenario:** Driver Monitoring System (detect drowsy / distracted / medical-emergency states
and respond safely).

**Audience:** Mixed, leaning non-technical (~15–30, executives present).

**Interaction:** Live discussion / show-of-hands moments throughout (see Discussion Prompts, file 04).

---

## Workshop thesis

AI is not just a productivity tool. It changes *how product teams work* — making expertise
available at the point of need, reducing dependency on functional silos, and enabling faster
iterative delivery while keeping humans accountable for safety.

## Story arc (5 acts)

1. **Why product development is slow** — handoffs, silos, months of coordination.
2. **What AI changes** — expertise on demand; small teams; compressed lifecycle.
3. **Live exercise** — one team takes a DMS feature through the whole lifecycle in minutes.
4. **What just happened** — reflect on the handoffs we skipped and where humans still matter.
5. **Future-state organization** — what this means for how we staff and govern product teams.

---

## Agenda at a glance

| Time | Segment | Interaction |
|------|---------|------------|
| 0–10 min | Why automotive development is slow | **Show of hands:** Where do we spend the most effort? |
| 10–20 min | AI and team transformation | **Call-out:** What slows delivery most today? |
| 20–55 min | **Live DMS exercise** (the core) | **Quick poll by hands:** Which step surprised you most? |
| 55–70 min | Traceability & digital engineering | — (show the digital thread we just created) |
| 70–85 min | Future-state team design | **Rank by discussion:** Where would you pilot AI first? |
| 85–90 min | Takeaways & discussion | **Call-out:** Biggest opportunity? |

---

## Detailed run sheet

### 0–10 min · Why automotive development is slow
- Open with the **drowsy-driver story** (see Scenario Brief). Make it human before it's technical.
- **▶ Show of hands (Opening):** *"Where does your organization spend the most engineering effort?"*
  Requirements / Architecture / Development / Testing / Compliance & Documentation
- Land the point: specialization exists for good reasons (risk, compliance, expertise) but
  creates handoffs, delays, and rework.

### 10–20 min · AI and team transformation
- Traditional team (Requirements → Systems → Architecture → Dev → Test → Release) vs.
  AI-augmented team (small cross-functional team + AI copilot).
- **▶ Call-out:** *"What slows product delivery the most today?"* (jot answers on a board)
- Frame the exercise: "We're going to be that small team — for a Driver Monitoring System."

### 20–55 min · Live DMS exercise  ⭐ the centerpiece
Run the **Prompt Book** (separate file) live on screen — six SDLC phases, each building on the last:
1. **Plan** — vision, stakeholder needs, roadmap, risks
2. **Analyze** — requirements spec + acceptance criteria; find gaps
3. **Design** — architecture + SysML v2 model (traces to requirements)
4. **Develop** — runnable code for the detect-assess-respond loop
5. **Test** — pytest run (green/red) + scenario simulation
6. **Deploy** — OTA rollout, rollback, monitoring plan

> For **Develop** and **Test**, use a tool that can run code (Code Interpreter / Claude / Jupyter),
> or fall back to the runnable reference in `simulation/`.

Facilitation rhythm for each step: **prompt → read output aloud → ask the room "what would you
challenge?" → move on.** Don't perfect the output; momentum is the point.
- **▶ Quick poll by hands (Midpoint):** *"Which SDLC activity benefited most from AI so far?"*
  Requirements / Architecture / Testing / Implementation / Deployment

### 55–70 min · Traceability & digital engineering
- Walk the **digital thread** you just produced: Need → Requirement → Design → Test → Code → Deploy.
- Show the requirements-to-test traceability matrix from the exercise.
- Point: the small team didn't just move fast — it left a connected, auditable trail.

### 70–85 min · Future-state team design
- Old operating model (sequential specialist handoffs) vs. future (outcome-oriented product
  teams with specialist oversight for governance, standards, reviews, exceptions).
- **▶ Rank by discussion:** *"Where would you pilot AI first?"*
  Systems Engineering / Software Development / Test Engineering / Program Management / Operations

### 85–90 min · Takeaways & discussion
- Three takeaways: **smaller teams · faster learning · better outcomes** — humans stay accountable.
- **▶ Closing call-out:** *"What is the biggest opportunity?"*
  Smaller teams / Faster delivery / Better quality / Lower cost / More innovation
- Close on the DMS story: "We just took a feature that protects a tired driver from idea to
  deployment plan — as one small team, in minutes. Imagine this across your whole portfolio."

---

## Facilitator reminders
- Keep steering "cool AI" tangents back to **systems thinking and safety**.
- If the room is non-technical and the SysML step lands flat, narrate it as *"this is just a
  structured way of writing down the design so a machine and a human can both read it"* and move on.
- Watch the clock on the live exercise — it's the easiest place to lose 15 minutes.
- Keep the interaction lightweight — a show of hands or quick call-out is enough to keep energy up.
