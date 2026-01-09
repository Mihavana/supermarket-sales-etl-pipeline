CREATE OR REPLACE VIEW vue_clients_tranche_age AS
SELECT
    CASE
        WHEN age < 20 THEN '<20'
        WHEN age BETWEEN 20 AND 29 THEN '20-29'
        WHEN age BETWEEN 30 AND 39 THEN '30-39'
        WHEN age BETWEEN 40 AND 49 THEN '40-49'
        ELSE '50+'
    END AS tranche_age,
    COUNT(client_id) AS nb_clients
FROM dim_client
GROUP BY tranche_age
ORDER BY tranche_age;
