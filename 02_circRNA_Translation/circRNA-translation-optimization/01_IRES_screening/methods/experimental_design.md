# Experimental Design — IRES Screening

## 1. Research motivation

Linear RNA can be unstable in cells and undergo degradation, limiting the duration of CDS expression. Circular RNA (circRNA) was therefore investigated as a more stable RNA format for sustained expression.

A key limitation of circRNA translation is the absence of a conventional 5′ cap. Unlike linear mRNA, circRNA cannot rely on cap-dependent translation initiation and therefore requires a cap-independent initiation mechanism such as an internal ribosome entry site (IRES).

The purpose of the IRES screening experiment was to identify IRES elements that could improve translation efficiency from the circRNA system and to establish candidates suitable for subsequent circRNA optimization and applications such as vaccine constructs.

## 2. Screening objective

The screening had two related goals:

1. identify IRES elements with high relative translation activity; and
2. determine which high-performing candidates remain reproducible in an independent repeat experiment.

The initial screening included approximately **100 IRES candidates**.

## 3. Reporter construct

The reporter plasmid used for screening contained **Firefly luciferase (F-luc)** and **Gaussia luciferase (Gluc)** reporter components. The variable sequence region was designed so that different UTR sequences could be introduced/replaced for subsequent optimization experiments.

For the IRES screening, candidate IRES elements were evaluated in the same reporter framework. The plasmid map used during the experimental design is retained as the construct reference for this project.

> **Figure note:** The current construct map shows the F-luc and Gluc reporter regions and the variable sequence region used for UTR replacement. Exact sequence-level annotation should be added only when the corresponding construct record is available.

## 4. Cell and transfection system

- **Cell line:** HEK293T
- **Plate format:** 96-well plate
- **Cell seeding density:** 4 × 10⁴ cells/well
- **Transfection reagent:** Lipofectamine 3000
- **Replicates:** 2 technical replicates per condition
- **Final well volume:** 100 µL/well

### Transfection setup

The transfection mixture was prepared using the following volumes per well:

**Plasmid/sample mixture**
- Plasmid (sample): **8 µL**
- Opti-MEM: **5 µL**
- P3000: **0.2 µL**

**Lipofectamine mixture**
- Opti-MEM: **5 µL**
- Lipofectamine 3000: **0.3 µL**

The two mixtures were prepared separately and then used for transfection. No additional protocol parameters are inferred beyond the values recorded above.

The initial and repeat screens were performed approximately one week apart. Experimental conditions were kept consistent between the two screens. Cell passage differed by approximately one to two passages between experiments.

## 5. Luciferase assay

A dual-luciferase-based measurement was used to quantify reporter activity.

- **Firefly luciferase (F-luc):** control/reference reporter
- **Gaussia luciferase (Gluc):** experimental reporter reflecting the translation activity being compared across IRES candidates

The Gluc signal was normalized to the corresponding Firefly signal for each technical replicate before averaging replicates.

## 6. Initial and repeat screening design

The repeat experiment was designed to test **reproducibility across the full candidate set**, rather than selectively repeating only the highest-performing candidates.

The same IRES candidates were screened again under the same overall experimental conditions approximately one week after the initial experiment. Luciferase measurements were collected **24 hours after transfection** in both experiments.

This design allowed candidate ranking and quantitative performance to be compared between independent experimental runs.

## 7. Follow-up strategy

The initial screening identified several high-performing candidates, with **EVB80** showing particularly strong translation activity. EVB80 was therefore used as an important candidate for subsequent optimization experiments.

Additional candidates including **CVA3, CVA7, and CVA12** were also carried forward for subsequent experiments, where IRES candidates were combined with different UTR configurations to test whether performance could be further improved.

## 8. Experimental interpretation

The screening was not treated as a simple search for the single highest numerical value. Repeatability was considered important when prioritizing candidates for downstream experiments.

The subsequent IRES–UTR experiments also motivated an important design consideration: strong performance of an IRES and strong performance of a UTR do not necessarily guarantee strong performance when the two elements are combined. RNA secondary structure and potential higher-order structural interactions may influence the resulting translation phenotype, making the behavior of combined regulatory elements difficult to predict solely from the individual screening results.

These observations motivated the integrated optimization stage of the project.

## 9. Scope and reproducibility note

Only experimental details supported by the current experimental record are documented here. Exact plasmid sequences and any protocol-level parameters not provided in the experimental record are intentionally not inferred.
