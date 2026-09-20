#!/usr/bin/env python3
"""Generate all single-nucleotide substitutions from an RNA FASTA sequence."""
from __future__ import annotations
import argparse, csv
from pathlib import Path

BASES = "ACGU"

def read_fasta(path: Path) -> str:
    lines = [x.strip() for x in path.read_text().splitlines() if x.strip() and not x.startswith(">")]
    seq = "".join(lines).upper().replace("T", "U")
    if not seq or any(b not in BASES for b in seq):
        raise ValueError("FASTA sequence must contain only A/C/G/U (T is converted to U).")
    return seq

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--input", default="data/sz1_ires_wt.fasta")
    p.add_argument("--output", default="data/all_single_substitutions.csv")
    args = p.parse_args()
    seq = read_fasta(Path(args.input))
    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)

    with out.open("w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["variant", "position_1based", "wt_base", "mutant_base", "sequence"])
        for i, wt in enumerate(seq, start=1):
            for mut in BASES:
                if mut == wt:
                    continue
                mutated = seq[:i-1] + mut + seq[i:]
                w.writerow([f"pos{i}{wt}>{mut}", i, wt, mut, mutated])

    print(f"Generated {len(seq) * 3:,} single-substitution variants from {len(seq)} nt WT sequence.")
    print(f"Output: {out}")

if __name__ == "__main__":
    main()
