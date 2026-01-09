CREATE OR REPLACE VIEW vue_ventes_journalieres AS
SELECT
    t.jour,
    t.mois,
    t.annee,
    p.designation AS produit,
    m.ville,
    SUM(f.quantite) AS quantite_totale,
    SUM(f.quantite * f.montant) AS chiffre_affaires
FROM ventes f
JOIN dim_temps t ON f.date_id = t.date_id
JOIN dim_produit p ON f.produit_id = p.produit_id
JOIN dim_magasin m ON f.id_magasin = m.magasin_id
GROUP BY
    t.jour, t.mois, t.annee,
    p.designation,
    m.ville
ORDER BY
    t.annee, 
    CASE t.mois
        WHEN 'Janvier' THEN 1
        WHEN 'Février' THEN 2
        WHEN 'Mars' THEN 3
        WHEN 'Avril' THEN 4
        WHEN 'Mai' THEN 5
        WHEN 'Juin' THEN 6
        WHEN 'Juillet' THEN 7
        WHEN 'Août' THEN 8
        WHEN 'Septembre' THEN 9
        WHEN 'Octobre' THEN 10
        WHEN 'Novembre' THEN 11
        WHEN 'Décembre' THEN 12
    END,
    t.jour;
