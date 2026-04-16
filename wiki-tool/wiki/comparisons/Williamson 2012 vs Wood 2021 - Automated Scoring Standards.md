---
type: comparison
subjects:
  - "[[Williamson Xi Breyer 2012 - Framework for Automated Scoring]]"
  - "[[Wood Yao Haisfield Lottridge 2021 - Standards of Best Practice in Automated Scoring]]"
sources:
  - "[[Williamson Xi Breyer 2012 - Framework for Automated Scoring]]"
  - "[[Wood Yao Haisfield Lottridge 2021 - Standards of Best Practice in Automated Scoring]]"
created: "2026-04-16"
updated: "2026-04-16"
status: current
tags: [automated-scoring, standards, framework, comparison]
---

> [!tldr]
> Williamson, Xi, and Breyer (2012) propose a five-area argument-based validity framework for automated scoring, illustrated with ETS's e-rater; Wood, Yao, Haisfield, and Lottridge (2021) codify 10 practice-level standards by aggregating across 16 sources; the two sources are complementary — Williamson provides the validity backbone and the QWK/SMD thresholds, Wood adds five practice standards (process monitoring, input quality, alert papers, recalibration, impact) and two accuracy metrics (SD ratio and exact-agreement-rate difference) sourced from Wang & von Davier and CTB/Pearson respectively.

## Comparison

**Table 1.** Structural comparison of the two sources.

| Dimension | Williamson, Xi, & Breyer (2012) | Wood, Yao, Haisfield, & Lottridge (2021) |
|---|---|---|
| Posture | Validity framework | Practice-standards codification |
| Organizing principle | Kane's argument-based validity (five inferences) | 10 numbered standards |
| Evidence base | One paper, illustrated with one engine (e-rater) | 16-source literature review |
| Publisher | ETS, via *Educational Measurement: Issues and Practice* | ACT, Inc., as a research technical brief |
| Primary contribution | Maps AS evaluation onto construct, agreement, independent measures, generalizability, and impact, with fairness cross-cutting | Synthesizes existing standards into a compact taxonomy usable by AS professionals across organizations |
| Thresholds originated here | QWK >= 0.70, QWK degradation <= 0.10, SMD +/- 0.15 (overall), SMD +/- 0.10 (subgroup) | None (Wood codifies, does not originate) |
| Thresholds imported from other sources | — | SD ratio 2/3-1.50 (Wang & von Davier 2014); EA difference <= 5.125% (CTB 2014; Pearson & ETS 2015) |

**Table 2.** Content mapping — which Wood standards overlap Williamson framework areas.

| Wood Standard | Williamson framework component | Relationship |
|---|---|---|
| 1: Accuracy against human scores | Evaluation (agreement, degradation, SMD) | Direct overlap; Wood adds SD ratio and exact-agreement difference as new metrics |
| 2: Transparency and construct coverage | Construct relevance and representation | Direct overlap; Wood emphasizes documentation and stakeholder access |
| 3: Fairness for all populations | Fairness (subgroup SMD, associations, generalizability, prediction, decisions) | Direct overlap; Wood adds Differential Feature Functioning (Penfield 2016; Zhang et al. 2017) and RSMTool (Madnani et al. 2017) tooling references |
| 4: Convergent and discriminant validity | Extrapolation (association with independent measures) | Direct overlap |
| 5: Context-appropriate implementation | Implementation models and impact | Williamson's five-model ladder (human-only to AS-only) is re-cited by Wood as a standard |
| 6: Live process monitoring | Not a named area in Williamson | New; Wood imports from Wang & von Davier (2014) and CCSSO/ATP (2013) |
| 7: Input quality before training | Agreement area mentions human-scoring quality, but not a named check | Largely new; Wood foregrounds non-attempts workflow and response-universe suitability |
| 8: Impact and consequences | Utilization (impact on decisions and score-user behavior) | Direct overlap; Wood elevates to a named standard. See [[Impact and Consequences of Automated Scoring]] |
| 9: Alert-paper procedures | Williamson mentions cheating as a validity challenge in passing | New operational standard |
| 10: Recalibration policies | Not a named area in Williamson | New; Wood imports from CCSSO/ATP (2013) |

