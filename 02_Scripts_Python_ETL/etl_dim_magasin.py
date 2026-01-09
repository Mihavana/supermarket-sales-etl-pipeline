import pandas as pd
from connexion_db import get_db_engine
from sqlalchemy import text
import numpy as np

def etl_dim_magasin(file_path):
    engine = get_db_engine()
    df = pd.read_csv(file_path)
    
    
    # Extraire les villes uniques
    df_magasin = df[['City']].drop_duplicates().reset_index(drop=True)
    df_magasin.rename(columns={'City': 'ville'}, inplace=True)
    
    # Simuler une région et une surface pour l'exercice
    df_magasin['region'] = df_magasin['ville'].apply(lambda x: "Région_" + x[:3])
    
    # Génère une surface aléatoire entre 100 et 1500 m2 pour chaque magasin
    df_magasin['surface'] = np.random.randint(100, 1501, size=len(df_magasin))
    
    # Chargement
    with engine.connect() as conn:
        conn.execute(text("TRUNCATE TABLE dim_magasin RESTART IDENTITY CASCADE;"))
        conn.commit()
        
    df_magasin.to_sql('dim_magasin', engine, if_exists='append', index=False)
    print(f"✅ DIM_MAGASIN chargée ({len(df_magasin)} villes).")