from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
FIGURES = ROOT / "figures"
RESULTS = ROOT / "results"
FIGURES.mkdir(exist_ok=True)
RESULTS.mkdir(exist_ok=True)

initial = pd.read_csv(DATA / "02_initial_screening_summary.csv").set_index("condition")
repeat = pd.read_csv(DATA / "04_repeat_screening_summary.csv").set_index("condition")
comparison = pd.read_csv(DATA / "05_initial_vs_repeat_comparison.csv").set_index("condition")

# The repeat screening summary contains the replicate SD, allowing a simple
# coefficient-of-variation estimate for within-experiment variability.
summary = comparison.copy()
summary["repeat_SD"] = repeat["SD"]
summary["repeat_CV_percent"] = summary["repeat_SD"] / summary["repeat_260702_mean"] * 100
summary["absolute_percent_change"] = (
    summary["repeat_minus_initial"].abs() / summary["initial_260626_mean"] * 100
)
summary["initial_rank"] = initial["relative_to_FHB_mean"].rank(ascending=False, method="min").astype(int)
summary["repeat_rank"] = repeat["relative_to_FHB_mean"].rank(ascending=False, method="min").astype(int)
summary["rank_change"] = summary["repeat_rank"] - summary["initial_rank"]

# Conservative screening rule for a reproducible follow-up set.
# A candidate must be reasonably strong in the repeat experiment, have <=10%
# within-repeat CV, and change by <=20% between the two experiments.
summary["candidate_class"] = "Other"
stable = (
    (summary["repeat_260702_mean"] >= 300)
    & (summary["repeat_CV_percent"] <= 10)
    & (summary["absolute_percent_change"] <= 20)
)
summary.loc[stable, "candidate_class"] = "Stable high performer"

high_but_variable = (
    (summary["repeat_260702_mean"] >= 300)
    & ~stable
)
summary.loc[high_but_variable, "candidate_class"] = "High performer; requires validation"

summary.to_csv(RESULTS / "ires_reproducibility_summary.csv")

# Global reproducibility metrics (excluding FHB reference, which is fixed at 100 in both summaries).
non_reference = summary.index != "FHB"
spearman = initial.loc[non_reference, "relative_to_FHB_mean"].corr(
    repeat.loc[non_reference, "relative_to_FHB_mean"], method="spearman"
)
pearson = initial.loc[non_reference, "relative_to_FHB_mean"].corr(
    repeat.loc[non_reference, "relative_to_FHB_mean"], method="pearson"
)

with open(RESULTS / "reproducibility_metrics.txt", "w", encoding="utf-8") as f:
    f.write("IRES screening reproducibility metrics\n")
    f.write(f"Spearman rank correlation (excluding FHB): {spearman:.3f}\n")
    f.write(f"Pearson correlation (excluding FHB): {pearson:.3f}\n")
    f.write("\nCandidate rule: repeat mean >= 300, repeat CV <= 10%, absolute inter-experiment change <= 20%.\n")
    f.write("\nStable high performers:\n")
    for name in summary.index[summary["candidate_class"] == "Stable high performer"]:
        f.write(f"- {name}\n")
    f.write("\nHigh performers requiring validation:\n")
    for name in summary.index[summary["candidate_class"] == "High performer; requires validation"]:
        f.write(f"- {name}\n")

# Figure 1: initial vs repeat performance.
fig, ax = plt.subplots(figsize=(7, 6))
for name in summary.index:
    if name == "FHB":
        continue
    ax.scatter(
        initial.loc[name, "relative_to_FHB_mean"],
        repeat.loc[name, "relative_to_FHB_mean"],
        s=55,
    )
    ax.annotate(name, (initial.loc[name, "relative_to_FHB_mean"], repeat.loc[name, "relative_to_FHB_mean"]),
                xytext=(5, 5), textcoords="offset points", fontsize=8)
lims = [0, max(initial.loc[non_reference, "relative_to_FHB_mean"].max(), repeat.loc[non_reference, "relative_to_FHB_mean"].max()) * 1.08]
ax.plot(lims, lims, linestyle="--", linewidth=1)
ax.set_xlim(lims)
ax.set_ylim(lims)
ax.set_xlabel("Initial screening: relative translation activity")
ax.set_ylabel("Repeat screening: relative translation activity")
ax.set_title("IRES screening reproducibility")
fig.tight_layout()
fig.savefig(FIGURES / "initial_vs_repeat_reproducibility.png", dpi=300)
plt.close(fig)

# Figure 2: within-repeat variability.
plot_df = summary.drop(index="FHB").sort_values("repeat_CV_percent")
fig, ax = plt.subplots(figsize=(8, 5))
ax.barh(plot_df.index, plot_df["repeat_CV_percent"])
ax.axvline(10, linestyle="--", linewidth=1)
ax.set_xlabel("Repeat-screening coefficient of variation (%)")
ax.set_title("Within-repeat variability of IRES candidates")
fig.tight_layout()
fig.savefig(FIGURES / "repeat_screening_cv.png", dpi=300)
plt.close(fig)

print(f"Spearman rho: {spearman:.3f}")
print(f"Pearson r: {pearson:.3f}")
print("Stable high performers:")
print(summary.index[summary["candidate_class"] == "Stable high performer"].tolist())
