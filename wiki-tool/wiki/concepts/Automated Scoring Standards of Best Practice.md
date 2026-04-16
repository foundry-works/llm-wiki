---
type: concept
sources:
  - "[[Wood Yao Haisfield Lottridge 2021 - Standards of Best Practice in Automated Scoring]]"
created: "2026-04-16"
updated: "2026-04-16"
status: current
tags: [automated-scoring, standards, taxonomy, best-practice]
---

> [!tldr]
> Wood, Yao, Haisfield, and Lottridge (2021) codify 10 high-level standards of best practice for automated scoring (AS) by synthesizing 16 sources from assessment, AS, and machine-learning literature; the standards cover accuracy, transparency, fairness, validity, implementation, monitoring, inputs, impact, alert papers, and recalibration.

## Definition

> [!source] The standards are derived from a targeted 16-source literature review.
> "This paper reviews the assessment and AS literature to identify key standards of best practice and ethical behavior for AS professionals and codifies those standards in a single resource... In all, 16 sources were identified as representative of the literature." [[Wood Yao Haisfield Lottridge 2021 - Standards of Best Practice in Automated Scoring]]

> [!source] The standards were produced through aggregated note-taking.
> "AS research staff divided the sources amongst themselves for further reading and standard identification... Commonalities across the notes were grouped together. This process resulted in 10 core high-level AS standards of best practice." [[Wood Yao Haisfield Lottridge 2021 - Standards of Best Practice in Automated Scoring]]

## The ten standards

**Table 1.** The 10 AS standards of best practice, with the one-line principle Wood et al. give in each standard header. Standard ordering follows the paper.

| # | Title | Principle |
|---|---|---|
| 1 | Accuracy against human scores | Automated scores should achieve industry absolute and relative thresholds for accuracy when compared with human scores. |
| 2 | Transparency and construct coverage | AS engines and procedures should be transparently described such that stakeholders understand how they operate and whether they satisfy construct coverage. |
| 3 | Fairness for all populations | Scores produced by AS should demonstrate fairness for all populations. |
| 4 | Convergent and discriminant validity | Convergent and discriminant validity studies should be conducted to establish empirical relationships between AS scores and other constructs. |
| 5 | Context-appropriate implementation | When implementing AS, consideration must be given to contextual factors such as the stakes associated with test performance, item types, and scoring approaches that integrate human and AS. |
| 6 | Live process monitoring | During live testing, accuracy and reliability of AS via process monitoring should be made available to the client. |
| 7 | Input quality before training | It is essential to evaluate the quality of inputs to an AS engine (responses, human scoring, universe of acceptable responses) before training. |
| 8 | Impact and consequences | The impact or consequences of AS on the test or reported score should be considered and documented. |
| 9 | Alert-paper procedures | Procedures should be in place to identify alert papers (i.e., responses reflecting cheating or disturbing content). |
| 10 | Recalibration policies | Policies around how and when to recalibrate the engine should be established. |

> [!source] Standards 9 and 10 are less frequently cited than 1-8.
> Wood et al. introduce Standard 9 with "A less frequently recognized core standard is that there should be engine procedures to identify 'alert papers,'" and its exemplar-citations table lists only one supporting source (CCSSO & ATP 2013). Standard 10 is supported only by the same CCSSO & ATP 2013 reference. The other eight standards each draw on three or more sources. [[Wood Yao Haisfield Lottridge 2021 - Standards of Best Practice in Automated Scoring]]

## Standard 1 acceptance metrics

**Table 2.** Wood's Table 2 reproduced, preserving the primary-reference attributions. Each metric is the origin source's criterion, not Wood's.

| Metric | Threshold | Primary reference (as cited by Wood) |
|---|---|---|
| Standardized Mean Difference (SMD) between human and AS | -0.15 <= SMD <= 0.15 | Williamson, Xi, & Breyer (2012) |
| Standard Deviation (SD) ratio between human and AS | 2/3 <= SD_H/SD_AS <= 1.50 | Wang & von Davier (2014) |
| Difference between human-human and human-AS exact agreement rates | EA_H,H - EA_H,AS <= 5.125% | McGraw-Hill Education CTB (2014); Pearson & ETS (2015) |
| Quadratic-weighted kappa between human and AS | QWK_H,AS >= 0.70 | Williamson, Xi, & Breyer (2012) |
| Difference between human-human and human-AS QWK | QWK_H,H - QWK_H,AS <= 0.10 | Williamson, Xi, & Breyer (2012) |

See [[Standardized Mean Score Difference]], [[Standard Deviation Ratio]], [[Exact Agreement Rate Difference]], and [[Quadratic-Weighted Kappa]] for the individual metrics.

