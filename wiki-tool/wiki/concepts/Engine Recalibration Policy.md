---
type: concept
sources:
  - "[[Wood Yao Haisfield Lottridge 2021 - Standards of Best Practice in Automated Scoring]]"
created: "2026-04-16"
updated: "2026-04-16"
status: current
tags: [automated-scoring, recalibration, drift, maintenance, operations]
---

> [!tldr]
> Wood's Standard 10 requires AS programs to establish written policies for when to recalibrate the engine; named triggers are major program or population changes, significant shifts in score-point distributions relative to training, and decay in human-AS agreement rates over time.

## Definition

> [!source] Standard 10 requires recalibration policies.
> "The final core standard is that policies must be established to determine when it is appropriate to recalibrate the engine (Council of Chief State Schools Officers and Association of Test Publishers, 2013)." [[Wood Yao Haisfield Lottridge 2021 - Standards of Best Practice in Automated Scoring]]

> [!analysis] The quoted body-text variant is a typo in Wood.
> Wood's Standard 10 body-text renders the organization as "Council of Chief State **Schools** Officers" (plural, p. 23). Wood's references list and every other occurrence in the paper (including the Standard 9 body) use the canonical "Council of Chief State School Officers" (singular). The wiki preserves Wood's body-text wording verbatim, but the correct organization name is the singular form. Same organization; see [[Alert Paper Detection]] for a separate Wood typo that drops "Officers" entirely.

## The three triggers

**Table 1.** Recalibration triggers named in Wood's Standard 10.

| # | Trigger | Example |
|---|---|---|
| 1 | Major change to program or population | Changing test-takers from 4th graders to 6th graders |
| 2 | Significant shift in human-score point distribution relative to training | Ramping difficulty or changing rubric levels changes the empirical score distribution |
| 3 | Decay in human-AS agreement rates over time | Ongoing monitoring shows agreement trending down |

> [!source] The three triggers are enumerated in the standard text.
> "When there are major changes made to the program or population, it is necessary to recalibrate the engine. For example, changing the population of test-takers from 4th graders to 6th graders would warrant recalibration. Recalibration should also be considered if: the score point distribution (using human scores) changes significantly from the score point distribution of human scores used for training, or the human-AS agreement rates decrease over time." [[Wood Yao Haisfield Lottridge 2021 - Standards of Best Practice in Automated Scoring]]

## Why it matters

> [!source] Without recalibration, models drift.
> "Without this type of maintenance of scoring models, models may become less accurate and not meet performance standards and thresholds previously discussed." [[Wood Yao Haisfield Lottridge 2021 - Standards of Best Practice in Automated Scoring]]

> [!source] CCSSO/ATP specifies regular performance measurement.
> "Al performance results should be measured and analyzed regularly. A process should be established to permit recalibration and/or retraining, as appropriate" (CCSSO & ATP 2013, p. 131, as cited by Wood et al.). [[Wood Yao Haisfield Lottridge 2021 - Standards of Best Practice in Automated Scoring]]

## Key Claims

> [!analysis] Recalibration is the bridge between Standards 6 and 1.
> Process monitoring (Standard 6) produces the data. The Standard-1 thresholds (QWK 0.70 floor, QWK degradation <= 0.10, SMD +/- 0.15, SD ratio 2/3-1.50, exact-agreement difference 5.125%) define the acceptance bounds. Standard 10 connects them: when monitored metrics drift toward those bounds, recalibration is triggered. Without Standard 10, a monitored decay produces reports but no action.

> [!analysis] Two of the three triggers are distribution-shift detectors.
> Population change (Trigger 1) and score-distribution shift (Trigger 2) are covariate-shift and label-shift instances respectively from the machine-learning literature. Agreement decay (Trigger 3) is a performance-monitoring trigger that is downstream of the first two. A well-designed policy could use Triggers 1 and 2 as leading indicators, with Trigger 3 as a lagging backstop.

> [!analysis] Standard 10 leaves magnitude unspecified.
> "Major," "significant," and "decrease" are qualitative. An operational policy needs numeric thresholds — for example, how much score-distribution drift counts as significant, or how many consecutive weeks of agreement decay trigger retraining. Wood references CCSSO/ATP's "regular" measurement but neither source specifies a trigger magnitude.

## Connections

- Standard 10 of [[Automated Scoring Standards of Best Practice]].
- Operationally downstream of [[Process Monitoring in Automated Scoring]] (Standard 6), which feeds the agreement-decay trigger.
- Thresholds that define "out of spec" are carried by [[Human-Automated Score Agreement]] and its component metrics.

## Open Questions

> [!gap] Trigger magnitudes are unspecified.
> Wood does not define "major," "significant," or "decrease" numerically.

> [!gap] Retraining data requirements are unspecified.
> Wood does not discuss how much new labeled data is needed for a recalibration cycle to be valid, or whether partial retraining (fine-tuning on new data) is acceptable versus full rebuild.

> [!gap] Governance of recalibration decisions is unspecified.
> Standards 1-9 sometimes involve psychometric review committees. Standard 10 does not name who owns the recalibration trigger or the approval process for a recalibrated model.
