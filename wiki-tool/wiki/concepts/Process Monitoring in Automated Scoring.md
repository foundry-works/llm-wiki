---
type: concept
sources:
  - "[[Wood Yao Haisfield Lottridge 2021 - Standards of Best Practice in Automated Scoring]]"
created: "2026-04-16"
updated: "2026-04-16"
status: current
tags: [automated-scoring, monitoring, operations, transparency, audit]
---

> [!tldr]
> Wood's Standard 6 requires that during live testing, scoring-process accuracy and reliability be made available to the client, typically via a real-time dashboard reporting AS score distributions, human score distributions, and human-AS agreement statistics when human scores are present.

## Definition

> [!source] Standard 6 requires client-accessible process monitoring.
> "Providing clients with access to scoring process monitoring is another AS standard crucial to ensure accuracy, reliability, and transparency (Wang & von Davier, 2014). Typically, a dashboard is provided to allow clients or a third party a way to audit scoring accuracy and error rates in real time. This provides a way for scoring errors to be immediately identified and addressed during a testing or scoring event." [[Wood Yao Haisfield Lottridge 2021 - Standards of Best Practice in Automated Scoring]]

> [!source] Dashboard metrics include score distributions and agreement statistics.
> "Reported metrics should include AS score point distributions, human score point distributions, and human-AS agreement statistics, if human scores are available." [[Wood Yao Haisfield Lottridge 2021 - Standards of Best Practice in Automated Scoring]]

## Supporting references

> [!source] AERA/APA/NCME Standard 6.9 covers scoring quality control.
> "Those responsible for test scoring should establish and document quality control processes and criteria. Adequate training should be provided. The quality of scoring should be monitored and documented. Any systematic source of scoring errors should be documented and corrected" (AERA, APA, & NCME, 2014, Standard 6.9, p. 118, as cited by Wood et al.). [[Wood Yao Haisfield Lottridge 2021 - Standards of Best Practice in Automated Scoring]]

> [!source] CCSSO/ATP requires client access to accuracy analyses.
> "Any measure or analysis used to check accuracy and reliability of the scoring process should be made available for the client's review" (CCSSO & ATP 2013, p. 131, as cited by Wood et al.). [[Wood Yao Haisfield Lottridge 2021 - Standards of Best Practice in Automated Scoring]]

> [!source] ITC requires independent monitoring.
> "Independent Monitoring of Quality Control Procedures... should be carried out in collaboration with all stakeholders, with the aim of auditing specific processes, for example, monitoring inter-rater reliability and checking data entry error rates" (ITC 2014a, p. 204, as cited by Wood et al.). [[Wood Yao Haisfield Lottridge 2021 - Standards of Best Practice in Automated Scoring]]

## Key Claims

> [!analysis] Standard 6 is the operational feed for Standard 10.
> Standard 10 ([[Engine Recalibration Policy]]) lists "decrease in human-AS agreement over time" as a recalibration trigger. Standard 6 is how that decrease becomes visible. Without live dashboards, drift is only detectable post hoc in annual reviews.

> [!analysis] Third-party access is a governance choice, not a technical one.
> Wood notes that dashboards can be provided "to allow clients or a third party a way to audit." That framing is unusual in ML-ops literature, which typically treats monitoring as internal. The assessment framing centralizes client audit rights as a matter of best practice, which shifts dashboard design toward accessibility and interpretability for non-developers.

> [!analysis] Real-time monitoring requires human score feeds.
> Wood's "if human scores are available" qualifier matters. In Model 5 deployments (AS alone, per [[Automated Scoring Implementation Models]]), there is no human feed to monitor against. That reduces Standard 6's monitoring to distribution checks against historical baselines, which are weaker than comparison to concurrent human raters.

## Connections

- Standard 6 of [[Automated Scoring Standards of Best Practice]].
- Feeds [[Engine Recalibration Policy]] (Standard 10) via agreement-decay signals.
- Reports on [[Human-Automated Score Agreement]] and its component metrics.
- Typical deployment context: models in [[Automated Scoring Implementation Models]] that retain human involvement (Models 2 and 3); weakened under Model 5.

## Open Questions

> [!gap] No guidance on dashboard metrics for AS-only deployments.
> Wood's monitoring recipe assumes concurrent human scores. Model 5 programs need alternative monitoring targets (e.g., historical-baseline distributions, adversarial-response flagging rates), which Wood does not specify.

> [!gap] No latency or refresh-rate requirements.
> "Real time" is used but not quantified. A dashboard that refreshes daily is technically real-time but may miss session-level anomalies.

> [!gap] No governance rule for who acts on alerts.
> Dashboards produce alerts; someone needs to respond. Wood does not specify role ownership between vendor and client.
