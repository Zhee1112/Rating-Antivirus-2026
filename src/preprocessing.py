"""Module for data preprocessing and normalization (TOPSIS vector normalization)."""

import numpy as np
import pandas as pd

CRITERIA_COLS = ["protection", "performance", "usability"]


def aggregate_by_product(df):
    """
    Aggregate scores across test periods per antivirus product per platform.

    Uses the mean of all test periods for each product-platform combination.

    Parameters
    ----------
    df : pd.DataFrame
        Filtered AV-TEST data (single platform recommended).

    Returns
    -------
    pd.DataFrame
        Aggregated DataFrame with mean scores per product.
    """
    agg = df.groupby(["antivirus_name", "platform"]).agg(
        protection=("protection", "mean"),
        performance=("performance", "mean"),
        usability=("usability", "mean"),
        periods_tested=("test_period", "count"),
    ).reset_index()

    return agg


def normalize_scores(df):
    """
    Perform vector normalization on the criteria columns.

    Formula: norm_ij = x_ij / sqrt(sum(x_ij^2))

    This is the standard normalization step for TOPSIS before
    multiplying with weights.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame with criteria columns (protection, performance, usability).

    Returns
    -------
    pd.DataFrame
        Copy of df with normalized scores.
    """
    norm_df = df.copy()

    for col in CRITERIA_COLS:
        denominator = np.sqrt(np.sum(df[col] ** 2))
        if denominator == 0:
            norm_df[col] = 0.0
        else:
            norm_df[col] = df[col] / denominator

    return norm_df


def build_weighted_matrix(norm_df, weights):
    """
    Multiply normalized matrix by weights.

    Parameters
    ----------
    norm_df : pd.DataFrame
        Normalized DataFrame from normalize_scores().
    weights : list of float
        Weights for [protection, performance, usability].
        Must sum to 1.0.

    Returns
    -------
    pd.DataFrame
        Weighted normalized matrix.
    """
    if len(weights) != len(CRITERIA_COLS):
        raise ValueError(
            f"weights length ({len(weights)}) must match "
            f"criteria count ({len(CRITERIA_COLS)})"
        )

    if abs(sum(weights) - 1.0) > 1e-6:
        raise ValueError(f"Weights must sum to 1.0, got {sum(weights)}")

    weighted = norm_df.copy()
    for i, col in enumerate(CRITERIA_COLS):
        weighted[col] = norm_df[col] * weights[i]

    return weighted
