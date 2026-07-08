import pandas as pd

df = pd.read_csv('data/raw/av_test_ratings_multiplatform.csv')
print('=== DISTRIBUSI DATA BARU (748 records) ===')
print()

for platform in ['Windows', 'macOS', 'Android']:
    p = df[df['platform'] == platform]
    print(f'{platform}: {len(p)} records')
    for year in sorted(p['test_period'].str[:4].unique()):
        y = p[p['test_period'].str[:4] == year]
        print(f'  {year}: {len(y)} records, {y["antivirus_name"].nunique()} products')
    print()
