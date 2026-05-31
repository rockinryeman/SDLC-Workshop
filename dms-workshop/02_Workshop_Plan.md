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
| 0–8 min | Why automotive development is slow | **Show of hands:** Where do we spend the most effort? |
| 8–18 min | AI and team transformation (+ the 6 SDLC phases) | **Call-out:** What slows delivery most today? |
| 18–58 min | **Live DMS exercise** — 6 phases incl. live code (the core) | **Quick poll by hands:** Which phase surprised you most? |
| 58–68 min | Digital thread & traceability recap | — (walk the connected trail we just created) |
| 68–82 min | Future-state team design | **Rank by discussion:** Where would you pilot AI first? |
| 82–90 min | Takeaways & discussion | **Call-out:** Biggest opportunity? |

**Live exercise breakdown (18–58 min, ~40 min):** Plan 6 · Analyze 6 · Design 7 · **Develop 8** · **Test 8** · Deploy 5

---

## Detailed run sheet

### 0–8 min · Why automotive development is slow
- Open with the **drowsy-driver story** (see Scenario Brief). Make it human before it's technical.
- **▶ Show of hands (Opening):** *"Where does your organization spend the most engineering effort?"*
  Requirements / Architecture / Development / Testing / Compliance & Documentation
- Land the point: specialization exists for good reasons (risk, compliance, expertise) but
  creates handoffs, delays, and rework.

### 8–18 min · AI and team transformation
- Traditional team (Requirements → Systems → Architecture → Dev → Test → Release) vs.
  AI-augmented team (small cross-functional team + AI copilot).
- Introduce the **6 SDLC phases** (Plan → Analyze → Design → Develop → Test → Deploy) — see file 10.
- **▶ Call-out:** *"What slows product delivery the most today?"* (jot answers on a board)
- Frame the exercise: "We're going to be that small team — for a Driver Monitoring System."

### 18–58 min · Live DMS exercise  ⭐ the centerpiece (~40 min)
Run the **Prompt Book** (file 03) live on screen — six SDLC phases, each building on the last.
Rhythm per phase: **prompt → read output aloud → ask the room → move on.** Don't perfect anything.

| Phase | Time | What happens |
|-------|------|--------------|
| 1 · Plan | 18–24 (6m) | Vision, stakeholder needs, roadmap, risks |
| 2 · Analyze | 24–30 (6m) | Requirements spec + acceptance criteria; find gaps |
| 3 · Design | 30–37 (7m) | Architecture + SysML model (traces to requirements) |
| 4 · **Develop** | 37–45 (8m) | **Runnable code** for the detect-assess-respond loop — *run it* |
| 5 · **Test** | 45–53 (8m) | **pytest live (green/red)** + scenario simulation |
| 6 · Deploy | 53–58 (5m) | OTA rollout, rollback, monitoring plan |

> For **Develop** and **Test**, use a tool that can run code (Code Interpreter / Claude / Jupyter),
> or fall back to the runnable reference in `simulation/`. **Protect Develop + Test** — the working
> code is the payoff.
- **▶ Quick poll by hands (after Develop):** *"Which SDLC phase benefited most from AI so far?"*
  Plan / Analyze / Design / Develop / Test / Deploy

### 58–68 min · Digital thread & traceability recap
- Walk the **digital thread** you just produced: Need → Requirement → Design → Test → Code → Deploy.
- Tie the **passing tests** back to the requirements — verification is now evidence, not a paragraph.
- Point: the small team didn't just move fast — it left a connected, auditable, *running* trail.

### 68–82 min · Future-state team design
- Old operating model (sequential specialist handoffs) vs. future (outcome-oriented product
  teams with specialist oversight for governance, standards, reviews, exceptions).
- **▶ Rank by discussion:** *"Where would you pilot AI first?"*
  Systems Engineering / Software Development / Test Engineering / Program Management / Operations

### 82–90 min · Takeaways & discussion
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
