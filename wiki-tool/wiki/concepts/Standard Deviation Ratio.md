---
type: concept
sources:
  - "[[Wood Yao Haisfield Lottridge 2021 - Standards of Best Practice in Automated Scoring]]"
created: "2026-04-16"
updated: "2026-04-16"
status: current
tags: [statistics, automated-scoring, agreement, variance]
---

> [!tldr]
> The standard deviation ratio is a Standard-1 accuracy metric that requires the ratio of human to automated score standard deviations to fall within 2/3 and 1.50, guarding against an AS engine that compresses or inflates score variance relative to human raters; the metric is attributed to Wang and von Davier (2014).

## Definition

> [!source] Wood codifies the SD-ratio threshold with Wang & von Davier (2014) as the primary reference.
> Wood's Table 2 specifies "2/3 <= (SD_Human / SD_AS) <= 1.50," with the reference given as "Wang & von Davier (2014)." [[Wood Yao Haisfield Lottridge 2021 - Standards of Best Practice in Automated Scoring]]

> [!analysis] The ratio is symmetric in multiplicative form.
> The 2/3 lower bound and 1.50 upper bound are multiplicative reciprocals (2/3 = 1 / 1.50). The threshold flags a 50% distortion in either direction: an AS engine whose scores are more than 50% too variable or more than 33% too compressed relative to human scores is out of range. This symmetric framing makes the bound invariant to which rater is in the numerator — flipping the ratio flips the bound but not the flagging decision.

## Why it matters

> [!source] Variance differences are a separate failure mode from mean shift.
> Wood lists SD ratio alongside SMD in the Standard 1 accuracy-metrics table. Where SMD catches mean-center mismatch, the SD ratio catches spread mismatch. [[Wood Yao Haisfield Lottridge 2021 - Standards of Best Practice in Automated Scoring]]

> [!analysis] SD ratio closes a gap that Williamson 2012 left open.
> Williamson, Xi, & Breyer (2012) discusses variance differences but explicitly does not specify a threshold: "we do not have a strict rule of thumb for what constitutes a large difference. Judgments about the acceptability of variance differences are made case by case by a technical review committee at ETS." Wang & von Davier (2014), as cited by Wood, provides the quantitative rule that Williamson's technical review committee approximates. See [[Standardized Mean Score Difference]] for the Williamson variance note.

## Key Claims

> [!source] The metric sits in the absolute-threshold family.
> The 2/3 and 1.50 bounds are constants, not comparisons to human-human values. This places SD ratio in the absolute bucket of [[Absolute vs Relative Thresholds in Automated Scoring]]. [[Wood Yao Haisfield Lottridge 2021 - Standards of Best Practice in Automated Scoring]]

> [!analysis] Regression-based engines typically compress variance.
> e-rater-style regression models tend to regress predicted scores toward the training-set mean, which compresses predicted-score variance relative to human-score variance. That pushes SD_H / SD_AS above 1 toward the 1.50 ceiling. The SD-ratio flag thus acts as a shrinkage check in a way that SMD does not: a regression model can be zero-mean-biased (SMD near zero) while still over-compressed (SD ratio near 1.50).

## Connections

- One of five metrics in [[Automated Scoring Standards of Best Practice]] Standard 1.
- Classified absolute under [[Absolute vs Relative Thresholds in Automated Scoring]].
- Complements [[Standardized Mean Score Difference]] (center) and [[Quadratic-Weighted Kappa]] (agreement).
- Wang & von Davier (2014) is cited in Wood's Standard 6 context as well, for live monitoring via [[Process Monitoring in Automated Scoring]].

## Open Questions

> [!gap] Wood does not reproduce Wang & von Davier's empirical justification.
> The 2/3 / 1.50 bounds are stated without the Wang & von Davier rationale being summarized. Ingesting Wang & von Davier (2014) directly would fill this.

> [!gap] Sensitivity to scale range is not discussed.
> A 50% distortion on a 6-point essay rubric and a 50% distortion on a 2-point short-answer rubric differ operationally. Wood does not discuss how the SD-ratio threshold interacts with scale length.
