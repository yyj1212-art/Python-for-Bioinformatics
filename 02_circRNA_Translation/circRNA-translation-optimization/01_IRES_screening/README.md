# 01 — IRES Screening

## Objective

Identify candidate IRES elements that support strong cap-independent translation from the engineered circRNA reporter system and assess whether the observed ranking is reproducible in an independent screening experiment.

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
Candidate prioritization
```

## Data organization

The original quantitative files are preserved without changing their values. They are stored under `data/` and include raw luminescence, normalized initial screening results, repeat-screening values, repeat summaries, and the initial-vs-repeat comparison.

The data-level README remains focused on describing those files; this README describes the overall screening project and analysis logic.

## Analysis

The `analysis/` directory contains lightweight scripts used to generate reproducible summary figures from the stored CSV files.

## Figures

The `figures/` directory contains presentation-ready visualizations generated from the screening summary data. Figures are derived from the stored measurements rather than manually recreated values.

## Interpretation note

The purpose of the repeat experiment is not simply to reproduce a single numerical value, but to determine whether the relative performance of candidate IRES elements is sufficiently consistent to support downstream selection. Differences between experiments should therefore be considered alongside the magnitude and variability of each candidate's response.
