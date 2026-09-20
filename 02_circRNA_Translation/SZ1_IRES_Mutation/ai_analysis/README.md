# AI Analysis — SZ1 IRES Translation Efficiency

This folder documents the computational workflow used to connect the SZ1 IRES mutation experiments with RNA-structure analysis and a proof-of-concept machine-learning workflow.

## Workflow

1. Generate all single-nucleotide substitutions from the 650-nt SZ1 IRES sequence.
   - 650 positions × 3 alternative RNA bases = 1,950 variants.
2. Predict RNA secondary structures and minimum free energy (MFE) with ViennaRNA/RNAfold.
3. Calculate ΔMFE relative to the WT sequence.
4. Map experimentally measured translation efficiency to the corresponding sequence positions.
5. Build a training dataset combining experimental translation efficiency and RNA-structure features.
6. Train a Random Forest regressor as a proof-of-concept model and inspect feature importance.

## Current experimental dataset

The experimentally measured dataset currently contains a small number of validated SZ1 variants. The present model is therefore a **proof-of-concept**, not a validated predictive model. The code is kept reproducible so the dataset can be expanded as additional experiments are performed.

## Local PowerShell workflow

From the project root:

```powershell
python .\src\generate_mutants.py
python .\src\run_rnafold.py --input .\data\all_single_substitutions.csv --output .\results\rnafold_results.csv --wt-fasta .\data\sz1_ires_wt.fasta --circ
python .\src\build_training_dataset.py
python .\src\train_model.py
```

> `--circ` treats the supplied 650-nt sequence itself as circular for the RNAfold calculation. It does not mean that the full biological circRNA construct has been modeled.

## Files

- `src/generate_mutants.py` — generates the 1,950 single-substitution library.
- `src/run_rnafold.py` — runs RNAfold and calculates MFE/ΔMFE.
- `src/build_training_dataset.py` — combines experimental labels with structure features.
- `src/train_model.py` — Random Forest proof-of-concept model.
