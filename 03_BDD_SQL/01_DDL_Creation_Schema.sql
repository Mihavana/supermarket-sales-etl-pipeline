-- Création de la table DIM_TEMPS
CREATE TABLE DIM_TEMPS (
    date_id INT PRIMARY KEY, -- Clé de substitution: AAAAMMJJ
    date_complete DATE NOT NULL,
    jour INT NOT NULL,
    semaine INT NOT NULL,
    mois INT NOT NULL,
    annee INT NOT NULL,
    nom_mois VARCHAR(20),
    est_ferie BOOLEAN
);

-- Création de la table DIM_CLIENT
CREATE TABLE DIM_CLIENT (
    client_id SERIAL PRIMARY KEY, -- Clé de substitution
    id_source VARCHAR(50) UNIQUE NOT NULL, -- Clé technique de la source
    age INT,
    sexe VARCHAR(10),
    code_postal VARCHAR(10),
    statut_fidelite VARCHAR(50) -- Ex: Bronze, Silver, Gold
);

-- Simplification: Utiliser Mockaroo pour DIM_PRODUIT et DIM_MAGASIN
CREATE TABLE DIM_PRODUIT (
    produit_id SERIAL PRIMARY KEY, -- Clé de substitution
    designation VARCHAR(255) NOT NULL,
    categorie VARCHAR(100),
    fournisseur VARCHAR(100)
);

CREATE TABLE DIM_MAGASIN (
    magasin_id SERIAL PRIMARY KEY, -- Clé de substitution
    ville VARCHAR(100) NOT NULL,
    region VARCHAR(100) NOT NULL
);

-- Création de la table de FAITS VENTES
CREATE TABLE VENTES (
    vente_id SERIAL PRIMARY KEY,
    date_id INT NOT NULL REFERENCES DIM_TEMPS(date_id),
    produit_id INT NOT NULL REFERENCES DIM_PRODUIT(produit_id),
    client_id INT NOT NULL REFERENCES DIM_CLIENT(client_id),
    magasin_id INT NOT NULL REFERENCES DIM_MAGASIN(magasin_id),
    montant DECIMAL(10, 2) NOT NULL,
    quantite INT NOT NULL
);