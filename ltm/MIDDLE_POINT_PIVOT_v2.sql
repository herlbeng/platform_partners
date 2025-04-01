--CREATE OR REPLACE VIEW gp-technologies-dev.gold.dashboard_test AS (
WITH company_middle_point AS (
    SELECT company_new_name
         , company_join_date AS middle_point  
      FROM gp-technologies-dev.bronze.companies
--     WHERE company_new_name 
--        IN ('Shape NEWE - Sharp PHC','Shape GEM - Green Energy')
),
company_months AS (
    -- Secuencia de 24 meses alrededor del punto medio
    SELECT cm.company_new_name
         , cm.middle_point
         , DATE_TRUNC(DATE_ADD(cm.middle_point, INTERVAL n - 11 MONTH), MONTH) AS month_date
         , n - 11 AS month_offset
      FROM company_middle_point cm
     CROSS JOIN UNNEST(GENERATE_ARRAY(0, 23)) AS n
)
--select * from CompanyMonths
, ltm_kpis_data AS (
    -- Valores de los KPIs a cada mes generado
    SELECT cm.company_new_name
         , cm.middle_point
         , cm.month_date
--         , FORMAT("%'.d", CAST(COALESCE(cr.revenue_total, 0) AS INT64)) AS total
         , COALESCE(cr.revenue_total, 0) AS total
         , cm.month_offset
         , CAST('revenue' AS STRING) AS tag
      FROM company_months cm
--      LEFT JOIN `gp-technologies-dev.silver.ltm_cons_test1` cr 
      LEFT JOIN `gp-technologies-dev.silver.ltm_consolidate_group` cr 
        ON cm.company_new_name = cr.company_new_name 
       AND cm.month_date = cr.month
     UNION ALL       
    SELECT cm.company_new_name
         , cm.middle_point
         , cm.month_date
--         , FORMAT("%'.d", CAST(COALESCE(cr.single_jobs_total, 0) AS INT64)) AS total
         , COALESCE(cr.single_jobs_total, 0) AS total
         , cm.month_offset
         , CAST('single_jobs' AS STRING) AS tag
      FROM company_months cm
--      LEFT JOIN `gp-technologies-dev.silver.ltm_cons_test1` cr 
      LEFT JOIN `gp-technologies-dev.silver.ltm_consolidate_group` cr 
        ON cm.company_new_name = cr.company_new_name 
       AND cm.month_date = cr.month
)
--select * from ltm_kpis_data;
-- Filas a columnas con el punto medio siempre en la posición central
SELECT * FROM (
    SELECT company_new_name
         , middle_point
         , tag
         , month_offset
         , SUM(total) AS total
        --, FORMAT("%'.d", CAST(SUM(total) AS INT64)) AS total
      FROM ltm_kpis_data
     GROUP BY company_new_name, middle_point, tag, month_offset 
     ORDER BY middle_point, company_new_name, tag, month_offset 
) 
PIVOT (
    --SUM(total) 
    FORMAT("%'.d", CAST(SUM(total) AS INT64)) AS total
    FOR month_offset IN (
        -11 AS `-11`, -10 AS `-10`, -9 AS `-9`, -8 AS `-8`, -7 AS `-7`, -6 AS `-6`, 
         -5 AS  `-5`,  -4 AS  `-4`, -3 AS `-3`, -2 AS `-2`, -1 AS `-1`,  0 AS  `0`, 
          1 AS   `1`,   2 AS   `2`,  3 AS  `3`,  4 AS  `4`,  5 AS  `5`,  6 AS  `6`,  
          7 AS   `7`,   8 AS   `8`,  9 AS  `9`, 10 AS `10`, 11 AS `11`, 12 AS `12`
    )
)
ORDER BY middle_point,company_new_name
--);
