import sys
sys.path.insert(0, 'scraper')
from av_test_scraper import AVTestScraper

scraper = AVTestScraper()

# Test single URL
url = 'https://www.av-test.org/en/antivirus/home-windows/windows-11/april-2026/'
html = scraper.fetch_page(url)
results = scraper.parse_test_results(html, 'Windows', 'april-2026')

print('Results:', len(results))
for r in results[:5]:
    print(f"{r['antivirus_name']}: P={r['protection']}, Pf={r['performance']}, U={r['usability']}")
