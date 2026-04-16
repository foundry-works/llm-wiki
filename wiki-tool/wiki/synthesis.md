---
type: synthesis
sources:
  - "[[Williamson Xi Breyer 2012 - Framework for Automated Scoring]]"
  - "[[Wood Yao Haisfield Lottridge 2021 - Standards of Best Practice in Automated Scoring]]"
created: "2026-04-16"
updated: "2026-04-16"
status: current
tags: [automated-scoring, validity, framework, standards, synthesis]
---

> [!tldr]
> Automated scoring of constructed-response items is governed by two complementary bodies of guidance: Williamson, Xi, and Breyer (2012) supply a Kane-style five-area validity framework with the core QWK and SMD thresholds, and Wood, Yao, Haisfield, and Lottridge (2021) codify 10 practice-level standards that add process monitoring, input quality, alert papers, and recalibration, plus two accuracy metrics (SD ratio, exact-agreement-rate difference) imported from Wang & von Davier and from CTB/Pearson.

## Current knowledge baseline

The wiki now rests on two sources: Williamson, Xi, & Breyer (2012) as the validity framework backbone, and Wood, Yao, Haisfield, & Lottridge (2021) as the ACT-published consensus-standards layer aggregated across 16 references. Williamson supplies the "why each check matters" logic; Wood supplies the "what a program should do" checklist. The two layer cleanly — most Wood standards either corroborate a Williamson area or add an operations concern Williamson leaves implicit.

### The shape of the field

Automated scoring (AS) assigns scores to constructed-response items algorithmically. Constructed-response items cost more to score than multiple choice; automation promises speed, consistency, and lower cost but introduces failure modes around construct representation, adversarial responses, and score-user interpretation.

Systems divide into two families. Simulation-based systems score task-bound scenarios (medical case simulations, CAD tasks, accounting simulations) and do not generalize beyond the task they were built for. Response-type systems score a recurrent response format (essays, equations, spoken utterances) and generalize more readily. Essay scoring is the most mature domain, with four well-known engines (IEA, e-rater, PEG, IntelliMetric).

### The validity framework (Williamson 2012)

Williamson evaluates AS across five emphasis areas mapped to Kane's argument-based validity inferences:

- **[[Construct Representation in Automated Scoring|Construct relevance and representation]]** (Explanation).
- **[[Human-Automated Score Agreement|Association with human scores]]** (Evaluation).
- **[[Generalizability of Automated Scores|Generalizability]]** (Generalization).
- **[[Association with Independent Measures]]** (Extrapolation).
- **Impact on decisions and consequences** (Utilization).

[[Fairness in Automated Scoring|Fairness]] is applied across these areas via five subgroup checks (SMD, associations, generalizability, prediction, decision differences), with the SMD flag tightened from 0.15 overall to 0.10 for subgroups.

### The operations layer (Wood 2021)

Wood et al. consolidate 16 sources into 10 numbered AS standards:

