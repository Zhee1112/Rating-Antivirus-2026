"""Visualization module for antivirus rating results."""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from src.preprocessing import CRITERIA_COLS


def plot_ranking(result_df, title="Antivirus TOPSIS Rating Ranking", save_path=None):
    """
    Bar chart of TOPSIS rating scores.

    Parameters
    ----------
    result_df : pd.DataFrame
        Result from calculate_topsis() with 'antivirus_name' and 'rating_score'.
    title : str
        Chart title.
    save_path : str, optional
        Path to save the figure.
    """
    fig, ax = plt.subplots(figsize=(12, 7))

    sorted_df = result_df.sort_values("rating_score", ascending=True)
    colors = plt.cm.RdYlGn(sorted_df["rating_score"].values / sorted_df["rating_score"].max())

    bars = ax.barh(sorted_df["antivirus_name"], sorted_df["rating_score"], color=colors)
    ax.set_xlabel("TOPSIS Preference Score (V)", fontsize=12)
    ax.set_title(title, fontsize=14, fontweight="bold")
    ax.set_xlim(0, 1.05)

    for bar, score in zip(bars, sorted_df["rating_score"]):
        ax.text(
            bar.get_width() + 0.01,
            bar.get_y() + bar.get_height() / 2,
            f"{score:.4f}",
            va="center",
            fontsize=10,
        )

    plt.tight_layout()
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches="tight")
    plt.show()


def plot_radar(
    result_df, product_name, raw_df=None, title=None, save_path=None
):
    """
    Radar chart comparing a product's scores against the average.

    Parameters
    ----------
    result_df : pd.DataFrame
        Aggregated result from calculate_topsis().
    product_name : str
        Name of the product to highlight.
    raw_df : pd.DataFrame, optional
        Original aggregated data for computing average.
    title : str, optional
        Chart title.
    save_path : str, optional
        Path to save the figure.
    """
    product_row = result_df[result_df["antivirus_name"] == product_name]
    if product_row.empty:
        print(f"Product '{product_name}' not found.")
        return

    if raw_df is not None:
        avg_row = raw_df[CRITERIA_COLS].mean()
    else:
        avg_row = result_df[CRITERIA_COLS].mean()

    product_scores = product_row[CRITERIA_COLS].values.flatten()

    labels = ["Protection", "Performance", "Usability"]
    num_vars = len(labels)
    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
    product_scores_plot = np.concatenate((product_scores, [product_scores[0]]))
    avg_scores_plot = np.concatenate((avg_row.values, [avg_row.values[0]]))
    angles += angles[:1]

    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

    ax.plot(angles, product_scores_plot, "o-", linewidth=2, label=product_name)
    ax.fill(angles, product_scores_plot, alpha=0.25)

    ax.plot(angles, avg_scores_plot, "o--", linewidth=1.5, label="Average", color="gray")
    ax.fill(angles, avg_scores_plot, alpha=0.1, color="gray")

    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(labels, fontsize=11)
    ax.set_ylim(0, 6.5)
    ax.set_title(
        title or f"Radar: {product_name}",
        fontsize=13,
        fontweight="bold",
        pad=20,
    )
    ax.legend(loc="upper right", bbox_to_anchor=(1.3, 1.1))

    plt.tight_layout()
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches="tight")
    plt.show()


def plot_sensitivity(
    sensitivity_results, top_n=5, title="Sensitivity Analysis", save_path=None
):
    """
    Plot ranking stability across weight scenarios.

    Parameters
    ----------
    sensitivity_results : dict
        Output from sensitivity_analysis().
    top_n : int
        Number of top products to display.
    title : str
        Chart title.
    save_path : str, optional
        Path to save the figure.
    """
    scenario_names = list(sensitivity_results.keys())

    all_products = set()
    for res in sensitivity_results.values():
        all_products.update(res["antivirus_name"].tolist())

    rank_data = {}
    for scenario, res in sensitivity_results.items():
        ranks = {}
        for _, row in res.iterrows():
            ranks[row["antivirus_name"]] = row["rank"]
        rank_data[scenario] = ranks

    avg_ranks = {}
    for prod in all_products:
        ranks = [rank_data[s].get(prod, len(all_products) + 1) for s in scenario_names]
        avg_ranks[prod] = np.mean(ranks)

    top_products = sorted(avg_ranks.keys(), key=lambda x: avg_ranks[x])[:top_n]

    fig, ax = plt.subplots(figsize=(14, 7))

    x = np.arange(len(scenario_names))
    width = 0.15

    for i, prod in enumerate(top_products):
        ranks = [rank_data[s].get(prod, len(all_products) + 1) for s in scenario_names]
        ax.bar(x + i * width, ranks, width, label=prod)

    ax.set_xlabel("Weight Scenario", fontsize=12)
    ax.set_ylabel("Rank", fontsize=12)
    ax.set_title(title, fontsize=14, fontweight="bold")
    ax.set_xticks(x + width * (len(top_products) - 1) / 2)
    ax.set_xticklabels(
        [s.split("(")[0].strip() for s in scenario_names],
        rotation=15,
        ha="right",
        fontsize=9,
    )
    ax.invert_yaxis()
    ax.set_yticks(range(1, top_n + 2))
    ax.legend(title="Product", bbox_to_anchor=(1.02, 1), loc="upper left", fontsize=9)

    plt.tight_layout()
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches="tight")
    plt.show()
