"""
Analisis Ranking Antivirus Multi-Platform (2023-2026)
"""
import sys
sys.path.insert(0, '.')

import pandas as pd
from src.data_ingestion import load_av_test_data, filter_by_platform, filter_by_year, get_available_years
from src.models import calculate_topsis

# Load data
df = load_av_test_data('data/raw/av_test_ratings_multiplatform.csv')

print("=" * 70)
print("ANALISIS RANKING ANTIVIRUS MULTI-PLATFORM (2023-2026)")
print("=" * 70)

# Analisis per platform
for platform in ['Windows', 'macOS', 'Android']:
    print()
    print("=" * 70)
    print(f"PLATFORM: {platform.upper()}")
    print("=" * 70)
    
    df_platform = filter_by_platform(df, platform)
    years = sorted(df_platform['test_period'].str[:4].unique())
    
    print(f"Tahun tersedia: {years}")
    print()
    
    # Ranking per tahun
    all_top_products = []
    
    for year in years:
        df_year = filter_by_year(df_platform, year)
        if len(df_year) > 0:
            result = calculate_topsis(df_year, [0.50, 0.20, 0.30], ['benefit', 'benefit', 'benefit'])
            
            print(f"--- TAHUN {year} ---")
            print(result[['antivirus_name', 'protection', 'performance', 'usability', 'rating_score', 'rank']].head(10).to_string(index=False))
            print()
            
            # Simpan top 1
            top1 = result.iloc[0]
            all_top_products.append({
                'year': year,
                'antivirus_name': top1['antivirus_name'],
                'rating_score': top1['rating_score'],
                'protection': top1['protection'],
                'performance': top1['performance'],
                'usability': top1['usability'],
            })
    
    # Juara sepanjang tahun
    if all_top_products:
        print("=" * 70)
        print(f"TOP 1 {platform.upper()} SETIAP TAHUN")
        print("=" * 70)
        top_df = pd.DataFrame(all_top_products)
        print(top_df.to_string(index=False))
        
        # Hitung berapa kali jadi juara
        print()
        print(f"JUARA TERBANYAK {platform.upper()} (2023-2026):")
        champion_counts = top_df['antivirus_name'].value_counts()
        for name, count in champion_counts.items():
            print(f"  {name}: {count} kali juara")
        
        # Overall juara
        overall_champion = champion_counts.index[0]
        print()
        print(f">> JUARA OVERALL {platform.upper()}: {overall_champion} ({champion_counts.iloc[0]} kali juara)")
    
    print()

# Ringkasan akhir
print()
print("=" * 70)
print("RINGKASAN JUARA OVERALL PER PLATFORM (2023-2026)")
print("=" * 70)

for platform in ['Windows', 'macOS', 'Android']:
    df_platform = filter_by_platform(df, platform)
    years = sorted(df_platform['test_period'].str[:4].unique())
    
    champions = []
    for year in years:
        df_year = filter_by_year(df_platform, year)
        if len(df_year) > 0:
            result = calculate_topsis(df_year, [0.50, 0.20, 0.30], ['benefit', 'benefit', 'benefit'])
            champions.append(result.iloc[0]['antivirus_name'])
    
    if champions:
        from collections import Counter
        counter = Counter(champions)
        overall = counter.most_common(1)[0]
        print(f"{platform:10}: {overall[0]} ({overall[1]} kali juara dari {len(champions)} tahun)")
