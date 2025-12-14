# AI Text Detection Study - Statistical Analysis

**Analysis Date:** 2025-12-14 12:53:22  
**Data Source:** `Response-2025-12-14.csv`

---

✓ Text ID mapping saved to: `text_id_mapping.md`

## 1. Descriptive Statistics

**Number of participants:** 4

### Participant Demographics

- **Mean teaching experience:** 6.75 years (SD = 3.59)
- **Range:** 2 - 10 years

**Departments represented:**

- English Linguistics: 2
- Language Competence: 1
- IfA: 1

### Text Information

- **Total number of texts:** 10
- **AI-generated texts:** 5
- **Human-written texts:** 5

### Response Information

**Total responses collected:** 40

**Classifications:**
- Classified as AI: 14
- Classified as Human: 26

### Confidence Ratings

- **Mean:** 3.65 (SD = 0.74)
- **Median:** 4
- **Range:** 2 - 5

### Response Times

- **Mean:** 70.83 seconds (SD = 45.85)
- **Median:** 63.69 seconds
- **Range:** 12.02 - 206.24 seconds

---

## 2. Accuracy Analysis

**Overall accuracy:** 80.00%

### Participant-Level Accuracy

- **Mean:** 80.00% (SD = 16.33%)
- **Range:** 60.00% - 100.00%

### Accuracy by Text Origin

- **AI-generated:** 65.00% (13/20 correct)
- **HUMAN-generated:** 95.00% (19/20 correct)

### Confusion Matrix

| Actual \ Classified | AI | Human | Total |
|---------------------|----:|------:|------:|
| **AI** | 13 | 7 | 20 |
| **HUMAN** | 1 | 19 | 20 |
| **Total** | **14** | **26** | **40** |

### Diagnostic Measures

- **Sensitivity (True Positive Rate):** 65.00%
- **Specificity (True Negative Rate):** 95.00%

---

## 3. Hypothesis Testing

### Hypotheses

- **H₀ (Null Hypothesis):** Accuracy = 50% (chance level)
- **H₁ (Alternative Hypothesis):** Accuracy ≠ 50%

### One-Sample t-Test Results

- **t-statistic:** t(3) = 3.674
- **p-value:** 0.0349
- **Mean accuracy:** 80.00%
- **95% Confidence Interval:** [64.00%, 96.00%]

### Interpretation

**Result:** REJECT H₀ (p < 0.05)

**Conclusion:** Participants performed significantly **better than chance**.

### Effect Size

- **Cohen's d:** 1.837
- **Interpretation:** large effect

---

## 4. Correlation Analysis

### Participant-Level Correlations

**Accuracy vs. Confidence:**
- Pearson r = 0.707, p = 0.2929

**Accuracy vs. Response Time:**
- Pearson r = -0.933, p = 0.0670

**Accuracy vs. Teaching Experience:**
- Pearson r = 0.114, p = 0.8864

### Response-Level Analysis

**Confidence by Correctness:**

- **Correct responses:** M = 3.81 (SD = 0.64)
- **Incorrect responses:** M = 3.00 (SD = 0.76)

**Independent t-test:** t = 3.084, p = 0.0038

---

## 5. Text Difficulty Analysis

Texts ranked by difficulty (lowest accuracy first):

| Text ID | Origin | Accuracy (%) | Confidence | Response Time (ms) |
|--------:|:-------|-------------:|-----------:|-------------------:|
| 6 | AI | 25.0 | 3.25 | 111473 |
| 7 | AI | 50.0 | 3.00 | 69898 |
| 2 | HUMAN | 75.0 | 3.75 | 73504 |
| 8 | AI | 75.0 | 3.00 | 66910 |
| 9 | AI | 75.0 | 3.25 | 48920 |
| 4 | HUMAN | 100.0 | 3.75 | 117866 |
| 1 | HUMAN | 100.0 | 4.25 | 55923 |
| 3 | HUMAN | 100.0 | 4.25 | 60547 |
| 5 | HUMAN | 100.0 | 4.25 | 62732 |
| 10 | AI | 100.0 | 3.75 | 40506 |

---

## 6. Visualizations

Generating visualizations...

- ✓ `accuracy/histogram.png`
- ✓ `accuracy/boxplot.png`
- ✓ `accuracy/by_origin.png`
- ✓ `accuracy/confusion_matrix.png`
- ✓ `confidence_time/confidence_distribution.png`
- ✓ `confidence_time/confidence_by_correctness.png`
- ✓ `confidence_time/response_time_distribution.png`
- ✓ `confidence_time/response_time_by_correctness.png`
- ✓ `correlations/experience_vs_accuracy.png`
- ✓ `correlations/confidence_vs_accuracy.png`
- ✓ `by_text/accuracy_by_text.png`

---

## Summary

Analysis complete! All results have been saved to: `analysis_Response-2025-12-14_20251214_125322`

### Generated Files

**Reports:**
- `analysis_results.md` - This comprehensive analysis report
- `text_id_mapping.md` - Reference guide mapping text IDs to titles

**Visualizations:**
- `accuracy/` - Accuracy distribution and performance metrics
- `confidence_time/` - Confidence and response time analyses
- `correlations/` - Relationship analyses between variables
- `by_text/` - Item-level difficulty analysis

