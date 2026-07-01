"""Analisis Ranking Antivirus Multi-Platform (2023-2026)"""
import sys
sys.path.insert(0, '.')

import pandas as pd
from collections import Counter
from src.data_ingestion import load_av_test_data, filter_by_platform, filter_by_year
from src.models import calculate_topsis

df = load_av_test_data('data/raw/av_test_ratings_multiplatform.csv')
WEIGHTS = [0.50, 0.20, 0.30]
CT = ['benefit', 'benefit', 'benefit']

champions_all = {}

for platform in ['Windows', 'macOS', 'Android']:
    df_p = filter_by_platform(df, platform)
    years = sorted(df_p['test_period'].str[:4].unique())
    
    print('=' * 70)
    print(f'PLATFORM: {platform.upper()}')
    print('=' * 70)
    
    yearly_results = []
    
    for year in years:
        df_y = filter_by_year(df_p.copy(), int(year))
        if len(df_y) == 0:
            continue
        
        result = calculate_topsis(df_y, WEIGHTS, CT)
        
        # Average scores per product (for products tested multiple times in same year)
        avg = result.groupby('antivirus_name').agg({
            'protection': 'mean',
            'performance': 'mean',
            'usability': 'mean',
            'rating_score': 'mean'
        }).reset_index()
        
        avg = avg.sort_values('rating_score', ascending=False).reset_index(drop=True)
        avg['rank'] = range(1, len(avg) + 1)
        
        print(f'\n--- TAHUN {year} ({len(df_y)} records, {len(avg)} produk unik) ---\n')
        print(f'{"Rank":<5} {"Produk":<42} {"Prot":<6} {"Perf":<6} {"Usab":<6} {"Score":<8}')
        print('-' * 73)
        
        for _, row in avg.head(10).iterrows():
            print(f'{int(row["rank"]):<5} {row["antivirus_name"]:<42} {row["protection"]:<6.2f} {row["performance"]:<6.2f} {row["usability"]:<6.2f} {row["rating_score"]:<8.4f}')
        
        top1_score = avg.iloc[0]['rating_score']
        top1_products = avg[avg['rating_score'] == top1_score]['antivirus_name'].tolist()
        
        print(f'\n>> TOP 1: {", ".join(top1_products)} (skor: {top1_score:.4f})')
        
        yearly_results.append({
            'year': year,
            'top1_products': top1_products,
            'top1_score': top1_score,
            'num_products': len(avg)
        })
    
    champions_all[platform] = yearly_results

# SUMMARY
print()
print('=' * 70)
print('RINGKASAN TOP 1 SETIAP TAHUN PER PLATFORM')
print('=' * 70)

for platform, results in champions_all.items():
    print(f'\n{platform.upper()}:')
    print('-' * 50)
    for r in results:
        products = ', '.join(r['top1_products'])
        print(f'  {r["year"]}: {products} (skor: {r["top1_score"]:.4f})')

print()
print('=' * 70)
print('JUARA TERBANYAK (2023-2026)')
print('=' * 70)

for platform, results in champions_all.items():
    all_winners = []
    for r in results:
        all_winners.extend(r['top1_products'])
    
    if all_winners:
        counter = Counter(all_winners)
        print(f'\n{platform.upper()}:')
        for name, count in counter.most_common():
            print(f'  {name}: {count} kali juara')
