import pandas as pd
from src.data_ingestion import load_av_test_data, filter_by_platform, filter_by_year
from src.models import calculate_topsis

df = load_av_test_data('data/raw/av_test_ratings_multiplatform.csv')
WEIGHTS = [0.50, 0.20, 0.30]
CT = ['benefit', 'benefit', 'benefit']

for platform in ['Windows', 'macOS', 'Android']:
    df_p = filter_by_platform(df, platform)
    years = sorted(df_p['test_period'].str[:4].unique())
    
    print(f'\n{"="*60}')
    print(f'{platform.upper()} - Juara per Tahun')
    print(f'{"="*60}')
    
    for year in years:
        df_y = filter_by_year(df_p.copy(), int(year))
        if len(df_y) == 0:
            continue
        
        result = calculate_topsis(df_y, WEIGHTS, CT)
        
        top1_score = result.iloc[0]['rating_score']
        top1_products = result[result['rating_score'] == top1_score]['antivirus_name'].tolist()
        
        print(f'\n{year} ({len(df_y)} records, {result["antivirus_name"].nunique()} products):')
        print(f'  TOP 1 (score={top1_score:.4f}): {", ".join(top1_products[:5])}')
        if len(top1_products) > 5:
            print(f'    ... dan {len(top1_products)-5} lainnya')
