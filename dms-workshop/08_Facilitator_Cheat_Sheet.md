# Facilitator Cheat-Sheet — Live DMS Exercise (one page)

**Prime the chat once (before Prompt 1):** *"We're running a live workshop. Keep each answer concise and skimmable — bullets over prose."*

Run in a **fresh chat**, in order. Rhythm: **paste → read aloud → ask the room → move on.** Don't perfect anything.

| # | Slide | Prompt (paste) | Ask the room |
|---|-------|----------------|--------------|
| 1 | 13 | Requirements: stakeholder needs, functional + non-functional reqs (latency, accuracy, privacy), constraints, assumptions, acceptance criteria. | What's missing? What would you challenge? |
| 2 | 14 | Architecture: context diagram (text), components (sensors, AI, decision logic, HMI, vehicle), interfaces/data flows, failure modes, safety, privacy/cyber. | Where could this go wrong, and how does it stay safe? |
| 3 | 15 | SysML v2 text model: requirements, actions (DetectDrowsiness, AssessConfidence, TriggerResponse), interfaces/flows, elements. Readability over correctness. | (Non-tech framing) A structured way to write the design — see how it traces to the requirements. |
| 4 | 16 | Tests: verification strategy, functional + edge (sunglasses, darkness, head turned, passenger) + negative (false-positive) cases, requirements-to-test matrix, pass/fail criteria. | Which test would you most want to pass before shipping? |
| 5 | 18 | Implementation: approach, pseudocode for detect-assess-respond loop, logic flow, data steps, assumptions. How it satisfies the requirements. | Notice: idea → logic, no separate dev-team handoff. |
| 6 | 18 | Verification review: which reqs satisfied, which tests pass, defects, risks (false alarms, missed detections), improvements. Pass/fail assessment. | Where does human expertise make the final call? |
| 7 | 19 | Deployment: OTA plan, rollback, monitoring metrics (accuracy, false-alarm rate, trust), release notes, customer impact, success criteria. | How many teams would this normally take? |

## Discussion moments (no tools — show of hands / call-out)
- **Opening:** Where does your org spend the most engineering effort?
- **Setup:** What slows product delivery the most today? (jot on a board)
- **Midpoint:** Which SDLC activity benefited most from AI so far?
- **Future-state:** Where would you pilot AI first?
- **Closing:** What is the biggest opportunity?

## Closing discussion
What surprised you? · What would you challenge before trusting it? · Where is human expertise still required? · How many teams would this traditionally need? · What handoffs did we eliminate? · It's a safety system — what changes that AI helped design it?

## If running long
Skip the SysML step (15 / Prompt 3) or collapse 5–6 into one read. **Never skip Deployment** — the "we reached a release plan" payoff matters.
