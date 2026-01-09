# 1. Top 10 des produits par chiffre d'affaires mensuel
SELECT 
    t.mois,
    p.designation,
    SUM(v.montant) as chiffre_affaires
FROM ventes v
JOIN dim_produit p ON v.produit_id = p.produit_id
JOIN dim_temps t ON v.date_id = t.date_id
GROUP BY t.mois, t.mois, p.designation
ORDER BY chiffre_affaires DESC
LIMIT 10;

# 2. Répartition des clients par segment d'âge et fidélité
SELECT 
    CASE 
        WHEN age < 25 THEN 'Jeunes (<25)'
        WHEN age BETWEEN 25 AND 50 THEN 'Adultes (25-50)'
        ELSE 'Seniors (>50)'
    END as segment_age,
    statut_fidelite,
    COUNT(client_id) as nombre_clients
FROM dim_client
GROUP BY segment_age, statut_fidelite
ORDER BY segment_age;

# 3. Analyse des ventes par zone géographique
SELECT 
    m.ville,
    m.region,
    SUM(v.montant) as total_ventes,
    SUM(v.quantite) as volume_articles
FROM ventes v
JOIN dim_magasin m ON v.id_magasin = m.magasin_id
GROUP BY m.ville, m.region
ORDER BY total_ventes DESC;

# 4. Saisonnalité (Croisement produits × période)
SELECT 
    p.categorie,
    t.semaine,
    SUM(v.montant) as CA_hebdomadaire
FROM ventes v
JOIN dim_produit p ON v.produit_id = p.produit_id
JOIN dim_temps t ON v.date_id = t.date_id
GROUP BY p.categorie, t.semaine
ORDER BY t.semaine, CA_hebdomadaire DESC;

# 5. Corrélation entre catégorie produit et récurrence d’achat
SELECT 
    p.categorie,
    COUNT(v.produit_id) as volume_total_ventes,
    COUNT(DISTINCT v.client_id) as nombre_clients_uniques,
    ROUND(CAST(COUNT(v.produit_id) AS DECIMAL) / COUNT(DISTINCT v.client_id), 2) as indice_recurrence
FROM ventes v
JOIN dim_produit p ON v.produit_id = p.produit_id
GROUP BY p.categorie
ORDER BY indice_recurrence DESC;