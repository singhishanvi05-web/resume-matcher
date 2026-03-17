import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

def plot_results(matched_skills, missing_skills, match_pct):
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    fig.suptitle(f"Resume Match Analysis — {match_pct}% Overall Fit",
                 fontsize=14, fontweight='bold')

    # Chart 1 — Skill breakdown bar chart
    top_matched = list(matched_skills)[:5]
    top_missing = list(missing_skills)[:5]
    labels = top_matched + top_missing
    colors = ['#2ECC71'] * len(top_matched) + ['#E74C3C'] * len(top_missing)

    ax1 = axes[0]
    ax1.barh(labels, [1] * len(labels), color=colors, height=0.6)
    ax1.set_xticks([])
    ax1.set_title("Top Matched vs Missing Skills", fontweight='bold')
    ax1.invert_yaxis()
    ax1.legend(handles=[
        mpatches.Patch(color='#2ECC71', label='Matched'),
        mpatches.Patch(color='#E74C3C', label='Missing')
    ], loc='lower right')

    # Chart 2 — Donut chart
    ax2 = axes[1]
    ax2.pie(
        [match_pct, 100 - match_pct],
        colors=['#2ECC71', '#F0F0F0'],
        startangle=90,
        wedgeprops=dict(width=0.45, edgecolor='white')
    )
    ax2.text(0, 0, f"{match_pct}%", ha='center', va='center',
             fontsize=26, fontweight='bold', color='#2ECC71')
    ax2.set_title("Overall Match Score", fontweight='bold')

    plt.tight_layout()
    plt.savefig("match_report.png", dpi=150, bbox_inches='tight')
    plt.show()
    print("Chart saved as match_report.png")