ACT Research | Technical Brief | July 2021 

1 

## **Establishing Standards of Best Practice in Automated Scoring** 

## **Scott Wood, Erin Yao, Lisa Haisfield, and Susan Lottridge** 

## **Introduction** 

Many professions have published standards of best practices for their members to follow, which provide direction to professionals about how best to conduct their work. Some standards include ethical guidelines to ensure that professionals conduct their business in ways that are fair and considerate toward others. Most importantly, published standards provide confidence to stakeholders, including customers, who are invested in the work that professionals offer, by documenting expectations of best practice and ethical professional behavior. 

For professionals in the assessment industry, the _Standards for Educational and Psychological Testing_ (American Educational Research Association [AERA], American Psychological Association [APA], & National Council on Measurement in Education [NCME], 2014) are frequently cited as standards of best practice and ethical behavior. For professionals involved in large-scale assessment at the state level, the _Operational Best Practices for Statewide Large-Scale Assessment Programs_ provide additional guidelines (Council of Chief State School Officers [CCSSO] & Association of Test Publishers [ATP], 2013). The International Test Commission maintains six sets of published guidelines for assessment: _The ITC Guidelines on Adapting Tests_ (International Test Commission, 2017), _The ITC Guidelines on Test Use_ (International Test Commission, 2001), _The ITC Guidelines on Computer-Based and Internet-delivered Testing_ (International Test Commission, 2006), _The ITC Guidelines on Quality Control in Scoring, Test Analysis and Reporting of Test Scores_ (International Test Commission, 2014a), _The ITC Guidelines on the Security of Tests, Examinations, and Other Assessments_ (International Test Commission, 2014b), and _The ITC Guidelines on Practitioner Use of Test Revisions, Obsolete Tests, and Test Disposal_ (International Test Commission, 2015). 

Professions in fields that overlap with educational assessment may have their own standards of best practice. For example, statisticians have the _Ethical Guidelines for Statistical Practice_ (American Statistical Association, 2018). Data scientists have the 

**==> picture [129 x 34] intentionally omitted <==**

Copyright ® 2021 by ACT, Inc. All rights reserved. | 2100 

ACT Research | Technical Brief | July 2021 

2 

_Data Science Code of Professional Conduct_ (Data Science Association, n.d.). Linguists have the _Linguistic Society of America Code of Ethics_ (Linguistic Society of America, 2019). Educational researchers have the _American Educational Research Association Code of Ethics_ (American Educational Research Association, 2011). Computer 

programmers have both the _Association of Computing Machinery Code of Ethics and Professional Conduct_ (Association for Computing Machinery, 2018) and the _Association of Computing Machinery/International of Electrical and Electronics Engineers Computer Society Software Engineering Code of Ethics and Professional Practice_ (Gotterbarn, Miller, & Rogerson, 1997). 

For assessment professionals who are also automated scoring (AS) professionals, there is no single set of standards of best practice. Certainly, standards can be extracted from the documents cited above, as AS professionals are involved with assessment, statistics, data science, linguistics, educational research, and computer programming. Additional standards can be extracted from seminal papers, books, and technical reports in the field of AS. However, these standards are not centralized in one location for AS professionals and AS consumers to utilize. 

This paper reviews the assessment and AS literature to identify key standards of best practice and ethical behavior for AS professionals and codifies those standards in a single resource. Having a unified set of AS standards is important for several reasons. First, given that AS is an emerging technology in educational assessment, it is important to establish guidelines of good practice for professionals and stakeholders learning to use this new technology. Second, due to the wide variety of professionals involved in AS technology development (e.g., psychometricians, linguists, data scientists, and computer programmers), a unified set of standards would guide these diverse professionals toward common objectives. Third, and most importantly, having standards for which stakeholders can hold AS professionals accountable can provide stakeholders with greater confidence in the use of AS. 

The next section describes the methods used to identify, review, and summarize the standards and recommendations in the AS literature. This is followed by a summary of 10 important, high-level standards for AS professionals. Each standard is supported by exemplar citations from the AS literature. A summary and references list appear at the end of the report. 

## **Methods** 

## **Source Identification** 

AS research staff searched for documents that referenced AS standards, processes, recommendations, or implementations. The set of sources was not expected to be 

ACT Research | Technical Brief | July 2021 

3 

exhaustive of the literature; rather, it was intended to identify those references illustrative of best practice. 

The sources can be divided into a few categories: 

- Standards, guidelines, or recommendations from professional organizations 

- Published work offering frameworks on the use and evaluation of AS 

- Results of large-scale programs that use standards to evaluate AS 

- Published work offering frameworks on the evaluation of machine learning models 

In all, 16 sources were identified as representative of the literature. Table 1 presents the 16 sources, organized by the four categories above. Five sources represented standards, guidelines, or recommendations from professional organizations. Six sources were published works offering frameworks on the evaluation of AS. Four sources cited results and evaluation standards on large-scale programs, including national programs. One source provided evaluation standards used in machine learning model evaluations—a set of evaluations broader than those relevant to AS. This last source was included because it provided an excellent overview of machine learning evaluation methods for the novice user of machine learning. 

**Table 1.** Sources Used for Standards Review 

**Standards, Guidelines, or Recommendations from Professional Organizations** American Educational Research Association, American Psychological Association, & National Council on Measurement in Education. (2014). _Standards for educational and psychological testing_ . Washington, DC: American Educational Research Association. Council of Chief State School Officers, & Association of Test Publishers. (2013). Scoring. In _Operational best practices for statewide large-scale assessment programs_ . (pp. 125–134) Washington, DC: Council of Chief State School Officers and the Association of Test Publishers. International Test Commission. (2014a). ITC guidelines on quality control in scoring, test analysis, and reporting of test scores. _International Journal of Testing, 14_ (3), 195–217. Joint Committee on Testing Practices. (2004). _Code of fair testing practices in education_ . Washington, DC: Joint Committee on Testing Practices. _https://www.apa.org/science/programs/testing/fair-testing.pdf_ . International Test Commission. (2006). International guidelines on computer-based and internet-delivered testing. _International Journal of Testing, 6_ (2), 143–171. 

ACT Research | Technical Brief | July 2021 

4 

## **Published Work Offering Frameworks on the Use and Evaluation of Automated Scoring** 

Madnani, N., Loukina, A., von Davier, A., Burstein, J., & Cahill, A. (2017, April). Building better open-source tools to support fairness in automated scoring. In D. Hovy, S. Spruit, M. Mitchell, E. Bender, M. Strube, & H. Wallach (Eds.), _Proceedings of the first ACL workshop on ethics in natural language processing_ (pp. 41–52). 

Powers, D. E., Escoffery, D. S., & Duchnowski, M. P. (2015). Validating automated essay scoring: A (modest) refinement of the “gold standard.” _Applied Measurement in Education, 28_ (2), 130–142. 

Shermis, M. D., Burstein, J., Elliot, N., Miel, S., & Foltz, P. (2016). Automated writing evaluation: An expanding body of knowledge. In C. A. MacArthur, S. Graham, & J. Fitzgerald (Eds.), _Handbook of writing research_ (2nd ed., pp. 395–409). New York, NY: Guilford. 

Williamson, D. M., Bennett, R. E., Lazer, S., Bernstein, J., Foltz, P., Landauer, T. K., Rubin, D. 

