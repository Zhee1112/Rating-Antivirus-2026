"""Antivirus Rating System using TOPSIS MCDM Method."""

from src.data_ingestion import load_av_test_data, filter_by_platform
from src.preprocessing import normalize_scores, aggregate_by_product
from src.models import calculate_topsis, sensitivity_analysis
from src.visualization import plot_ranking, plot_radar, plot_sensitivity

__all__ = [
    "load_av_test_data",
    "filter_by_platform",
    "normalize_scores",
    "aggregate_by_product",
    "calculate_topsis",
    "sensitivity_analysis",
    "plot_ranking",
    "plot_radar",
    "plot_sensitivity",
]
