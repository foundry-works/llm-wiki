---
type: concept
sources:
  - "[[Wood Yao Haisfield Lottridge 2021 - Standards of Best Practice in Automated Scoring]]"
created: "2026-04-16"
updated: "2026-04-16"
status: current
tags: [automated-scoring, agreement, thresholds, evaluation]
---

> [!tldr]
> Wood et al. (2021) frame automated-scoring accuracy evaluation along two threshold types: absolute thresholds compare a metric to a fixed constant (e.g., QWK >= 0.70), and relative thresholds compare a metric to the corresponding human-human value on the same item (e.g., QWK_H,H - QWK_H,AS <= 0.10).

## Definition

> [!source] The absolute-vs-relative distinction is Wood's framing for Standard 1.
> "Numerous publications have identified AS and human scoring metrics suitable for evaluating the reliability and accuracy of AS scoring. Such metrics can be evaluated via absolute or relative thresholds. Absolute thresholds are used when a metric is compared to a constant value, such as when a human-AS quadratic weighted kappa is compared to 0.70. Relative thresholds are used when a metric is compared to a corresponding human or human-human metric for the item, such as when a human-AS quadratic weighted kappa is compared to the human-human metric." [[Wood Yao Haisfield Lottridge 2021 - Standards of Best Practice in Automated Scoring]]

## Examples across the Standard 1 metrics

**Table 1.** Wood's Table 2 metrics classified by threshold type.

| Metric | Threshold type | Form |
|---|---|---|
| QWK between human and AS (>= 0.70) | Absolute | Compared to the 0.70 constant |
| QWK_H,H - QWK_H,AS <= 0.10 | Relative | Compared to human-human QWK on the same item |
| SMD between human and AS (-0.15 <= SMD <= 0.15) | Absolute | Compared to the +/- 0.15 constants |
| SD ratio (2/3 <= SD_H/SD_AS <= 1.50) | Absolute | Compared to constants |
| EA_H,H - EA_H,AS <= 5.125% | Relative | Compared to human-human exact agreement on the same item |

> [!analysis] The two types answer different questions.
> An absolute threshold asks "is the engine good enough in the population at large?" It is a floor. A relative threshold asks "given how hard this item is for humans, is the engine comparably good?" It is a degradation bound. An engine can clear the absolute floor by a wide margin on an easy item and still fail the relative check, which would indicate the engine is missing something specific to the item's difficulty structure.

> [!analysis] Relative thresholds compensate for item difficulty variance.
> The 0.70 absolute QWK floor is more forgiving on items where human-human QWK is 0.90 than on items where human-human QWK is 0.72. The relative 0.10-degradation rule tightens the criterion on easy items (where 0.80 is a clear failure) while loosening it on hard items (where 0.62 is acceptable when humans only reach 0.72). Together the two types close the loophole either one leaves open. See [[Human-Automated Score Agreement]] for the conjunctive-bundle treatment.

## Key Claims

> [!source] Wood's framing of absolute vs. relative is used as a classification scheme, not a recommendation.
> Wood et al. do not argue that one type is superior; they note that industry uses both. The ten standards do not require any specific relative-vs-absolute mix. [[Wood Yao Haisfield Lottridge 2021 - Standards of Best Practice in Automated Scoring]]

## Connections

- Organizes the metrics in [[Automated Scoring Standards of Best Practice]] Standard 1.
- Applied across [[Quadratic-Weighted Kappa]] (absolute 0.70 and relative 0.10 degradation), [[Standardized Mean Score Difference]] (absolute 0.15), [[Standard Deviation Ratio]] (absolute 2/3 and 1.50), [[Exact Agreement Rate Difference]] (relative 5.125%).
- Informs [[Human-Automated Score Agreement]] as the conjunctive bundle structure.

## Open Questions

> [!gap] Wood does not specify tie-breaking when the two types disagree.
> An engine that passes the absolute floor but fails the relative degradation bound (or vice versa) produces a split verdict. The ten standards do not specify which signal takes precedence or whether both must pass.
