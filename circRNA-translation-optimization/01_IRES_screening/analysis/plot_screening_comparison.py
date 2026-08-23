"""Generate a simple initial-vs-repeat IRES screening comparison figure.

Input: ../data/05_initial_vs_repeat_comparison.csv
Output: ../figures/initial_vs_repeat_comparison.svg
"""

from pathlib import Path
import csv

DATA = Path(__file__).resolve().parents[1] / "data" / "05_initial_vs_repeat_comparison.csv"
OUT = Path(__file__).resolve().parents[1] / "figures" / "initial_vs_repeat_comparison.svg"

rows = []
with DATA.open(newline="", encoding="utf-8") as f:
    for row in csv.DictReader(f):
        if row["condition"] != "FHB":
            rows.append(row)

# Keep the SVG dependency-free so it can be viewed directly in GitHub.
W, H = 1100, 650
left, right, top, bottom = 90, 50, 70, 100
plot_w, plot_h = W - left - right, H - top - bottom
max_value = max(float(r["repeat_260702_mean"]) for r in rows)
ymax = max(550, ((max_value + 49) // 50) * 50)

bar_gap = plot_w / len(rows)
bar_w = bar_gap * 0.32
scale = plot_h / ymax

svg = [
    f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">',
    '<rect width="100%" height="100%" fill="white"/>',
    '<text x="90" y="38" font-family="Arial, sans-serif" font-size="24" font-weight="bold">IRES screening: initial vs repeat</text>',
    '<text x="90" y="60" font-family="Arial, sans-serif" font-size="13">Relative translation activity, FHB = 100</text>',
    f'<line x1="{left}" y1="{top}" x2="{left}" y2="{top+plot_h}" stroke="#333"/>',
    f'<line x1="{left}" y1="{top+plot_h}" x2="{W-right}" y2="{top+plot_h}" stroke="#333"/>',
]

for tick in range(0, int(ymax) + 1, 100):
    y = top + plot_h - tick * scale
    svg.append(f'<line x1="{left}" y1="{y:.1f}" x2="{W-right}" y2="{y:.1f}" stroke="#ddd"/>')
    svg.append(f'<text x="{left-12}" y="{y+5:.1f}" text-anchor="end" font-family="Arial, sans-serif" font-size="12">{tick}</text>')

for i, row in enumerate(rows):
    cx = left + (i + 0.5) * bar_gap
    initial = float(row["initial_260626_mean"])
    repeat = float(row["repeat_260702_mean"])
    x1 = cx - bar_w
    x2 = cx
    y1 = top + plot_h - initial * scale
    y2 = top + plot_h - repeat * scale
    h1 = initial * scale
    h2 = repeat * scale
    svg.append(f'<rect x="{x1:.1f}" y="{y1:.1f}" width="{bar_w:.1f}" height="{h1:.1f}" fill="#8aa"/>')
    svg.append(f'<rect x="{x2:.1f}" y="{y2:.1f}" width="{bar_w:.1f}" height="{h2:.1f}" fill="#557"/>')
    svg.append(f'<text x="{cx:.1f}" y="{top+plot_h+20}" text-anchor="middle" font-family="Arial, sans-serif" font-size="11" transform="rotate(45 {cx:.1f} {top+plot_h+20})">{row["condition"]}</text>')

legend_y = H - 28
svg.append(f'<rect x="{W-250}" y="{legend_y-11}" width="14" height="14" fill="#8aa"/>')
svg.append(f'<text x="{W-230}" y="{legend_y}" font-family="Arial, sans-serif" font-size="12">Initial (260626)</text>')
svg.append(f'<rect x="{W-120}" y="{legend_y-11}" width="14" height="14" fill="#557"/>')
svg.append(f'<text x="{W-100}" y="{legend_y}" font-family="Arial, sans-serif" font-size="12">Repeat (260702)</text>')
svg.append('</svg>')

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text("\n".join(svg), encoding="utf-8")
print(f"Wrote {OUT}")
