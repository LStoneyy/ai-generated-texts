# Statistical Analysis Documentation

## AI Text Detection Study - Analytical Framework

This document provides a comprehensive overview of all statistical analyses and visualizations performed in the study examining university instructors' ability to distinguish between AI-generated and human-written student essays.

---

## Table of Contents

1. [Descriptive Statistics](#1-descriptive-statistics)
2. [Accuracy Analysis](#2-accuracy-analysis)
3. [Hypothesis Testing](#3-hypothesis-testing)
4. [Correlation Analysis](#4-correlation-analysis)
5. [Text Difficulty Analysis](#5-text-difficulty-analysis)
6. [Visualizations](#6-visualizations)

---

## 1. Descriptive Statistics

### 1.1 Participant Demographics

**Teaching Experience:**

To characterize the expertise level of our participant sample, we calculated the mean teaching experience across all participants. The arithmetic mean provides a measure of central tendency that represents the average years of teaching experience in our sample. This metric is essential for understanding whether our participants have sufficient domain expertise to potentially distinguish between AI-generated and authentic student writing.

$$\bar{x}_{exp} = \frac{1}{n}\sum_{i=1}^{n} x_i$$

```latex
\bar{x}_{exp} = \frac{1}{n}\sum_{i=1}^{n} x_i
```

where $n$ is the number of participants and $x_i$ is the teaching experience of participant $i$.

**Standard Deviation:**

To assess the variability in teaching experience across participants, we computed the standard deviation. This measure quantifies how much individual experience levels deviate from the sample mean, providing insight into the homogeneity of our participant group. A larger standard deviation indicates greater diversity in experience levels, while a smaller value suggests a more uniform sample.

$$SD = \sqrt{\frac{1}{n-1}\sum_{i=1}^{n}(x_i - \bar{x})^2}$$

```latex
SD = \sqrt{\frac{1}{n-1}\sum_{i=1}^{n}(x_i - \bar{x})^2}
```

### 1.2 Response Metrics

**Overall Accuracy:**

The primary dependent variable in this study is classification accuracy, which represents the proportion of texts correctly identified as either AI-generated or human-written. This metric provides a straightforward measure of participants' detection ability and serves as the foundation for subsequent hypothesis testing. Accuracy is expressed as a percentage to facilitate interpretation and comparison with the chance level of 50%.

$$Accuracy = \frac{\text{Number of Correct Classifications}}{\text{Total Number of Classifications}} \times 100\%$$

```latex
Accuracy = \frac{\text{Number of Correct Classifications}}{\text{Total Number of Classifications}} \times 100\%
```

**Confidence Rating:**

Participants rated their confidence in each classification decision using a 5-point Likert scale, where 1 indicates "very unsure" and 5 indicates "very sure." This self-reported measure allows us to examine metacognitive accuracy—the alignment between participants' subjective confidence and their objective performance. Analyzing confidence ratings alongside accuracy enables assessment of calibration, which is crucial for understanding whether instructors can reliably gauge their own detection abilities.

Measured on a 5-point Likert scale (1 = very unsure, 5 = very sure).

**Response Time:**

Response time, measured in milliseconds from text presentation to classification submission, serves as a behavioral indicator of cognitive processing demands. Longer response times may indicate deeper analytical engagement, while shorter times could reflect intuitive judgments. To facilitate interpretation and align with conventional reporting practices in cognitive research, raw millisecond values are converted to seconds for all analyses and visualizations.

$$t_{sec} = \frac{t_{ms}}{1000}$$

```latex
t_{sec} = \frac{t_{ms}}{1000}
```

---

## 2. Accuracy Analysis

### 2.1 Overall Accuracy

Overall accuracy represents the aggregate performance across all participants and all texts, providing a global measure of detection ability in the sample. This metric collapses individual and text-level variation to yield a single summary statistic, which can be directly compared to the theoretical chance level of 50% to provide an initial assessment of whether participants demonstrate any systematic ability to distinguish between text types.

$$ACC_{overall} = \frac{1}{N}\sum_{i=1}^{N} c_i \times 100\%$$

```latex
ACC_{overall} = \frac{1}{N}\sum_{i=1}^{N} c_i \times 100\%
```

where $N$ is the total number of responses and $c_i \in \{0,1\}$ indicates whether response $i$ was correct.

### 2.2 Participant-Level Accuracy

Individual participant accuracy scores are calculated to capture between-subject variability in detection performance. By computing accuracy separately for each participant, we can examine the distribution of detection abilities within our sample and identify whether performance is relatively uniform or whether certain participants demonstrate markedly superior or inferior classification skills. These individual scores form the basis for subsequent hypothesis testing and correlation analyses.

$$ACC_p = \frac{1}{n_p}\sum_{j=1}^{n_p} c_{pj} \times 100\%$$

```latex
ACC_p = \frac{1}{n_p}\sum_{j=1}^{n_p} c_{pj} \times 100\%
```

where $n_p$ is the number of texts classified by participant $p$ and $c_{pj}$ indicates correctness of participant $p$'s classification of text $j$.

### 2.3 Accuracy by Text Origin

To determine whether participants exhibit differential ability in detecting AI-generated versus human-written texts, we calculate accuracy rates separately for each text type. Asymmetric performance across text origins would suggest systematic biases or differential feature salience. For instance, higher accuracy for AI texts would indicate that AI-generated content contains more detectable artifacts, while the reverse pattern would suggest that human writing has more distinctive characteristics.

**AI-generated texts:**

$$ACC_{AI} = \frac{\text{Correctly identified AI texts}}{\text{Total AI texts}} \times 100\%$$

```latex
ACC_{AI} = \frac{\text{Correctly identified AI texts}}{\text{Total AI texts}} \times 100\%
```

**Human-written texts:**

$$ACC_{Human} = \frac{\text{Correctly identified Human texts}}{\text{Total Human texts}} \times 100\%$$

```latex
ACC_{Human} = \frac{\text{Correctly identified Human texts}}{\text{Total Human texts}} \times 100\%
```

### 2.4 Confusion Matrix

The confusion matrix provides a detailed decomposition of classification outcomes, revealing the specific patterns of correct and incorrect judgments. This 2×2 contingency table distinguishes between four possible outcomes: true positives (correctly identified AI texts), true negatives (correctly identified human texts), false positives (human texts misclassified as AI), and false negatives (AI texts misclassified as human). Analysis of these patterns can illuminate whether participants exhibit response biases, such as a tendency to over- or under-attribute texts to AI generation.

|                    | Classified as AI | Classified as Human |
|--------------------|------------------|---------------------|
| **Actual: AI**     | True Positive (TP) | False Negative (FN) |
| **Actual: Human**  | False Positive (FP) | True Negative (TN) |

### 2.5 Diagnostic Measures

**Sensitivity (True Positive Rate):**

Sensitivity quantifies the proportion of AI-generated texts that participants successfully identified as AI-generated. This metric, also known as recall in machine learning contexts, assesses detection capability specifically for AI content. High sensitivity indicates that participants rarely miss AI-generated texts, while low sensitivity suggests that AI content frequently goes undetected. This measure is particularly relevant for evaluating the practical effectiveness of human detection in educational settings where identifying AI use is the primary concern.

$$Sensitivity = \frac{TP}{TP + FN} \times 100\%$$

```latex
Sensitivity = \frac{TP}{TP + FN} \times 100\%
```

**Specificity (True Negative Rate):**

Specificity measures the proportion of human-written texts correctly identified as human-written, representing the complement of the false positive rate. High specificity indicates that participants rarely misattribute authentic student work to AI generation, which is crucial from an ethical standpoint—false accusations of AI use could unjustly penalize students. Together with sensitivity, specificity provides a complete picture of classification performance across both text types.

$$Specificity = \frac{TN}{TN + FP} \times 100\%$$

```latex
Specificity = \frac{TN}{TN + FP} \times 100\%
```

---

## 3. Hypothesis Testing

### 3.1 Research Hypotheses

The central research question concerns whether university instructors possess better-than-chance ability to distinguish AI-generated from human-written texts. We operationalize this through a formal hypothesis testing framework:

- **H₀ (Null Hypothesis):** University instructors cannot distinguish between AI-generated and human-written texts better than chance: $\mu_{accuracy} = 50\%$
- **H₁ (Alternative Hypothesis):** University instructors can distinguish between AI-generated and human-written texts at a rate different from chance: $\mu_{accuracy} \neq 50\%$

The null hypothesis posits that participants are essentially guessing, yielding 50% accuracy on average in a balanced two-alternative forced-choice task. Rejection of the null hypothesis would provide evidence for systematic detection ability, though it would not necessarily indicate practically useful performance levels.

### 3.2 One-Sample t-Test

To evaluate whether mean participant accuracy differs significantly from the chance level of 50%, we employ a one-sample t-test. This parametric test compares the observed sample mean against the theoretical chance value, accounting for sample variability through the standard error. The t-test is appropriate given that individual participant accuracy scores represent our unit of analysis, and these scores can be assumed to be approximately normally distributed (an assumption we verify through visual inspection of the distribution).

**Test Statistic:**

The t-statistic quantifies how many standard errors the observed mean accuracy deviates from the hypothesized chance level. Larger absolute t-values provide stronger evidence against the null hypothesis, indicating that the observed deviation is unlikely to have occurred by sampling variability alone.

$$t = \frac{\bar{x} - \mu_0}{SE}$$

```latex
t = \frac{\bar{x} - \mu_0}{SE}
```

where:
- $\bar{x}$ = mean participant accuracy
- $\mu_0$ = 50% (chance level)
- $SE$ = standard error of the mean

**Standard Error:**

The standard error represents the estimated standard deviation of the sampling distribution of the mean. It decreases with larger sample sizes, reflecting increased precision in estimating the population mean. The standard error is crucial for determining statistical significance, as it scales the difference between the observed and hypothesized means.

$$SE = \frac{SD}{\sqrt{n}}$$

```latex
SE = \frac{SD}{\sqrt{n}}
```

**Degrees of Freedom:**

Degrees of freedom for a one-sample t-test equal the sample size minus one, reflecting the number of independent pieces of information available for estimating the population variance. This value determines the appropriate t-distribution for calculating p-values and is essential for accurate probability statements about the test statistic.

$$df = n - 1$$

```latex
df = n - 1
```

**Decision Rule:**

Statistical significance is determined by comparing the obtained p-value against a predetermined alpha level (conventionally set at 0.05 for a 5% Type I error rate). A p-value below this threshold leads to rejection of the null hypothesis, providing evidence that the observed accuracy differs significantly from chance. However, statistical significance should be interpreted in conjunction with effect size to assess practical importance.

- If $p < 0.05$: Reject H₀ (significant difference from chance)
- If $p \geq 0.05$: Fail to reject H₀ (no significant difference from chance)

### 3.3 Effect Size (Cohen's d)

While statistical significance indicates whether an effect is likely real, effect size quantifies the magnitude of that effect. Cohen's d expresses the difference between observed and chance-level accuracy in standard deviation units, providing a standardized measure that facilitates comparison across studies. This metric is essential for distinguishing between statistically significant but trivial effects (common with large samples) and meaningful differences with practical implications.

$$d = \frac{\bar{x} - \mu_0}{SD}$$

```latex
d = \frac{\bar{x} - \mu_0}{SD}
```

**Interpretation (Cohen, 1988):**

Cohen's conventional benchmarks provide rough guidelines for interpreting effect sizes, though context-specific considerations should also inform interpretation. In the present context, even a "small" effect (d = 0.2-0.5) might be practically meaningful if it translates to reliably above-chance detection, while a "large" effect (d > 0.8) would indicate robust discrimination ability.

- $|d| < 0.2$: Negligible effect
- $0.2 \leq |d| < 0.5$: Small effect
- $0.5 \leq |d| < 0.8$: Medium effect
- $|d| \geq 0.8$: Large effect

### 3.4 Confidence Interval

The 95% confidence interval provides a range of plausible values for the true population mean accuracy, complementing the point estimate. This interval estimate acknowledges sampling uncertainty and conveys the precision of our estimate. If the interval excludes 50%, this provides converging evidence for rejecting the null hypothesis. Moreover, the width of the interval indicates estimation precision—narrower intervals reflect more precise estimates.

$$CI_{95\%} = \bar{x} \pm 1.96 \times SE$$

```latex
CI_{95\%} = \bar{x} \pm 1.96 \times SE
```

The multiplier 1.96 corresponds to the critical value from the standard normal distribution that captures 95% of the distribution, appropriate for large samples. For smaller samples, the t-distribution critical value should be used instead.

---

## 4. Correlation Analysis

### 4.1 Pearson Correlation Coefficient

The Pearson correlation coefficient quantifies the strength and direction of linear relationships between two continuous variables. This parametric measure ranges from -1 (perfect negative relationship) through 0 (no linear relationship) to +1 (perfect positive relationship). In this study, correlation analysis examines whether individual differences in participant characteristics (experience, confidence) systematically relate to detection accuracy, providing insight into factors that may enhance or impair AI text detection.

$$r = \frac{\sum_{i=1}^{n}(x_i - \bar{x})(y_i - \bar{y})}{\sqrt{\sum_{i=1}^{n}(x_i - \bar{x})^2}\sqrt{\sum_{i=1}^{n}(y_i - \bar{y})^2}}$$

```latex
r = \frac{\sum_{i=1}^{n}(x_i - \bar{x})(y_i - \bar{y})}{\sqrt{\sum_{i=1}^{n}(x_i - \bar{x})^2}\sqrt{\sum_{i=1}^{n}(y_i - \bar{y})^2}}
```

**Interpretation:**

The magnitude of the correlation coefficient indicates relationship strength, while its sign indicates direction. Statistical significance testing determines whether observed correlations are likely to reflect true population relationships or could plausibly arise from sampling variability.

- $r = 1$: Perfect positive correlation
- $r = 0$: No correlation
- $r = -1$: Perfect negative correlation
- $|r| < 0.3$: Weak correlation
- $0.3 \leq |r| < 0.7$: Moderate correlation
- $|r| \geq 0.7$: Strong correlation

### 4.2 Analyzed Correlations

#### 4.2.1 Accuracy vs. Confidence

This analysis examines the relationship between participants' subjective confidence in their classifications and their objective accuracy. A positive correlation would indicate good metacognitive calibration—participants who are more confident are indeed more accurate. Conversely, a near-zero or negative correlation would suggest poor calibration, indicating that participants cannot reliably assess their own detection abilities. This has important practical implications: if instructors cannot gauge when they are correctly identifying AI-generated work, they may make consequential decisions based on unfounded certainty.

**Hypothesis:** Positive correlation expected if metacognitive awareness is accurate.

#### 4.2.2 Accuracy vs. Response Time

The relationship between response time and accuracy can illuminate the cognitive processes underlying AI text detection. A positive correlation would suggest that careful, deliberate analysis improves detection accuracy, supporting interventions that encourage thorough evaluation. A negative correlation might indicate that quick, intuitive judgments are more accurate, perhaps because overthinking leads to second-guessing of initially correct impressions. A null relationship would suggest that speed-accuracy tradeoffs are not operative in this task.

**Hypothesis:** Could be positive (more careful analysis) or negative (overthinking).

#### 4.2.3 Accuracy vs. Teaching Experience

Examining whether teaching experience correlates with detection accuracy addresses whether expertise in evaluating student work confers advantages in identifying AI-generated texts. A positive correlation would support the notion that experienced instructors have developed tacit knowledge of authentic student writing characteristics. However, a null or negative correlation would suggest that traditional pedagogical expertise does not necessarily transfer to AI detection, potentially because AI-generated texts may differ qualitatively from the kinds of student errors experienced instructors have learned to recognize.

**Hypothesis:** Positive correlation if experience improves detection ability.

### 4.3 Independent Samples t-Test

To assess whether confidence judgments track classification accuracy, we compare mean confidence ratings between correct and incorrect classifications using an independent samples t-test. This analysis treats correctness as a grouping variable and tests whether the two groups (correct vs. incorrect responses) differ significantly in average confidence. Higher confidence for correct classifications would indicate some degree of metacognitive sensitivity, even if the correlation between confidence and accuracy is modest.

$$t = \frac{\bar{x}_1 - \bar{x}_2}{\sqrt{\frac{s_1^2}{n_1} + \frac{s_2^2}{n_2}}}$$

```latex
t = \frac{\bar{x}_1 - \bar{x}_2}{\sqrt{\frac{s_1^2}{n_1} + \frac{s_2^2}{n_2}}}
```

where:
- $\bar{x}_1, \bar{x}_2$ = mean confidence for correct/incorrect responses
- $s_1^2, s_2^2$ = variances
- $n_1, n_2$ = sample sizes

The denominator represents the pooled standard error, accounting for variability and sample size in both groups. This formulation assumes unequal variances (Welch's t-test), which is more robust than the traditional equal-variance assumption.

---

## 5. Text Difficulty Analysis

### 5.1 Text-Level Accuracy

Analyzing accuracy separately for each text item reveals which specific passages were most difficult or easiest to classify correctly. This item-level analysis can identify texts that systematically confused participants, potentially due to ambiguous stylistic features or atypical characteristics. Such texts may warrant qualitative analysis to understand what features led to misclassification. Conversely, texts with very high or low accuracy may possess salient features that strongly signal their origin, providing insights into detectable AI-generated text characteristics.

$$ACC_t = \frac{\text{Correct classifications of text } t}{\text{Total classifications of text } t} \times 100\%$$

```latex
ACC_t = \frac{\text{Correct classifications of text } t}{\text{Total classifications of text } t} \times 100\%
```

### 5.2 Text-Level Metrics

For each text, we calculate three complementary metrics that together characterize its difficulty and the cognitive processes it elicits. Accuracy indicates objective difficulty, confidence reflects participants' subjective assessment of task difficulty for that text, and response time indexes cognitive effort. Texts that combine low accuracy with high confidence are particularly concerning, as they may represent cases where AI-generated content successfully mimics human writing characteristics, leading to confident but incorrect classifications.

**Mean Confidence for text $t$:**

Average confidence for a given text indicates participants' collective certainty about that text's origin. Low confidence across participants suggests the text contains ambiguous or conflicting cues, while high confidence indicates apparent clarity—though this confidence may or may not be justified by accuracy.

$$\bar{C}_t = \frac{1}{n_t}\sum_{i=1}^{n_t} c_i$$

```latex
\bar{C}_t = \frac{1}{n_t}\sum_{i=1}^{n_t} c_i
```

where $n_t$ is the number of participants who classified text $t$ and $c_i$ is the confidence rating given by participant $i$.

**Mean Response Time for text $t$:**

Average response time for a text provides a behavioral indicator of processing difficulty. Longer times suggest that participants found the classification decision challenging, perhaps due to subtle or contradictory features. However, response time should be interpreted cautiously, as it may also reflect factors like text length or engagement level rather than strictly classification difficulty.

$$\bar{RT}_t = \frac{1}{n_t}\sum_{i=1}^{n_t} rt_i$$

```latex
\bar{RT}_t = \frac{1}{n_t}\sum_{i=1}^{n_t} rt_i
```

where $rt_i$ is the response time (in milliseconds or seconds) for participant $i$ classifying text $t$.

### 5.3 Difficulty Ranking

Ranking texts by classification accuracy provides an ordered list from most to least difficult, facilitating identification of problematic texts for qualitative follow-up analysis. Texts at the extremes of this distribution are particularly informative: the most difficult texts may reveal the limitations of human detection capabilities or characteristics of sophisticated AI-generated content, while the easiest texts may exemplify clear distinguishing features that could inform detection strategies or training interventions.

Texts are ranked by accuracy (ascending), where:
- **Lowest accuracy** = Most difficult to classify correctly
- **Highest accuracy** = Easiest to classify correctly

This ranking enables systematic investigation of whether text difficulty relates to specific features such as topic, length, complexity, or the particular AI model that generated it (for AI texts) or writing proficiency level (for human texts).

---

## 6. Visualizations

### 6.1 Accuracy Visualizations

#### 6.1.1 Histogram: Distribution of Participant Accuracy

**Purpose:** 

The histogram provides a visual representation of how individual accuracy scores are distributed across participants, revealing the shape of the distribution and whether performance clusters around particular values. This visualization is essential for assessing whether the sample exhibits relatively uniform detection ability or whether it is characterized by substantial individual differences. The distribution's position relative to the chance line (50%) provides an immediate visual test of the research hypothesis, while its spread indicates the degree of between-subject variability that must be accounted for in subsequent analyses.

**Key Elements:**
- Bins represent accuracy ranges (typically in 10% increments)
- Red dashed line indicates chance level (50%)
- Green solid line indicates mean accuracy
- Frequency on y-axis shows number of participants in each accuracy range

**Interpretation:** 

A distribution shifted right of 50% suggests better-than-chance performance at the sample level. The distribution's shape also provides information: a roughly normal distribution supports the appropriateness of parametric statistical tests, while strong skewness or multimodality might suggest subgroups of participants with qualitatively different detection abilities. The spread of the distribution indicates whether most participants perform similarly or whether there are substantial individual differences.

#### 6.1.2 Box Plot: Accuracy Distribution

**Purpose:** 

The box plot complements the histogram by providing a compact summary of the distribution's central tendency, spread, and outliers. This visualization is particularly useful for identifying the median (which is robust to outliers), the interquartile range (representing the middle 50% of participants), and any participants with exceptionally high or low performance. The box plot format also facilitates comparison across groups if additional analyses involve subgroup comparisons.

**Components:**
- **Box:** Interquartile range (IQR) containing 50% of data (from Q₁ to Q₃)
- **Line in box:** Median accuracy (Q₂), which is the 50th percentile
- **Whiskers:** Extend to 1.5 × IQR or to the most extreme data point within this range
- **Outliers:** Individual points beyond whiskers, representing unusual cases

**Formula for IQR:**

The interquartile range quantifies the spread of the middle 50% of the distribution, providing a robust measure of variability that is not influenced by extreme scores.

$$IQR = Q_3 - Q_1$$

```latex
IQR = Q_3 - Q_1
```

where $Q_1$ and $Q_3$ are the first and third quartiles (25th and 75th percentiles, respectively).

**Interpretation:**

The position of the median line relative to the 50% chance level provides a quick visual assessment of whether typical performance exceeds chance. A narrow IQR indicates consistent performance across participants, while a wide IQR suggests substantial individual differences. Outliers warrant particular attention, as they may represent participants with unique characteristics (expertise, strategies) that could inform interventions.

#### 6.1.3 Bar Chart: Accuracy by Text Origin

**Purpose:** 

This visualization directly addresses whether participants exhibit differential detection ability for AI-generated versus human-written texts. Symmetric performance (similar accuracy for both types) would indicate balanced detection ability, while asymmetry reveals systematic biases or differential feature salience. This analysis is crucial for understanding the practical implications of detection performance: if one text type is consistently misclassified, this identifies a specific vulnerability in human detection capabilities.

**Interpretation:**

The interpretation depends on the pattern of results:
- **Equal bars near 50%:** No discrimination ability—participants are essentially guessing for both text types
- **Both bars substantially above 50%:** Good detection for both types, suggesting robust discrimination
- **One bar high, one low:** Asymmetric performance indicating that one origin is easier to detect
- **Both bars below 50%:** Systematic reversal—participants are worse than chance, possibly due to consistent misattribution

For example, if AI texts show 70% accuracy but human texts show 40%, this indicates that AI texts contain more detectable artifacts, but participants struggle to correctly identify authentic student writing, perhaps due to a bias toward attributing polished writing to AI.

#### 6.1.4 Confusion Matrix Heatmap

**Purpose:** 

The confusion matrix provides the most detailed decomposition of classification outcomes, revealing not just overall accuracy but the specific patterns of correct and incorrect judgments. This visualization is essential for diagnosing response biases and understanding the types of errors participants make. Heat map encoding (with color intensity representing cell frequency) makes patterns immediately apparent, while numerical annotations provide precise values.

**Key Metrics Derived:**

Beyond simple accuracy, the confusion matrix enables calculation of several important diagnostic metrics that characterize different aspects of classification performance.

**Overall Accuracy:**

$$Accuracy = \frac{TP + TN}{TP + TN + FP + FN}$$

```latex
Accuracy = \frac{TP + TN}{TP + TN + FP + FN}
```

This represents the proportion of all classifications that were correct, regardless of text type.

**Precision:**

Precision answers the question: "When participants classified a text as AI, how often were they correct?" High precision indicates few false alarms—rarely attributing human texts to AI.

$$Precision = \frac{TP}{TP + FP}$$

```latex
Precision = \frac{TP}{TP + FP}
```

**Recall (Sensitivity):**

Recall answers: "Of all AI texts, what proportion were correctly identified?" High recall means AI texts are rarely missed.

$$Recall = \frac{TP}{TP + FN}$$

```latex
Recall = \frac{TP}{TP + FN}
```

**F1-Score:**

The F1-score provides a single metric that balances precision and recall through their harmonic mean, useful when both false positives and false negatives carry costs.

$$F1\text{-}Score = 2 \times \frac{Precision \times Recall}{Precision + Recall}$$

```latex
F1\text{-}Score = 2 \times \frac{Precision \times Recall}{Precision + Recall}
```

**Interpretation:**

The confusion matrix can reveal several patterns:
- **Liberal bias:** Many false positives (human texts called AI) indicate participants are too quick to attribute texts to AI
- **Conservative bias:** Many false negatives (AI texts called human) suggest participants underestimate AI prevalence or capability
- **Balanced errors:** Similar rates of false positives and false negatives suggest unbiased classification, though not necessarily accurate

### 6.2 Confidence and Response Time Visualizations

#### 6.2.1 Histogram: Confidence Distribution

**Purpose:** 

This visualization reveals how confident participants felt about their classifications overall, which has important implications for interpreting accuracy results and for practical applications. If participants are consistently highly confident regardless of actual accuracy, this suggests poor metacognitive calibration and raises concerns about real-world decision-making based on AI text detection. Conversely, if confidence is generally low, this might indicate appropriate uncertainty recognition.

**Analysis:** 

The distribution's shape provides insights into participants' subjective experience:
- **Right skew (toward higher values):** Participants generally felt confident in their judgments, which is concerning if this confidence is not justified by accuracy
- **Left skew (toward lower values):** Participants recognized uncertainty, which may indicate appropriate epistemic humility
- **Uniform distribution:** Varied confidence across trials suggests that participants adjusted their confidence based on text-specific features
- **Bimodal distribution:** Some texts or participants elicited high confidence while others elicited low confidence, suggesting qualitatively different types of classification decisions

#### 6.2.2 Box Plot: Confidence by Correctness

**Purpose:** 

This critical visualization examines metacognitive calibration by comparing confidence levels between correct and incorrect classifications. Perfect calibration would show markedly higher confidence for correct responses, indicating that participants possess insight into when their judgments are likely to be accurate. Poor calibration (similar confidence for correct and incorrect responses) suggests that subjective confidence is an unreliable indicator of actual accuracy.

**Expected Pattern:** 

From a normative perspective, we would hope to observe significantly higher confidence for correct responses, as this would indicate that instructors can identify situations where they can confidently detect AI-generated work versus situations requiring additional verification. If confidence does not track accuracy, this implies that instructors' subjective certainty cannot guide decision-making about when to trust their AI detection judgments.

**Calibration Score:**

A simple calibration index can be computed as the mean difference in confidence between correct and incorrect responses. Positive values indicate some degree of metacognitive sensitivity.

$$Calibration = \bar{C}_{correct} - \bar{C}_{incorrect}$$

```latex
Calibration = \bar{C}_{correct} - \bar{C}_{incorrect}
```

Values near zero suggest poor calibration, while larger positive values indicate better calibration. However, this simple index should be interpreted alongside the formal statistical test of the confidence difference.

#### 6.2.3 Histogram: Response Time Distribution

**Purpose:** 

Response time distributions provide insight into the cognitive processes underlying classification decisions and can reveal whether participants approached the task uniformly or varied their processing depending on text characteristics. The distribution's shape also has methodological implications: extreme outliers might indicate distraction or technical issues rather than genuine classification time, necessitating consideration of data cleaning procedures.

**Skewness:**

Response time distributions are typically right-skewed (positively skewed) in cognitive tasks, as there is a lower bound (minimum time needed to read and respond) but no firm upper bound. The degree of skewness indicates whether most classifications were completed relatively quickly with a few trials requiring much longer processing.

$$Skewness = \frac{n}{(n-1)(n-2)}\sum_{i=1}^{n}\left(\frac{x_i - \bar{x}}{SD}\right)^3$$

```latex
Skewness = \frac{n}{(n-1)(n-2)}\sum_{i=1}^{n}\left(\frac{x_i - \bar{x}}{SD}\right)^3
```

**Interpretation:**
- **Positive skew:** A few very long response times alongside many moderate times, typical of cognitive tasks. This is expected and indicates that some texts or participants required extended processing.
- **Negative skew:** Few very short response times with most being moderate to long, which might suggest that participants consistently engaged in careful analysis rather than quick intuitive judgments.
- **Approximately normal:** Rare in response time data, would suggest symmetric processing times across trials.

#### 6.2.4 Box Plot: Response Time by Correctness

**Purpose:** 

Comparing response times between correct and incorrect classifications can illuminate the relationship between processing depth and accuracy. This analysis addresses whether "fast and frugal" intuitive judgments are more or less accurate than slower, deliberative processing. The pattern observed has implications for practical recommendations: if accuracy increases with processing time, this would support encouraging thorough evaluation, while the reverse pattern might suggest that initial intuitions should be trusted.

**Possible Interpretations:**

The relationship between response time and accuracy is theoretically ambiguous and empirically variable across tasks:

- **Longer times for correct classifications:** Suggests that careful, systematic analysis improves detection accuracy. This pattern would support interventions that provide checklists or structured evaluation procedures, and would argue against time pressure in assessment contexts.

- **Shorter times for correct classifications:** Suggests that accurate detection relies on rapid pattern recognition and that overthinking may lead to second-guessing of initially correct intuitions. This pattern appears in some expert judgment domains where extensive experience enables quick, accurate decisions.

- **No systematic difference:** Would indicate that speed-accuracy tradeoffs are not operative in this task, or that different participants employ different strategies (some fast and accurate, others slow and accurate). This pattern necessitates more fine-grained analysis to identify effective classification strategies.

The interpretation should also consider text difficulty: perhaps easy texts are classified quickly and accurately, while difficult texts take longer regardless of whether the final classification is correct or incorrect.

### 6.3 Correlation Visualizations

#### 6.3.1 Scatter Plot: Experience vs. Accuracy

**Purpose:** 

This visualization examines whether teaching experience—a proxy for expertise in evaluating student work—relates to AI text detection accuracy. The scatter plot format allows assessment of both the strength and linearity of any relationship, while also revealing the distribution of both variables. If experience relates to accuracy, this would support targeted recruitment of experienced instructors for AI detection tasks or suggest that experience-based training might improve detection capabilities.

**Linear Regression Line:**

A linear regression line (or "line of best fit") is superimposed on the scatter plot to summarize the overall trend. This line represents the predicted accuracy for any given experience level, under the assumption of a linear relationship.

The regression line is defined by two parameters: the intercept (expected accuracy at zero years of experience) and the slope (expected change in accuracy for each additional year of experience).

$$\hat{y} = \beta_0 + \beta_1 x$$

```latex
\hat{y} = \beta_0 + \beta_1 x
```

where $\hat{y}$ is predicted accuracy, $x$ is teaching experience, $\beta_0$ is the intercept, and $\beta_1$ is the slope.

**Slope Calculation:**

The slope quantifies the rate of change—how much accuracy is expected to increase (positive slope) or decrease (negative slope) for each additional year of teaching experience.

$$\beta_1 = \frac{\sum_{i=1}^{n}(x_i - \bar{x})(y_i - \bar{y})}{\sum_{i=1}^{n}(x_i - \bar{x})^2}$$

```latex
\beta_1 = \frac{\sum_{i=1}^{n}(x_i - \bar{x})(y_i - \bar{y})}{\sum_{i=1}^{n}(x_i - \bar{x})^2}
```

A positive $\beta_1$ indicates that accuracy tends to increase with experience, while a negative $\beta_1$ would suggest that more experienced instructors actually perform worse (perhaps due to overconfidence or outdated expectations about student writing).

**Intercept Calculation:**

The intercept represents the expected accuracy for a hypothetical instructor with zero years of experience, serving as the baseline from which experience-related changes are measured.

$$\beta_0 = \bar{y} - \beta_1\bar{x}$$

```latex
\beta_0 = \bar{y} - \beta_1\bar{x}
```

**R-squared (Coefficient of Determination):**

R-squared quantifies the proportion of variance in accuracy that can be predicted from teaching experience. This metric ranges from 0 (experience explains none of the accuracy variance) to 1 (experience perfectly predicts accuracy). In social science research, R-squared values are typically modest even for meaningful relationships, as individual outcomes are influenced by many factors.

$$R^2 = 1 - \frac{SS_{res}}{SS_{tot}}$$

```latex
R^2 = 1 - \frac{SS_{res}}{SS_{tot}}
```

where:

$$SS_{res} = \sum_{i=1}^{n}(y_i - \hat{y}_i)^2, \quad SS_{tot} = \sum_{i=1}^{n}(y_i - \bar{y})^2$$

```latex
SS_{res} = \sum_{i=1}^{n}(y_i - \hat{y}_i)^2, \quad SS_{tot} = \sum_{i=1}^{n}(y_i - \bar{y})^2
```

$SS_{res}$ represents unexplained variance (residual sum of squares—how much accuracy varies even after accounting for experience), while $SS_{tot}$ represents total variance in accuracy. Their ratio indicates what proportion of variance remains unexplained, and subtracting from 1 yields the proportion explained.

**Interpretation:**

- **$R^2 = 0.25$:** Experience explains 25% of accuracy variance—a modest but potentially meaningful relationship
- **$R^2 = 0.09$:** Experience explains only 9% of variance—a weak relationship suggesting that other factors are more important
- **$R^2 < 0.01$:** Essentially no relationship between experience and accuracy

#### 6.3.2 Scatter Plot: Confidence vs. Accuracy

**Purpose:** 

This visualization assesses calibration at the participant level by examining whether individuals who report higher average confidence also demonstrate higher accuracy. Perfect calibration would manifest as a strong positive correlation, indicating that participants who feel more certain are indeed more accurate. This analysis complements the response-level confidence analysis (confidence by correctness) by examining stable individual differences rather than trial-by-trial variation.

**Perfect Calibration:** 

In an ideally calibrated sample, points would cluster along an ascending line where high confidence corresponds to high accuracy. Deviations from this pattern are informative: points in the upper-left quadrant (low confidence, high accuracy) represent unwarranted uncertainty, while points in the lower-right quadrant (high confidence, low accuracy) represent concerning overconfidence—participants who feel certain but are frequently wrong.

**Interpretation:**

Different scatter plot patterns have distinct implications:
- **Strong positive correlation:** Good calibration—more confident participants are more accurate
- **Weak or no correlation:** Poor calibration—confidence does not track ability
- **Negative correlation:** Paradoxical pattern suggesting that less confident participants are more accurate, possibly indicating that recognition of task difficulty (appropriate uncertainty) characterizes better performers

The practical importance of calibration cannot be overstated: in educational contexts, uncalibrated confidence could lead to unjust consequences if instructors act on unfounded certainty about AI detection.

### 6.4 Text-Level Visualization

#### 6.4.1 Horizontal Bar Chart: Accuracy by Text

**Purpose:** 

This item-level analysis identifies which specific texts were most and least successfully classified, providing an empirical basis for selecting texts for qualitative follow-up analysis. Texts that systematically confused participants may contain features that make AI generation difficult to detect or may represent particularly authentic-seeming AI output. Conversely, easily classified texts may exemplify salient distinguishing characteristics that could inform training interventions or automated detection approaches.

**Color Coding:**
- **Red bars:** AI-generated texts
- **Blue bars:** Human-written texts

This color coding allows immediate visual assessment of whether AI or human texts tend to be more accurately classified, complementing the aggregate accuracy-by-origin analysis with item-specific information.

**Analysis:**

The horizontal format (with text identifiers on the y-axis) facilitates labeling of many texts and makes comparisons straightforward. Key patterns to note:

- **Texts far below 50%:** These texts are systematically misclassified, indicating that they possess features strongly associated with the opposite origin. For AI texts below 50%, this suggests highly convincing AI generation; for human texts below 50%, this indicates authentic writing that participants mistakenly perceive as AI-generated (possibly very polished or formal student writing).

- **Texts near 100%:** Easily and reliably classified texts. For AI texts, these may contain obvious artifacts of generation (repetitiveness, generic phrasing, factual errors); for human texts, these may exhibit characteristics that AI rarely replicates (very informal language, clear personal voice, domain-specific errors).

- **Texts near 50%:** Ambiguous texts where participants performed at chance levels. These are particularly interesting as they may represent:
  - AI-generated texts that successfully mimic human writing characteristics
  - Human texts that happen to possess AI-like qualities (perhaps due to template-following or heavily revised writing)
  - Texts with genuinely indeterminate features that provide no reliable detection cues

This visualization should be supplemented with the text ID mapping document to enable qualitative review of specific texts at the extremes and middle of the distribution.

---

## Statistical Power and Sample Size Considerations

### Minimum Detectable Effect

Statistical power analysis is essential for interpreting null results and for planning future research. The minimum detectable effect size represents the smallest true population effect that could be reliably detected given the study's sample size and design. If the study fails to find significant results, but the minimum detectable effect is large, this does not rule out the existence of smaller but still meaningful effects—the study simply lacked sufficient power to detect them.

For a one-sample t-test with conventional parameters:
- $\alpha = 0.05$ (significance level): The probability of falsely rejecting a true null hypothesis (Type I error rate)
- Power = 0.80: The probability of correctly rejecting a false null hypothesis (1 - Type II error rate)
- Two-tailed test: We test for deviations in either direction from chance (better or worse than 50%)

$$d_{min} = \frac{(z_{1-\alpha/2} + z_{power})}{\sqrt{n}}$$

```latex
d_{min} = \frac{(z_{1-\alpha/2} + z_{power})}{\sqrt{n}}
```

where $z_{1-\alpha/2} \approx 1.96$ (critical value for 95% confidence) and $z_{power} \approx 0.84$ (critical value for 80% power).

This formula reveals the fundamental relationship: larger samples enable detection of smaller effects. For example, with n=20 participants, the minimum detectable effect is approximately d=0.65 (medium effect), meaning the study would have low power to detect small effects even if they exist.

### Required Sample Size

Prospective power analysis, conducted before data collection, determines how many participants are needed to reliably detect an effect of specified size. This calculation should be informed by prior research and by consideration of what effect size would be practically meaningful. Detecting trivially small effects with very large samples may be statistically significant but practically unimportant.

For desired power to detect effect size $d$:

$$n = \left(\frac{z_{1-\alpha/2} + z_{power}}{d}\right)^2$$

```latex
n = \left(\frac{z_{1-\alpha/2} + z_{power}}{d}\right)^2
```

For example:
- To detect a small effect (d = 0.3) with 80% power: n ≈ 88 participants
- To detect a medium effect (d = 0.5) with 80% power: n ≈ 34 participants  
- To detect a large effect (d = 0.8) with 80% power: n ≈ 15 participants

These calculations assume equal numbers of AI and human texts and a balanced design. Unbalanced designs or additional complexity (covariates, multiple groups) may require larger samples.

---

## Assumptions and Limitations

### Statistical Assumptions

Parametric statistical tests rest on assumptions that should be verified to ensure valid inference. Violations of assumptions can lead to inflated Type I error rates (false positives) or reduced power.

1. **Normality:** 

The one-sample t-test assumes that participant-level accuracy scores are approximately normally distributed, or that the sample is large enough for the Central Limit Theorem to ensure approximately normal sampling distribution of the mean. Normality can be assessed through visual inspection (histogram, Q-Q plot) and formal tests (Shapiro-Wilk). Moderate violations are generally tolerable with samples of n>30, but severe skewness or outliers may necessitate non-parametric alternatives (Wilcoxon signed-rank test) or bootstrapping methods.

2. **Independence:** 

Each participant's classifications must be independent of others' responses, meaning that participants cannot collaborate or influence each other. This assumption is satisfied by study design if participants complete the task individually. However, within-participant dependencies (each participant classifies multiple texts) necessitate participant-level aggregation for between-subject analyses, which our analytical approach respects.

3. **Random Sampling:** 

For results to generalize to a broader population, participants should ideally be randomly sampled from that population. In practice, educational research often relies on convenience samples (volunteer participants), which may limit generalizability. Similarly, the texts should represent the range of student writing and AI capabilities of interest. Selection biases in either participants or texts could limit the external validity of findings.

### Potential Limitations

1. **Sample Size:** 

Small participant samples, while potentially adequate for detecting large effects, limit power to detect subtle relationships and increase sampling variability. Small samples also reduce precision of effect size estimates and correlation coefficients. Future research with larger samples could detect smaller but potentially important effects and provide more precise parameter estimates.

2. **Text Selection:** 

The texts used in this study necessarily represent a limited sample of possible student writing and AI-generated content. They may not capture the full range of writing quality, topics, or AI generation strategies. Texts from specific academic contexts may not generalize to other disciplines or levels of education. Additionally, rapidly evolving AI capabilities mean that contemporary findings may not apply to future models.

3. **Order Effects:** 

Although randomization mitigates systematic order effects, learning and fatigue could still influence performance across the sequence of classifications. Early texts might be classified differently than later ones if participants develop strategies or become fatigued. The recorded trial number (index) enables examination of these potential order effects in post-hoc analyses.

4. **Binary Classification Task:** 

The forced-choice classification (AI vs. human) oversimplifies the reality that texts may involve AI assistance at varying levels (from minor editing suggestions to complete generation). Real-world writing increasingly involves human-AI collaboration, creating a continuum rather than a dichotomy. Participants' performance on this binary task may not predict their ability to detect or evaluate AI-assisted work.

5. **Time Period Specificity:** 

AI text generation capabilities improve rapidly. Findings from this study characterize detection accuracy for specific AI models at a particular point in time. As newer models generate increasingly sophisticated text, detection difficulty will likely increase, potentially making these findings conservative estimates of future challenges.

6. **Ecological Validity:** 

The experimental context—evaluating decontextualized text excerpts under time recording—differs from authentic assessment scenarios where instructors have contextual knowledge about students, can consider writing trajectory, and evaluate complete assignments rather than isolated passages. Performance in this controlled setting may not fully predict real-world detection accuracy.

7. **Participant Motivation:** 

Research participants may not exert the same level of effort or employ the same strategies they would use in high-stakes authentic assessment situations. Knowing that their judgments carry no real consequences might influence both accuracy and confidence ratings.

---

## References

Cohen, J. (1988). *Statistical Power Analysis for the Behavioral Sciences* (2nd ed.). Hillsdale, NJ: Lawrence Erlbaum Associates.

Field, A. (2013). *Discovering Statistics Using IBM SPSS Statistics* (4th ed.). London: SAGE Publications.

Fleckenstein, J., Meyer, J., Jansen, T., Keller, S. D., Köller, O., & Möller, J. (2024). Do teachers spot AI? Evaluating the detectability of AI-generated texts among student essays. *Computers and Education: Artificial Intelligence*, 6, 100209.

---

## Appendix: Quick Reference Formulas

### Descriptive Statistics

| Metric | Formula | LaTeX |
|--------|---------|-------|
| Mean | $\bar{x} = \frac{1}{n}\sum_{i=1}^{n} x_i$ | `\bar{x} = \frac{1}{n}\sum_{i=1}^{n} x_i` |
| Standard Deviation | $SD = \sqrt{\frac{1}{n-1}\sum_{i=1}^{n}(x_i - \bar{x})^2}$ | `SD = \sqrt{\frac{1}{n-1}\sum_{i=1}^{n}(x_i - \bar{x})^2}` |
| Standard Error | $SE = \frac{SD}{\sqrt{n}}$ | `SE = \frac{SD}{\sqrt{n}}` |

### Inferential Statistics

| Test | Formula | LaTeX |
|------|---------|-------|
| t-statistic | $t = \frac{\bar{x} - \mu_0}{SE}$ | `t = \frac{\bar{x} - \mu_0}{SE}` |
| Cohen's d | $d = \frac{\bar{x} - \mu_0}{SD}$ | `d = \frac{\bar{x} - \mu_0}{SD}` |
| Pearson r | $r = \frac{\sum(x_i - \bar{x})(y_i - \bar{y})}{\sqrt{\sum(x_i - \bar{x})^2\sum(y_i - \bar{y})^2}}$ | `r = \frac{\sum(x_i - \bar{x})(y_i - \bar{y})}{\sqrt{\sum(x_i - \bar{x})^2\sum(y_i - \bar{y})^2}}` |

### Accuracy Metrics

| Metric | Formula | LaTeX |
|--------|---------|-------|
| Accuracy | $\frac{TP + TN}{TP + TN + FP + FN}$ | `\frac{TP + TN}{TP + TN + FP + FN}` |
| Sensitivity | $\frac{TP}{TP + FN}$ | `\frac{TP}{TP + FN}` |
| Specificity | $\frac{TN}{TN + FP}$ | `\frac{TN}{TN + FP}` |
| Precision | $\frac{TP}{TP + FP}$ | `\frac{TP}{TP + FP}` |

---

*Document Version: 1.0*  
*Last Updated: December 2025*