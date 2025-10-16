# Motor Activity as Depression Biomarker: Statistical Analysis using SPSS

## Background

Major Depressive Disorder features psychomotor disturbances observable through activity monitoring. This analysis investigates whether actigraphy data can differentiate depressed patients from controls and correlate with symptom severity.

**Dataset:** Depresjon (Garcia-Ceja et al., 2018)  
**Sample:** 23 depressed patients, 32 healthy controls  
**Measures:** Wrist accelerometer activity, MADRS scores

---

## Research Questions

**Q1:** Do depressed patients show different mean motor activity than controls?  
**Hypothesis:** Lower activity in depression (psychomotor retardation)

**Q2:** Do depressed patients show different activity variability?  
**Hypothesis:** Higher variability in depression (circadian dysregulation)

**Q3:** Does activity correlate with depression severity (MADRS)?  
**Hypothesis:** Lower activity correlates with higher MADRS scores

**Q4:** Can activity features predict depression status?  
**Hypothesis:** Logistic model achieves >70% classification accuracy

---

## Methods

### Data Preparation
1. Aggregated timeseries to person-level metrics (mean, SD per subject)
2. Merged with clinical data from scores.csv
3. Created binary grouping variable (0=Control, 1=Condition)

### Statistical Analyses

**Analysis 1:** Independent t-test (mean_activity × group)  
**Analysis 2:** Independent t-test (sd_activity × group)  
**Analysis 3:** Pearson correlation (mean_activity × madrs1, condition group only)  
**Analysis 4:** Binary logistic regression (predictors: mean_activity, sd_activity)

**Visualizations:** Boxplot (Q1), Scatterplot (Q3)

---

## Key Results

| Analysis | Test | Result | Effect Size | Interpretation |
|----------|------|--------|-------------|----------------|
| Q1: Mean Activity | t(52) = 2.182 | p = .034 | d = 0.575 | Controls > Condition |
| Q2: Variability | t(53) = 2.653 | p = .010 | d = 0.725 | Controls > Condition |
| Q3: MADRS Correlation | r = .080 | p = .717 | - | Not significant |
| Q4: Prediction Model | χ²(2) = 7.362 | p = .025 | R² = .169 | 65.5% accuracy |

[View Full Results (PDF)](output2.pdf)

---

## Conclusions

**Supported:**
- Depressed patients have lower motor activity (psychomotor retardation)
- Depressed patients show lower variability (behavioral rigidity)
- Activity features predict depression status

**Not Supported:**
- Activity does not correlate with symptom severity
- Classification accuracy modest (65.5%)

**Clinical Implications:**  
Activity monitoring shows promise as categorical biomarker (depressed vs. not) but insufficient for tracking symptom severity or standalone diagnosis.

---

## Limitations

- Small sample (n=55)
- Heterogeneous depression group (unipolar + bipolar)
- Cross-sectional design
- Simple metrics (mean, SD only)
- No medication data

---

## Files

- `aggregate_activity_data.py` - Data processing script
- `depression_analysis_dataset.csv` - Analysis-ready dataset
- SPSS output tables and visualizations
