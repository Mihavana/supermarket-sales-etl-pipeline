CREATE OR REPLACE VIEW vue_clients_code_postal AS
SELECT
    code_postal,
    COUNT(client_id) AS nb_clients
FROM dim_client
GROUP BY code_postal
ORDER BY code_postal;
