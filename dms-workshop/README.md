# DMS Workshop — GenAI for MBSE

A 90-minute workshop showing how GenAI lets a small, cross-functional team take an automotive
feature through the full SDLC — and **run real, working code** — in minutes. Built around the
**Driver Monitoring System** use case (detect drowsy / distracted / medical-emergency drivers and
respond safely), chosen because it's relatable for a mixed, non-technical audience.

> **Slides:** this repo holds the **content and facilitation**, not the deck. Build/upload your own
> presentation (e.g. in **Gamma**). The facilitator guide and prompt book are the source of truth
> for what's on each slide.

## Run order
1. **[01_Scenario_Brief.md](01_Scenario_Brief.md)** — the story and why DMS; read first.
2. **[02_Workshop_Plan.md](02_Workshop_Plan.md)** — 90-min agenda with discussion touchpoints.
3. **[03_Prompt_Book.md](03_Prompt_Book.md)** — the 7 prompts you paste live.
4. **[04_Discussion_Prompts.md](04_Discussion_Prompts.md)** — 5 show-of-hands / discussion moments.
5. **[05_DMS_Feature_Package.md](05_DMS_Feature_Package.md)** — worked "answer key" for prep.
6. **[07_Facilitator_Guide.md](07_Facilitator_Guide.md)** — minute-by-minute script (hold this while running).
7. **[08_Facilitator_Cheat_Sheet.md](08_Facilitator_Cheat_Sheet.md)** — one-page prompt + discussion sheet.
8. **[09_Code_Simulation_Prompts.md](09_Code_Simulation_Prompts.md)** — make the build runnable (code + tests + UI).
9. **[simulation/](simulation/)** — runnable reference DMS (console sim, pytest, Streamlit UI).

**Framework reference:** **[10_AI_Across_SDLC.md](10_AI_Across_SDLC.md)** — the 7 SDLC phases
(Plan → Analyze → Design → Develop → Test → Deploy → Operate), AI impacts at each, and how they map
to the live exercise.

## On the day
- Have the AI tool open in a fresh chat (prime it with the line in the Prompt Book).
- Use a tool that can **run code** (Code Interpreter / Claude / Jupyter) for the simulation steps.
- Pre-test the [simulation](simulation/) so you have a working backup.
- Keep it human first, technical second. Protect the live exercise.