1. Accuracy against human scores (Standard 1 carries the Table-2 thresholds).
2. Transparency and construct coverage.
3. Fairness for all populations.
4. Convergent and discriminant validity.
5. Context-appropriate implementation (re-cites Williamson's five-model ladder).
6. Live process monitoring.
7. Input quality before training.
8. Impact and consequences.
9. Alert-paper procedures (cheating, disturbing content).
10. Recalibration policies.

Standards 1-5 and 8 map onto Williamson framework areas. Standards 6, 7, 9, and 10 add practice-level requirements Williamson touches only in passing. See [[Automated Scoring Standards of Best Practice]] and [[Williamson 2012 vs Wood 2021 - Automated Scoring Standards]].

### The accuracy threshold bundle

Williamson's original ETS bundle is conjunctive — any one failure is a substantive concern. Wood extends it with two imported metrics. The current consolidated bundle:

- Agreement with human scores (QWK on rounded engine values, Pearson correlation on unrounded, same 0.70 floor) — absolute, Williamson.
- Degradation from human-human agreement: kappa drop <= 0.10 — relative, Williamson.
- Standardized mean score difference overall: <= 0.15 (Williamson) or <= 0.12 (CTB tightening reported by Wood).
- Standardized mean score difference for any subgroup: <= 0.10 — Williamson.
- Standard deviation ratio: 2/3 <= SD_H/SD_AS <= 1.50 — absolute, Wang & von Davier (2014) via Wood.
- Difference between human-human and human-AS exact agreement rates: <= 5.125% — relative, CTB (2014) and Pearson & ETS (2015) via Wood.

The SD ratio catches score-distribution compression that QWK tolerates. The exact-agreement difference catches the "adjacent-score loophole" where the engine gives consistent off-by-one scores, inflating QWK while collapsing exact agreement. Together, the two Wood imports make the bundle more sensitive to distribution-shape pathologies than Williamson alone.

All thresholds remain working conventions, not empirically derived values. The 0.70 QWK floor is justified as the "tipping point where signal outweighs noise." Wood reproduces these conventions but does not evaluate them.

### A live SMD disagreement

Williamson, Xi, & Breyer (2012) flag overall SMD at 0.15. McGraw-Hill Education CTB (2014), as cited by Wood, tightens this to 0.12, explicitly to reduce subgroup-level false negatives. Wood reports both without adjudicating. The wiki surfaces this as an open disagreement rather than collapsing it. A conservative practitioner applies 0.12; a practitioner seeking continuity with historical ETS practice applies 0.15.

### Five implementation models

Programs can deploy AS under one of five models ordered from conservative to liberal:

1. Human scoring (engine may run as silent shadow).
2. Automated quality control of human scoring. Used for GRE Issue and Argument at a 0.5 discrepancy threshold.
3. Combined AS and human scoring. Used for TOEFL Independent/Integrated (e-rater) and GMAT Argument/Issue (IntelliMetric after GMAT's vendor transition) at a 1.5 TOEFL discrepancy threshold.
4. Composite scoring (human score becomes a weighted feature alongside AS features). No operational example is cited.
5. Automated-only. Used by IEA in Pearson Test of English.

Wood re-cites this ladder intact as Standard 5. Model choice depends on stakes, construct fit, population, scale-history continuity, and market research on score-user perception.

### Fairness tooling and feature-level checks

Williamson's five subgroup checks operate at the score level. Wood adds two feature-level references. Madnani et al. (2017) contribute RSMTool, open-source software for subgroup evaluation. Penfield (2016) and Zhang et al. (2017) contribute Differential Feature Functioning (DFF), which compares feature values across subgroups conditional on score. DFF catches construct-irrelevant features that correlate with subgroup membership even when overall score calibration looks fine.

### e-rater as illustrative case

Williamson illustrates the framework with ETS's e-rater. e-rater is a regression model over 10 features (8 linguistic, 2 content) mapped to the Culham 6+1 trait model. Content representation is primitive. e-rater performs better on unconstrained prompts (GRE Issue) than on constrained prompts (GRE Argument). Responses with excessive length or brevity, repetition, too many problems, or off-topic content are flagged for human scoring.

### Gaps and tensions the baseline surfaces

- Threshold sensitivity analyses remain unavailable across both sources. Every numeric criterion is a working convention.
- Standards 2-10 in Wood are qualitative. Only Standard 1 carries numeric thresholds.
- Wood does not specify trigger magnitudes for recalibration ("major," "significant," "decrease" are undefined).
- AS-only deployments (Model 5) weaken Wood's Standard-6 monitoring recipe, which assumes concurrent human scores.
- Wood's alert-paper standard (Standard 9) specifies no precision, recall, or time-to-escalation targets.
- The CTB 0.12 vs. Williamson 0.15 SMD disagreement persists.
- Generalization beyond essay scoring is asserted but not demonstrated in either source; every concrete criterion is anchored in essay-scoring practice.

## Next directions

The wiki should next ingest primary sources behind Wood's imports: Wang and von Davier (2014) for the SD ratio and process monitoring; McGraw-Hill Education CTB (2014) for the 0.12 SMD tightening and 5.0-percentage-point exact-agreement trigger; and Penfield (2016) or Zhang et al. (2017) for Differential Feature Functioning. Each ingest would let the wiki cite the primary sources directly rather than through Wood. Beyond that: Kane (1992, 2006) for the argument-based validity foundation; Madnani et al. (2017) for RSMTool and fairness tooling; and work on AS engines other than e-rater (IEA, PEG, IntelliMetric) and outside essay writing (speech, math, simulations).
