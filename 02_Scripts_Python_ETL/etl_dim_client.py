import pandas as pd
from connexion_db import get_db_engine
from sqlalchemy import text

def etl_dim_client(file_path):
    engine = get_db_engine()
    
    # Lecture du fichier avec les noms que tu m'as donnés
    df = pd.read_csv(file_path)
    
    # 1. Sélection et Renommage pour correspondre au Modèle en Étoile (SQL)
    # On mappe : age -> age, gender -> sexe, loyalty -> fidelite, postal_code -> ville
    df_client = df[['age', 'gender', 'loyalty', 'postal_code']].copy()
    
    df_client.columns = ['age', 'sexe', 'statut_fidelite', 'code_postal']
    
    # 2. Nettoyage simple
    df_client = df_client.drop_duplicates()
    
    # 3. Chargement vers SQL
    # if_exists='replace' va recréer la table proprement
    with engine.connect() as conn:
        conn.execute(text("TRUNCATE TABLE dim_client RESTART IDENTITY CASCADE;"))
        conn.commit()

    df_client.to_sql('dim_client', engine, if_exists='append', index=False)
    
    print(f"✅ DIM_CLIENT : {len(df_client)} clients chargés avec succès.")