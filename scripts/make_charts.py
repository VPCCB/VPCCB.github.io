import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager
import os

# Terracotta theme palette
CLAY = "#c1603d"
CLAY_DEEP = "#a24c2e"
CLAY_SOFT = "#e0a184"
SAND = "#f7f0e9"
INK = "#2c2622"
TEAL = "#3f7a72"

plt.rcParams.update({
    "font.family": "serif",
    "font.serif": ["Georgia", "Times New Roman", "DejaVu Serif"],
    "text.color": INK,
    "axes.edgecolor": INK,
    "axes.labelcolor": INK,
    "xtick.color": INK,
    "ytick.color": INK,
    "axes.linewidth": 0.8,
    "figure.dpi": 160,
})

OUT = os.path.join(os.path.dirname(__file__), "public")
os.makedirs(OUT, exist_ok=True)

def style(ax):
    ax.set_facecolor(SAND)
    for s in ["top", "right"]:
        ax.spines[s].set_visible(False)
    ax.grid(axis="y", color=INK, alpha=0.10, linewidth=0.7)
    ax.tick_params(length=0)

# 1) ASER Grade 3 reading proficiency: government vs private (2014-2024)
def chart_reading():
    years = [2014, 2018, 2022, 2024]
    govt = [17.2, 20.9, 16.3, 23.4]
    priv = [37.8, 40.6, 33.1, 35.5]
    overall = [23.6, 27.3, 20.5, 27.1]
    fig, ax = plt.subplots(figsize=(6.4, 4.0))
    fig.patch.set_facecolor(SAND)
    ax.plot(years, priv, "-o", color=CLAY, lw=2.4, ms=6, label="Private schools")
    ax.plot(years, overall, "-o", color=TEAL, lw=2.4, ms=6, label="All schools")
    ax.plot(years, govt, "-o", color=CLAY_DEEP, lw=2.4, ms=6, label="Government schools")
    style(ax)
    ax.set_ylim(0, 50)
    ax.set_xticks(years)
    ax.set_ylabel("% able to read a Grade 2 text")
    ax.set_title("Grade 3 reading proficiency in India (2014\u20132024)",
                 fontsize=12.5, fontweight="bold", color=INK, pad=12)
    ax.legend(frameon=False, fontsize=9, loc="lower center", ncol=3,
              bbox_to_anchor=(0.5, -0.22))
    fig.tight_layout()
    fig.savefig(os.path.join(OUT, "chart-reading.png"), facecolor=SAND, bbox_inches="tight")
    plt.close(fig)

# 2) Dropout rate by school level (2024-25)
def chart_dropout():
    levels = ["Primary", "Upper\nprimary", "Secondary"]
    vals = [0.3, 3.5, 11.5]
    fig, ax = plt.subplots(figsize=(6.4, 3.8))
    fig.patch.set_facecolor(SAND)
    bars = ax.bar(levels, vals, color=[CLAY_SOFT, CLAY, CLAY_DEEP], width=0.6)
    style(ax)
    ax.set_ylim(0, 13)
    ax.set_ylabel("Dropout rate (%)")
    ax.set_title("The system leaks as children grow older (2024\u201325)",
                 fontsize=12.5, fontweight="bold", color=INK, pad=12)
    for b, v in zip(bars, vals):
        ax.text(b.get_x() + b.get_width()/2, v + 0.25, f"{v}%",
                ha="center", va="bottom", fontsize=11, fontweight="bold", color=INK)
    fig.tight_layout()
    fig.savefig(os.path.join(OUT, "chart-dropout.png"), facecolor=SAND, bbox_inches="tight")
    plt.close(fig)

# 3) Enrolment share: government vs private (2014-15 vs 2024-25)
def chart_enrolment():
    labels = ["Government", "Private unaided"]
    y2014 = [54.3, 31.7]
    y2024 = [49.25, 38.8]
    import numpy as np
    x = np.arange(len(labels))
    w = 0.36
    fig, ax = plt.subplots(figsize=(6.4, 3.9))
    fig.patch.set_facecolor(SAND)
    b1 = ax.bar(x - w/2, y2014, w, label="2014\u201315", color=CLAY_SOFT)
    b2 = ax.bar(x + w/2, y2024, w, label="2024\u201325", color=CLAY_DEEP)
    style(ax)
    ax.set_ylim(0, 60)
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.set_ylabel("Share of total enrolment (%)")
    ax.set_title("Families are quietly leaving government schools",
                 fontsize=12.5, fontweight="bold", color=INK, pad=12)
    for bars in (b1, b2):
        for b in bars:
            ax.text(b.get_x()+b.get_width()/2, b.get_height()+0.7,
                    f"{b.get_height():.0f}%", ha="center", va="bottom",
                    fontsize=10, color=INK)
    ax.legend(frameon=False, fontsize=9.5)
    fig.tight_layout()
    fig.savefig(os.path.join(OUT, "chart-enrolment.png"), facecolor=SAND, bbox_inches="tight")
    plt.close(fig)

# 4) Education spending as % of GDP: international comparison (2021)
def chart_spending():
    data = [
        ("UK", 5.9), ("USA", 5.9), ("Brazil", 5.5), ("Germany", 5.4),
        ("France", 5.4), ("Canada", 4.7), ("India", 4.6), ("Italy", 4.2),
        ("China", 3.9), ("Japan", 3.3),
    ]
    data.sort(key=lambda d: d[1])
    labels = [d[0] for d in data]
    vals = [d[1] for d in data]
    colors = [CLAY_DEEP if l == "India" else CLAY_SOFT for l in labels]
    fig, ax = plt.subplots(figsize=(6.4, 4.2))
    fig.patch.set_facecolor(SAND)
    bars = ax.barh(labels, vals, color=colors)
    style(ax)
    ax.grid(axis="y", alpha=0)
    ax.grid(axis="x", color=INK, alpha=0.10, linewidth=0.7)
    ax.set_xlim(0, 7)
    ax.set_xlabel("Government spending on education (% of GDP)")
    ax.set_title("India spends less than most large economies (2021)",
                 fontsize=12.5, fontweight="bold", color=INK, pad=12)
    for b, v, l in zip(bars, vals, labels):
        ax.text(v + 0.1, b.get_y()+b.get_height()/2, f"{v}%",
                va="center", fontsize=9.5,
                fontweight="bold" if l == "India" else "normal", color=INK)
    fig.tight_layout()
    fig.savefig(os.path.join(OUT, "chart-spending-gdp.png"), facecolor=SAND, bbox_inches="tight")
    plt.close(fig)

chart_reading()
chart_dropout()
chart_enrolment()
chart_spending()
print("charts written to", OUT)
