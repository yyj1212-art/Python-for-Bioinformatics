#!/usr/bin/env python3
"""Merge experimental translation-efficiency labels with RNAfold features."""
from __future__ import annotations
import argparse
from pathlib import Path
import pandas as pd

# Experimentally mapped sites used in the current SZ1 proof-of-concept dataset.
DEFAULT_VARIANTS = {
    "SZ1-0A": (344, "G", "A"),
    "SZ1-0C": (344, "G", "C"),
    "SZ1-0T": (344, "G", "T"),
    "SZ1-1A": (345, "C", "A"),
    "SZ1-1G": (345, "C", "G"),
    "SZ1-1T": (345, "C", "T"),
    "SZ1-2A": (346, "T", "A"),
    "SZ1-2C": (346, "T", "C"),
    "SZ1-2G": (346, "T", "G"),
}

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--rnafold", default="results/rnafold_results.csv")
    p.add_argument("--experimental", default="data/experimental_variant_summary.csv")
    p.add_argument("--output", default="results/training_dataset.csv")
    args = p.parse_args()

    rnafold = pd.read_csv(args.rnafold)
    experimental = pd.read_csv(args.experimental)

    required = {"variant", "experimental_TE_WT100", "n_experiments"}
    missing = required - set(experimental.columns)
    if missing:
        raise ValueError(f"Experimental file is missing columns: {sorted(missing)}")

    meta = pd.DataFrame([
        {
            "variant": name,
            "position_1based": info[0],
            "wt_base": info[1],
            "mutant_base": info[2],
        }
        for name, info in DEFAULT_VARIANTS.items()
    ])

    experimental = experimental.merge(meta, on="variant", how="inner")
    experimental["variant_key"] = (
        experimental["position_1based"].astype(str)
        + experimental["wt_base"]
        + ">" + experimental["mutant_base"]
    )
    rnafold["variant_key"] = (
        rnafold["position_1based"].astype(str)
        + rnafold["wt_base"]
        + ">" + rnafold["mutant_base"]
    )

    features = [
        "position_1based", "wt_base", "mutant_base",
        "mfe_kcal_mol", "wt_mfe_kcal_mol",
        "delta_mfe_vs_wt", "structure"
    ]
    merged = experimental.merge(
        rnafold[["variant_key"] + features],
        on="variant_key",
        how="left",
        suffixes=("", "_rnafold"),
    )

    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    merged.to_csv(out, index=False)

    print(merged[
        ["variant", "position_1based", "experimental_TE_WT100",
         "n_experiments", "mfe_kcal_mol", "delta_mfe_vs_wt"]
    ].to_string(index=False))
    print(f"\nOutput: {out}")

if __name__ == "__main__":
    main()
