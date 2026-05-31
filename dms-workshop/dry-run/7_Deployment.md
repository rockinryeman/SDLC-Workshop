# Prompt 7 · Deployment

## INPUT (prompt)
> Using the verified implementation, create the deployment plan: OTA & rollback · monitoring metrics
> mapped back to the Success Metrics from Planning · release notes · customer impact · success criteria.

## OUTPUT (AI result)
- **OTA rollout:** shadow-mode → 1% → 10% → 100%, each gate held on live metrics.
- **Rollback:** auto-revert if false-alarm rate breaches SM-2 within 48 h.
- **Monitoring → Planning Success Metrics:**
  - detection accuracy → **SM-1 (≥95%)**
  - false-alarm rate → **SM-2 (<1 / 8 h)**
  - alert latency → **SM-3 (<2 s)**
  - missed-detection events → **SM-4 (zero critical)**
  - + driver override / trust signal
- **Release notes:** new DMS drowsy/distracted detection + emergency escalation; on-device, privacy-safe.
- **Customer impact:** improved safety; expect occasional advisory alerts; no data leaves the vehicle.
- **Success criteria (30 days):** SM-1–SM-4 all met in-field before exiting staged rollout.

## 🔗 Chain check
"Using the verified implementation"; every monitoring metric maps to a Planning **SM-#**, closing the
loop back to Phase 1. **Verification → Deployment → Planning: loop closed.**

**Ask the room:** *We just reached a deployment plan — how many teams would this normally take?*
