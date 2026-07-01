"""Main pipeline for Antivirus Rating System using TOPSIS."""

import argparse
import os

import pandas as pd

from src.data_ingestion import (
    filter_by_platform,
    filter_by_year,
    get_available_years,
    load_av_test_data,
)
from src.models import calculate_topsis, sensitivity_analysis
from src.preprocessing import aggregate_by_product
from src.visualization import plot_radar, plot_ranking, plot_sensitivity


def main():
    parser = argparse.ArgumentParser(
        description="Antivirus Rating System using TOPSIS MCDM"
    )
    parser.add_argument(
        "--csv",
        type=str,
        default="data/raw/av_test_ratings_multiplatform.csv",
        help="Path to AV-TEST CSV dataset",
    )
    parser.add_argument(
        "--platform",
        type=str,
        default="Windows",
        choices=["Windows", "macOS", "Android", "all"],
        help="Platform to rate (default: Windows)",
    )
    parser.add_argument(
        "--year",
        type=int,
        default=None,
        help="Filter by year (e.g., 2025). If not specified, uses all years.",
    )
    parser.add_argument(
        "--cumulative",
        action="store_true",
        help="Calculate cumulative rating across all years",
    )
    parser.add_argument(
        "--weights",
        type=float,
        nargs=3,
        default=[0.50, 0.20, 0.30],
        help="Weights [protection performance usability] (must sum to 1.0)",
    )
    parser.add_argument(
        "--sensitivity",
        action="store_true",
        help="Run sensitivity analysis with multiple weight scenarios",
    )
    parser.add_argument(
        "--output",
        type=str,
        default="data/final_antivirus_rating.csv",
        help="Output path for final rating CSV",
    )
    parser.add_argument(
        "--no-plot",
        action="store_true",
        help="Disable plot output",
    )

    args = parser.parse_args()

    # Validate weights
    if abs(sum(args.weights) - 1.0) > 1e-6:
        print(f"Error: weights must sum to 1.0, got {sum(args.weights)}")
        return

    criteria_types = ["benefit", "benefit", "benefit"]

    # Step 1: Load data
    print("=" * 60)
    print("ANTIVIRUS RATING SYSTEM - TOPSIS MCDM")
    print("=" * 60)
    print(f"\n1. Loading data from: {args.csv}")

    if not os.path.exists(args.csv):
        print(f"Error: CSV file not found: {args.csv}")
        return

    df = load_av_test_data(args.csv)
    print(f"   Loaded {len(df)} records")

    # Show available years
    available_years = get_available_years(df)
    print(f"   Available years: {available_years}")

    # Step 2: Filter by platform
    if args.platform != "all":
        print(f"\n2. Filtering platform: {args.platform}")
        df = filter_by_platform(df, args.platform)
        print(f"   {len(df)} records after filtering")
    else:
        print("\n2. Using all platforms")

    # Step 3: Filter by year (if specified)
    if args.year:
        print(f"\n3. Filtering year: {args.year}")
        df = filter_by_year(df, args.year)
        print(f"   {len(df)} records after filtering")
        year_label = str(args.year)
    else:
        year_label = "All Years"

    # Step 4: Run TOPSIS
    print(f"\n4. Running TOPSIS with weights: {args.weights}")
    result = calculate_topsis(df, args.weights, criteria_types)

    # Step 5: Display results
    print("\n" + "=" * 60)
    print(f"RATING RESULTS ({year_label})")
    print("=" * 60)
    display_cols = [
        "antivirus_name",
        "platform",
        "protection",
        "performance",
        "usability",
        "periods_tested",
        "rating_score",
        "rank",
    ]
    print(result[display_cols].to_string(index=False))

    # Step 6: Save output
    os.makedirs(os.path.dirname(args.output), exist_ok=True)
    result.to_csv(args.output, index=False)
    print(f"\n5. Results saved to: {args.output}")

    # Step 7: Visualization
    if not args.no_plot:
        print("\n6. Generating visualizations...")
        platform_label = args.platform if args.platform != "all" else "All Platforms"
        plot_ranking(
            result,
            title=f"Antivirus TOPSIS Rating - {platform_label} ({year_label})",
            save_path=f"data/ranking_{args.platform.lower()}_{year_label.lower().replace(' ', '_')}.png",
        )

        # Radar chart for top product
        top_product = result.iloc[0]["antivirus_name"]
        agg = aggregate_by_product(df)
        plot_radar(
            result,
            top_product,
            raw_df=agg,
            title=f"Profile: {top_product} ({platform_label}, {year_label})",
            save_path=f"data/radar_{args.platform.lower()}_{year_label.lower().replace(' ', '_')}.png",
        )

    # Step 8: Sensitivity analysis
    if args.sensitivity:
        print("\n7. Running sensitivity analysis...")
        sens_results = sensitivity_analysis(df)
        for name, res in sens_results.items():
            print(f"\n--- {name} ---")
            print(res[["antivirus_name", "rating_score", "rank"]].to_string(index=False))

        if not args.no_plot:
            plot_sensitivity(
                sens_results,
                title=f"Sensitivity Analysis - {platform_label} ({year_label})",
                save_path=f"data/sensitivity_{args.platform.lower()}_{year_label.lower().replace(' ', '_')}.png",
            )

        # Save all sensitivity results
        sens_dfs = []
        for name, res in sens_results.items():
            tmp = res.copy()
            tmp["scenario"] = name
            sens_dfs.append(tmp)
        pd.concat(sens_dfs).to_csv(
            f"data/sensitivity_analysis_{args.platform.lower()}_{year_label.lower().replace(' ', '_')}.csv",
            index=False,
        )

    # Step 9: Multi-year comparison (if not filtering by specific year)
    if not args.year and not args.cumulative:
        print("\n" + "=" * 60)
        print("MULTI-YEAR COMPARISON")
        print("=" * 60)
        for year in available_years:
            year_df = filter_by_year(df, year)
            if len(year_df) > 0:
                year_result = calculate_topsis(year_df, args.weights, criteria_types)
                top = year_result.iloc[0]
                print(f"{year}: {top['antivirus_name']} (Score: {top['rating_score']:.4f})")

    print("\nDone!")
