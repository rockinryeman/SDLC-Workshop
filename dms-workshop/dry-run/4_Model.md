# Prompt 4 · Model the System (SysML v2)

*(Still Phase 3 — Architecture / Design — on the deck's breadcrumb.)*

## INPUT (prompt)
> Using the architecture, generate a simple SysML v2 textual model: requirements · actions
> (DetectDrowsiness, AssessConfidence, TriggerResponse) · interfaces/flows · major system elements.
> Focus on readability, not tool-specific correctness.

## OUTPUT (AI result)
```
package DriverMonitoringSystem {
  requirement REQ_F_01;        // detect drowsiness in time
  requirement REQ_F_04;        // suppress false alarms

  part sensors;  part perception;  part decisionLogic;  part hmi;  part vehicleIf;

  action DetectDriverState  { in CabinFrames;   out StateEstimate; }
  action AssessConfidence   { in StateEstimate; out GatedState; }     // satisfies REQ_F_04
  action TriggerResponse    { in GatedState;    out ResponseCommand; } // satisfies REQ_F_03

  flow CabinFrames     from sensors to perception;
  flow StateEstimate   from perception to decisionLogic;
  flow ResponseCommand from decisionLogic to hmi, vehicleIf;
}
```

## 🔗 Chain check
`part`s mirror the architecture components; `action`s `satisfy` REQ IDs. **Architecture → Model:
connected.**

**Ask the room:** *What should we watch for?*
