"""TOPSIS (Technique for Order of Preference by Similarity to Ideal Solution) engine."""

import numpy as np
import pandas as pd

from src.preprocessing import (
    CRITERIA_COLS,
    aggregate_by_product,
    build_weighted_matrix,
    normalize_scores,
)


def calculate_topsis(df, weights, criteria_types):
    """
    Calculate TOPSIS scores and ranking for antivirus products.

    Parameters
    ----------
    df : pd.DataFrame
        Raw or filtered AV-TEST data with criteria columns.
    weights : list of float
        Weights for [protection, performance, usability]. Must sum to 1.0.
    criteria_types : list of str
        'benefit' (higher is better) or 'cost' (lower is better)
        for each criterion.

    Returns
    -------
    pd.DataFrame
        DataFrame with original data plus columns:
        rating_score, rank.
    """
    raw_grouped = aggregate_by_product(df)
    norm_df = normalize_scores(raw_grouped)
    weighted = build_weighted_matrix(norm_df, weights)

    # Step 1: Determine ideal solutions (A+ and A-)
    a_plus = []
    a_minus = []

    for i, col in enumerate(CRITERIA_COLS):
        if criteria_types[i] == "benefit":
            a_plus.append(weighted[col].max())
            a_minus.append(weighted[col].min())
        else:  # cost
            a_plus.append(weighted[col].min())
            a_minus.append(weighted[col].max())

    a_plus = np.array(a_plus)
    a_minus = np.array(a_minus)

    # Step 2: Calculate Euclidean distances
    d_plus = []
    d_minus = []

    for _, row in weighted.iterrows():
        row_values = row[CRITERIA_COLS].values.astype(float)
        d_plus.append(np.sqrt(np.sum((row_values - a_plus) ** 2)))
        d_minus.append(np.sqrt(np.sum((row_values - a_minus) ** 2)))

    # Step 3: Calculate preference scores
    scores = []
    for dp, dm in zip(d_plus, d_minus):
        if dp + dm == 0:
            scores.append(0.5)
        else:
            scores.append(dm / (dp + dm))

    # Step 4: Build result
    result = raw_grouped.copy()
    result["rating_score"] = scores
    result["rank"] = result["rating_score"].rank(ascending=False, method="min").astype(int)

    return result.sort_values(by="rank").reset_index(drop=True)


def sensitivity_analysis(df, scenarios=None):
    """
    Run TOPSIS with multiple weight scenarios for paper analysis.

    Parameters
    ----------
    df : pd.DataFrame
        Raw AV-TEST data.
    scenarios : dict, optional
        Dictionary of {scenario_name: (weights, criteria_types)}.
        If None, uses default scenarios.

    Returns
    -------
    dict
        Dictionary of {scenario_name: result_DataFrame}.
    """
    if scenarios is None:
        scenarios = {
            "Default (50/20/30)": (
                [0.50, 0.20, 0.30],
                ["benefit", "benefit", "benefit"],
            ),
            "Protection-heavy (70/15/15)": (
                [0.70, 0.15, 0.15],
                ["benefit", "benefit", "benefit"],
            ),
            "Balanced (33/33/34)": (
                [0.33, 0.33, 0.34],
                ["benefit", "benefit", "benefit"],
            ),
            "Performance-focus (30/50/20)": (
                [0.30, 0.50, 0.20],
                ["benefit", "benefit", "benefit"],
            ),
        }

    results = {}
    for name, (weights, crit_types) in scenarios.items():
        results[name] = calculate_topsis(df, weights, crit_types)

    return results
