import pandas as pd
from connexion_db import get_db_engine
from sqlalchemy import text

def etl_dim_temps():
    engine = get_db_engine()
    
    # 1. Charger les dates des ventes
    path_sales = '/mnt/44D2A11AD2A1116A/Studies/INSI/M1/BI et Data Analytics/Exercices/supermarket-sales-etl-pipeline/01_ Source_brutes/supermarket_sales.csv'
    df_ventes = pd.read_csv(path_sales)
    df_ventes['Date'] = pd.to_datetime(df_ventes['Date'])
    
    # 2. Charger le fichier des jours fériés
    try:
        path_feries = '/mnt/44D2A11AD2A1116A/Studies/INSI/M1/BI et Data Analytics/Exercices/supermarket-sales-etl-pipeline/01_ Source_brutes/jours_feries.csv'
        df_feries = pd.read_csv(path_feries)
        df_feries['date'] = pd.to_datetime(df_feries['date'])
    except FileNotFoundError:
        print("⚠️ Jours_feries.csv non trouvé, toutes les valeurs seront 'False'")
        df_feries = pd.DataFrame(columns=['date'])

    # 3. Créer la liste des dates uniques
    df_temps = pd.DataFrame(df_ventes['Date'].unique(), columns=['date_complete'])
    df_temps = df_temps.sort_values('date_complete')
    
    # 4. Extraire les attributs et calculer les nouvelles colonnes
    df_temps['date_id'] = df_temps['date_complete'].dt.strftime('%Y%m%d').astype(int)
    df_temps['jour'] = df_temps['date_complete'].dt.day
    df_temps['semaine'] = df_temps['date_complete'].dt.isocalendar().week
    df_temps['annee'] = df_temps['date_complete'].dt.year
    df_temps['mois'] = df_temps['date_complete'].dt.month_name()

    mapping_mois = {
        'January': 'Janvier', 'February': 'Février', 'March': 'Mars',
        'April': 'Avril', 'May': 'Mai', 'June': 'Juin',
        'July': 'Juillet', 'August': 'Août', 'September': 'Septembre',
        'October': 'Octobre', 'November': 'Novembre', 'December': 'Décembre'
    }
    df_temps['mois'] = df_temps['mois'].map(mapping_mois)
    
    # Calcul de la colonne ferie
    df_temps['ferie'] = df_temps['date_complete'].isin(df_feries['date'])

    # 5. Sélectionner UNIQUEMENT les colonnes cibles du SQL
    # On exclut 'date_complete' ici
    colonnes_sql = ['date_id', 'jour', 'semaine', 'mois', 'annee', 'ferie']
    df_final = df_temps[colonnes_sql].copy()
    
    # 6. Chargement dans la BDD
    with engine.connect() as conn:
        print("Vidage de la table dim_temps...")
        conn.execute(text("TRUNCATE TABLE dim_temps RESTART IDENTITY CASCADE;"))
        conn.commit()

    df_final.to_sql('dim_temps', engine, if_exists='append', index=False)
    print(f"✅ DIM_TEMPS chargée : {len(df_final)} dates insérées avec indicateur férié.")