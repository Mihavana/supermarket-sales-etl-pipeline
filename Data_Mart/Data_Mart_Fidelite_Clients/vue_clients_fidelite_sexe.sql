CREATE OR REPLACE VIEW vue_clients_statut_sexe AS
SELECT
    sexe,
    statut_fidelite,
    COUNT(client_id) AS nb_clients
FROM dim_client
GROUP BY statut_fidelite, sexe
ORDER BY statut_fidelite, sexe;
