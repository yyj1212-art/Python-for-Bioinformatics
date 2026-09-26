#!/usr/bin/env python3
"""Run ViennaRNA RNAfold on WT/mutant sequences and calculate ΔMFE vs WT."""
from __future__ import annotations
import argparse, csv, subprocess
from pathlib import Path

def fold(seq: str, circ: bool = False):
    cmd = ["RNAfold", "--noPS"]
    if circ:
        cmd.append("--circ")
    result = subprocess.run(cmd, input=seq + "\n", text=True, capture_output=True, check=True)
    lines = [x.strip() for x in result.stdout.splitlines() if x.strip()]
    if len(lines) < 2:
        raise RuntimeError(f"Unexpected RNAfold output: {result.stdout}")
    structure, mfe_text = lines[-1].rsplit(" ", 1)
    return structure, float(mfe_text.strip("()"))

def read_fasta(path: Path):
    seq = "".join(
        x.strip() for x in path.read_text().splitlines()
        if x.strip() and not x.startswith(">")
    )
    return seq.upper().replace("T", "U")

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--input", default="data/all_single_substitutions.csv")
    p.add_argument("--output", default="results/rnafold_results.csv")
    p.add_argument("--wt-fasta", default="data/sz1_ires_wt.fasta")
    p.add_argument("--circ", action="store_true")
    args = p.parse_args()

    wt = read_fasta(Path(args.wt_fasta))
    _, wt_mfe = fold(wt, args.circ)

    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)

    with open(args.input, newline="") as f, out.open("w", newline="") as g:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames + [
            "mfe_kcal_mol", "wt_mfe_kcal_mol", "delta_mfe_vs_wt", "structure"
        ]
        writer = csv.DictWriter(g, fieldnames=fieldnames)
        writer.writeheader()

        for row in reader:
            structure, mfe = fold(row["sequence"], args.circ)
            row.update(
                mfe_kcal_mol=mfe,
                wt_mfe_kcal_mol=wt_mfe,
                delta_mfe_vs_wt=mfe - wt_mfe,
                structure=structure,
            )
            writer.writerow(row)

    print(f"WT MFE: {wt_mfe:.3f} kcal/mol")
    print(f"Output: {out}")

if __name__ == "__main__":
    main()
