---
type: source-summary
raw_path: "raw/Wood et al. - Establishing Standards of Best Practice in Automated Scoring.pdf"
raw_hash: "0aff6066ff3c75226aece282aead25b3b1e8e5fe0bff61d66497e79489e4da39"
sources: []
created: "2026-04-16"
updated: "2026-04-16"
status: current
tags: [automated-scoring, standards, literature-review, assessment, ACT]
---

> [!tldr]
> An ACT Research Technical Brief by Wood, Yao, Haisfield, and Lottridge (July 2021) that reviews 16 sources from assessment, machine learning, and professional ethics literature and codifies 10 high-level standards of best practice for automated-scoring professionals.

## Citation

Wood, S., Yao, E., Haisfield, L., & Lottridge, S. (2021). *Establishing Standards of Best Practice in Automated Scoring*. ACT Research Technical Brief, July 2021. ACT, Inc.

## Key Takeaways

> [!source] Automated scoring (AS) has no unified standards of best practice, so this brief synthesizes them.
> "For assessment professionals who are also automated scoring (AS) professionals, there is no single set of standards of best practice... This paper reviews the assessment and AS literature to identify key standards of best practice and ethical behavior for AS professionals and codifies those standards in a single resource." [[Wood Yao Haisfield Lottridge 2021 - Standards of Best Practice in Automated Scoring]]

> [!source] Wood names three motivations for a unified set of AS standards.
> "First, given that AS is an emerging technology in educational assessment, it is important to establish guidelines of good practice for professionals and stakeholders learning to use this new technology. Second, due to the wide variety of professionals involved in AS technology development (e.g., psychometricians, linguists, data scientists, and computer programmers), a unified set of standards would guide these diverse professionals toward common objectives. Third, and most importantly, having standards for which stakeholders can hold AS professionals accountable can provide stakeholders with greater confidence in the use of AS" (p. 2). [[Wood Yao Haisfield Lottridge 2021 - Standards of Best Practice in Automated Scoring]]

> [!source] 16 sources were reviewed, spanning four categories.
> "In all, 16 sources were identified as representative of the literature." Five sources were professional-organization standards (AERA/APA/NCME 2014; CCSSO/ATP 2013; ITC 2006, 2014a; Joint Committee on Testing Practices 2004); six were AS evaluation frameworks (Madnani et al. 2017; Powers et al. 2015; Shermis et al. 2016; Williamson et al. 2010; Yang et al. 2002, n.d.); four were large-scale program results (McGraw-Hill Education CTB 2014; Pearson & ETS 2015; Wang & von Davier 2014; Williamson, Xi, & Breyer 2012); and one was a machine-learning-evaluation reference (Zheng 2015). [[Wood Yao Haisfield Lottridge 2021 - Standards of Best Practice in Automated Scoring]]

> [!source] The review produced 10 high-level standards.
> "This process resulted in 10 core high-level AS standards of best practice. All authors reviewed the 10 core standards and refined the language based on experience with AS projects." [[Wood Yao Haisfield Lottridge 2021 - Standards of Best Practice in Automated Scoring]]

See [[Automated Scoring Standards of Best Practice]] for the full enumerated list.

> [!source] Standard 1 names five acceptance metrics and their primary references.
> Table 2 pairs each accuracy metric with a threshold and a reference: standardized mean difference between human and AS at -0.15 <= SMD <= 0.15 (Williamson, Xi, & Breyer 2012); SD ratio between human and AS at 2/3 <= SD_H/SD_AS <= 1.50 (Wang & von Davier 2014); difference between human-human and human-AS exact agreement rates at EA_H,H - EA_H,AS <= 5.125% (McGraw-Hill Education CTB 2014; Pearson & ETS 2015); quadratic-weighted kappa between human and AS at QWK_H,AS >= 0.70 (Williamson, Xi, & Breyer 2012); and difference between human-human and human-AS QWK at QWK_H,H - QWK_H,AS <= 0.10 (Williamson, Xi, & Breyer 2012). [[Wood Yao Haisfield Lottridge 2021 - Standards of Best Practice in Automated Scoring]]

