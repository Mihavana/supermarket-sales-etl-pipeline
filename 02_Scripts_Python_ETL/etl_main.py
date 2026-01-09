from etl_dim_produit import etl_dim_produit_off
from etl_dim_magasin import etl_dim_magasin
from etl_dim_client import etl_dim_client
from etl_dim_temps import etl_dim_temps

def run_all():
    print("--- Lancement de l'ETL des Dimensions ---")
    etl_dim_produit_off('/mnt/44D2A11AD2A1116A/Studies/INSI/M1/BI et Data Analytics/Exercices/supermarket-sales-etl-pipeline/01_ Source_brutes/products_sample.csv')
    etl_dim_magasin("/mnt/44D2A11AD2A1116A/Studies/INSI/M1/BI et Data Analytics/Exercices/supermarket-sales-etl-pipeline/01_ Source_brutes/supermarket_sales.csv")
    etl_dim_client('/mnt/44D2A11AD2A1116A/Studies/INSI/M1/BI et Data Analytics/Exercices/supermarket-sales-etl-pipeline/01_ Source_brutes/clients.csv')
    etl_dim_temps()
    print("--- Fin de l'ETL des Dimensions ---")

if __name__ == "__main__":
    run_all()