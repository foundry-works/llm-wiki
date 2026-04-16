---
type: concept
sources:
  - "[[Wood Yao Haisfield Lottridge 2021 - Standards of Best Practice in Automated Scoring]]"
created: "2026-04-16"
updated: "2026-04-16"
status: current
tags: [statistics, automated-scoring, agreement, exact-agreement]
---

> [!tldr]
> The exact agreement rate difference is a Standard-1 relative accuracy metric: the human-human exact agreement rate minus the human-AS exact agreement rate must not exceed 5.125 percentage points; the metric is attributed to McGraw-Hill Education CTB (2014) and Pearson & ETS (2015).

## Definition

> [!source] Wood codifies the threshold with CTB and Pearson/ETS as primary references.
> Wood's Table 2 specifies "EA_Human,Human - EA_Human,AS <= 5.125%," with the reference given as "McGraw-Hill Education CTB (2014); Pearson & ETS (2014)." (The year typo in Wood is likely "Pearson & ETS 2015" based on the references list.) [[Wood Yao Haisfield Lottridge 2021 - Standards of Best Practice in Automated Scoring]]

> [!analysis] The 5.125% figure is unusually precise.
> A 5.125-percentage-point bound is oddly specific. The most likely origin is a derivation in the primary references (CTB 2014 or Pearson & ETS 2015) that Wood reproduces without further commentary. Ingesting one of those sources would clarify whether this value comes from a sample-size calculation, a power analysis, or a rounded quantile.

## Why it matters

> [!source] CTB uses exact-agreement monitoring to catch a QWK loophole.
> "Bridgeman (2013) noted that the high agreement between two raters can occur when raters are truncating the rubric score range. CTB has found that an engine's quadratic weighted kappa (QWK) may be high even though the engine exact agreement rate in comparison is low. In this situation, engines are usually giving adjacent scores to humans so that both the percent agreement and kappa statistics are not comparable to humans. For this reason, CTB also monitors engine performance for a notable reduction (greater than 0.05 difference) in perfect agreement rates between the human-human and engine-human scores" (McGraw-Hill Education CTB 2014, p. 15, as cited by Wood et al.). [[Wood Yao Haisfield Lottridge 2021 - Standards of Best Practice in Automated Scoring]]

> [!source] Bridgeman (2013) originated the truncated-rubric observation.
> The rationale for monitoring exact agreement alongside QWK traces to Bridgeman (2013), quoted inside the CTB passage: "the high agreement between two raters can occur when raters are truncating the rubric score range." CTB adopted this observation to motivate its exact-agreement flag; Wood reproduces the attribution chain (Bridgeman 2013 → CTB 2014 → Wood 2021) without modifying it. [[Wood Yao Haisfield Lottridge 2021 - Standards of Best Practice in Automated Scoring]]

> [!analysis] Exact agreement complements QWK, which ETS deprioritizes.
> Williamson, Xi, & Breyer (2012) explicitly does not use exact or exact-plus-adjacent agreement percentages as acceptance thresholds, citing scale dependence and base-distribution sensitivity. CTB and Pearson/ETS restore the exact-agreement check in relative form (difference from human-human) to address the specific failure mode where an engine issues consistent adjacent scores: QWK stays high because squared-error weighting tolerates 1-point misses, but exact agreement collapses. See [[Quadratic-Weighted Kappa]].

## Key Claims

> [!source] The metric sits in the relative-threshold family.
> The 5.125% bound is applied to a difference between human-human and human-AS exact agreement rates, not to an absolute rate. This places it in the relative bucket of [[Absolute vs Relative Thresholds in Automated Scoring]]. [[Wood Yao Haisfield Lottridge 2021 - Standards of Best Practice in Automated Scoring]]

> [!source] CTB also monitors a 0.05 drop as a separate flag.
> The CTB quotation reports a "notable reduction (greater than 0.05 difference) in perfect agreement rates" as its practical operational trigger. Whether the Table-2 5.125% threshold corresponds to a different operational use or is a refinement of the 0.05 rule is not clarified in Wood. [[Wood Yao Haisfield Lottridge 2021 - Standards of Best Practice in Automated Scoring]]

> [!analysis] Two distinct thresholds in the same source need reconciliation.
> Wood cites CTB (2014) as supporting both the 5.125% bound (Table 2) and the 5.0-percentage-point monitoring rule (quoted narrative). These are close enough that they are probably the same threshold expressed two ways, but the 0.125-percentage-point gap is not trivial at small sample sizes. The wiki treats both values as reported, with the operational use of each left open pending ingest of the CTB primary source.

## Connections

- One of five metrics in [[Automated Scoring Standards of Best Practice]] Standard 1.
- Classified relative under [[Absolute vs Relative Thresholds in Automated Scoring]].
- Pairs with [[Quadratic-Weighted Kappa]] to close CTB's "adjacent-score loophole."
- Feeds into [[Human-Automated Score Agreement]] as a second relative check alongside QWK degradation.

## Open Questions

> [!gap] Origin of the 5.125% figure.
> Wood reports the number without derivation. Primary sources (McGraw-Hill Education CTB 2014; Pearson & ETS 2015) would clarify.

> [!gap] Reconciliation with CTB's 0.05 operational trigger.
> Wood quotes a 5.0-percentage-point CTB trigger in Standard 1's narrative and a 5.125% Table-2 threshold attributed to the same source. Whether these are the same rule or distinct rules is not clarified.

> [!gap] Bridgeman (2013) is referenced but not ingested.
> The truncated-rubric argument is attributed to Bridgeman (2013) via CTB via Wood. The original Bridgeman (2013) source is not in the wiki; ingesting it would clarify the scope of the truncation observation and whether it was stated as a CTB-specific finding or a broader rater-behavior result.
