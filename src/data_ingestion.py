"""Module for loading and ingesting AV-TEST rating data."""

import pandas as pd


def load_av_test_data(csv_path):
    """
    Load AV-TEST rating data from a CSV file.

    Parameters
    ----------
    csv_path : str
        Path to the CSV file containing AV-TEST ratings.

    Returns
    -------
    pd.DataFrame
        DataFrame with columns: antivirus_name, platform, test_period,
        protection, performance, usability, version.
    """
    df = pd.read_csv(csv_path)

    required_cols = [
        "antivirus_name",
        "platform",
        "test_period",
        "protection",
        "performance",
        "usability",
    ]
    missing = [c for c in required_cols if c not in df.columns]
    if missing:
        raise ValueError(f"CSV missing required columns: {missing}")

    df["protection"] = pd.to_numeric(df["protection"], errors="coerce")
    df["performance"] = pd.to_numeric(df["performance"], errors="coerce")
    df["usability"] = pd.to_numeric(df["usability"], errors="coerce")

    return df


def filter_by_platform(df, platform):
    """
    Filter DataFrame by platform (Windows, macOS, Android).

    Parameters
    ----------
    df : pd.DataFrame
        Raw AV-TEST data.
    platform : str
        Platform to filter: 'Windows', 'macOS', or 'Android'.

    Returns
    -------
    pd.DataFrame
        Filtered DataFrame.
    """
    mask = df["platform"].str.lower() == platform.lower()
    return df[mask].copy()


def filter_by_period(df, test_period):
    """
    Filter DataFrame by test period (e.g. '2026-04').

    Parameters
    ----------
    df : pd.DataFrame
        Raw AV-TEST data.
    test_period : str
        Period to filter.

    Returns
    -------
    pd.DataFrame
        Filtered DataFrame.
    """
    return df[df["test_period"] == test_period].copy()
