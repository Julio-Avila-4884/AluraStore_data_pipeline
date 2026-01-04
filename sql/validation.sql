-- Verificar cantidad de registros
SELECT COUNT(*) AS total_rows
FROM telecom_customers;

-- Verificar valores nulos críticos
SELECT
    COUNT(*) AS null_tenure
FROM telecom_customers
WHERE tenure IS NULL;

-- Verificar distribución de churn
SELECT
    churn,
    COUNT(*) AS count
FROM telecom_customers
GROUP BY churn;
