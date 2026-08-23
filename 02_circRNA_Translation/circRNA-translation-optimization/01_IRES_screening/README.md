# 01 — IRES Screening

## Research question

Which candidate IRES elements provide strong translation activity in the engineered circRNA reporter system, and which candidates remain strong when the screening is repeated?

The analysis treats IRES screening as a **selection problem**, not simply a ranking exercise. A useful lead should combine translation performance with reproducibility and acceptable experimental variability.

## Experimental workflow

```text
Candidate IRES elements
        ↓
Initial screening
        ↓
Normalization to FHB reference
        ↓
Repeat screening
        ↓
Initial vs repeat comparison
        ↓
Reproducibility analysis
        ↓
Candidate prioritization
```

## Data organization

The original quantitative files are preserved without changing their values. They are stored under `data/` and include raw luminescence, normalized initial screening results, repeat-screening values, repeat summaries, and the initial-vs-repeat comparison.

The data-level README remains focused on describing those files; this README describes the overall screening project and analysis logic.

## Analysis workflow

The `analysis/` directory contains reproducible Python scripts that read the stored CSV files and calculate:

- initial vs repeat performance
- Pearson correlation and Spearman rank correlation
- within-repeat coefficient of variation (CV)
- absolute inter-experiment change
- rank changes between experiments
- a conservative candidate-prioritization class

The current reproducibility analysis excludes the FHB reference from correlation calculations because FHB is fixed at 100 in both summary datasets.

## Candidate-selection logic

To avoid selecting candidates based only on a single high measurement, the current analysis defines a **stable high performer** using three criteria:

1. Repeat-screening mean ≥ 300 relative translation units
2. Repeat-screening CV ≤ 10%
3. Absolute change between initial and repeat means ≤ 20%

Candidates with high repeat performance that fail one or more stability criteria are classified as **high performers requiring validation** rather than being discarded.

## Key result

The initial and repeat experiments show strong overall agreement in candidate ranking:

- **Spearman rank correlation: 0.923**
- **Pearson correlation: 0.896**

Using the criteria above, the current dataset identifies **EVB80, FMDV (A/O), CVA3, and CVA17** as stable high performers. **Echo26, CVA7, and CVA12** remain high-performing candidates but require additional validation because one or more stability criteria are not met.

CVA12 is particularly informative: its repeat mean is high and its within-repeat CV is low, but its repeat performance increased substantially relative to the initial experiment. This makes it a strong candidate for follow-up validation rather than an automatic final selection.

## Interpretation

The repeat experiment therefore supports a more nuanced conclusion than simply choosing the highest-scoring IRES. The overall ranking is reproducible, but individual candidates differ in inter-experiment stability and within-repeat variability. Candidate selection should consider all three dimensions before downstream optimization.

## Figures and results

- `figures/initial_vs_repeat_reproducibility.png` — relationship between initial and repeat screening performance
- `figures/repeat_screening_cv.png` — within-repeat variability for each candidate
- `results/` — derived reproducibility metrics and interpretation

The analysis is intentionally separated from the underlying measurements so that the workflow can be rerun when additional screening experiments are added.
