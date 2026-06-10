# Evaluation Report — AI-Powered Product Development Prompt Pack (7-stage chain)

> **Method:** the 7-prompt chain was run end-to-end (fresh-chat, fed-forward) **12 times** — across
> 3 model tiers (Opus / Sonnet / Haiku) × 4 reps each. Every run was scored by a rubric judge pinned
> to the worked answer key ([05_DMS_Feature_Package.md](05_DMS_Feature_Package.md)) on five dimensions
> per stage (completeness, credibility, traceability, workshop-fit, hallucination-free), had 3 golden
> threads traced end-to-end, and was independently probed by an adversarial skeptic for fabricated
> rigor / safety errors / broken traceability. 37 agents total.

## Bottom line
**Do not run this pack live as-is.** Across 12 fully-judged runs the headline scores look reassuringly
stable, but that stability hides two failures that happen in *every single run* and that a knowledgeable
audience is most likely to poke at. The workshop's real goal is for the room to believe a small team went
idea → deployment with a traceable, credible thread inside the time box. On craft and traceability the
pack delivers. On the one thing a driver-monitoring safety audience checks first, it fails universally.

## The numbers at a glance
| Model | Reps | Median overall | Worst overall | Live verdict |
|---|---|---|---|---|
| opus | 4 | 4 | 4 | Safest; honest verification; still drops the emergency thread |
| sonnet | 4 | 4 | 4 | Same score, riskier — confidently-wrong fabrications |
| haiku | 4 | 3 | 3 | Not safe — scope collapse + fabricated test results |

Every one of the 12 runs was flagged "would embarrass live."

## The two universal problems

**1. The system never acts when the driver is incapacitated (golden thread T3 = 0% survival).**
In all 12 runs, the system can *detect* a drowsy or unresponsive driver but the response chain dead-ends
at a beep/buzz. There is no safe-stop, no emergency call, no "if the driver doesn't respond, do something"
logic — no requirement, no architecture, no code branch, no test. It dies at Planning/Requirements because
nobody ever writes down "the driver becomes unresponsive" as a scenario. This is the single most important
behaviour of a driver-monitoring system, and it is missing every time. The first expert question — "what
happens when the driver passes out?" — breaks the demo.

**2. The lower tiers fabricate test evidence.**
Haiku (all 4 reps) and sonnet's weaker reps report concrete *measured* results — 96.2% sensitivity,
ROC-AUC 0.915, 99.7% uptime, a completed "6-month pilot" — for tests that were never run in a single-pass
design exercise. Some even mark sub-threshold numbers (84% vs an 85% bar) as PASS. One question — "show me
the test report" — collapses the artifact.

## Golden-thread survival (13 of 36 instances = 36%)
- **T1 (false alarms / trust):** 10/12 — robust. Breaks only on haiku (r1, r3).
- **T2 (distraction <1.5s timing):** 3/12 — survives only on opus (r2, r3) and sonnet (r3). Usually
  dropped because no distraction *timing* requirement is written.
- **T3 (medical-emergency / no-response):** 0/12 — never survives, anywhere. Weakest thread by far.

## Where each stage is weak (systematic, not random)
- **Planning (avg ~4.3):** strong, but omits the emergency scenario (seeding the T3 failure) and invents
  specifics — "Euro NCAP 2026 mandate" (NCAP is voluntary), "30–40% fatality reduction," wrong regulation numbers.
- **Requirements (avg ~3.9):** the break point. T3 and often T2 are dropped here; safety bars get silently
  loosened (TPR 95%→90/85%, false alarms loosened). Traceability columns look great, which *hides* the missing safety requirements.
- **Architecture (avg ~4.2):** clean pipelines, but no emergency/safe-stop vehicle interface, and several
  runs declare "alert-only, no intervention" as a design choice.
- **SysML (avg ~3.8):** weakest stage; omits the response-selection and emergency actions; asserts satisfy-links it doesn't enforce.
- **Implementation (avg ~4.0):** good loops, but recurring latency contradictions and no emergency/low-confidence handling.
- **Verification (avg ~3.6):** highest-variance, the credibility fault line. Opus is honest (CONDITIONAL
  PASS, named defects); haiku fabricates numbers. Missing the attentive-driver negative test, distraction test, and emergency test almost everywhere.
- **Deployment (avg ~4.3):** best traceability (metrics map back to planning), but almost always skips
  shadow mode and sometimes sets rollback gates looser than the requirements.

## What to do
1. **Pin the model to opus.** Same score as sonnet, but it does not fabricate test results and is the only
   tier that carries the distraction thread through. Its worst case is honestly-incomplete, not confidently-wrong.
2. **Patch the prompts (text edits below):** force a named "driver unresponsive" scenario in Planning and a
   full requirement→architecture→code→test→deployment chain for it; ban invented test numbers in Verification;
   pin the numeric targets (<2s / <1.5s latency, ≥95% TPR, <1-per-8h false alarms); require a shadow-mode deployment gate.
3. **Do one dry-run on opus** and confirm T3 now survives and Verification carries no fabricated metrics.

---

## The 9 prompt edits (applied in the v2 prompt pack)

