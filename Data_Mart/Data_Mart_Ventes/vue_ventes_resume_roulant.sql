CREATE OR REPLACE VIEW vue_ventes_resume_roulant AS
SELECT *
FROM (
    -- Détail journalier pour les 3 derniers mois de 2019
    SELECT
        t.jour,
        t.mois,
        t.annee,
        p.designation AS produit,
        m.ville,
        SUM(f.quantite) AS quantite,
        SUM(f.quantite * f.montant) AS chiffre_affaires
    FROM ventes f
    JOIN dim_temps t ON f.date_id = t.date_id
    JOIN dim_produit p ON f.produit_id = p.produit_id
    JOIN dim_magasin m ON f.id_magasin = m.magasin_id
    WHERE t.annee = 2019
      AND t.mois IN ('Octobre', 'Novembre', 'Décembre')
    GROUP BY t.jour, t.mois, t.annee, p.designation, m.ville

    UNION ALL

    -- Agrégation mensuelle pour les mois précédents
    SELECT
        NULL AS jour,
        t.mois,
        t.annee,
        p.designation AS produit,
        m.ville,
        SUM(f.quantite) AS quantite,
        SUM(f.quantite * f.montant) AS chiffre_affaires
    FROM ventes f
    JOIN dim_temps t ON f.date_id = t.date_id
    JOIN dim_produit p ON f.produit_id = p.produit_id
    JOIN dim_magasin m ON f.id_magasin = m.magasin_id
    WHERE t.annee = 2019
      AND t.mois NOT IN ('Octobre', 'Novembre', 'Décembre')
    GROUP BY t.mois, t.annee, p.designation, m.ville
) AS union_ventes
ORDER BY
    annee,
    CASE mois
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
    jour;
