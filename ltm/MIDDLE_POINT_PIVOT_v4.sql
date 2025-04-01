CREATE OR REPLACE VIEW gp-technologies-dev.gold.dashboard_kpis AS (
WITH company_middle_point AS (
    SELECT company_new_name
         , company_join_date AS middle_point  
      FROM gp-technologies-dev.bronze.companies
),
company_months AS (
    -- Secuencia de 24 meses alrededor del punto medio
    SELECT cm.company_new_name
         , cm.middle_point
         , DATE_TRUNC(DATE_ADD(cm.middle_point, INTERVAL n - 12 MONTH), MONTH) AS month_date
         , n - 12 AS month_offset
      FROM company_middle_point cm
     CROSS JOIN UNNEST(GENERATE_ARRAY(0, 23)) AS n
)
--select * from company_months
, ltm_kpis_data AS (
    -- Valores de los KPIs a cada mes generado
    SELECT cm.company_new_name
         , cm.middle_point
         , cm.month_date
         , COALESCE(cr.revenue_total, 0) AS total
         , cm.month_offset
         , CAST('Revenue' AS STRING) AS tag
      FROM company_months cm
      LEFT JOIN `gp-technologies-dev.silver.ltm_kpis_consolidate_group` cr 
        ON cm.company_new_name = cr.company_new_name 
       AND EXTRACT(YEAR FROM cm.month_date) = cr.year
       AND EXTRACT(MONTH FROM cm.month_date) = cr.month
     UNION ALL       
    SELECT cm.company_new_name
         , cm.middle_point
         , cm.month_date
         , COALESCE(cr.single_jobs_total, 0) AS total
         , cm.month_offset
         , CAST('Single Jobs' AS STRING) AS tag
      FROM company_months cm
      LEFT JOIN `gp-technologies-dev.silver.ltm_kpis_consolidate_group` cr 
        ON cm.company_new_name = cr.company_new_name 
       AND EXTRACT(YEAR FROM cm.month_date) = cr.year
       AND EXTRACT(MONTH FROM cm.month_date) = cr.month
     UNION ALL 
    SELECT cm.company_new_name
         , cm.middle_point
         , cm.month_date
         , COALESCE(cr.gba_pace, 0) AS total
         , cm.month_offset
         , CAST('GBA' AS STRING) AS tag
      FROM company_months cm
      LEFT JOIN `gp-technologies-dev.silver.ltm_kpis_consolidate_group` cr 
        ON cm.company_new_name = cr.company_new_name 
       AND EXTRACT(YEAR FROM cm.month_date) = cr.year
       AND EXTRACT(MONTH FROM cm.month_date) = cr.month
     UNION ALL            
    SELECT cm.company_new_name
         , cm.middle_point
         , cm.month_date
         , COALESCE(cr.sold_estimates_pace, 0) AS total
         , cm.month_offset
         , CAST('Sold Estimates' AS STRING) AS tag
      FROM company_months cm
      LEFT JOIN `gp-technologies-dev.silver.ltm_kpis_consolidate_group` cr 
        ON cm.company_new_name = cr.company_new_name 
       AND EXTRACT(YEAR FROM cm.month_date) = cr.year
       AND EXTRACT(MONTH FROM cm.month_date) = cr.month
     UNION ALL                 
    SELECT cm.company_new_name
         , cm.middle_point
         , cm.month_date
         , COALESCE(cr.manpower_sj_qty, 0) AS total
         , cm.month_offset
         , CAST('Manpower' AS STRING) AS tag
      FROM company_months cm
      LEFT JOIN `gp-technologies-dev.silver.ltm_kpis_consolidate_group` cr 
        ON cm.company_new_name = cr.company_new_name 
       AND EXTRACT(YEAR FROM cm.month_date) = cr.year
       AND EXTRACT(MONTH FROM cm.month_date) = cr.month
     UNION ALL       
    SELECT cm.company_new_name
         , cm.middle_point
         , cm.month_date
         , COALESCE(cr.sold_hours_total_sold_hrs, 0) AS total
         , cm.month_offset
         , CAST('Sold Hours' AS STRING) AS tag
      FROM company_months cm
      LEFT JOIN `gp-technologies-dev.silver.ltm_kpis_consolidate_group` cr 
        ON cm.company_new_name = cr.company_new_name 
       AND EXTRACT(YEAR FROM cm.month_date) = cr.year
       AND EXTRACT(MONTH FROM cm.month_date) = cr.month
     UNION ALL       
    SELECT cm.company_new_name
         , cm.middle_point
         , cm.month_date
         , COALESCE(cr.sj__usd_100_total, 0) AS total
         , cm.month_offset
         , CAST('SJ<$100' AS STRING) AS tag
      FROM company_months cm
      LEFT JOIN `gp-technologies-dev.silver.ltm_kpis_consolidate_group` cr 
        ON cm.company_new_name = cr.company_new_name 
       AND EXTRACT(YEAR FROM cm.month_date) = cr.year
       AND EXTRACT(MONTH FROM cm.month_date) = cr.month
     UNION ALL       
    SELECT cm.company_new_name
         , cm.middle_point
         , cm.month_date
         , COALESCE(cr.recalls_total, 0) AS total
         , cm.month_offset
         , CAST('Recalls' AS STRING) AS tag
      FROM company_months cm
      LEFT JOIN `gp-technologies-dev.silver.ltm_kpis_consolidate_group` cr 
        ON cm.company_new_name = cr.company_new_name 
       AND EXTRACT(YEAR FROM cm.month_date) = cr.year
       AND EXTRACT(MONTH FROM cm.month_date) = cr.month
     UNION ALL       
    SELECT cm.company_new_name
         , cm.middle_point
         , cm.month_date
         , COALESCE(cr.sj_repair_pct_total, 0) AS total
         , cm.month_offset
         , CAST('SJ Repair %' AS STRING) AS tag
      FROM company_months cm
      LEFT JOIN `gp-technologies-dev.silver.ltm_kpis_consolidate_group` cr 
        ON cm.company_new_name = cr.company_new_name 
       AND EXTRACT(YEAR FROM cm.month_date) = cr.year
       AND EXTRACT(MONTH FROM cm.month_date) = cr.month
     UNION ALL       
    SELECT cm.company_new_name
         , cm.middle_point
         , cm.month_date
         , COALESCE(cr.sj_repair_avg_usd_total, 0) AS total
         , cm.month_offset
         , CAST('SJ Repair Avg$$' AS STRING) AS tag
      FROM company_months cm
      LEFT JOIN `gp-technologies-dev.silver.ltm_kpis_consolidate_group` cr 
        ON cm.company_new_name = cr.company_new_name 
       AND EXTRACT(YEAR FROM cm.month_date) = cr.year
       AND EXTRACT(MONTH FROM cm.month_date) = cr.month
     UNION ALL       
    SELECT cm.company_new_name
         , cm.middle_point
         , cm.month_date
         , COALESCE(cr.opportunity_to_pct_total, 0) AS total
         , cm.month_offset
         , CAST('Opportunity TO %' AS STRING) AS tag
      FROM company_months cm
      LEFT JOIN `gp-technologies-dev.silver.ltm_kpis_consolidate_group` cr 
        ON cm.company_new_name = cr.company_new_name 
       AND EXTRACT(YEAR FROM cm.month_date) = cr.year
       AND EXTRACT(MONTH FROM cm.month_date) = cr.month
     UNION ALL       
    SELECT cm.company_new_name
         , cm.middle_point
         , cm.month_date
         , COALESCE(cr.to_conversion_pct_total, 0) AS total
         , cm.month_offset
         , CAST('TO Conversion %' AS STRING) AS tag
      FROM company_months cm
      LEFT JOIN `gp-technologies-dev.silver.ltm_kpis_consolidate_group` cr 
        ON cm.company_new_name = cr.company_new_name 
       AND EXTRACT(YEAR FROM cm.month_date) = cr.year
       AND EXTRACT(MONTH FROM cm.month_date) = cr.month
     UNION ALL       
    SELECT cm.company_new_name
         , cm.middle_point
         , cm.month_date
         , COALESCE(cr.conversion_usd_avg_total, 0) AS total
         , cm.month_offset
         , CAST('Conversion $Avg' AS STRING) AS tag
      FROM company_months cm
      LEFT JOIN `gp-technologies-dev.silver.ltm_kpis_consolidate_group` cr 
        ON cm.company_new_name = cr.company_new_name 
       AND EXTRACT(YEAR FROM cm.month_date) = cr.year
       AND EXTRACT(MONTH FROM cm.month_date) = cr.month
     UNION ALL       
    SELECT cm.company_new_name
         , cm.middle_point
         , cm.month_date
         , COALESCE(cr.sj_mktestimates_total, 0) AS total
         , cm.month_offset
         , CAST('SJ MKTEstimates' AS STRING) AS tag
      FROM company_months cm
      LEFT JOIN `gp-technologies-dev.silver.ltm_kpis_consolidate_group` cr 
        ON cm.company_new_name = cr.company_new_name 
       AND EXTRACT(YEAR FROM cm.month_date) = cr.year
       AND EXTRACT(MONTH FROM cm.month_date) = cr.month
     UNION ALL       
    SELECT cm.company_new_name
         , cm.middle_point
         , cm.month_date
         , COALESCE(cr.sj_mkte_conv_pct_total, 0) AS total
         , cm.month_offset
         , CAST('SJ MKTE Conv %' AS STRING) AS tag
      FROM company_months cm
      LEFT JOIN `gp-technologies-dev.silver.ltm_kpis_consolidate_group` cr 
        ON cm.company_new_name = cr.company_new_name 
       AND EXTRACT(YEAR FROM cm.month_date) = cr.year
       AND EXTRACT(MONTH FROM cm.month_date) = cr.month
     UNION ALL       
    SELECT cm.company_new_name
         , cm.middle_point
         , cm.month_date
         , COALESCE(cr.sj_mkte_conv_usd_total, 0) AS total
         , cm.month_offset
         , CAST('SJ MKTE Conv $' AS STRING) AS tag
      FROM company_months cm
      LEFT JOIN `gp-technologies-dev.silver.ltm_kpis_consolidate_group` cr 
        ON cm.company_new_name = cr.company_new_name 
       AND EXTRACT(YEAR FROM cm.month_date) = cr.year
       AND EXTRACT(MONTH FROM cm.month_date) = cr.month
     UNION ALL       
         SELECT cm.company_new_name
         , cm.middle_point
         , cm.month_date
         , COALESCE(cr.airflow_prj_mix_pct_total, 0) AS total
         , cm.month_offset
         , CAST('Airflow PRJ MIX %' AS STRING) AS tag
      FROM company_months cm
      LEFT JOIN `gp-technologies-dev.silver.ltm_kpis_consolidate_group` cr 
        ON cm.company_new_name = cr.company_new_name 
       AND EXTRACT(YEAR FROM cm.month_date) = cr.year
       AND EXTRACT(MONTH FROM cm.month_date) = cr.month
     UNION ALL       
    SELECT cm.company_new_name
         , cm.middle_point
         , cm.month_date
         , COALESCE(cr.af_prj_avg_usd_total, 0) AS total
         , cm.month_offset
         , CAST('AF PRJ AVG $' AS STRING) AS tag
      FROM company_months cm
      LEFT JOIN `gp-technologies-dev.silver.ltm_kpis_consolidate_group` cr 
        ON cm.company_new_name = cr.company_new_name 
       AND EXTRACT(YEAR FROM cm.month_date) = cr.year
       AND EXTRACT(MONTH FROM cm.month_date) = cr.month
     UNION ALL       
     SELECT cm.company_new_name
         , cm.middle_point
         , cm.month_date
         , COALESCE(cr.equip_mix_pct_total, 0) AS total
         , cm.month_offset
         , CAST('Equip MIX %' AS STRING) AS tag
      FROM company_months cm
      LEFT JOIN `gp-technologies-dev.silver.ltm_kpis_consolidate_group` cr 
        ON cm.company_new_name = cr.company_new_name 
       AND EXTRACT(YEAR FROM cm.month_date) = cr.year
       AND EXTRACT(MONTH FROM cm.month_date) = cr.month
     UNION ALL       
    SELECT cm.company_new_name
         , cm.middle_point
         , cm.month_date
         , COALESCE(cr.equip_avg_usd_total, 0) AS total
         , cm.month_offset
         , CAST('Equip AVG $' AS STRING) AS tag
      FROM company_months cm
      LEFT JOIN `gp-technologies-dev.silver.ltm_kpis_consolidate_group` cr 
        ON cm.company_new_name = cr.company_new_name 
       AND EXTRACT(YEAR FROM cm.month_date) = cr.year
       AND EXTRACT(MONTH FROM cm.month_date) = cr.month
     UNION ALL       
    SELECT cm.company_new_name
         , cm.middle_point
         , cm.month_date
         , COALESCE(cr.svc_prj_pct_total, 0) AS total
         , cm.month_offset
         , CAST('SVC PRJ %' AS STRING) AS tag
      FROM company_months cm
      LEFT JOIN `gp-technologies-dev.silver.ltm_kpis_consolidate_group` cr 
        ON cm.company_new_name = cr.company_new_name 
       AND EXTRACT(YEAR FROM cm.month_date) = cr.year
       AND EXTRACT(MONTH FROM cm.month_date) = cr.month
     UNION ALL 
    SELECT cm.company_new_name
         , cm.middle_point
         , cm.month_date
         , COALESCE(cr.svc_prj_avg_usd_total, 0) AS total
         , cm.month_offset
         , CAST('SVC PRJ AVG$' AS STRING) AS tag
      FROM company_months cm
      LEFT JOIN `gp-technologies-dev.silver.ltm_kpis_consolidate_group` cr 
        ON cm.company_new_name = cr.company_new_name 
       AND EXTRACT(YEAR FROM cm.month_date) = cr.year
       AND EXTRACT(MONTH FROM cm.month_date) = cr.month
)
--select * from ltm_kpis_data WHERE company_new_name = "Shape DEAR - Dear Services";
-- Filas a columnas con el punto medio siempre en la posición central
SELECT * FROM (
    SELECT company_new_name
         , middle_point
         , tag
         , month_offset
         , SUM(total) AS total
      FROM ltm_kpis_data
     GROUP BY company_new_name, middle_point, tag, month_offset 
     ORDER BY middle_point, company_new_name, tag, month_offset 
) 
PIVOT (
    SUM(total) 
    FOR month_offset IN (
        -12 AS `-12`, -11 AS `-11`, -10 AS `-10`, -9 AS `-9`, -8 AS `-8`, -7 AS `-7`,
         -6 AS `-6`,   -5 AS  `-5`,  -4 AS  `-4`, -3 AS `-3`, -2 AS `-2`, -1 AS `-1`,
          0 AS  `0`,    1 AS   `1`,   2 AS   `2`,  3 AS  `3`,  4 AS  `4`,  5 AS  `5`,  
          6 AS  `6`,    7 AS   `7`,   8 AS   `8`,  9 AS  `9`, 10 AS `10`, 11 AS `11`
    )
)
ORDER BY middle_point,company_new_name
);

