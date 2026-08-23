# Assay and Data Processing — IRES Screening

## 1. Measurement workflow

The screening workflow was:

```text
HEK293T cells
      ↓
Lipofectamine 3000 transfection in 96-well plates
      ↓
24 h incubation
      ↓
Dual-luciferase measurement
      ↓
Firefly and Gaussia luminescence values
      ↓
Gluc / F-luc normalization
      ↓
Average of technical replicates
      ↓
WT (FHB) normalization
      ↓
Relative translation activity
```

## 2. Technical replicate processing

Each IRES condition was measured in two technical replicates.

For each replicate, the Gaussia luciferase signal was normalized to the corresponding Firefly luciferase signal:

`G/F = Gaussia luminescence / Firefly luminescence`

The two replicate-level G/F values were then averaged to obtain the condition-level mean.

The standard deviation between the two technical replicates was also calculated to represent within-condition measurement variability.

## 3. WT (FHB) normalization

The **FHB sample was the WT normalization reference**.

The mean G/F value of each candidate was divided by the mean G/F value of FHB (WT) and multiplied by 100:

`Relative translation activity = (candidate mean G/F / FHB mean G/F) × 100`

Under this normalization, FHB (WT) corresponds to **100 relative translation units**.

The replicate standard deviation was normalized using the same FHB (WT) reference so that variability remained on the same relative scale as the normalized mean.

## 4. Initial vs repeat comparison

The same processing workflow was applied to both the initial and repeat screening experiments.

The resulting normalized values were compared across experiments to evaluate:

- absolute performance differences
- candidate rank stability
- within-repeat variability
- reproducibility of high-performing candidates

The full candidate set was repeated rather than selecting only the initial top performers. This provides a stronger basis for assessing whether the initial screening ranking was robust to an independent experimental run.

## 5. Data hierarchy in the repository

The repository separates the experimental measurements from derived analysis products:

```text
raw luminescence
      ↓
initial screening summary
      ↓
repeat screening values
      ↓
repeat screening summary
      ↓
initial-vs-repeat comparison
      ↓
reproducibility analysis
      ↓
candidate prioritization
```

The original CSV files are retained without changing their measured values. Derived tables and figures are generated separately so that the analysis can be reproduced without overwriting the experimental record.

## 6. Important interpretation boundary

The normalized value represents **relative reporter activity within the screening system**. It should not be interpreted as an absolute translation rate or as a direct measurement of circRNA abundance.

The screening therefore answers the practical question of which IRES configurations produced stronger reporter output under the tested conditions, while additional experiments are required to distinguish effects arising from RNA abundance, stability, translation initiation, or other biological mechanisms.