P., Way, W. D., & Sweeney, K. (2010). _Automated scoring for the assessment of Common Core Standards_ . ETS, Pearson, & The College Board. 

Yang, Y., Buckendahl, C. W., Juszkiewicz, P. J., & Bhola, D. S. (2002). A review of strategies for validating computer-automated scoring. _Applied Measurement in Education, 15_ (4), 391–412. 

Yang, Y., Buckendahl, C. W., Juszkiewicz, P. J., & Bhola, D. S. (n.d.). _Validating computer automated scoring: A conceptual framework and a review of strategies_ [Unpublished manuscript]. 

**Results of Large-Scale Programs on the Use of Standards to Evaluate and Monitor Automated Scoring** 

McGraw-Hill Education CTB (2014). _Smarter Balanced Assessment Consortium--Field_ 

_test: Automated scoring research studies_ . Monterey, CA: Smarter Balanced Assessment Consortium. 

Pearson, & Educational Testing Service. (2015). _Research results of PARCC automated scoring proof of concept study_ . 

Wang, Z., & von Davier, A. A. (2014). _Monitoring of scoring using the e-rater automated scoring system and human raters on a writing test_ (ETS Research Report ETS RR-1404). Princeton, NJ: ETS. 

Williamson, D. M., Xi, X., & Breyer, F. J. (2012). A framework for evaluation and use of 

automated scoring. _Educational Measurement: Issues and Practice, 31_ (1), 2–13. 

**Published Work Offering Frameworks on the Evaluation of Machine Learning Models** 

Zheng, A. (2015). _Evaluating machine learning models: A beginner's guide to key concepts and pitfalls_ . Sebastopol, CA: O'Reilly Media. 

## **Source Review and Summarization** 

AS research staff divided the sources amongst themselves for further reading and standard identification. Staff members took notes where sources described a 

ACT Research | Technical Brief | July 2021 

5 

standard or best practice. Notes were aggregated across the reviewers. Commonalities across the notes were grouped together. This process resulted in 10 core high-level AS standards of best practice. All authors reviewed the 10 core standards and refined the language based on experience with AS projects. 

## **Results** 

This section presents the key standards of best practice and ethical behavior for AS professionals, as identified by the authors of this report. 

## **Standard 1: Automated scores should achieve industry absolute and relative thresholds for accuracy when compared with human scores.** 

Numerous publications have identified AS and human scoring metrics suitable for evaluating the reliability and accuracy of AS scoring. Such metrics can be evaluated via _absolute_ or _relative_ thresholds. Absolute thresholds are used when a metric is compared to a constant value, such as when a human-AS quadratic weighted kappa is compared to 0.70. Relative thresholds are used when a metric is compared to a corresponding human or human-human metric for the item, such as when a humanAS quadratic weighted kappa is compared to the human-human metric. 

AS agreement with a human rater is frequently cited in the literature. At a minimum, desired levels of agreement with human raters at the summed score and trait level must be demonstrated. These statistics demonstrate consistency in scoring with an expert human rater using statistics such as exact agreement, quadratic weighted kappa, and standardized mean differences (Williamson, Xi, & Breyer, 2012). 

Table 2 includes several common metrics used to evaluate human-AS accuracy, including the standardized mean difference, the standard deviation (SD) ratio, the difference in exact agreement rates, quadratic weighted kappa, and the difference in quadratic weighted kappa. Included are thresholds recommended by AS professionals. Models meeting these thresholds are considered appropriate for operational use. 

ACT Research | Technical Brief | July 2021 

6 

**Table 2.** Common Metrics for Evaluating AS Accuracy, with Thresholds 

|**Metric**|**Threshold**|**Reference**|
|---|---|---|
|Standardized Mean|-0.15 ≤ SMD ≤ 0.15|Williamson, Xi, & Breyer|
|Difference between||(2012)|
|Human and AS|||
|Standard Deviation|2/3 ≤ (SDHuman/ SDAS) ≤ 1.50|Wang & von Davier|
|(SD) Ratio between||(2014)|
|Human and AS|||
|Difference between|EAHuman,Human- EAHuman,AS≤ 5.125%|McGraw-Hill Education|
|Human-Human and||CTB (2014); Pearson &|
|Human-AS Exact||ETS (2014)|
|Agreement Rate|||
|Quadratic Weighted|<br>QWKHuman,AS≥ 0.70|Williamson, Xi, & Breyer|
|Kappa between||(2012)|
|Human and AS|||
|Difference between|QWKHuman,Human– QWKHuman,AS≤ 0.10|Williamson, Xi, & Breyer|
|Human-Human and||(2012)|
|Human-AS|||
|Quadratic Weighted|||
|Kappa|||



Table 3 provides exemplar citations from the literature review that support this standard. 

ACT Research | Technical Brief | July 2021 

7 

**Table 3.** Exemplar Citations Supporting Standard 1 

|**Source**|**Examples**|
|---|---|
|**AERA, APA, &**<br>**NCME, 2014**|“Standard 2.7: When subjective judgement enters into test scoring,<br>evidence should be provided on both interrater consistency in scoring<br>and within-examinee consistency over repeated measurements. A clear<br>distinction should be made among reliability data based on (a)<br>independent panels of raters scoring the same performances or<br>products, (b) a single panel scoring successive performances or new<br>products, and (c) independent panels scoring successive performances<br>or newproducts” (p. 44).|
||“[Standard 2.7] Comment: Task to task variation in the quality of an<br>examinee’s performance and rater to rater consistencies in scoring<br>represent independent sources of measurement error. Reports of<br>reliability/precision studies should make clear which of these sources are<br>reflected in the data. Generalizability studies and variance component<br>analyses can be helpful in estimating the error variances arising from<br>each source of error. These analyses can provide separate error variance<br>estimates for tasks, for judges, and for occasions within the time period<br>of trait stability. Information should be provided on the qualifications<br>and trainings of the judges used in the reliability studies. Interrater or<br>interobserver agreement may be particularly important for ratings and<br>observational data that involve subtle discriminations. It should be noted,<br>however, that when raters evaluate positively correlated characteristics, a<br>favorable or unfavorable assessment of one trait might color their<br>opinions of other traits. Moreover, high interrater consistency does not<br>imply high examinee consistency from task to task. Therefore, interrater<br>agreement does notguarantee high reliabilityof examinee scores” (p. 44).|
||“Standard 2.8: When constructed-response tests are scored locally,<br>reliability/precision data should be gathered and reported for the local<br>scoringwhen adequate-size samples are available” (p. 44).|
|**Williamson,**<br>**Xi, & Breyer,**<br>**2012**|“The model building and evaluation process for automated scoring is<br>largely dependent on the quality of human scores...[I]f the inter-rater<br>agreement of independent human raters is low, especially below the .70<br>threshold, then automated scoring is disadvantaged in demonstrating<br>this level ofperformance…” (p. 7).|
||“In typical practice at ETS, we first conduct the empirical associations<br>with human score (agreement, degradation, and standardized mean<br>score difference) at the task level. At the task type level (aggregated<br>results across the individual tasks within the task type) and the reported<br>section score level the entire contingent of measures discussed above are<br>also employed in the evaluation ofperformance” (p. 8).|



ACT Research | Technical Brief | July 2021 

8 