> [!source] CTB tightens the overall SMD threshold to 0.12.
> "Because the larger the population SMD value the more likely the subpopulation SMD value will be flagged, CTB reduced the amount of SMD separation tolerated by flagging the population SMD if it exceeds .12 in absolute value" (McGraw-Hill Education CTB 2014, p. 15, as cited by Wood et al.). [[Wood Yao Haisfield Lottridge 2021 - Standards of Best Practice in Automated Scoring]]

> [!source] Wood re-quotes a seven-item Williamson et al. 2010 acceptance checklist.
> Inside the Standard 1 exemplar-citations table, Wood reproduces a seven-item enumeration from Williamson et al. (2010, p. 7): "[1] Human scoring process and core quality; [2] Agreement of automated scores with human scores [using QWK (.70), Pearson correlations (.70), human rater reliability]; [3] Degradation from the human-human score agreement [AES-Human cannot be more than .1 lower than H1-H2]; [4] Standardized mean score difference between human and automated scores [cannot exceed .15]; [5] Threshold for human adjudication [how much difference is required before adjudication is used]; [6] Human intervention of automated scoring [response characteristics that render AES inappropriate for scoring]; [7] Evaluation at the task type and reported score level." This is the Williamson et al. 2010 version of what Williamson, Xi, & Breyer (2012) later formalized. [[Wood Yao Haisfield Lottridge 2021 - Standards of Best Practice in Automated Scoring]]

> [!source] CTB also monitors a notable reduction in exact-agreement rates.
> "CTB has found that an engine's quadratic weighted kappa (QWK) may be high even though the engine exact agreement rate in comparison is low. In this situation, engines are usually giving adjacent scores to humans so that both the percent agreement and kappa statistics are not comparable to humans. For this reason, CTB also monitors engine performance for a notable reduction (greater than 0.05 difference) in perfect agreement rates between the human-human and engine-human scores" (McGraw-Hill Education CTB 2014, p. 15, as cited by Wood et al.). [[Wood Yao Haisfield Lottridge 2021 - Standards of Best Practice in Automated Scoring]]

> [!source] Standard 2 (frequently cited in the literature) requires transparency about engine operation and construct coverage.
> "AS engines and procedures should be transparently described such that stakeholders understand how they operate and whether they satisfy construct coverage." Wood frames transparency itself as "another frequently cited standard" (p. 10). Transparency extends beyond feature sets to a five-item enumeration: (1) how data were collected for engine training, (2) how human raters produced training scores, (3) how the engine was trained, (4) how accurate the scoring models are, and (5) how AS and human scoring will be used together operationally (p. 10). [[Wood Yao Haisfield Lottridge 2021 - Standards of Best Practice in Automated Scoring]]

> [!source] Standard 3 (frequently cited) requires fairness evidence for subgroups, plus feature auditing.
> "Scores produced by AS should demonstrate fairness for all populations." Wood names subgroup H-AS mean-difference comparison as "a common approach" (p. 14), citing Madnani et al. 2017 and Williamson, Xi, & Breyer 2012. The source also cites Differential Feature Functioning (Penfield 2016; Zhang et al. 2017) and RSMTool (Madnani et al. 2017) as corroborating fairness tooling. [[Wood Yao Haisfield Lottridge 2021 - Standards of Best Practice in Automated Scoring]]

> [!source] Standard 4 requires convergent and discriminant validity studies.
> "Convergent and discriminant validity studies should be conducted to establish empirical relationships between AS scores and other constructs." The expectation is that AS scores relate to external criteria (other test sections, grades, alternate-form scores) similarly in magnitude and direction to human scores. [[Wood Yao Haisfield Lottridge 2021 - Standards of Best Practice in Automated Scoring]]

