import subprocess
import time
import sys

def run_script(path):
    """Exécute un script python et attend la fin."""
    print(f"⏳ Exécution de : {path}...")
    try:
        # On utilise sys.executable pour s'assurer d'utiliser le bon interpréteur python
        result = subprocess.run([sys.executable, path], check=True, capture_output=True, text=True)
        print(result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Erreur dans {path} :")
        print(e.stderr)
        return False

def main():
    start_time = time.time()
    print("==================================================")
    print("🚀 DÉMARRAGE DU PIPELINE ETL FULL PYTHON")
    print("==================================================")

    # 1. Liste des scripts dans l'ordre logique (Dimensions -> Faits)
    pipeline = [
        "02_Scripts_Python_ETL/etl_dim_temps.py",
        "02_Scripts_Python_ETL/etl_dim_produit.py",
        "02_Scripts_Python_ETL/etl_dim_client.py",
        "02_Scripts_Python_ETL/etl_dim_magasin.py",
        "02_Scripts_Python_ETL/etl_fait_ventes.py" # Les faits en dernier !
    ]

    success = True
    for script in pipeline:
        if not run_script(script):
            success = False
            print("🛑 Arrêt du pipeline suite à une erreur.")
            break
        print("--------------------------------------------------")

    if success:
        end_time = time.time()
        duree = round(end_time - start_time, 2)
        print(f"✅ PIPELINE TERMINÉ AVEC SUCCÈS en {duree} secondes.")
        print("📊 Vous pouvez maintenant ouvrir 04_Analyses_SQL pour les analyses et 05_Visualisations pour les visualisations.")
    print("==================================================")

if __name__ == "__main__":
    main()