> [!source] Standard 1 frames these as absolute vs. relative thresholds.
> "Absolute thresholds are used when a metric is compared to a constant value, such as when a human-AS quadratic weighted kappa is compared to 0.70. Relative thresholds are used when a metric is compared to a corresponding human or human-human metric for the item, such as when a human-AS quadratic weighted kappa is compared to the human-human metric." [[Wood Yao Haisfield Lottridge 2021 - Standards of Best Practice in Automated Scoring]] See [[Absolute vs Relative Thresholds in Automated Scoring]].

## Supporting-source breakdown

> [!source] The 16 sources fall into four categories.
> Five sources: professional-organization standards (AERA/APA/NCME 2014; CCSSO/ATP 2013; ITC 2006, 2014a; JCTP 2004). Six sources: AS evaluation frameworks (Madnani et al. 2017; Powers et al. 2015; Shermis et al. 2016; Williamson et al. 2010; Yang et al. 2002, n.d.). Four sources: large-scale-program results (McGraw-Hill Education CTB 2014; Pearson & ETS 2015; Wang & von Davier 2014; Williamson, Xi, & Breyer 2012). One source: machine-learning evaluation (Zheng 2015). [[Wood Yao Haisfield Lottridge 2021 - Standards of Best Practice in Automated Scoring]]

## Key Claims

> [!analysis] The taxonomy complements Williamson's validity framework rather than replacing it.
> Williamson, Xi, & Breyer (2012) organizes AS evaluation around five Kane-style validity inferences. Wood's ten standards are more operational: five of them (1, 3, 4, 5, 8) overlap with Williamson areas, and five (2, 6, 7, 9, 10) add practice-level requirements that Williamson mentions only in passing or not at all. See [[Williamson 2012 vs Wood 2021 - Automated Scoring Standards]].

> [!analysis] Wood codifies; primary references originate.
> Every threshold in Standard 1's Table 2 is attributed to a primary reference. When citing these standards, distinguish "Wood 2021 codifies X from primary source Y" from "Wood 2021 proposes X." The paper's method section is explicit that the standards are extracted from existing literature, not proposed by ACT de novo.

> [!analysis] The standards privilege consensus over novelty.
> Because the method aggregates commonalities across sources, standards where the literature disagrees will be softened or dropped. This is visible in Standard 1's Table 2: a real disagreement between Williamson's 0.15 overall SMD flag and CTB's 0.12 tightening is surfaced in the qualitative discussion of CTB's monitoring practice, but the Table-2 threshold is the Williamson number. The compact taxonomy form trades nuance for actionability.

## Connections

- Integrates into [[Automated Scoring]] as a practice-level standards layer.
- Standard 1 (accuracy) operationalizes [[Human-Automated Score Agreement]] and its component metrics.
- Standard 2 (transparency and construct coverage) corroborates [[Construct Representation in Automated Scoring]].
- Standard 3 (fairness) corroborates [[Fairness in Automated Scoring]].
- Standard 5 (context-appropriate implementation) corroborates [[Automated Scoring Implementation Models]].
- Standard 6 is the root concept [[Process Monitoring in Automated Scoring]].
- Standard 7 is the root concept [[Input Quality in Automated Scoring]].
- Standard 8 is the root concept [[Impact and Consequences of Automated Scoring]].
- Standard 9 is the root concept [[Alert Paper Detection]].
- Standard 10 is the root concept [[Engine Recalibration Policy]].
- Compared to Williamson 2012 in [[Williamson 2012 vs Wood 2021 - Automated Scoring Standards]].

## Contradictions & Tensions

- **CTB 0.12 vs. Williamson 0.15 SMD flag.** Wood reports McGraw-Hill Education CTB (2014, p. 15) tightening the population SMD flag to 0.12 to reduce subgroup false negatives, while simultaneously listing the 0.15 Williamson threshold in Table 2. Wood does not adjudicate. See [[Standardized Mean Score Difference]].

## Open Questions

> [!gap] No sensitivity analysis for the thresholds in Standard 1.
> Wood et al. present Table 2 as codified thresholds but do not report how test decisions would change at alternative values, and do not evaluate the thresholds against new empirical data.

> [!gap] Intersection between standards is not operationalized.
> The 10 standards read as parallel axes. Wood does not specify decision rules when standards pull in different directions (e.g., Standard 5 may recommend integrated human-AS scoring at high stakes, while Standard 7 may recommend AS-only for items with a well-bounded universe of responses).

> [!gap] Numeric thresholds are absent from Standards 2-10.
> Standard 1 carries all five numeric thresholds in Table 2. Standards 2 through 10 are qualitative. Wood does not propose quantitative flags for fairness by subgroup (Standard 3), for client-dashboard metrics (Standard 6), for input-quality checks (Standard 7), or for recalibration-trigger magnitudes (Standard 10).
