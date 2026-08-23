# IRES Screening — Data

This folder contains the quantitative data extracted from the experimental screening records.

## Files

- `01_initial_screening_raw_luminescence.csv` — raw Firefly and Gaussia luminescence values from the initial screening.
- `02_initial_screening_summary.csv` — initial screening normalized to FHB = 100 with the reported SD values.
- `03_repeat_screening_values.csv` — visible replicate-level normalized values from the repeat experiment.
- `04_repeat_screening_summary.csv` — repeat screening normalized to FHB = 100 with the reported SD values.
- `05_initial_vs_repeat_comparison.csv` — direct comparison of the reported initial and repeat means.

## Conditions

FHB, EVB80, Echo20, Echo26, Echo33, FMDV (A/O), CVA3, CVA7, CVA9, CVA12, CVA17, CVA19, CVB5

## Data handling

- The quantitative values are preserved from the existing screening data.
- No missing replicate values are reconstructed.
- FHB is retained as the reference condition (100) where the source summary used that normalization.
- The 260626 and 260702 labels are preserved in the comparison file.