/*
CREATE OR REPLACE VIEW gp-technologies-dev.gold.dashboard_ltm_kpis AS (
SELECT company_new_name AS `Company Name` 
     , FORMAT_DATE("%m/%d/%Y", middle_point) AS `Platform Join Date`
     , tag 
     , CASE WHEN `-12` = CAST(`-12` AS INT64) THEN FORMAT("%'.d", CAST(`-12` AS INT64))
       ELSE FORMAT("%.2f", CAST(`-12` AS FLOAT64)) END AS `-12`
     , CASE WHEN `-11` = CAST(`-11` AS INT64) THEN FORMAT("%'.d", CAST(`-11` AS INT64))
       ELSE FORMAT("%.2f", CAST(`-11` AS FLOAT64)) END AS `-11`       
     , CASE WHEN `-10` = CAST(`-10` AS INT64) THEN FORMAT("%'.d", CAST(`-10` AS INT64))
       ELSE FORMAT("%.2f", CAST(`-10` AS FLOAT64)) END AS `-10`       
     , CASE WHEN `-9` = CAST(`-9` AS INT64) THEN FORMAT("%'.d", CAST(`-9` AS INT64))
       ELSE FORMAT("%.2f", CAST(`-9` AS FLOAT64)) END AS `-9`
     , CASE WHEN `-8` = CAST(`-8` AS INT64) THEN FORMAT("%'.d", CAST(`-8` AS INT64))
       ELSE FORMAT("%.2f", CAST(`-8` AS FLOAT64)) END AS `-8`       
     , CASE WHEN `-7` = CAST(`-7` AS INT64) THEN FORMAT("%'.d", CAST(`-7` AS INT64))
       ELSE FORMAT("%.2f", CAST(`-7` AS FLOAT64)) END AS `-7`       
     , CASE WHEN `-6` = CAST(`-6` AS INT64) THEN FORMAT("%'.d", CAST(`-6` AS INT64))
       ELSE FORMAT("%.2f", CAST(`-6` AS FLOAT64)) END AS `-6`
     , CASE WHEN `-5` = CAST(`-5` AS INT64) THEN FORMAT("%'.d", CAST(`-5` AS INT64))
       ELSE FORMAT("%.2f", CAST(`-5` AS FLOAT64)) END AS `-5`       
     , CASE WHEN `-4` = CAST(`-4` AS INT64) THEN FORMAT("%'.d", CAST(`-4` AS INT64))
       ELSE FORMAT("%.2f", CAST(`-4` AS FLOAT64)) END AS `-4`       
     , CASE WHEN `-3` = CAST(`-3` AS INT64) THEN FORMAT("%'.d", CAST(`-3` AS INT64))
       ELSE FORMAT("%.2f", CAST(`-3` AS FLOAT64)) END AS `-3`
     , CASE WHEN `-2` = CAST(`-2` AS INT64) THEN FORMAT("%'.d", CAST(`-2` AS INT64))
       ELSE FORMAT("%.2f", CAST(`-2` AS FLOAT64)) END AS `-2`       
     , CASE WHEN `-1` = CAST(`-1` AS INT64) THEN FORMAT("%'.d", CAST(`-1` AS INT64))
       ELSE FORMAT("%.2f", CAST(`-1` AS FLOAT64)) END AS `-1`       
     , CASE WHEN `0` = CAST(`0` AS INT64) THEN FORMAT("%'.d", CAST(`0` AS INT64))
       ELSE FORMAT("%.2f", CAST(`0` AS FLOAT64)) END AS `0`
     , CASE WHEN `1` = CAST(`1` AS INT64) THEN FORMAT("%'.d", CAST(`1` AS INT64))
       ELSE FORMAT("%.2f", CAST(`1` AS FLOAT64)) END AS `1`       
     , CASE WHEN `2` = CAST(`2` AS INT64) THEN FORMAT("%'.d", CAST(`2` AS INT64))
       ELSE FORMAT("%.2f", CAST(`2` AS FLOAT64)) END AS `2`       
     , CASE WHEN `3` = CAST(`3` AS INT64) THEN FORMAT("%'.d", CAST(`3` AS INT64))
       ELSE FORMAT("%.2f", CAST(`3` AS FLOAT64)) END AS `3`
     , CASE WHEN `4` = CAST(`4` AS INT64) THEN FORMAT("%'.d", CAST(`4` AS INT64))
       ELSE FORMAT("%.2f", CAST(`4` AS FLOAT64)) END AS `4`       
     , CASE WHEN `5` = CAST(`5` AS INT64) THEN FORMAT("%'.d", CAST(`5` AS INT64))
       ELSE FORMAT("%.2f", CAST(`5` AS FLOAT64)) END AS `5`       
     , CASE WHEN `6` = CAST(`6` AS INT64) THEN FORMAT("%'.d", CAST(`6` AS INT64))
       ELSE FORMAT("%.2f", CAST(`6` AS FLOAT64)) END AS `6`
     , CASE WHEN `7` = CAST(`7` AS INT64) THEN FORMAT("%'.d", CAST(`7` AS INT64))
       ELSE FORMAT("%.2f", CAST(`7` AS FLOAT64)) END AS `7`       
     , CASE WHEN `8` = CAST(`8` AS INT64) THEN FORMAT("%'.d", CAST(`8` AS INT64)) 
       ELSE FORMAT("%.2f", CAST(`8` AS FLOAT64)) END AS `8`
     , CASE WHEN `9` = CAST(`9` AS INT64) THEN FORMAT("%'.d", CAST(`9` AS INT64))
       ELSE FORMAT("%.2f", CAST(`9` AS FLOAT64)) END AS `9`
     , CASE WHEN `10` = CAST(`10` AS INT64) THEN FORMAT("%'.d", CAST(`10` AS INT64))
       ELSE FORMAT("%.2f", CAST(`10` AS FLOAT64)) END AS `10`       
     , CASE WHEN `11` = CAST(`11` AS INT64) THEN FORMAT("%'.d", CAST(`11` AS INT64))
       ELSE FORMAT("%.2f", CAST(`11` AS FLOAT64)) END AS `11`
     , FORMAT("%'.d", CAST((`-12`+`-11`+`-10`+`-9`+`-8`+`-7`+`-6`+`-5`+`-4`+`-3`+`-2`+`-1`) AS INT64)) AS `Before`
     , FORMAT("%'.d", CAST((`0`+`1`+`2`+`3`+`4`+`5`+`6`+`7`+`8`+`9`+`10`+`11`) AS INT64)) AS `After`
     , FORMAT("%'.d", CAST(((`0`+`1`+`2`+`3`+`4`+`5`+`6`+`7`+`8`+`9`+`10`+`11`)-(`-12`+`-11`+`-10`+`-9`+`-8`+`-7`+`-6`+`-5`+`-4`+`-3`+`-2`+`-1`)) AS INT64)) AS `Variance`
  FROM gp-technologies-dev.gold.dashboard_kpis
);
*/  
