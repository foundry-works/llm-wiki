# Wiki Index

## Entities

- [[ACT]] (1) — US testing organization; publisher of the 2021 technical brief codifying 10 AS standards of best practice.
- [[David M Williamson]] (1) — ETS researcher, first author of the 2012 automated-scoring evaluation framework.
- [[Erin Yao]] (1) — ACT automated-scoring researcher; second author of the 2021 AS standards brief.
- [[e-rater]] (1) — ETS's regression-based essay scorer with 10 features (8 linguistic, 2 content) mapped to a 6+1 trait model; used in GRE and TOEFL Writing.
- [[Educational Testing Service]] (1) — Princeton-based assessment organization, developer of e-rater, first to deploy automated essay scoring in high-stakes testing.
- [[F Jay Breyer]] (1) — ETS researcher, third author of the 2012 framework paper.
- [[Lisa Haisfield]] (1) — ACT automated-scoring researcher; third author of the 2021 AS standards brief.
- [[Scott Wood]] (1) — ACT automated-scoring researcher; first author of the 2021 AS standards brief.
- [[Susan Lottridge]] (1) — ACT automated-scoring researcher; fourth author of the 2021 AS standards brief.
- [[Xiaoming Xi]] (1) — ETS researcher, second author; her earlier validity work shapes the framework's argument-based structure.

## Concepts

- [[Absolute vs Relative Thresholds in Automated Scoring]] (1) — Wood's framing for Standard 1: absolute = compared to a constant; relative = compared to human-human metric on same item.
- [[Alert Paper Detection]] (1) — Standard 9: engine procedures to identify cheating or disturbing content; copy filters and hybrid keyword/ML methods.
- [[Argument-Based Validity]] (1) — Kane's approach: score interpretation is a chain of five inferences (explanation, evaluation, generalization, extrapolation, utilization).
- [[Association with Independent Measures]] (1) — Extrapolation check: do automated scores correlate with external and within-test criteria the way human scores do?
- [[Automated Scoring]] (2) — Algorithmic scoring of constructed-response items; simulation-based vs. response-type systems.
- [[Automated Scoring Evaluation Framework]] (1) — Williamson-Xi-Breyer five-area framework (construct, agreement, independent measures, generalizability, impact) plus fairness.
- [[Automated Scoring Implementation Models]] (2) — Five deployment models from human-only to automated-only, ordered by liberalization; re-cited as Standard 5 by Wood.
- [[Automated Scoring Standards of Best Practice]] (1) — Wood's 10-standard taxonomy codified from 16 sources.
- [[Construct Representation in Automated Scoring]] (2) — Fit between construct, task, rubric, and reporting goals; corroborated by Wood's Standard 2.
- [[Engine Recalibration Policy]] (1) — Standard 10: triggers are population change, score-distribution shift, and human-AS agreement decay.
- [[Exact Agreement Rate Difference]] (1) — EA_H,H - EA_H,AS <= 5.125%; catches QWK's adjacent-score loophole (CTB 2014; Pearson & ETS 2015).
- [[Fairness in Automated Scoring]] (2) — Five subgroup checks (SMD at 0.10, associations, generalizability, prediction, decisions); Wood adds DFF and RSMTool tooling.
- [[Generalizability of Automated Scores]] (1) — Generalization check via G/Phi coefficients across tasks and alternate-form prediction of human scores.
- [[Human-Automated Score Agreement]] (2) — Conjunctive acceptance bundle: QWK, correlation, degradation, SMD, adjudication, intervention; Wood adds SD ratio and exact-agreement-rate difference.
- [[Impact and Consequences of Automated Scoring]] (2) — Standard 8: document test-taker behavior changes, misclassification risk, and claims/disclosures to score users.
- [[Input Quality in Automated Scoring]] (1) — Standard 7: check non-attempts, human-scoring quality, and the item's universe of acceptable responses before training.
- [[Process Monitoring in Automated Scoring]] (1) — Standard 6: live dashboards of AS score distributions, human score distributions, and human-AS agreement, accessible to the client.
- [[Quadratic-Weighted Kappa]] (2) — Chance-corrected agreement statistic with squared-error weighting; 0.70 floor and 0.10 degradation bound (Williamson; codified by Wood).
- [[Standard Deviation Ratio]] (1) — 2/3 <= SD_H/SD_AS <= 1.50; guards against variance compression or inflation (Wang & von Davier 2014).
- [[Standardized Mean Score Difference]] (2) — Standardized human-vs-automated mean gap; 0.15 overall flag (Williamson), 0.12 variant (CTB), 0.10 subgroup flag.

## Sources

- [[Williamson Xi Breyer 2012 - Framework for Automated Scoring]] (0) — Proposes a five-area framework for evaluating automated scoring in high-stakes assessment, illustrated with ETS's e-rater.
- [[Wood Yao Haisfield Lottridge 2021 - Standards of Best Practice in Automated Scoring]] (0) — ACT Research Technical Brief codifying 10 AS standards of best practice from a 16-source literature review.

## Comparisons

- [[GRE vs TOEFL e-rater Implementation]] (1) — Same engine, different implementation models and discrepancy thresholds (0.5 vs. 1.5) driven by population, scale history, and score-user perceptions.
- [[Williamson 2012 vs Wood 2021 - Automated Scoring Standards]] (2) — Williamson supplies the validity framework and most accuracy thresholds; Wood adds the operations layer (monitoring, input quality, alert papers, recalibration) and two new metrics (SD ratio, exact-agreement difference).
