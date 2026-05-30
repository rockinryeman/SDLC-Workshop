# Scenario Brief — Driver Monitoring System (DMS)

**Workshop:** GenAI for MBSE — AI-Powered Product Development
**Use Case:** Driver Monitoring System (Use Case 2)
**Audience:** Mixed, leaning non-technical (~15–30 people, executives present)
**Duration:** 90 minutes

---

## The story (say this out loud, no jargon)

> It's late. A driver has been on the highway for three hours. Their eyes start to droop,
> their head dips, they drift toward the lane line. **Could the car notice — and help —
> before anything goes wrong?**

That's the Driver Monitoring System: an in-vehicle system that watches for signs the driver
is **drowsy, distracted, or having a medical emergency**, and decides how the car should respond —
a gentle alert, a stronger warning, or in the worst case, helping bring the vehicle to safety.

Everyone in the room has felt tired behind the wheel. That's why this scenario works: **no
engineering background is needed to care about it or have an opinion.**

## Why we picked this one

- **Instantly relatable** — it's a human problem, not a technical one.
- **Clear value** — safety and trust, things executives and customers both care about.
- **Great discussion fuel** — "Do you trust the car to judge *your* state?" sparks ethics,
  trust, and explainability conversations anyone can join.
- **Still a real systems problem** — sensors, AI, decision logic, human-machine interaction,
  and safety all have to work together. Perfect for showing how GenAI helps a small team
  reason through the whole thing.

## What we're really demonstrating

The point of the live exercise is **not** to build a real DMS. It's to show that **one small,
mixed team — guided by GenAI — can travel the entire product development lifecycle in minutes**,
producing work that traditionally takes many specialized teams and months of handoffs:

needs → requirements → architecture → model → tests → implementation → verification → deployment

## Scope dial (keep it controlled)

| If the room is... | Then... |
|---|---|
| Engaged and moving fast | Stay broad — the full driver-monitoring system |
| Getting overwhelmed | Zoom in to **fatigue detection only** |
| Wanting depth | Zoom into **decision logic / escalation strategy** or **HMI (how the car talks to the driver)** |

## The watch-out

DMS can pull the conversation toward "cool AI" and away from systems thinking. As facilitator,
keep gently steering back to: *"Okay — and what does the rest of the system need for that to
work safely?"* (sensors, fallbacks, how we'd test it, what happens when it's wrong).

## Three human moments to land

1. **Detection** — how does the car even *know* you're impaired? (signals, not mind-reading)
2. **Judgment** — how sure should it be before it acts? (false alarms erode trust)
3. **Response** — what should it actually *do*, and who's still responsible? (human accountability)
