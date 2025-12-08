## 📁 Projet Data Warehouse : Analyse des Ventes de Supermarché

Ce projet a pour objectif la mise en place d'un **Entrepôt de Données (Data Warehouse)** pour un supermarché, en utilisant le processus **ETL (Extraction, Transformation, Chargement)** intégralement développé en Python.

L'entrepôt est modélisé selon un **Schéma en Étoile** pour permettre l'analyse multidimensionnelle (OLAP) des ventes par produit, client, période et localisation. 

### Objectifs Principaux
* Construire un modèle en étoile comprenant une Table de Faits (`VENTES`) et quatre Dimensions (`DIM_PRODUIT`, `DIM_TEMPS`, `DIM_CLIENT`, `DIM_MAGASIN`).
* Implémenter le pipeline ETL en **Python** (avec Pandas/SQLAlchemy).
* Réaliser des analyses OLAP pour identifier les tendances de vente et le comportement client.

***

## 🛠️ Prérequis Techniques

Pour exécuter ce projet, vous devez disposer des outils et librairies suivants :

### 1. Environnement
* **Python 3.x**
* **SGBD :** PostgreSQL (ou MySQL/MariaDB).

### 2. Librairies Python

Installez toutes les dépendances requises en utilisant `pip` :

```bash
pip install -r requirements.txt
```

Le fichier `requirements.txt` doit contenir au minimum :
```bash
pip install -r requirements.txt
```pandas
sqlalchemy
# Choisissez le connecteur approprié à votre BDD
psycopg2-binary  # Pour PostgreSQL
# mysql-connector-python  # Pour MySQL
```
## 🚀 Guide de Démarrage Rapide
### Étape 1 : Configuration de la Base de Données
1. Assurez-vous que votre instance PostgreSQL (ou autre SGBD) est en cours d'exécution.

2. Créez la base de données cible (ex: supermarket_dw).

3. Exécutez le script DDL pour créer les tables de l'entrepôt :
```bash
# Exemple de commande psql
psql -U votre_utilisateur -d supermarket_dw -f 03_BDD_SQL/01_DDL_Creation_Schema.sql
```
### Étape 2 : Configuration de la Connexion
Modifiez le fichier `03_BDD_SQL/connexion_db.py` (ou le fichier où vous définissez votre SQLAlchemy Engine) avec vos identifiants de connexion.

Exemple de chaîne de connexion SQLAlchemy : `'postgresql://utilisateur:motdepasse@localhost:5432/supermarket_dw'`

### Étape 3 : Exécution du Pipeline ETL
Le script principal orchestre l'extraction, la transformation et le chargement dans le bon ordre (Dimensions puis Faits).

Exécuter le script principal :
```bash
python 02_Scripts_Python_ETL/etl_main.py
```

### Étape 4 : Analyse et Vérification
1. Exécuter les requêtes OLAP : Utilisez le fichier 03_BDD_SQL/02_DQL_OLAP_Queries.sql pour interroger la base de données et obtenir les analyses demandées.

2. Visualisation : Connectez votre outil de BI (Metabase, Power BI, etc.) à la base de données supermarket_dw pour générer le tableau de bord de visualisation.

## 📂 Structure des Dossiers
Référence de la structure des fichiers du projet :

* 01_Sources_Brutes/: Fichiers de données initiaux (supermarket_sales.csv, produits, clients...).

* 02_Scripts_Python_ETL/: Scripts Python de transformation et de chargement.

* 03_BDD_SQL/: Scripts SQL de création de tables et d'analyse.

* 04_Analyses_Visualisations/: Sorties de l'analyse et du tableau de bord.

* 05_Livrables/: Rapport final et présentation.

* README.md (ce fichier)

* requirements.txt