||“Empirical Performance: Associated with Typical Scoring Method<br>(Human Scores). This entails making sure [1] Human scoring process and<br>core quality …, [2] Agreement of automated scores with human scores”<br>using QWK (.70), Pearson correlations (.70), human rater reliability among<br>other raters (so H1-H2), ”[3] Degradation from the human-human score<br>agreement” AES-Human cannot be more than .1 lower than H1-H2 to<br>ensure that .70 QWK doesn’t allow a pass for if the AES model is deficient<br>as compared to the H1-H2 reliability, “[4] Standardized mean score<br>difference between human and automated scores” SMD between human<br>and automated scores cannot exceed .15, “[5] Threshold for human<br>adjudication” how much difference is required before adjudication is<br>used, “[6] Human intervention of automated scoring” response<br>characteristics that render AES inappropriate for scoring, and “[7]<br>Evaluation at the task type and reported score level” look at distribution<br>of changes in reported scores that would results from AES at the task<br>score level (p. 7).|
|---|---|
||“The model building and evaluation process for automated scoring is<br>largely dependent on the quality of human scores...[I]f the inter-rater<br>agreement of independent human raters is low, especially below the .70<br>threshold, then automated scoring is disadvantaged in demonstrating<br>this level ofperformance…” (p. 7).|
|**CCSSO & ATP,**<br>**2013**|“When Al engines are used in a place of human scoring, or for<br>confirmation or quality control of human scoring, scoring procedures<br>should meet the same standards for accuracy and reliability that exist for<br>human scoringof the same item type” (p. 131).|
|**Yang et al.,**<br>**2002**|“…[A] straightforward way to demonstrate the accuracy and<br>appropriateness of CAS [computer-automated scoring] -system-<br>generated scores is to evaluate their relationship to the scores assigned<br>by human scorers to the same item (e.g., task, prompt) or the same<br>scores given by CAS systems have a high level of agreement with those<br>trained scorers….Furthermore, one can also compare agreement between<br>two human experts and between a CAS system and a human expert to<br>demonstrate that a CAS system is no less consistent than human<br>experts” (p. 400).|
||“…[O]ne can investigate the reliability of CAS-system-generated scores by<br>correlating them with expert scores as well as by comparing the<br>reliability of scores assigned by human scorers and by a CAS system” (p.<br>400).|
||“It is also possible to approximate the true scores by using the consensus<br>scores given by a group of experts…These consensus scores…are the<br>scores a group of experts agreed on after discussion” (p. 401).<br>“If a CAS system produces scores that agree completely with a human<br>rater, it may indicate that the system not only modeled the construct-<br>relevant aspects of a scoring process but also possibly emulated the<br>personal and situational characteristics that may contribute to the errors<br>and biases in measurement” (p. 401).|



ACT Research | Technical Brief | July 2021 

9 

|**Williamson et**<br>**al., 2010**|“Automated scores are consistent with the scores from expert human<br>grader” (p. 5). The distribution of scores should approximate human<br>scores of essays.|
|---|---|
||“This similarity is typically demonstrated through statistical measures of<br>agreement between automated and human scores, such as correlations<br>and weighted kappa (rather than percent agreement, which may<br>overestimate the agreement rate between automated and human<br>scores)” (p. 5).|
|**Shermis et al.,**<br>**2016**|“Individual-response-level measures included exact agreement,<br>exact+adjacent agreement, kappa, quadratic weighted kappa, and the<br>Pearsonproduct moment correlation” (p. 402).|
|**Pearson &**<br>**ETS, 2015**|“Evaluation criteria for the scoring models was based on criteria most<br>often used in evaluating automated scoring…and consisted of the<br>following measures of inter-rater agreement: Pearson correlation,<br>quadratic-weighted kappa, exact and adjacent agreement, and<br>standardized mean difference” (p. 9-10). The resource also provides<br>summed score metrics and by trait metrics, as well as score point<br>distribution metrics, recall,precision, and F1.|
||“Throughout the report, we include discussions of the percentage of<br>prompt / trait combinations that might be considered to perform less<br>well using Williamson et al.’s criteria, as a way of comparing human<br>performance to automated scoring performance” (p. 10). This resource<br>discusses the typical metrics between human-machine difference<br>(relative) and absolute threshold overall for Pearson Correlation, QWK<br>[quadratic weighted kappa], EA [exact agreement], and SMD<br>[standardized mean difference] (p. 11).|
|**Yang et al.,**<br>**n.d.**|“First, one should perform a test on the similarity of score distributions<br>produced by the raters. This can be done by testing marginal<br>homogeneity of the two raters’ scores … If marginal homogeneity is not<br>rejected, Kappa, or preferably, according to Zwick (1988), Scott's π<br>coefficient can be used to further assess chance-corrected agreement” (p.<br>16)|
||“The first series of analyses examined the agreement between the<br>pairwise comparisons of total score distributions. These analyses utilized<br>two non-parametric tests, the Kolmogorov-Smirnov (K-S) two-sample<br>test and the Wilcoxon-Mann-Whitney (W-M-W) test….[S]tatistical<br>significance tests were conducted usingan alpha level of .10” (p. 22).|



ACT Research | Technical Brief | July 2021 

10 

“Bridgeman (2013) noted that the high agreement between two raters can occur when raters are truncating the rubric score range. CTB has found that an engine’s quadratic weighted kappa (QWK) may be high even though the engine exact agreement rate in comparison is low. In this situation, engines are usually giving adjacent scores to humans so that both the percent agreement and kappa statistics are not comparable to humans. For this reason, CTB also monitors engine performance for a notable reduction (greater than 0.05 difference) in perfect agreement rates between the human-human and engine-human scores” (p. 15). Statistical criteria can be divided into 3 broad categories: evaluated against the final human scores of records, evaluated against **McGraw-Hill** the inter-rater performance of the two initial human raters, and **Education** evaluated for the performance in different subgroups. **CTB, 2014** “Note the difference between the evaluation criteria in the first and second category. For the first category, the scores assigned by the Automated Scoring system are compared against the final human scores of record. For the second category, statistics from the first category are compared against performance of the two human raters…In other words, evaluation of the criteria of the second category should be subsequent to evaluation of the criteria in the first category. Hence, one could argue that these three categories constitute a hierarchy. For example, if an Automated Scoring system does not meet the performance criteria for the entire population, then evaluating its performance on subgroups may be less relevant” (p. 17). 

## **Standard 2: AS engines and procedures should be transparently described such that stakeholders understand how they operate and whether they satisfy construct coverage.** 

Transparency about what response features are used in AS is another frequently cited standard. This information is crucial to determine if an AS engine can properly score responses to items designed to elicit evidence of a certain construct (International Test Commission, 2006). Construct coverage is the ability of an AS engine’s candidate feature set to reflect the construct being assessed. 

For example, in essay scoring, an AS score that primarily depends on word count for scoring would be called into question given this standard (Williamson et al., 2010). Word count does not have a meaningful relationship to the quality of writing or knowledge of content and therefore should not be utilized as the sole determinant of an AS score. In addition, the features used to predict scores may not adequately represent the breadth of the construct, thereby introducing bias. 

Transparency in AS goes beyond the candidate feature set used for training the engine. Where possible, all aspects of human and automated scoring should be documented and made available to stakeholders. Such information can include: 

ACT Research | Technical Brief | July 2021 

11 

- how the data were collected for engine training, 

- how human raters produced scores for the training sample, 

- how the engine was trained, 

- how accurate the scoring models are, and 

- how AS and human scoring will be used together for operational scoring. 

