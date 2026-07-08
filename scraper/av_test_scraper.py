"""
AV-TEST Scraper - Mengambil data penilaian antivirus dari av-test.org
Untuk 5 tahun terakhir (2021-2026)
"""

import csv
import os
import time
from datetime import datetime

import requests
from bs4 import BeautifulSoup


class AVTestScraper:
    """Scraper untuk mengambil data dari AV-TEST Institute."""

    BASE_URL = "https://www.av-test.org/en/antivirus/"

    # URL patterns untuk berbagai platform dan periode
    # Windows: bulan genap (Feb, Apr, Jun, Aug, Oct, Dec)
    # macOS: bulan Maret, Juni, September, Desember
    # Android: bulan ganjil (Jan, Mar, May, Jul, Sep, Nov)
    PLATFORMS = {
        "Windows": {
            "base_url": "home-windows/windows-11/",
            "years_available": [2023, 2024, 2025, 2026],
            "months": ["february", "april", "june", "august", "october", "december"],
        },
        "macOS": {
            "base_url": "home-macos/",
            "versions": {
                2023: "macos-ventura",
                2024: "macos-sonoma",
                2025: "macos-sequoia",
                2026: "macos-tahoe",
            },
            "years_available": [2023, 2024, 2025, 2026],
            "months": ["march", "june", "september", "december"],
        },
        "Android": {
            "base_url": "mobile-devices/android/",
            "years_available": [2023, 2024, 2025, 2026],
            "months": ["january", "march", "may", "july", "september", "november"],
        },
    }

    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.5",
        })

    def fetch_page(self, url):
        """Fetch halaman dari URL."""
        try:
            response = self.session.get(url, timeout=30)
            response.raise_for_status()
            return response.text
        except requests.RequestException as e:
            print(f"Error fetching {url}: {e}")
            return None

    def parse_test_results(self, html, platform, period):
        """Parse hasil pengujian dari HTML."""
        soup = BeautifulSoup(html, "html.parser")
        results = []

        # Cari semua item antivirus (tag <a> dengan class antivirus__list-item)
        items = soup.find_all("a", class_="antivirus__list-item")

        for item in items:
            try:
                # Ambil nama produk
                producer = item.get("data-sort-producer", "Unknown")

                # Ambil scores dari data-percentage
                score_elements = item.find_all("div", class_="circular-progress-container")

                if len(score_elements) >= 3:
                    protection = float(score_elements[0].get("data-percentage", 0))
                    performance = float(score_elements[1].get("data-percentage", 0))
                    usability = float(score_elements[2].get("data-percentage", 0))

                    # Konversi periode ke format YYYY-MM
                    month_map = {
                        "january": "01", "march": "03", "may": "05",
                        "july": "07", "september": "09", "november": "11"
                    }

                    period_parts = period.split("-")
                    month_name = period_parts[0]
                    year = period_parts[1]
                    month = month_map.get(month_name, "01")
                    test_period = f"{year}-{month}"

                    results.append({
                        "antivirus_name": producer,
                        "platform": platform,
                        "test_period": test_period,
                        "protection": protection,
                        "performance": performance,
                        "usability": usability,
                        "version": "",
                    })
            except Exception as e:
                print(f"Error parsing item: {e}")
                continue

        return results

    def scrape_all(self, years=None):
        """Scrape semua data dari AV-TEST."""
        if years is None:
            years = [2023, 2024, 2025, 2026]

        all_results = []

        for platform, platform_info in self.PLATFORMS.items():
            for year in years:
                # Skip jika tahun tidak tersedia untuk platform ini
                if year not in platform_info["years_available"]:
                    continue

                for month in platform_info["months"]:
                    period = f"{month}-{year}"

                    # macOS memerlukan versi OS di URL
                    if platform == "macOS":
                        os_version = platform_info.get("versions", {}).get(year, "")
                        if os_version:
                            url = f"{self.BASE_URL}{platform_info['base_url']}{os_version}/{period}/"
                        else:
                            continue
                    else:
                        url = f"{self.BASE_URL}{platform_info['base_url']}{period}/"

                    print(f"Scraping: {platform} - {period}...")

                    html = self.fetch_page(url)
                    if html:
                        results = self.parse_test_results(html, platform, period)
                        all_results.extend(results)
                        print(f"  Found {len(results)} products")
                    else:
                        print(f"  No data available")

                    # Delay untuk menghindari rate limiting
                    time.sleep(2)

        return all_results

    def save_to_csv(self, results, filename):
        """Simpan hasil ke CSV."""
        if not results:
            print("No results to save")
            return

        # Buat direktori jika belum ada
        os.makedirs(os.path.dirname(filename), exist_ok=True)

        # Tulis CSV
        with open(filename, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(
                f,
                fieldnames=[
                    "antivirus_name",
                    "platform",
                    "test_period",
                    "protection",
                    "performance",
                    "usability",
                    "version",
                ],
            )
            writer.writeheader()
            writer.writerows(results)

        print(f"Saved {len(results)} records to {filename}")


def main():
    """Fungsi utama."""
    print("=" * 60)
    print("AV-TEST SCRAPER - Multi-Platform (2023-2026)")
    print("=" * 60)
    print()
    print("Platform yang tersedia:")
    print("- Windows: Data dari 2025 (bulan genap)")
    print("- macOS: Data dari 2025 (bulan Maret, Juni, Sep, Des)")
    print("- Android: Data dari 2023 (bulan ganjil)")
    print("- Linux: TIDAK tersedia di AV-TEST")
    print()

    scraper = AVTestScraper()

    # Scrape data
    print("Memulai scraping...")
    results = scraper.scrape_all(years=[2023, 2024, 2025, 2026])

    # Simpan ke CSV
    output_file = "data/raw/av_test_ratings_multiplatform.csv"
    scraper.save_to_csv(results, output_file)

    print()
    print("=" * 60)
    print("Selesai!")
    print(f"Total records: {len(results)}")
    print("=" * 60)


if __name__ == "__main__":
    main()