> [!source] Standard 5 ties implementation choices to stakes, item types, and human-AS integration.
> "When implementing AS, consideration must be given to contextual factors such as the stakes associated with test performance, item types, and scoring approaches that integrate human and AS." High-stakes assessments may warrant integrated scoring with a human-adjudication resolution rule; low-stakes tests may use AS alone. [[Wood Yao Haisfield Lottridge 2021 - Standards of Best Practice in Automated Scoring]]

> [!source] Standard 6 requires live process monitoring accessible to clients.
> "During live testing, accuracy and reliability of AS via process monitoring should be made available to the client." A dashboard is typical, reporting AS and human score-point distributions and human-AS agreement statistics in real time. [[Wood Yao Haisfield Lottridge 2021 - Standards of Best Practice in Automated Scoring]]

> [!source] Standard 7 requires quality checks on inputs before training.
> "It is essential to evaluate the quality of inputs to an AS engine (responses, human scoring, universe of acceptable responses) before training." Three inputs are named: non-attempts must be separated and routed through a condition-code workflow; human scoring quality must be high enough that the model is not learning noise; and the item's universe of acceptable responses must be narrow enough for AS to be suitable. [[Wood Yao Haisfield Lottridge 2021 - Standards of Best Practice in Automated Scoring]]

> [!source] Standard 8 requires documenting the impact of AS on reported scores.
> "The impact or consequences of AS on the test or reported score should be considered and documented." This includes test-taker behavior changes when AS is known to be used ("if students write differently given their knowledge that the test is scored by AS," p. 21), misclassification consequences ("potential misclassification errors and proper interpretation of proficiency classifications," p. 21-22), and claims/disclosures communicated to score users. See [[Impact and Consequences of Automated Scoring]]. [[Wood Yao Haisfield Lottridge 2021 - Standards of Best Practice in Automated Scoring]]

> [!source] Standard 9 is a less frequently recognized alert-paper standard.
> "A less frequently recognized core standard is that there should be engine procedures to identify 'alert papers' — that is, responses reflecting cheating or disturbing content, to which a school might need to respond" (Standard 9). Copy-detection filters and hybrid keyword/ML techniques are cited. [[Wood Yao Haisfield Lottridge 2021 - Standards of Best Practice in Automated Scoring]]

> [!source] Standard 10 requires recalibration policies.
> "Policies around how and when to recalibrate the engine should be established." Named triggers: major population or program changes, significant shifts in score-point distributions relative to training, and agreement-rate decay over time. [[Wood Yao Haisfield Lottridge 2021 - Standards of Best Practice in Automated Scoring]]

## Method

> [!source] Sources were selected to illustrate, not exhaust, the literature.
> "The set of sources was not expected to be exhaustive of the literature; rather, it was intended to identify those references illustrative of best practice." [[Wood Yao Haisfield Lottridge 2021 - Standards of Best Practice in Automated Scoring]]

> [!source] The standards were produced via aggregated note-taking across reviewers.
> "AS research staff divided the sources amongst themselves for further reading and standard identification. Staff members took notes where sources described a standard or best practice. Notes were aggregated across the reviewers. Commonalities across the notes were grouped together. This process resulted in 10 core high-level AS standards of best practice." [[Wood Yao Haisfield Lottridge 2021 - Standards of Best Practice in Automated Scoring]]

## Entities Mentioned

- [[Scott Wood]] — first author.
- [[Erin Yao]] — second author.
- [[Lisa Haisfield]] — third author.
- [[Susan Lottridge]] — fourth author.
- [[ACT]] — publisher.
- [[David M Williamson]], [[Xiaoming Xi]], [[F Jay Breyer]] — cited via Williamson, Xi, & Breyer (2012) as the primary reference for SMD, QWK, and QWK-degradation thresholds.
- [[Educational Testing Service]] — cited via Williamson et al. (2010), Wang & von Davier (2014), and Pearson & ETS (2015).
- [[e-rater]] — referenced in Wang & von Davier (2014) on live process monitoring.

## Concepts Covered