If both paper and online tests are administered, comparability studies should make it clear when AS will be used. If human scoring will be used for paper testing and AS for online tests, comparability studies are necessary to show that one format will not produce biased scores relative to the other. 

Some item types are better suited for automated scoring than others. For example, portfolio assessment and items involving hand-drawn input would be challenging to score accurately via AS. If an assessment program uses AS for a unique item type, AS professionals should be transparent about why AS was chosen as a scoring method, including evidence that AS scores a unique item type accurately. 

Table 4 provides exemplar citations from the literature review that support this standard. 

**Table 4.** Exemplar Citations Supporting Standard 2 

|**Source**|**Examples**|
|---|---|
|**ITC, 2006**|In a section titled “Ensure knowledge, competence, and appropriate use<br>of CBT [computer-based testing]/Internet testing”: “Document the<br>constructs intended to be measured and investigated” (p. 153).|
||“Ensure all those involved in test design and development…have<br>sufficient knowledge and competence to develop CBT/Internet tests” (p.<br>153).|
||“Consider the psychometric qualities of the CBT/Internet test.” For<br>example, provide “documentation for psychometric properties of the<br>CBT/Internet test” and “ensure that current psychometric standards (test<br>reliability, validity, etc.) apply even though the way in which the tests are<br>developed and delivered maydiffer” (p. 155).|
||One section focuses on ensuring that an online test (CBT) is equivalent to<br>a paper test, and certain aspects might be likened to human scorers:<br>“Provide clear documented evidence of the equivalence between the<br>CBT/Internet test and noncomputer version…have comparable<br>reliabilities…correlate each other at the expected level from the reliability<br>estimates” (p. 156).|



ACT Research | Technical Brief | July 2021 

12 

|**Source**|**Examples**|
|---|---|
|**Williamson et**<br>**al., 2010**|“…[T]he most notable limitation is that automated scoring assumes<br>computer test delivery and data capture, which in turn may require an<br>equation editor or graphing interface that students can use comfortably”<br>(p. 2).|
|**AERA, APA, &**<br>**NCME, 2014**|“Standard 1.9: When a validation rests in part on the opinions or decisions<br>of expert judges, observers, or raters, procedures for selecting such<br>experts and for eliciting judgments or ratings should be fully described.<br>The qualifications and experience of the judges should be presented. The<br>description of procedures should include any training and instructions<br>provided, should indicate whether participants reached their decisions<br>independently, and should report the level of agreement reached. If<br>participants interacted with one another or exchanged information, the<br>procedures through which they may have influenced one another should<br>be set forth” (p. 25–26).|
||“Standard 4.18: Procedures for scoring and, if relevant, scoring criteria,<br>should be presented by the test developer with sufficient detail and<br>clarity to maximize accuracy of scoring. Instructions for using rating<br>scales or deriving scores obtained by coding, scaling, or classifying<br>constructed responses should be clear. This is especially critical for<br>constructed-response items such as performance tasks, portfolios, and<br>essays” (p. 91).|
||“Standard 4.20: The process for selecting, training, qualifying, and<br>monitoring scorers should be specified by the test developer. The<br>training materials, such as the scoring rubrics and examples of test<br>takers’ responses that illustrate the levels on the rubric score scale, and<br>the procedures for training scorers should result in a degree of accuracy<br>and agreement among scorers that allows for the scores to be<br>interpreted as originally intended by the test developer. Specifications<br>should also describe processes for assessing scorer consistency and<br>potential drift over time in raters’ scoring” (p. 92).|
||“Standard 4.21: When test users are responsible for scoring and scoring<br>requires scorer judgement, the test user is responsible for providing<br>adequate training and instruction to scorers and for examining scorer<br>agreement and accuracy. The test developer should document the<br>expected level of scorer agreement and accuracy and should provide as<br>much technical guidance as possible to aid users in satisfying this<br>standard” (p. 92).|
||“Standard 6.8: Those responsible for test scoring should establish scoring<br>protocols. Test scoring that involves human judgment should include<br>rubrics, procedures, and criteria for scoring. When scoring of complex<br>responses is done by computer, the accuracy of the algorithm and<br>processes should be documented” (p. 118).|



ACT Research | Technical Brief | July 2021 

13 

|**Source**|**Examples**|
|---|---|
||“Standard 6.8: Those responsible for test scoring should establish scoring<br>protocols. Test scoring that involves human judgment should include<br>rubrics, procedures, and criteria for scoring. When scoring of complex<br>responses is done by computer, the accuracy of the algorithm and<br>processes should be documented” (p. 118).|
||“Standard 6.11: When automatically generated interpretations of test<br>response protocols or test performance are reported, the sources,<br>rationale, and empirical basis for these interpretations should be<br>available, and their limitations should be described” (p. 119).|
||“Standard 4.19: When automated algorithms are to be used to score<br>complex examinee responses, characteristics at each score level should<br>be documented along with the theoretical and empirical bases for the<br>use of the algorithms” (p. 92).|
|**CCSSO & ATP,**<br>**2013**|“Any measure or analysis used to check accuracy and reliability of the<br>scoring process should be made available for the client’s review” (p. 130).|
|**Williamson et**<br>**al., 2010**|“In the area of mathematics, the performance of automated scoring<br>systems is typically quite robust when the response format is<br>constrained” (p. 2).|
||“The agreement between human raters may be lower than desired. Thus,<br>agreement with human scores may not always be a sufficient<br>accomplishment” (p. 2).|
||“Develop items with definitive correct answers that the automated<br>scoring system can verify” (p. 3) Opinion writing is difficult for AES<br>systems to discern.|
||“Also, it is often the case that human raters score short content responses<br>at considerably higher agreement rates than they do essay responses,<br>which creates a higher standard for automated scoring methods to<br>attain” (p. 3).|
||“The way automated scores are produced is understandable and<br>somewhat meaningful” (p. 5). Constructs are logical. For example, there<br>should not be scores primarily generated from word count because then<br>test takers wouldjust write longessays.|
||“However, it would be undesirable to have scores generated primarily<br>from word count because such generation might encourage the student<br>to maximize the number of words at expense of other, more valued<br>aspects of writing” (p. 5).|
|**Madnani et**<br>**al., 2017**|“…construct irrelevant factors includes continuous covariates which are<br>likely to be correlated with the human scores but are not relevant to the<br>construct measured by the test or, if relevant, should not be the main<br>factor behind the model prediction” (p. 5). For example, the length of an<br>essay may be an example of this. It should be only given relative weight<br>for fairness.|



ACT Research | Technical Brief | July 2021 

14 