| Stage | Edit | Why |
|---|---|---|
| **Planning** | Require enumerating safety-critical scenarios *as needs*, incl. "driver becomes UNRESPONSIVE after escalation." | T3 died at Planning in all 12 runs — it was never seeded as a need. |
| **Requirements** | Pin targets (<2s drowsiness, <1.5s distraction as separate reqs, ≥95% TPR, <1 FA/8h); require the no-response→safe-stop→emergency requirement; flag deviations. | Runs silently loosened FAR/TPR, collapsed two-tier latency, and omitted the no-response requirement. |
| **Requirements** | Force a bidirectional traceability TABLE (need ↔ requirement ↔ test ID); no orphans. | Orphaned NFRs and hollow "SATISFIED" claims that later stages contradicted. |
| **Architecture** | Specify the vehicle interface for the terminal safe action (safe-stop / emergency call); explicit DESCOPED-WITH-RISK note if omitted. | Runs silently went "alert-only," killing T3 as a hidden design decision. |
| **SysML** | Require SelectResponse + an emergency action; satisfy-links must point to the *enforcing* element. | Weakest stage; omitted those actions and asserted hollow satisfy-links. |
| **Implementation** | Mandate `if confidence<threshold → UNKNOWN, don't act` and `if no_response → initiate_emergency_protocol()`; state detect-to-alert time vs latency budget. | No run had an emergency branch; several lacked a low-confidence guard; latency claims self-contradicted. |
| **Verification** | "Single-pass design review, no tests run — do not invent metrics. Mark each criterion PASS-by-design-review / PENDING-empirical / AT-RISK." Add negative, distraction, and emergency tests + evidence column. | Fabricated results in 6/12 runs; missing TC-004/TC-002/TC-005 everywhere. Lowest hallucination-free score (3.6). |
| **Deployment** | Require a SHADOW MODE gate 0; rollback thresholds no looser than acceptance bars; emergency-path success criterion. | Shadow mode missing in 10/12; rollback gates sometimes looser than the requirements; no emergency criterion. |
| **All stages (priming)** | One skimmable screen per stage; label ungrounded standards/numbers as ASSUMPTION; EU GSR 2019/2144 is the binding mandate, Euro NCAP is voluntary. | Workshop-fit capped at 3–4 (density); hallucinated regulatory rigor in 8/12 runs. |

---

## Round 2 — v2 prompts (after the 9 edits)

Re-ran the identical evaluation (12 runs, same judge/rubric/threads) on the patched prompts.

| Metric | v1 (baseline) | v2 (9 edits) |
|---|---|---|
| Golden-thread survival (judge) | 36% | **89%** |
| T3 emergency thread *present in artifacts* | 0/12 | ~11/12 |
| Opus overall (median / worst) | 4 / 4 | **5 / 5** |
| Sonnet | 4 / 4 | **5 / 5** |
| Haiku | 3 / 3 | 4 / 3 |
| Fabricated test metrics | 6/12 | mostly gone on Opus/Sonnet; Haiku still slips |
| "Would embarrass live" (skeptic) | 12/12 | 12/12 |

**What the edits fixed:** the emergency scenario is now seeded in Planning and carried as a written
requirement → architecture interface → SysML action → test → deployment criterion in nearly every run.
Verification's "no tests run" taxonomy held across all tiers and largely killed fabricated metrics on
Opus/Sonnet. Shadow-mode and pinned targets stuck. Judge scores rose a full point.

**The failure migrated rather than vanished.** The rubric judge gave 8/12 a clean 5/5, but the
adversarial skeptic still flagged a high-severity defect in **all 12** — because the defect *type*
changed. In v1 the emergency path was **missing**; in v2 it is **present and traceable but the *logic*
is fail-dangerous** in ~9/12 runs (e.g. low-confidence/occluded-face `continue` so an unconscious
driver never triggers emergency; single-frame escalation reset; eCall gated behind safe-stop
succeeding). Because every stage now *mentions* the emergency path, the judge marks the thread
"intact" while the code doesn't implement the safety control — a subtler, more dangerous failure.
Residual hallucinated-standards (self-chosen latencies branded as binding EU GSR/ADDW; wrong ISO IDs)
persist on weaker tiers.

## Round 3 — v3 prompts (6 logic-hardening edits)

The v2 edits targeted *presence and traceability*; the remaining problem is *logic correctness*. Six
further edits were applied (and a full 3-model × 4-rep re-run launched to confirm):

| Stage | v3 edit |
|---|---|
| **Implementation** | Explicit FAIL-SAFE RULES: sustained UNKNOWN/low-confidence must escalate on its own timeout (never silently continue); escalation resets only after N *consecutive* attentive frames; emergency fires on non-response *regardless of confidence* and *independent of safe-stop success*; driver-cancelable abort window traced to a test. |
| **Planning / priming** | Cite a regulation only with its real acceptance criterion; tag self-chosen numbers as SELF-IMPOSED DESIGN TARGET; write STANDARD-REF-TBD when unsure rather than guessing. |
| **Requirements** | Force a *rendered* traceability table (not an assertion); every safety-critical action (safe-stop misfire, eCall, bias-before-release, logging) needs its own AC **and** its own negative/misfire test. |
| **SysML** | A satisfy-link is invalid unless its target appears as source/sink of a declared data flow — no binding the terminal-safety requirement to an unwired action. |
| **Verification** | No PASS-wording on any untested safety-critical/irreversible action; use REVIEWED-NO-DEFECT-FOUND vs UNVERIFIED-PENDING-TEST and re-trace each verdict against the actual code. |
| **Deployment** | All metric/dashboard values must be ILLUSTRATIVE/SYNTHETIC placeholders; never state fleet size, accuracy %, or crash reduction as observed. |
| **All (priming)** | ≤5-line summary box per stage; ≤2 tables; no ASCII diagrams; ASCII-only (workshop-fit). |

**Workshop-design takeaway:** rather than presenting a "perfect" chain an expert then breaks, have the
room **play skeptic** and hunt the emergency-logic / traceability hole — more credible and more memorable.

*Generated by repeated runs of a 37-agent evaluation workflow (`eval-prompt-pack`); v3 results pending.*