- [[Automated Scoring Standards of Best Practice]] — the 10-standard taxonomy.
- [[Absolute vs Relative Thresholds in Automated Scoring]] — framing distinction in Standard 1.
- [[Standard Deviation Ratio]] — Standard 1 accuracy metric.
- [[Exact Agreement Rate Difference]] — Standard 1 accuracy metric.
- [[Alert Paper Detection]] — Standard 9.
- [[Engine Recalibration Policy]] — Standard 10.
- [[Input Quality in Automated Scoring]] — Standard 7.
- [[Process Monitoring in Automated Scoring]] — Standard 6.
- [[Impact and Consequences of Automated Scoring]] — Standard 8.
- Corroborates [[Automated Scoring]], [[Human-Automated Score Agreement]], [[Standardized Mean Score Difference]], [[Fairness in Automated Scoring]], [[Construct Representation in Automated Scoring]], [[Automated Scoring Implementation Models]], [[Quadratic-Weighted Kappa]].

## Notes

> [!analysis] Wood is a codifier, not an originator.
> The paper's contribution is synthesis: each threshold in Table 2 is attributed to a primary reference. Wood et al. consolidate what already existed in the literature into a compact ten-item taxonomy rather than proposing new metrics. When citing this source, distinguish "Wood 2021 codifies X from primary source Y" from "Wood 2021 proposes X."

> [!analysis] Wood extends Williamson 2012 rather than replacing it.
> Williamson, Xi, & Breyer (2012) contributes four of the five metrics in Table 2 and provides the framework backbone (construct, agreement, fairness, implementation-model ordering). Wood adds the SD ratio, the exact-agreement-rate difference, and five non-Williamson standards (process monitoring, input quality, impact documentation, alert-paper detection, recalibration policy) that had appeared separately in other literature. See [[Williamson 2012 vs Wood 2021 - Automated Scoring Standards]].

> [!analysis] The conservative CTB tightening of SMD to 0.12 contradicts Williamson's 0.15.
> McGraw-Hill Education CTB (2014), as cited by Wood, reduced the population SMD flag from 0.15 to 0.12, explicitly to reduce the probability of subgroup-level false negatives. Wood does not take a position between the two thresholds; the wiki surfaces this as a live disagreement on [[Standardized Mean Score Difference]].

> [!gap] PDF conversion omitted one graphic on page 1.
> The raw markdown contains `==> picture [129 x 34] intentionally omitted <==` immediately after the header. Given its dimensions and position, this is almost certainly the ACT logo and carries no substantive content.