|**Source**|**Examples**|
|---|---|
|**Williamson et**<br>**al., 2012**|"Construct relevance and representation”—steps proposed to evaluate fit<br>between assessment and AES: “[1] construct evaluation” or match<br>between construct and AES capacity, “[2] task design” or fit between<br>features and test task, “[3] scoring rubric” or consistency between<br>features measured by AES and those on scoring rubric, and “[4] reporting<br>goals” or determining if the goal of the reporting is consistent with AES<br>capabilities (p. 6).|
||“Each system has at the core of the capability a set of features that are<br>designed to measure the elements of writing that are computer-<br>identifiable and believed to be relevant to the construct of writing, even<br>if they are not directly equivalent to what a human grader might identify<br>in a similar effort” (p. 3).|
||“Automated scoring poses some distinctive validity challenges such as<br>the potential to under- or misrepresent the construct of interest,<br>vulnerability to cheating, impact on examinee behavior, and score users'<br>interpretation and use of scores” (p. 4).|
|**Yang et al.,**<br>**2002**|“…[M]any researchers have also stressed the importance of understanding<br>the scoring processes that CAS [computer-automated scoring] systems<br>used” (p. 402). Similar to content validity, this discusses ensuring that the<br>engine is stressingfeatures that are important togood writing.|
||“...by analyzing the patterns and nature of disagreement between expert<br>ratings and CAS-system-generated scores, one may identify the<br>difference between human and computer scoring models in terms of the<br>factors that considered and the relative weighting of these factors” (p.<br>402–403).|
|**Zheng, 2015**|Outlines the need for using an independent validation dataset: “The<br>model training process receives training data and produces a model,<br>which is evaluated on validation data” (p. 20). This details cross-<br>validation, held-out validation, and bootstrapping techniques for<br>evaluatingvalidityof models.|
||“Optimal hyperparameter settings often differ for different datasets.<br>Therefore theyshould be tuned for each dataset” (p. 28).|
|**CCSSO & ATP,**<br>**2013**|“Methods for the calibration of the artificial intelligence scoring engines,<br>and evidence that the engine meets accuracy and reliability standards,<br>should be documented” (p. 131).|



## **Standard 3: Scores produced by AS should demonstrate fairness for all populations.** 

Related to validity, providing evidence that AS evaluation is fair for persons from diverse groups is another frequently cited standard. A common approach to addressing this standard is to compare human-to-AS engine mean score differences between a majority group and subgroups of interest (Madnani et al., 2017; Williamson, Xi, & Breyer, 2012). Those differences should be similar, so when larger differences are observed for a subgroup of interest, it indicates possible bias. That is, AS might not be 

ACT Research | Technical Brief | July 2021 

15 

appropriate if mean differences between human raters and AS scores surpass specified thresholds for subgroups compared to a majority group. 

AS professionals should also consider the feature set used in an engine. Constructirrelevant features should be avoided, especially features that may advantage or disadvantage one subgroup over another. Differential feature functioning provides a statistical methodology to identify any problematic features (Penfield, 2016; Zhang, Dorans, Li, & Rupp, 2017). 

Table 5 provides exemplar citations from the literature review that support this standard. 

**Table 5.** Exemplar Citations Supporting Standard 3 

|**Source**|**Examples**|
|---|---|
|**Yang et al.,**<br>**2002**|“In the published literature, both agreement/reliability approaches and<br>true score approaches demonstrate desirable performance of CAS<br>systems across various domains andpopulations” (p. 401).|
|**AERA, APA, &**<br>**NCME, 2014**|“Standard 3.8: When tests require the scoring of constructed responses,<br>test developers and/or users should collect and report evidence of the<br>validity of score interpretations for relevant subgroups in the intended<br>population of test takers for the intended uses of test scores” (p. 66).|
||“[Standard 3.8] Comment: For human scoring, scoring procedures should<br>be designed with the intent that the scores reflect the examinee’s<br>standing relative to the tested construct(s) and are not influenced by the<br>perceptions and personal predispositions of the scorers. It is essential<br>that adequate training and calibration of the scorers be carried out and<br>monitored throughout the scoring process to support the consistency of<br>scorer’s ratings for individuals from relevant subgroups. Where sample<br>sizes permit, the precision and accuracy of scores for relevant subgroups<br>should also be calculated” (p. 66).|
||“[Standards 3.8] Comment: Scoring algorithms need to be reviewed for<br>potential sources of bias. The precision of scores and validity of score<br>interpretations resulting from automated scoring should be evaluated<br>for all relevant subgroups of the intendedpopulation” (p. 66–67).|
|**CCSSO & ATP,**<br>**2013**|Raters should be provided with "information on disregarding cues<br>related to disability, English learner status or accommodations that are<br>unrelated to scoringcriteria” (p. 128).|
||“Al [Artificial Intelligence] validation should represent student responses<br>representative of the entire population of possible student response<br>submission. Validation should include a range of score points, types and<br>styles of writing, and other relevant considerations” (p. 131).|



ACT Research | Technical Brief | July 2021 

16 

|**Source**|**Examples**|
|---|---|
|**McGraw-Hill**<br>**Education**<br>**CTB, 2014**|“Williamson, Xi, and Breyer (2012) flag the SMD if the difference between<br>automated scores and human scores is greater than .15 in absolute value.<br>Similarly, they flag the SMD for a subgroup if the difference between the<br>automated scores and human scores for that subgroup is greater than .10<br>in absolute value. Because the larger the population SMD value the more<br>likely the subpopulation SMD value will be flagged, CTB reduced the<br>amount of SMD separation tolerated by flagging the population SMD if it<br>exceeds .12 in absolute value” (p. 15).|
|**Williamson et**<br>**al., 2010**|"Automated scores [should be] fair. It is critical that automated scoring<br>be equitable forpersons from diversegroups” (p. 5).|
|**Williamson et**<br>**al., 2012**|“We have established a more stringent criterion of performance, setting<br>the flagging criteria at .10, and applied this criterion to all subgroups of<br>interest to identify patterns of systematic differences in the distribution<br>of scores between human scoring and automated scoring for subgroups”<br>(p. 10).|
||“…examining differences in the associations between automated and<br>human scores across subgroups at the task, task type, and reported score<br>levels. Major differences by subgroups may indicate problems with the<br>automated scoring model for these subgroups and should be evaluated<br>for potentially undesirable performance with the subgroups in question”<br>(p. 10).|
||Investigating “the generalizability of automated scores by subgroup.<br>Substantial differences across subgroups may suggest that the scores are<br>differentiallyreliable for differentgroups” (p. 10).|
||Examining “differences in the predictive ability of automated scoring by<br>subgroup. … First is to compare an initial human score and the<br>automated score in their ability to predict the score of a second human<br>rater by subgroup. The second type of prediction is comparing the<br>automated and human score ability to predict an external variable of<br>interest bysubgroup” (p. 10).|
||“subgroup differences should also be investigated in relation to the<br>decisions made based on the scores. This is the most prominent<br>manifestation ofgroupdifferences” (p. 10).|
|**Madnani et**<br>**al., 2017**|“RSMTool [software for evaluating subgroup differences in automated<br>scoring] considers how well the automated scores agree with the human<br>scores (or another, user-specified gold standard criterion) and whether<br>this agreement is consistent across differentgroups of test-takers.” (p. 5)|
||“RSMTool also includes Differential feature functioning (DFF)<br>analysis…This approach compares the mean values of a given feature for<br>test-takers with the same score but belonging to different subgroups” (p.<br>5).|



ACT Research | Technical Brief | July 2021 

17 

## **Standard 4: Convergent and discriminant validity studies should be conducted to establish empirical relationships between AS scores and other constructs.** 

Test-criterion relationships reflect how well AS scores relate to relevant constructs as measured by an assessment or observable criterion (e.g., educational or job success) external to the assessment of interest. The recommendation to conduct criterionrelated validity studies is commonly cited in the literature (e.g., Powers, Escoffery, & Duchnowski, 2015; Shermis, et al., 2016). As with reliability, the expectation is that the relationship between AS scores and the external measure will be similar in magnitude and direction in comparison to the relationship of human scores with the external measure. For example, compared to human scores, one would expect AS scores from a writing test to have similar correlations with the multiple-choice portion of an English language arts exam. 

