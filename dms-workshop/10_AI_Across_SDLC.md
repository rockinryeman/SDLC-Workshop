# AI Across the SDLC — the six phases

The framework behind the workshop: AI shows up at **every** phase of the lifecycle, not just coding.
Each phase below has a short description, where AI helps, and how it appears in the live DMS exercise
(see [03_Prompt_Book.md](03_Prompt_Book.md)).

> Flow: **Plan → Analyze → Design → Develop → Test → Deploy**

---

## 1. Plan
*Decide what to build and when — vision, roadmap, requirements, and how they trace.*

**AI impacts**
- Requirement analysis
- Generate user stories
- Requirements traceability
- Develop roadmaps
- Dynamically adapt based on changing constraints

**DMS exercise → Phase 1 (Plan):** frame the DMS — vision, stakeholder needs, capability roadmap, risks.

## 2. Analyze
*Turn stakeholder needs into clear, validated functional requirements and a groomed backlog.*

**AI impacts**
- Summarize stakeholder needs
- Sentiment analysis
- Create functional requirements
- Discover new requirements
- Update backlogs

**DMS exercise → Phase 2 (Analyze):** generate the requirements spec + acceptance criteria; surface gaps.

## 3. Design
*Shape the architecture, interfaces, data models, and UX — and validate choices early.*

**AI impacts**
- Architecture writing / analysis
- Create API
- Sequence / flow diagrams
- Generate data models
- UI assist (wireframes, personas, story maps)
- Simulate / validate choices
- Integrate compliance constraints

**DMS exercise → Phase 3 (Design):** architecture + a SysML v2 model that traces to the requirements.

## 4. Develop
*Build it — generate, review, refactor, and explain code.*

**AI impacts**
- Code generation / debug
- Automated code review
- Code explain / commenting
- Refactoring
- Code translation
- Autonomous code agents

**DMS exercise → Phase 4 (Develop):** generate **runnable code** for the detect-assess-respond loop
(see the [simulation](simulation/)) — not just pseudocode.

## 5. Test
*Prove it works — generate and optimize tests, simulate scenarios, triage failures.*

**AI impacts**
- Test case optimization
- Unit / integration / regression generation
- Simulate multiple scenarios
- Triage failure
- Open bugs, generate rollback / fix

**DMS exercise → Phase 5 (Test):** generate pytest, **run it live (green/red)**, and simulate scenarios
(attentive, drowsy, distracted, sunglasses) — traceable to the requirements.

## 6. Deploy
*Release it safely — pipelines, infrastructure as code, monitored rollout, auto-fix.*

**AI impacts**
- Optimize release timing
- CI/CD pipelines
- Infrastructure as code
- Monitor pipeline
- Dynamically reconfigure resources
- Auto-fix failed builds

**DMS exercise → Phase 6 (Deploy):** OTA deployment, rollback, and monitoring plan (accuracy,
false-alarm rate, driver-trust signals) — which feeds back to Plan as new requirements.

---

## The point
One small, AI-augmented team can move across **all six phases** — not hand off between six siloed
teams. The DMS live exercise walks this whole loop in minutes, and the [simulation](simulation/)
proves the Develop → Test phases actually run.
