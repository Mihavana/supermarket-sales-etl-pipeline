import pandas as pd
import numpy as np
from sqlalchemy import text
from connexion_db import get_db_engine

def etl_fait_ventes():
    engine = get_db_engine()
    print("🚀 Chargement de la table de faits VENTES...")

    # 1. Charger la source brute
    path_sales = '/mnt/44D2A11AD2A1116A/Studies/INSI/M1/BI et Data Analytics/Exercices/supermarket-sales-etl-pipeline/01_ Source_brutes/supermarket_sales.csv'
    df_sales = pd.read_csv(path_sales)

    # 2. Récupérer les IDs des dimensions pour le mapping (Lookup)
    dim_client = pd.read_sql("SELECT client_id FROM dim_client", engine)
    dim_produit = pd.read_sql("SELECT produit_id FROM dim_produit", engine)
    # IMPORTANT : On récupère l'ID et la Ville pour faire la correspondance
    dim_magasin = pd.read_sql("SELECT magasin_id, ville FROM dim_magasin", engine)

    # 3. Transformations
    # a. Calcul de date_id (FK)
    df_sales['date_id'] = pd.to_datetime(df_sales['Date']).dt.strftime('%Y%m%d').astype(int)

    # b. Mapping Magasin : On lie la ville du CSV ('City') à l'ID de la table Magasin
    df_sales = df_sales.merge(dim_magasin, left_on='City', right_on='ville', how='left')

    # c. Attribution des IDs Client et Produit (Aléatoire pour l'exercice)
    client_ids = dim_client['client_id'].values
    produit_ids = dim_produit['produit_id'].values
    
    df_sales['client_id_mapped'] = np.random.choice(client_ids, size=len(df_sales))
    df_sales['produit_id_mapped'] = np.random.choice(produit_ids, size=len(df_sales))

    # 4. Sélection des colonnes finales
    # Attention : on utilise 'magasin_id' (récupéré du merge) et nos colonnes mappées
    fait_ventes = df_sales[['date_id', 'produit_id_mapped', 'client_id_mapped', 'magasin_id', 'Total', 'Quantity']].copy()
    
    # Renommage pour correspondre EXACTEMENT à ton SQL
    fait_ventes.columns = ['date_id', 'produit_id', 'client_id', 'id_magasin', 'montant', 'quantite']

    # 5. Chargement final
    with engine.connect() as conn:
        print("Nettoyage de la table VENTES...")
        conn.execute(text("TRUNCATE TABLE ventes RESTART IDENTITY CASCADE;"))
        conn.commit()
        
    fait_ventes.to_sql('ventes', engine, if_exists='append', index=False)
    print(f"✅ Table VENTES chargée : {len(fait_ventes)} lignes insérées.")

if __name__ == "__main__":
    etl_fait_ventes()