Table 6 provides exemplar citations from the literature review that support this standard. 

**Table 6.** Exemplar Citations Supporting Standard 4 

|**Source**|**Examples**|
|---|---|
||“For example, the specific directions given to raters might be varied|
||experimentally: some raters could be instructed to read essays slowly|
|**Powers et al.,**<br>**2015**|and deliberately, while others would be directed to read more rapidly<br>(and perhaps) superficially. The validity of automated scores would be<br>supported to the extent that they correlate more strongly with the scores|
||given by deliberate readers than by those given by less careful reader” (p.|
||141).|
||“Automated scores have been validated against external measures in the|
||same way as is done with human scoring….Examples of relevant external|
|**Williamson et**|<br>criteria include scores on other test sections, grades in relevant academic|
|**al., 2010**|classes, scores on the same test section on alternate occasions, and|
||scores on specially designed external measures of the construct of|
||interest” (p. 5).|
||“[I]t is of relevance to investigate more than just the consistency with|
||human scores and to also evaluate the patterns of relationship of|
|**Williamson et**|<br>automated scores, compared to their human counterparts, with external|
|**al., 2012**|criteria…These independent variables may be scores on other sections of|
||the same test or external variables that measure similar, related, or|
||different constructs” (p. 9).|



ACT Research | Technical Brief | July 2021 

18 

|**Source**|**Examples**|
|---|---|
||“Within test relationships: Are automated scores related to scores on<br>other sections of the test in similar ways compared to human scores?;<br>External relationships: Are automated scores related to other external<br>measures of interest in similar ways com- pared to human scores?;<br>Relationship at the task type and reported score level:Are the<br>relationships similar at the task type and reported score level? These<br>comparisons should be made both at the task/task type score level and<br>reported score level” (p. 9).|
||“How generalizable are the automated scores across tasks and test forms<br>in comparison to human scores? How generalizable are the automated–<br>human combined scores across test forms? A comparison of the<br>generalizability of human and automated scores across tasks and test<br>forms will provide insights into how consistently students perform across<br>tasks and test forms” (p. 9).|
||“To what extent do automated, human, and automated–human<br>combined scores on one test form predict human scores on an alternate<br>form? This analysis will reveal whether the use of automated scoring may<br>improve the alternate form reliabilityof the scores” (p. 10).|
|**Shermis et al.,**<br>**2016**|“Studies have examined the effects of automated evaluation of writing as<br>well as how they generalize to other criterion measures of student<br>performance. … Results [from one study] indicated that the students<br>using automated feedback received higher grades on their summaries,<br>spent more than twice as much time on writing and revising, and<br>managed to retain the skills they learned…. Results [in another study]<br>showed that students receiving feedback improved their summary<br>writing by an overall effect size of d=0.9 compared to control students”<br>(p. 21).|



## **Standard 5: When implementing AS, consideration must be given to contextual factors such as the stakes associated with test performance, item types, and scoring approached that integrate human and AS.** 

Given known limitations of AS—for example, critics point out that the engine does not “understand” writing the way a human does—there are many considerations for the implementation of AS in a specific program context. This standard dictates consideration of the stakes associated with test performance, item types, and scoring approaches that integrate human and AS. 

Often, decisions about how scoring is implemented depend on if the test is a highstakes assessment (McGraw-Hill Education CTB, 2014; Yang, et al., 2002). Whereas AS may be used as the sole scoring mechanism for low-stakes tests or feedback tools, it may be more appropriate to integrate AS and human scoring for high-stakes 

ACT Research | Technical Brief | July 2021 

19 

assessments—perhaps using a resolution score if the human score and AS differ substantially. 

Table 7 provides exemplar citations from the literature review that support this standard. 

**Table 7.** Exemplar Citations Supporting Standard 5 

|**Source**||**Examples**|
|---|---|---|
|**Shermis et al.,**<br>**2016**||“Considerations include the following…: construct-based scoring designs;<br>integrated assessments in which both automated scores and human<br>scores serve inter-related roles; strengthen operational human scoring to<br>support modeling of AWE [Automated Writing Evaluation] systems;<br>augmented use of human scores to broaden construct representation;<br>enhanced understanding of human scoring processes; disclosure of<br>scoring approaches; and use of a variety of evidential categories to justify<br>score use” (p. 26).|
|**Williamson et**<br>**al., 2012**||“A rough ordering (from more conservative to more liberal use) of<br>implementations for use of automated scoring is as follows: …Automated<br>quality control of human scoring. The results of a single human score and<br>an automated score are compared. If there is a discrepancy beyond a<br>certain threshold between the two then the response is sent to a second<br>human grader. The reported score is based solely on the human score<br>(either the single human score or the mean of the two human scores). …<br>Automated and human scoring.The score from a single human grader<br>and automated score are averaged or summed to produce the reported<br>score. Responses with score discrepancies beyond a certain threshold are<br>scored by additional human graders. Proposed reporting policies vary,<br>but adjudication procedures have included reporting the average of all<br>scores provided, as well as reporting the average of the two scores in<br>highest agreement, and several variations of these, conditional on the<br>particular distribution of scores involved. …Automated scoring alone.<br>Reporting scores solely from the automated system. This is the most<br>liberal use of automated scoring” (p. 5).|
|||“The use of automated scoring for high-stakes decisions is subject to a<br>higher burden of both the amount and quality of evidence to support the<br>intended use than for lower-stakes and practice applications. The choice<br>of implementation policies for automated scoring would be influenced<br>by the quantity and quality of evidence supporting the use of automated<br>scoring, the particular task types, testing purpose, test-taker population<br>to which it is applied, and the degree of receptivity of the population of<br>score users to models of implementation” (p. 5).|
|**Yang et al.,**<br>**2002**||“Differences in the level of integration reflect differences in the<br>perceptions of utility and implications stemming from the use of a CAS<br>system” (p. 408). For example, if CAS is viewed as the human scorer then<br>CAS mayhave a different validitycriteria then if viewed as a read-behind.|



ACT Research | Technical Brief | July 2021 

20 

|**Source**|**Examples**|
|---|---|
||“[R]ead and read behind scenarios … can be categorized based on 1. The|
||number of raters (one or two), 2. the type of the first and second rater|
|**McGraw-Hill**<br>**Education**<br>**CTB, 2014**|(human or Automated Scoring system), and 3. the adjudication rule<br>which determines when scores from the first and second rater need to<br>be adjudicated by the third rater: a. adjudicated when the scores of the<br>first and second rater disagree (non-exact) b. adjudicate when the scores|
||of the first and second rater differ by more than 1 score point (non-|
||adjacent)” (p. 40).|



## **Standard 6: During live testing, accuracy and reliability of AS via process monitoring should be made available to the client.** 

Providing clients with access to scoring process monitoring is another AS standard crucial to ensure accuracy, reliability, and transparency (Wang & von Davier, 2014). Typically, a dashboard is provided to allow clients or a third party a way to audit scoring accuracy and error rates in real time. This provides a way for scoring errors to be immediately identified and addressed during a testing or scoring event. 

Reported metrics should include AS score point distributions, human score point distributions, and human-AS agreement statistics, if human scores are available. 

Table 8 provides exemplar citations from the literature review that support this standard. 

**Table 8.** Exemplar Citations Supporting Standard 6 

