# IRES screening results

## Reproducibility analysis

The initial and repeat screening summaries were compared to determine whether candidate ranking was preserved across experiments and whether high-performing candidates were sufficiently stable for follow-up.

### Global reproducibility

- Spearman rank correlation, excluding the FHB reference: **0.923**
- Pearson correlation, excluding the FHB reference: **0.896**

The high rank correlation indicates that the overall ordering of IRES candidates was substantially preserved between the two screening experiments, while the differences for individual candidates show that ranking alone is not sufficient for candidate selection.

### Candidate-selection rule used in this analysis

A candidate was classified as a **stable high performer** when all three criteria were met:

1. Repeat-screening mean ≥ 300 relative translation units
2. Repeat-screening coefficient of variation (CV) ≤ 10%
3. Absolute change between initial and repeat means ≤ 20%

Candidates with high repeat performance but failing one or more stability criteria were retained as **high performers requiring validation**, rather than being discarded.

### Stable high performers

- EVB80
- FMDV (A/O)
- CVA3
- CVA17

### High performers requiring validation

- Echo26
- CVA7
- CVA12

CVA12 is particularly notable because its repeat mean increased substantially relative to the initial experiment. Its low within-repeat CV suggests that the repeat experiment itself was consistent, but the large inter-experiment shift means additional independent validation would be appropriate before treating it as a robust lead.

### Interpretation

The purpose of this analysis is not to declare a single definitive best IRES from the available experiments. Instead, it separates candidates into reproducible high performers and candidates that require further validation. This makes the screening workflow more defensible for subsequent optimization experiments.
