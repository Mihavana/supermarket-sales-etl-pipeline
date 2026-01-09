import pandas as pd

# Chemin d'accès à votre fichier OFF (assurez-vous qu'il est décompressé si possible, 
# sinon ajoutez compression='gzip' si c'est un .gz)
OFF_FILE_PATH = '/mnt/44D2A11AD2A1116A/Studies/INSI/M1/BI et Data Analytics/Exercices/supermarket-sales-etl-pipeline/01_ Source_brutes/products.csv' 
# Si c'est un fichier .tsv (tabulation) :
# OFF_FILE_PATH = '01_Sources_Brutes/fr.openfoodfacts.org.products.tsv' 

try:
    # Tenter de lire l'en-tête seulement (nrows=0) avec un séparateur Tabulation
    df_headers = pd.read_csv(
        OFF_FILE_PATH, 
        sep='\t', 
        nrows=0,
        encoding='utf-8', 
        low_memory=False
    )
    
    # Afficher la liste des colonnes
    print("✅ Succès ! Séparateur probable : TABULATION (\\t)")
    print("--- Liste des 50 premières colonnes : ---")
    print(df_headers.columns[:50].tolist())
    print("\n--- Liste des 5 dernières colonnes : ---")
    print(df_headers.columns[-5:].tolist())
    
    print("\nTotal de colonnes trouvées :", len(df_headers.columns))
    
except Exception as e:
    print(f"❌ Erreur avec le séparateur Tabulation (\\t) ou le chemin. Erreur: {e}")
    
    try:
        # Tenter de lire l'en-tête seulement avec un séparateur Virgule
        df_headers_virgule = pd.read_csv(
            OFF_FILE_PATH, 
            sep=',', 
            nrows=0,
            encoding='utf-8', 
            low_memory=False
        )
        print("\n✅ Succès ! Séparateur probable : VIRGULE (,)")
        print("--- Liste des 10 premières colonnes : ---")
        print(df_headers_virgule.columns[:10].tolist())
    except Exception as e_v:
        print(f"❌ Échec avec les séparateurs courants. Veuillez vérifier le fichier source. Erreur: {e_v}")