|**Source**|**Examples**|
|---|---|
||“Standard 6.9: Those responsible for test scoring should establish and|
|**AERA, APA, &**<br>**NCME, 2014**|document quality control processes and criteria. Adequate training<br>should be provided. The quality of scoring should be monitored and<br>documented. Any systematic source of scoring errors should be|
||documented and corrected” (p. 118).|
|**CCSSO & ATP,**|“Any measure or analysis used to check accuracy and reliability of the|
|**2013**|scoring process should be made available for the client’s review” (p. 131).|
||“Independent Monitoring of Quality Control Procedures… should be|
|**ITC, 2014**|carried out in collaboration with all stakeholders, with the aim of<br>auditing specific processes, for example, monitoring inter-rater reliability|
||and checkingdata entryerror rates” (p. 204).|



ACT Research | Technical Brief | July 2021 

21 

## **Standard 7: It is essential to evaluate the quality of inputs to an AS engine (responses, human scoring, universe of acceptable responses) before training.** 

Another standard identified in the review affirms the importance of evaluating the quality of inputs to the AS engine, including item responses, human scores for those responses, and the item’s universe of acceptable responses (Williamson, et al., 2010; Williamson, Xi, & Breyer, 2012). First, responses that are considered non-attempts (e.g., blank response, gibberish, refusals, etc.)—as identified by agreed-upon scoring rules— are separated from valid attempts and processed using a different workflow. Specifically, the non-attempt responses are used to establish rules and models for AS to assign condition codes, while valid attempts are used to create the scoring models. Second, AS models developed with data from low-quality human scoring will result in poor AS engine performance. Third, the item’s universe of acceptable responses can impact engine performance. For instance, differences in the number of concepts or ways of describing these concepts elicited by the item can affect the suitability of an item for AS. An item such as “Describe the characteristics of the chemical element mercury” might be more suitable for AS than the item “Describe how 19th-century American wars led to the expansion of the United States via manifest destiny.” The first item is likely to elicit several standard and common characteristics of mercury (silver colored, liquid at room temperature, poisonous, used in thermometers), while the second item is likely to elicit a broad range of many ideas (War of 1812, MexicanAmerican War, etc.) and may not therefore be as well suited to AS. 

Table 9 provides exemplar citations from the literature review that support this standard. 

**Table 9.** Exemplar Citations Supporting Standard 7 

|**Source**|**Examples**|
|---|---|
||“[T]he model building and evaluation process for automated scoring is|
|**Williamson et**<br>**al., 2012**|<br>largely dependent on the quality of human scores...[I]f the inter-rater<br>agreement of independent human raters is low, especially below the .70<br>threshold, then automated scoring is disadvantaged in demonstrating|
||this level ofperformance” (p. 7).|



## **Standard 8: The impact or consequences of AS on the test or reported score should be considered and documented.** 

Related to the stakes or context of the assessment, it is imperative to clearly define and consider the impact or consequences of AS on the test or reported score (Joint Committee on Testing Practices, 2004; Williamson, Xi, & Breyer, 2012). This standard recommends understanding how the use of AS may affect aspects of the test-taker’s experience (e.g., if students write differently given their knowledge that the test is 

ACT Research | Technical Brief | July 2021 

22 

scored by AS). Additionally, information about AS accuracy of score-based decisions should be transparently communicated, so that these scores are used responsibly at the test and item level. For example, if AS is used for a writing assessment to establish the proficiency of an examinee, AS professionals and test developers should be transparent around potential misclassification errors and proper interpretation of proficiency classifications. 

Table 10 provides exemplar citations from the literature review that support this standard. 

**Table 10.** Exemplar Citations Supporting Standard 8 

|**Source**|**Examples**|
|---|---|
|**Williamson et**<br>**al., 2010**|“The impact of automated scoring on reported scores is understood [by<br>ASprofessionals and stakeholders]” (p. 6).|
|**Williamson et**<br>**al., 2012**|“What impact does the use of automated scoring have on the accuracy of<br>score-based decisions? In some contexts, assessment scores are used for<br>classification purposes, for example, a binary decision about eligibility for<br>admissions or exemption from English language coursework once<br>admitted, or a decision regarding placing students into several levels of<br>English class. Depending on the intended use of the assessment scores,<br>the aggregated reported scores may be subject to further analyses to see<br>if human–machine combined scores introduce a greater amount of<br>decision errors than human scores” (p. 10).|
||“What claims and disclosures should be communicated to score users to<br>ensure appropriate use of scores? Researchers should work with the<br>operational program to establish a common understanding of the<br>intended claims and intent for disclosure of both strengths and<br>limitations of automated scoring to ensure an informed population of<br>score users. These claims and disclosures may include the extent to<br>which different aspects of the target construct are covered by automated<br>scoringand its major construct limitations” (p. 10).|
||“What consequences will the use of automated scoring bring about?<br>Replacing one human rater with automated scoring or using automated<br>scoring to quality-control human scoring may change users’ perceptions<br>of the assessment, how users interpret and use the scores for decision-<br>making, how test takers prepare for the test, and how the relevant<br>knowledge and skills are taught” (p. 10).|
||“Automated scoring poses some distinctive validity challenges such as<br>the potential to under- or misrepresent the construct of interest,<br>vulnerability to cheating, impact on examinee behavior, and score users'<br>interpretation and use of scores” (p. 4).|
||“What are the response characteristics that render automated scoring<br>inappropriate? … Currently the e-rater technology will flag essays of<br>excessive length or brevity, repetition, those with too many problems, or<br>off-topic responses for scoring by human raters. This adds additional<br>support for thequalityof the scoresproduced” (p. 8).|



ACT Research | Technical Brief | July 2021 

23 

## **Standard 9: Procedures should be in place to identify alert papers (i.e., responses reflecting cheating or disturbing content).** 

A less frequently recognized core standard is that there should be engine procedures to identify “alert papers”—that is, responses reflecting cheating or disturbing content, to which a school might need to respond (Council of Chief State Schools, & Association of Test Publishers, 2013; Williamson, Xi, & Breyer, 2012). Engines typically have mechanisms to identify and flag such responses, such as a filter that detects responses that have been copied from other sources. Hybrid approaches with keyword and machine learning techniques can also be used to flag alert papers. 

These mechanisms become crucial if only AS, and not human scoring, is used in operational practice. Cheating detection is important to maintain the integrity and validity of the test scores. Disturbing content can be a liability if an examinee follows through on any threats present in their response. These threats can include harming themselves, others, or property. 

Table 11 provides exemplar citations from the literature review that support this standard. 

**Table 11.** Exemplar Citations Supporting Standard 9 

|**Source**|**Examples**|
|---|---|
|**CCSSO & ATP,**|“Procedures should be established to identify, to evaluate, and if|
|**2013**|necessary, escalate alertpapers … to the client” (p. 133).|



## **Standard 10: Policies around how and when to recalibrate the engine should be established.** 

The final core standard is that policies must be established to determine when it is appropriate to recalibrate the engine (Council of Chief State Schools Officers and Association of Test Publishers, 2013). When there are major changes made to the program or population, it is necessary to recalibrate the engine. For example, changing the population of test-takers from 4th graders to 6th graders would warrant recalibration. 

Recalibration should also be considered if: 

- the score point distribution (using human scores) changes significantly from the score point distribution of human scores used for training, or 