> [!gap] Extraction coverage of this ingest (self-audit, 2026-04-16)
>
> **1. Missed claims**
> - Standard 5's CTB "read and read behind" three-axis categorization — (a) number of raters, (b) type of first/second rater (human or AS), (c) adjudication rule (non-exact vs. non-adjacent) — quoted on p. 19-20 is not carried into [[Automated Scoring Implementation Models]] or the source summary.
> - Standard 8's concrete test-taker-behavior claim ("if students write differently given their knowledge that the test is scored by AS," p. 21) and its misclassification/proficiency-interpretation example (p. 21-22) are absent — Standard 8 has no dedicated concept page or corroboration-update target.
> - The introduction's three motivations for unified AS standards (emerging-tech guidance, cross-disciplinary alignment, stakeholder accountability, p. 2) are compressed to the existence claim.
> - The Williamson et al. (2010) seven-item list quoted inside the Standard 1 table (p. 8, items [1]-[7]) — a key secondary-source enumeration — is not picked up anywhere.
> - Standard 2's item-type suitability examples (portfolio assessment, hand-drawn input as poorly suited to AS, p. 10) are not represented.
> - Standard 2's paper/online comparability clause (p. 10) is absent from the wiki.
>
> **2. Missed entities/concepts**
> - Bridgeman (2013) — the originator, quoted within the CTB block, of the "raters truncating the rubric score range" observation that motivates the exact-agreement-rate rule. [[Exact Agreement Rate Difference]] attributes to CTB without naming Bridgeman as the ultimate source.
> - Standard 8 (Impact and Consequences) has no concept page and no corroboration-update target, unlike Standards 6/7/9/10 (dedicated pages) and Standards 1/2/3/4/5 (update targets). Asymmetric coverage of Wood's taxonomy.
>
> **3. Narrowed enumerations**
> - Standard 2's five-item transparency list (p. 10: data collection, training scores, engine training, model accuracy, human-AS operational use) is paraphrased in the source summary but not preserved as an enumeration on [[Construct Representation in Automated Scoring]] or elsewhere.
> - Four source categories, three recalibration triggers, five Table-2 metrics: preserved. OK.
>
> **4. Attribution issues**
> - [[Fairness in Automated Scoring]]'s [!source] for DFF tooling (Penfield 2016; Zhang et al. 2017) reads as if Wood originates the methodology. Preferable: "as cited in Wood 2021." Minor.
> - [[Alert Paper Detection]] reproduces Wood's thin Williamson-2012 attribution for alert papers faithfully; Williamson 2012 mentions cheating only as a passing validity-challenge note, so the Wood-side citation is itself weak. The wiki callout is correct; the upstream attribution deserves an [!analysis] caveat.
> - Pearson & ETS 2014 (Wood's Table 2) vs. 2015 (Wood's references list): handled correctly on [[Exact Agreement Rate Difference]].
>
> **5. Reconstructed-figure issues**
> - None. The only image artifact is the p. 1 ACT logo, tagged [!gap] above.
>
> **6. Scoping-clause violations**
> - Wood's "frequently cited" qualifier for Standards 1/2/3 is dropped in the source-summary standard-level callouts. Minor.
> - Wood's "a common approach" framing on [[Fairness in Automated Scoring]]'s Wood-side treatment of subgroup H-AS mean differences is not preserved. Minor.
>
> **7. Contradictions handling**
> - CTB 0.12 vs. Williamson 0.15 SMD: surfaced across [[Standardized Mean Score Difference]], [[Human-Automated Score Agreement]], [[Automated Scoring Standards of Best Practice]] Contradictions, source summary, and comparison page. Strong.
> - CTB 5.0-pt vs. 5.125% EA difference: surfaced in [[Exact Agreement Rate Difference]] and [[Human-Automated Score Agreement]] as a [!gap]. Good.
> - Pearson & ETS 2014/2015: flagged on [[Exact Agreement Rate Difference]]. Good.
> - Source-internal CCSSO name variants: Wood has two distinct typos ("Schools Officers" on p. 23 of Standard 10; "Schools, & Association..." dropping "Officers" on p. 21 of Standard 9). Canonical: "Council of Chief State School Officers." Post-audit: both variants are quoted verbatim with [!analysis] notes on [[Engine Recalibration Policy]] and [[Alert Paper Detection]] flagging the typos. Resolved.
>
> **8. Schema issues**
> - [[ACT]] entity page is thin (three [!source] callouts, one [!gap], no Key Claims) but acceptable for a peripheral single-source entity.
> - All frontmatter, TLDRs, and wikilinks resolve. `raw_path` and `raw_hash` present on the source summary.
>
> **9. Overall assessment**
> Faithful and thorough. All ten Standards are named; the two new imported metrics (SD ratio, exact-agreement difference) got dedicated pages with primary-reference attribution; the Williamson-vs-Wood comparison is well-structured; CTB's 0.12 tightening is handled well across multiple pages without adjudicating it. Most valuable follow-up targets: (1) create a concept page or update-target for Standard 8 (Impact and Consequences) to eliminate the taxonomy asymmetry; (2) restore the five-item transparency enumeration from Standard 2 on [[Construct Representation in Automated Scoring]]; (3) preserve the CTB "read and read behind" three-axis categorization on [[Automated Scoring Implementation Models]]; (4) credit Bridgeman (2013) on [[Exact Agreement Rate Difference]].
