#!/usr/bin/env python3
"""Proof-of-concept Random Forest model for experimental SZ1 translation efficiency."""
from __future__ import annotations
import argparse
from pathlib import Path
import pandas as pd
from sklearn.ensemble import RandomForestRegressor

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--input", default="results/training_dataset.csv")
    p.add_argument("--output", default="results/model_feature_importance.csv")
    args = p.parse_args()

    df = pd.read_csv(args.input).dropna(
        subset=["experimental_TE_WT100", "mfe_kcal_mol", "delta_mfe_vs_wt"]
    )

    for base in "ACGU":
        df[f"mutant_is_{base}"] = (df["mutant_base"] == base).astype(int)

    feature_cols = [
        "position_1based", "mfe_kcal_mol",
        "wt_mfe_kcal_mol", "delta_mfe_vs_wt"
    ] + [f"mutant_is_{base}" for base in "ACGU"]

    X = df[feature_cols]
    y = df["experimental_TE_WT100"]

    model = RandomForestRegressor(
        n_estimators=300,
        random_state=42,
        min_samples_leaf=2,
    )
    model.fit(X, y)

    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    (
        pd.DataFrame({"feature": X.columns, "importance": model.feature_importances_})
        .sort_values("importance", ascending=False)
        .to_csv(out, index=False)
    )

    print(f"Training samples: {len(df)}")
    print("Note: this dataset is a proof-of-concept and is too small for a robust generalization claim.")
    print(f"Output: {out}")

if __name__ == "__main__":
    main()