- the human-AS agreement rates decrease over time. 

Without this type of maintenance of scoring models, models may become less accurate and not meet performance standards and thresholds previously discussed. 

ACT Research | Technical Brief | July 2021 

24 

Table 12 provides exemplar citations from the literature review that support this standard. 

**Table 12.** Exemplar Citations Supporting Standard 10 

|**Source**|||**Examples**|
|---|---|---|---|
|**CCSSO**<br>**2013**|**&**|**ATP,**|“Al performance results should be measured and analyzed regularly. A<br>process should be established to permit recalibration and/or retraining,<br>as appropriate” (p. 131).|



## **Conclusion** 

This report identified 10 AS standards common to the academic literature and professional standards in assessment, data science, and related fields. Having a unified set of AS standards establishes guidelines of good practice for an emerging technology, guides a diverse group of AS professionals, and provides stakeholders with the confidence that AS professionals are conducting their work in a proficient way. 

AS staff at ACT plan to review these standards on an annual basis. This ensures that the standards are based on current best practices and new research findings. Major updates to these standards will be published as needed. 

The authors encourage feedback about these standards from AS professionals. The standards are influenced by our experiences working with customers using AS but may represent only a partial view of the industry. AS professionals are invited to contact our team at _CRASE@act.org_ to provide feedback and suggestions, which we will incorporate into future versions of these standards. 

Finally, the authors hope that this document, along with similar documents being developed at other organizations using AS, can become the foundation for industrywide standards used worldwide. Such standards should ensure that AS yields accurate and reliable scores that meet the expectations of our stakeholders. 

ACT Research | Technical Brief | July 2021 

25 

## **References** 

American Educational Research Association. (2011). AERA code of ethics. _Educational Researcher, 40_ (3), 145–156. 

American Educational Research Association, American Psychological Association, & National Council on Measurement in Education. (2014). _Standards for educational and psychological testing_ . Washington, DC: American Educational Research Association. 

American Statistical Association. (2018). _Ethical guidelines for statistical practice_ . Alexandria, VA: Committee on Professional Ethics of the American Statistical Association. 

Association for Computing Machinery. (2018). _ACM code of ethics and professional conduct_ . _https://www.acm.org/code-of-ethics_ . 

Council of Chief State School Officers, & Association of Test Publishers. (2013). Scoring. In _Operational best practices for statewide large-scale assessment programs_ . (pp. 125–134). Washington, DC: Council of Chief State School Officers and the Association of Test Publishers. 

Data Science Association. (n.d.). _Data science code of professional conduct_ . _https://www.datascienceassn.org/code-of-conduct.html_ . 

Gotterbarn, D., Miller, K., & Rogerson, S. (1997). Software engineering code of ethics. _Communications of the Association for Computing Machinery, 40_ (11), 110–118. 

International Test Commission. (2001). International guidelines for test use. _International Journal of Testing, 1_ (2), 93–114. 

International Test Commission. (2006). International guidelines on computer-based and internet-delivered testing. _International Journal of Testing, 6_ (2), 143–171. 

International Test Commission. (2014a). ITC guidelines on quality control in scoring, test analysis, and reporting of test scores. _International Journal of Testing, 14_ (3), 195–217. 

ACT Research | Technical Brief | July 2021 

26 

International Test Commission. (2014b). _International guidelines on the security of tests, examinations, and other assessments_ . Lincoln, NE: ITC. _https://www.intestcom.org/files/guideline_test_security.pdf_ . 

International Test Commission. (2015). _International guidelines for practitioner use of test revisions, obsolete tests, and test disposal_ . Lincoln, NE: ITC. _https://www.intestcom.org/files/guideline_test_disposal.pdf_ . 

International Test Commission. (2017). _The ITC guidelines for translating and adapting tests_ (2nd Ed.). Lincoln, NE: ITC. 

_https://www.intestcom.org/files/guideline_test_adaptation_2ed.pdf_ . 

Joint Committee on Testing Practices. (2004). _Code of fair testing practices in education_ . Washington, DC: Joint Committee on Testing Practices. _https://www.apa.org/science/programs/testing/fair-testing.pdf_ . 

Linguistic Society of America. (2019). _LSA code of ethics_ . 

_https://www.linguisticsociety.org/content/lsa-revised-ethics-statementapproved-july-2019_ . 

Madnani, N., Loukina, A., von Davier, A., Burstein, J., & Cahill, A. (2017, April). Building better open-source tools to support fairness in automated scoring. In D. Hovy, S. Spruit, M. Mitchell, E. Bender, M. Strube, & H. Wallach (Eds.), _Proceedings of the first ACL workshop on ethics in natural language processing_ (pp. 41–52). 

McGraw-Hill Education CTB. (2014). _Smarter Balanced Assessment Consortium-Field test: Automated scoring research studies_ . Monterey, CA: Smarter Balanced Assessment Consortium. 

Pearson, & Educational Testing Service. (2015). _Research results of PARCC automated scoring proof of concept study_ . 

Penfield, R. (2016). Fairness in test scoring. In N. Dorans & L. Cook (Eds.), _Fairness in educational assessment and measurement_ (pp. 55–75). New York, NY: Routledge. 

ACT Research | Technical Brief | July 2021 

27 

Powers, D. E., Escoffery, D. S., & Duchnowski, M. P. (2015). Validating automated essay scoring: A (modest) refinement of the “gold standard.” _Applied Measurement in Education, 28_ (2), 130–142. 

Shermis, M. D., Burstein, J., Elliot, N., Miel, S., & Foltz, P. (2016). Automated writing evaluation: An expanding body of knowledge. In C. A. MacArthur, S. Graham, & J. Fitzgerald (Eds.), _Handbook of writing research_ (2nd ed., pp. 395–409). New York, NY: Guilford. 

Wang, Z., & von Davier, A. A. (2014). _Monitoring of scoring using the e-rater automated scoring system and human raters on a writing test_ (ETS Research Report ETS RR-14-04). Princeton, NJ: ETS. 

Williamson, D. M., Bennett, R. E., Lazer, S., Bernstein, J., Foltz, P., Landauer, T. K., Rubin, D. P., Way, W. D., & Sweeney, K. (2010). _Automated scoring for the assessment of Common Core Standards_ . ETS, Pearson, & The College Board. 

Williamson, D. M., Xi, X., & Breyer, F. J. (2012). A framework for evaluation and use of automated scoring. _Educational Measurement: Issues and Practice, 31_ (1), 2–13. 

Yang, Y., Buckendahl, C. W., Juszkiewicz, P. J., & Bhola, D. S. (2002). A review of strategies for validating computer-automated scoring. _Applied Measurement in Education, 15_ (4), 391–412. 

Yang, Y., Buckendahl, C. W., Juszkiewicz, P. J., & Bhola, D. S. (n.d.). _Validating computer automated scoring: A conceptual framework and a review of strategies_ [Unpublished manuscript]. The Gallup Organization. 

Zhang, M., Dorans, N., Li, C., & Rupp, A. (2017). Differential feature functioning in automated essay scoring. In H. Jiao & R. Lissitz (Eds.), _Test fairness in the new generation of large-scale assessment_ (pp. 185–208). Charlotte, NC: Information Age Publishing. 

Zheng, A. (2015). _Evaluating machine learning models: A beginner's guide to key concepts and pitfalls_ . Sebastopol, CA: O'Reilly Media. 

