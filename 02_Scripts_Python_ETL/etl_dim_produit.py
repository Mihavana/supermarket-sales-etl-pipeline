import pandas as pd
from sqlalchemy import text
from connexion_db import get_db_engine

def etl_dim_produit_off(off_file_path):
    print("Extraction simplifiée de DIM_PRODUIT...")
    
    COLS_NECESSAIRES = ['code', 'product_name', 'categories_en', 'brands']
    engine = get_db_engine()

    # 1. Extraction : On ne prend que les 100 000 premières lignes
    # C'est nrows qui permet d'éviter le "chunking" et de ne pas saturer la RAM
    df = pd.read_csv(
        off_file_path, 
        sep='\t', 
        usecols=COLS_NECESSAIRES, 
        nrows=100000, 
        low_memory=False
    )

    # 2. Transformation
    df = df.dropna(subset=['code', 'product_name', 'categories_en'])
    df = df.drop_duplicates(subset=['code'])
    
    df.rename(columns={
        'code': 'id_source', 
        'product_name': 'designation', 
        'categories_en': 'categorie',
        'brands': 'fournisseur'
    }, inplace=True)

    # 3. Chargement
    with engine.connect() as conn:
        conn.execute(text("TRUNCATE TABLE dim_produit RESTART IDENTITY CASCADE;"))
        conn.commit()
    
    df[['designation', 'categorie', 'fournisseur']].to_sql(
        'dim_produit', 
        engine, 
        if_exists='append', 
        index=False
    )
    
    print(f"✅ DIM_PRODUIT chargée avec {len(df)} produits.")