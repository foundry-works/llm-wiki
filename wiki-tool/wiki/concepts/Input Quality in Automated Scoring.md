---
type: concept
sources:
  - "[[Wood Yao Haisfield Lottridge 2021 - Standards of Best Practice in Automated Scoring]]"
created: "2026-04-16"
updated: "2026-04-16"
status: current
tags: [automated-scoring, data-quality, training, preprocessing]
---

> [!tldr]
> Wood's Standard 7 requires evaluating three inputs to an AS engine before training: non-attempts must be separated and routed through a condition-code workflow; human-scoring quality must be high enough to avoid training on noise; and the item's universe of acceptable responses must be narrow enough for AS to be suitable.

## Definition

> [!source] Standard 7 names three input-quality checks.
> "Another standard identified in the review affirms the importance of evaluating the quality of inputs to the AS engine, including item responses, human scores for those responses, and the item's universe of acceptable responses (Williamson, et al., 2010; Williamson, Xi, & Breyer, 2012)." [[Wood Yao Haisfield Lottridge 2021 - Standards of Best Practice in Automated Scoring]]

## The three checks

**Table 1.** The three Standard 7 input-quality checks, each with its rationale.

| # | Input | Check | Rationale |
|---|---|---|---|
| 1 | Item responses | Separate non-attempts (blanks, gibberish, refusals) from valid attempts | Non-attempts are used to establish rules and models for condition-code assignment; valid attempts are used to train the scoring model |
| 2 | Human scores for training responses | Verify human-scoring quality before training | Low-quality human scores produce engines trained on noise |
| 3 | Item's universe of acceptable responses | Verify the universe is narrow enough for AS | Broad universes with many valid answer paths are harder for AS to score well |

> [!source] Non-attempts are routed separately from valid attempts.
> "First, responses that are considered non-attempts (e.g., blank response, gibberish, refusals, etc.) — as identified by agreed-upon scoring rules — are separated from valid attempts and processed using a different workflow. Specifically, the non-attempt responses are used to establish rules and models for AS to assign condition codes, while valid attempts are used to create the scoring models." [[Wood Yao Haisfield Lottridge 2021 - Standards of Best Practice in Automated Scoring]]

> [!source] Poor human-scoring inputs produce poor AS models.
> "AS models developed with data from low-quality human scoring will result in poor AS engine performance." Williamson, Xi, & Breyer (2012, p. 7), as cited by Wood et al.: "if the inter-rater agreement of independent human raters is low, especially below the .70 threshold, then automated scoring is disadvantaged in demonstrating this level of performance." [[Wood Yao Haisfield Lottridge 2021 - Standards of Best Practice in Automated Scoring]]

> [!source] Narrower response universes are more AS-suitable.
> "Third, the item's universe of acceptable responses can impact engine performance. For instance, differences in the number of concepts or ways of describing these concepts elicited by the item can affect the suitability of an item for AS." Wood contrasts "Describe the characteristics of the chemical element mercury" (narrow universe — silver color, liquid at room temperature, poisonous, used in thermometers) with "Describe how 19th-century American wars led to the expansion of the United States via manifest destiny" (broad universe — War of 1812, Mexican-American War, manifest destiny framings). [[Wood Yao Haisfield Lottridge 2021 - Standards of Best Practice in Automated Scoring]]

## Key Claims

> [!analysis] The three checks are upstream of every Standard 1 metric.
> QWK (>= 0.70), SMD (+/- 0.15), SD ratio (2/3 to 1.50), and exact-agreement-rate difference (<= 5.125%) are all agreement metrics that assume the human-scoring target is well-defined. If human raters disagree, if responses are dominated by gibberish, or if the universe of acceptable answers is too wide, no accuracy threshold can save the model. Standard 7 is therefore logically prior to Standard 1, even though Standard 1 is listed first.

> [!analysis] The mercury-vs-manifest-destiny contrast is the clearest operational filter.
> Wood's pair of items sketches a rough taxonomy: items that elicit a small, stable set of facts are good AS candidates; items that elicit open-ended historical analysis are not. This suggests a pre-AS screening step — probably qualitative — that is currently operator-judgment rather than a specified procedure.

> [!analysis] Standard 7 is the pre-training counterpart to Standard 10.
> Standard 7 checks input quality before training. Standard 10 ([[Engine Recalibration Policy]]) checks input and output drift after deployment. Together they define a full lifecycle of data-quality gates, with Standards 1 and 6 as the interior monitoring loop.

## Connections

- Standard 7 of [[Automated Scoring Standards of Best Practice]].
- Logically prior to [[Human-Automated Score Agreement]] (the target metric).
- Complements [[Engine Recalibration Policy]] (post-deployment input/output drift).
- Human-scoring quality concerns overlap with [[Quadratic-Weighted Kappa]]'s 0.70 floor as applied to inter-rater agreement.

## Open Questions

> [!gap] No numeric criteria for "narrow enough" universes.
> Wood illustrates with two example items but does not offer a test for when an item's universe is suitable for AS versus when it is not.

> [!gap] No procedure for condition-code rule development.
> Wood says non-attempts are routed through a workflow to assign condition codes but does not specify how those rules are validated or maintained.

> [!gap] No interaction with fairness.
> Low human-scoring quality could be subgroup-specific. Wood does not describe how input-quality checks interact with the [[Fairness in Automated Scoring]] subgroup checks.
