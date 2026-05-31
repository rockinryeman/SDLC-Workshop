# Facilitator Cheat-Sheet — Live DMS Exercise (one page, synced to deck)

**Prime the chat once (before Prompt 1):** *"We're running a live workshop. Keep each answer concise and skimmable — bullets over prose."*

Fresh chat, in order. Rhythm: **paste → read aloud → ask the room → move on.** Phases match the deck slides.

| # | Phase | Paste | Ask the room |
|---|-------|-------|--------------|
| 1 | **Planning** | Product vision, business case (why now), stakeholders, capability roadmap (MVP→later), risks/constraints, traceability approach. | What's missing? What would you challenge? |
| 2 | **Requirements** | Design a DMS (drowsy/distracted/medical) — generate stakeholder needs, functional + non-functional reqs (latency, accuracy, privacy), constraints, acceptance criteria. | What's missing? What would you challenge? |
| 3 | **Architecture / Design** | Concise architecture: context, components (sensors, AI, decision logic, HMI, vehicle), interfaces/data flows, failure modes, safety, privacy/cyber. | Where could this go wrong, and how does it stay safe? |
| 4 | **Model** | SysML v2 textual model: requirements, actions (DetectDrowsiness, AssessConfidence, TriggerResponse), interfaces/flows, elements. Readability over correctness. | What should we watch for? |
| 5 | **Implementation** | Implementation approach, pseudocode for detect-assess-respond loop, logic flow, assumptions; explain how it satisfies the requirements. *(Optional: ask for runnable Python + run it.)* | Idea → logic, no separate dev-team handoff. |
| 6 | **Verification** | Review the implementation: requirements satisfied, tests that would pass, defects, risks (false alarms, missed detections), improvements; pass/fail. *(Optional: generate + run pytest.)* | Where does human expertise make the final call? |
| 7 | **Deployment** | OTA rollout + rollback, monitoring metrics (accuracy, false-alarm rate, trust), release notes, customer impact, success criteria. | How many teams would this normally take? |

## Discussion moments (no tools — show of hands / call-out)
- **Opening:** Where does your org spend the most engineering effort?
- **Setup:** What slows product delivery the most today? (jot on a board)
- **Midpoint:** Which SDLC phase benefited most from AI so far?
- **Future-state:** Where would you pilot AI first?
- **Closing:** What is the biggest opportunity?

## Closing discussion
What surprised you? · What would you challenge before trusting it? · Where is human expertise still required? · How many teams would this traditionally need? · What handoffs did we eliminate?

## If running long
Collapse **Model** into Architecture, or skip the optional code/test runs. **Never skip Planning or Deployment** — they bookend the "idea → deployable as one team" story.
