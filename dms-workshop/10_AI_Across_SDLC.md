# AI Across the SDLC — the seven phases

The framework behind the workshop: AI shows up at **every** phase of the software/systems
lifecycle, not just coding. Each phase below has a short description, where AI helps, and how it
appears in the live DMS exercise.

> Flow: **Plan → Analyze → Design → Develop → Test → Deploy → Operate**

---

## 1. Plan
*Decide what to build and when — vision, roadmap, requirements, and how they trace.*

**AI impacts**
- Requirement analysis
- Generate user stories
- Requirements traceability
- Develop roadmaps
- Dynamically adapt based on changing constraints

**In the DMS exercise:** Prompt 1 frames the DMS need and generates the initial requirements and
acceptance criteria.

## 2. Analyze
*Turn stakeholder needs into clear, validated functional requirements and a groomed backlog.*

**AI impacts**
- Summarize stakeholder needs
- Sentiment analysis
- Create functional requirements
- Discover new requirements
- Update backlogs

**In the DMS exercise:** the requirements review — "what's missing?" — surfaces gaps and new
requirements live.

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

**In the DMS exercise:** Prompts 2–3 produce the architecture and a SysML v2 model that traces back
to the requirements.

## 4. Develop
*Build it — generate, review, refactor, and explain code.*

**AI impacts**
- Code generation / debug
- Automated code review
- Code explain / commenting
- Refactoring
- Code translation
- Autonomous code agents

**In the DMS exercise:** Prompt 5 produces **runnable code** for the detect-assess-respond loop
(see the [simulation](simulation/)) — not just pseudocode.

## 5. Test
*Prove it works — generate and optimize tests, simulate scenarios, triage failures.*

**AI impacts**
- Test case optimization
- Unit / integration / regression generation
- Simulate multiple scenarios
- Triage failure
- Open bugs, generate rollback / fix

**In the DMS exercise:** Prompt 4 generates the test cases + traceability matrix; Prompt 6 reviews
them; the [pytest suite](simulation/test_dms.py) runs them live (green/red).

## 6. Deploy
*Release it safely — pipelines, infrastructure as code, monitored rollout, auto-fix.*

**AI impacts**
- Optimize release timing
- CI/CD pipelines
- Infrastructure as code
- Monitor pipeline
- Dynamically reconfigure resources
- Auto-fix failed builds

**In the DMS exercise:** Prompt 7 produces the OTA deployment, rollback, and monitoring plan.

## 7. Operate
*Run and improve it — detect anomalies, monitor performance, analyze feedback, patch.*

**AI impacts**
- Anomaly detection
- Feedback analysis
- Performance monitoring
- Incident reports
- Remediation runbooks
- Proactively patch vulnerabilities

**In the DMS exercise:** the deployment monitoring metrics (detection accuracy, false-alarm rate,
driver-trust signals) feed the operate loop — and close back to Plan as new requirements.

---

## The point
One small, AI-augmented team can move across **all seven phases** — not hand off between seven
siloed teams. The DMS live exercise walks this whole loop in minutes, and the
[simulation](simulation/) proves the Develop → Test phases actually run.