## Contradictions

> [!source] Williamson flags SMD at 0.15 overall; CTB tightens to 0.12 as reported by Wood.
> Williamson, Xi, & Breyer (2012) specify a 0.15 overall SMD flag and a 0.10 subgroup flag. McGraw-Hill Education CTB (2014, p. 15), as quoted in Wood et al., reports: "Because the larger the population SMD value the more likely the subpopulation SMD value will be flagged, CTB reduced the amount of SMD separation tolerated by flagging the population SMD if it exceeds .12 in absolute value." [[Williamson Xi Breyer 2012 - Framework for Automated Scoring]], [[Wood Yao Haisfield Lottridge 2021 - Standards of Best Practice in Automated Scoring]]

> [!analysis] Wood does not adjudicate the 0.12-vs-0.15 SMD disagreement.
> Wood's Standard 1 Table 2 reports the Williamson 0.15 value. The CTB 0.12 tightening is quoted in the narrative. Wood presents both without comment. The wiki treats this as a live disagreement; a conservative practitioner would apply 0.12, while a practitioner seeking continuity with historical ETS practice would apply 0.15.

## Analysis

> [!analysis] Williamson provides the thresholds; Wood provides the scope.
> Four of the five metrics in Wood's Standard 1 accuracy table are Williamson thresholds (QWK absolute and relative, SMD, and by implication the conjunctive bundle). Wood adds two imports — SD ratio from Wang & von Davier, exact-agreement-rate difference from CTB/Pearson. That makes Williamson the primary source for AS accuracy criteria and Wood the consolidator plus secondary-source importer.

> [!analysis] The two sources use different organizing principles, which produces different coverage gaps.
> Williamson's validity-argument organization foregrounds the "why each check matters" logic. Wood's standards organization foregrounds "what a program should do." Each covers gaps the other leaves. Williamson is light on operations (no process monitoring, no recalibration policy, no input-quality procedures); Wood is light on validity theory (no mapping to Kane's inferences, no construct-argument narrative).

> [!analysis] Wood extends Williamson's implementation-model ordering but does not change it.
> Williamson proposes a five-model ladder from human-only through AS-only. Wood's Standard 5 re-cites this ordering as a standard in its own right. The ladder itself — human scoring, AS quality control, integrated AS-plus-human, composite, AS alone — is not altered by Wood. See [[Automated Scoring Implementation Models]].

> [!analysis] Practitioners should treat the two sources as layered, not competing.
> For a program building an AS evaluation protocol, Williamson supplies the validity argument and agreement metrics, Wood adds the operations layer and consolidates other literature. Using Wood alone underweights the Kane-style validity framing. Using Williamson alone leaves out monitoring, input-quality, alert-paper, and recalibration requirements that the broader literature supports.

## Implications

- **Adopt Wood's 10-standard taxonomy as the operations-layer checklist; adopt Williamson's five-area framework as the validity-argument backbone.** The two are complementary layers on the same stack.
- **When a threshold is stated by both sources, cite Williamson as primary.** QWK 0.70, QWK degradation <= 0.10, SMD +/- 0.15 all originate in Williamson (with the 0.15 subgroup-tightening to 0.10 also originating there).
- **Treat CTB's 0.12 SMD as a known tightening, not as consensus.** The wiki's [[Standardized Mean Score Difference]] page surfaces both values. A program defending either choice should cite the original source, not Wood.
- **The SD ratio and exact-agreement-rate difference are operationally live thresholds with primary references predating Wood.** Citing Wood as the origin of either would be incorrect; Wang & von Davier (2014) and CTB (2014) / Pearson & ETS (2015) are the primary references.

## Open Questions

> [!gap] How should Wood's qualitative Standards 2-10 be operationalized with numeric criteria?
> Wood does not provide thresholds outside Standard 1. Williamson does not supply them either. Both sources leave magnitude decisions to practitioner judgment.

> [!gap] Which source's implementation-model ordering is more current?
> Williamson's five-model ladder predates GMAT's engine transition from e-rater to IntelliMetric. Wood re-cites without updating. Whether the ladder's sample-program column needs updating for 2021-era deployments is outside both sources' scope.
