ltm_fields_array = [
    ('revenue_new_cust','Revenue New Cust'),
    ('revenue_ncust__trend','Revenue NCust  Trend'),
    ('revenue_repeat_cust','Revenue Repeat Cust'),
    ('revenue_rcust__trend','Revenue RCust  Trend'),
    ('revenue_demand','Revenue Demand'),
    ('revenue_maint','Revenue Maint'),
    ('revenue_estimates','Revenue Estimates'),
    ('revenue_projects','Revenue Projects'),
    ('revenue_total','Revenue TOTAL'),
    ('revenue_pace','Revenue PACE'),
    ('revenue_rev_trend','Revenue Rev Trend'),
    ('single_jobs_new_cust','Single Jobs New Cust'),
    ('single_jobs_ncust__trend','Single Jobs NCust  Trend'),
    ('single_jobs_new_cust_ib','Single Jobs New Cust IB'),
    ('single_jobs_new_cust_ob','Single Jobs New Cust OB'),
    ('single_jobs_r_cust_ob','Single Jobs R Cust OB'),
    ('single_jobs_r_cust_ib','Single Jobs R Cust IB'),
    ('single_jobs_r_cust_ib_pace','Single Jobs R Cust IB PACE'),
    ('single_jobs_r_ib_trend','Single Jobs R IB Trend'),
    ('single_jobs_repeat_cust','Single Jobs Repeat Cust'),
    ('single_jobs_demand','Single Jobs Demand'),
    ('single_jobs_maint','Single Jobs Maint'),
    ('single_jobs_total','Single Jobs Total'),
    ('single_jobs_pace','Single Jobs PACE'),
    ('single_jobs_sj_trend','Single Jobs SJ Trend'),
    ('gba_new_cust','GBA New Cust'),
    ('gba_r_cust','GBA Repeat Cust'),
    ('gba_demand','GBA Demand'),
    ('gba_maint','GBA Maint'),
    ('gba_actual','GBA actual'),
    ('gba_pace','GBA pace'),
    ('gba_trend','GBA Trend'),
    ('sold_estimates_actual','SOLD ESTIMATES Actual'),
    ('sold_estimates_pace','SOLD ESTIMATES PACE'),
    ('sold_estimates_trend','SOLD ESTIMATES Trend'),
    ('manpower_sj_qty','MANPOWER SJ Qty'),
    ('manpower_svc_avg','MANPOWER Svc Avg'),
    ('manpower_svc_pj_qty','MANPOWER Svc Pj Qty'),
    ('manpower_svc_prj_avg','MANPOWER Svc Prj Avg'),
    ('manpower_repl_pj_qty','MANPOWER Repl Pj Qty'),
    ('manpower_installer_avg','MANPOWER Installer Avg'),
    ('sold_hours_total_sold_hrs','SOLD HOURS Total Sold Hrs'),
    ('sj__usd_100_new_cust','SJ<$100 New Cust'),
    ('sj__usd_100_repeat_cust','SJ<$100 Repeat Cust'),
    ('sj__usd_100_demand','SJ<$100 Demand'),
    ('sj__usd_100_maint','SJ<$100 Maint'),
    ('sj__usd_100_total','SJ<$100 Total'),
    ('recalls_total','Recalls Total'),
    ('sj_repair_pct_new_cust','SJ Repair % New Cust'),
    ('sj_repair_pct_repeat_cust','SJ Repair % Repeat Cust'),
    ('sj_repair_pct_demand','SJ Repair % Demand'),
    ('sj_repair_pct_maint','SJ Repair % Maint'),
    ('sj_repair_pct_total','SJ Repair % Total'),
    ('sj_repair_avg_usd_new_cust','SJ Repair Avg$$ New Cust'),
    ('sj_repair_avg_usd_repeat_cust','SJ Repair Avg$$ Repeat Cust'),
    ('sj_repair_avg_usd_demand','SJ Repair Avg$$ Demand'),
    ('sj_repair_avg_usd_maint','SJ Repair Avg$$ Maint'),
    ('sj_repair_avg_usd_total','SJ Repair Avg$$ Total'),
    ('opportunity_to_pct_new_cust','Opportunity TO % New Cust'),
    ('opportunity_to_pct_repeat_cust','Opportunity TO % Repeat Cust'),
    ('opportunity_to_pct_demand','Opportunity TO % Demand'),
    ('opportunity_to_pct_maint','Opportunity TO % Maint'),
    ('opportunity_to_pct_est','Opportunity TO % Est'),
    ('opportunity_to_pct_total','Opportunity TO % Total'),
    ('to_conversion_pct_new_cust','TO Conversion % New Cust'),
    ('to_conversion_pct_repeat_cust','TO Conversion % Repeat Cust'),
    ('to_conversion_pct_demand','TO Conversion % Demand'),
    ('to_conversion_pct_maint','TO Conversion % Maint'),
    ('to_conversion_pct_total','TO Conversion % Total'),
    ('conversion_usd_avg_new_cust','Conversion $AVG New Cust'),
    ('conversion_usd_avg_repeat_cust','Conversion $AVG Repeat Cust'),
    ('conversion_usd_avg_demand','Conversion $AVG Demand'),
    ('conversion_usd_avg_maint','Conversion $AVG Maint'),
    ('conversion_usd_avg_total','Conversion $AVG Total'),
    ('sj_mktestimates_new_cust','SJ MKTEstimates New Cust'),
    ('sj_mktestimates_repeat_cust','SJ MKTEstimates Repeat Cust'),
    ('sj_mktestimates_estimates','SJ MKTEstimates Estimates'),
    ('sj_mktestimates_total','SJ MKTEstimates Total'),
    ('sj_mktestimates_pace','SJ MKTEstimates PACE'),
    ('sj_mktestimates_est_trend','SJ MKTEstimates SJ Trend'),
    ('sj_mkte_conv_pct_new_cust','SJ MKTE Conv % New Cust'),
    ('sj_mkte_conv_pct_repeat_cust','SJ MKTE Conv % Repeat Cust'),
    ('sj_mkte_conv_pct_total','SJ MKTE Conv % Total'),
    ('sj_mkte_conv_usd_new_cust','SJ MKTE Conv $ New Cust'),
    ('sj_mkte_conv_usd_repeat_cust','SJ MKTE Conv $ Repeat Cust'),
    ('sj_mkte_conv_usd_estimates','SJ MKTE Conv $ Estimates'),
    ('sj_mkte_conv_usd_total','SJ MKTE Conv $ Total'),
    ('airflow_prj_mix_pct_new_cust','Airflow PRJ MIX % New Cust'),
    ('airflow_prj_mix_pct_repeat_cust','Airflow PRJ MIX % Repeat Cust'),
    ('airflow_prj_mix_pct_total','Airflow PRJ MIX % Total'),
    ('af_prj_avg_usd_new_cust','AF PRJ AVG $ New Cust'),
    ('af_prj_avg_usd_repeat_cust','AF PRJ AVG $ Repeat Cust'),
    ('af_prj_avg_usd_total','AF PRJ AVG $ Total'),
    ('equip_mix_pct_new_cust','Equip MIX % New Cust'),
    ('equip_mix_pct_repeat_cust','Equip MIX % Repeat Cust'),
    ('equip_mix_pct_total','Equip MIX % Total'),
    ('equip_avg_usd_new_cust','Equip AVG $ New Cust'),
    ('equip_avg_usd_repeat_cust','Equip AVG $ Repeat Cust'),
    ('equip_avg_usd_total','Equip AVG $ Total'),
    ('svc_prj_pct_new_cust','SVC PRJ % New Cust'),
    ('svc_prj_pct_repeat_cust','SVC PRJ % Repeat Cust'),
    ('svc_prj_pct_total','SVC PRJ % Total'),
    ('svc_prj_avg_usd_new_cust','SVC PRJ AVG $ New Cust'),
    ('svc_prj_avg_usd_repeat_cust','SVC PRJ AVG $ Repeat Cust'),
    ('svc_prj_avg_usd_total','SVC PRJ AVG $ Total'),
]

'''
MUESTRA:

Parte Externa de la vista: 

SELECT LTM.company_new_name
     , C.company_join_date AS middle_point
     , LTM.year AS year
     , LTM.month_num AS month
     , LTM.revenue_total
     , LTM.single_jobs_total
     , LTM.gba_pace
     , LTM.sold_estimates_pace
     , LTM.manpower_sj_qty, LTM.manpower_svc_pj_qty, LTM.manpower_repl_pj_qty
     , LTM.sold_hours_total_sold_hrs
     , LTM.sj__usd_100_total
     , LTM.recalls_total
     , LTM.sj_repair_pct_total
     , LTM.sj_repair_avg_usd_total
     , LTM.opportunity_to_pct_total
     , LTM.to_conversion_pct_total
     , LTM.conversion_usd_avg_total
     , LTM.sj_mktestimates_total
     , LTM.sj_mkte_conv_pct_total
     , LTM.sj_mkte_conv_usd_total
     , LTM.airflow_prj_mix_pct_total
     , LTM.af_prj_avg_usd_total
     , LTM.equip_mix_pct_total
     , LTM.equip_avg_usd_total
     , LTM.svc_prj_pct_total
     , LTM.svc_prj_avg_usd_total

Parte Interna de la vista:      

       SELECT company_new_name
            , year
            , month_num
            , SUM(revenue_total) AS revenue_total
            , ROUND(SUM(single_jobs_total),0) AS single_jobs_total
            , SUM(gba_pace) AS gba_pace
            , SUM(sold_estimates_pace) AS sold_estimates_pace
            , ROUND(SUM(manpower_sj_qty),0) AS manpower_sj_qty, ROUND(SUM(manpower_svc_pj_qty),0) AS manpower_svc_pj_qty, ROUND(SUM(manpower_repl_pj_qty),0) AS manpower_repl_pj_qty
            , ROUND(SUM(sold_hours_total_sold_hrs),0) AS sold_hours_total_sold_hrs
            , ROUND(SUM(sj__usd_100_total),0) AS sj__usd_100_total
            , ROUND(SUM(recalls_total),0) AS recalls_total
            , SUM(sj_repair_pct_total)*100 AS sj_repair_pct_total
            , SUM(sj_repair_avg_usd_total) AS sj_repair_avg_usd_total
            , SUM(opportunity_to_pct_total)*100 AS opportunity_to_pct_total
            , SUM(to_conversion_pct_total)*100 AS to_conversion_pct_total
            , SUM(conversion_usd_avg_total) AS conversion_usd_avg_total
            , ROUND(SUM(sj_mktestimates_total),0) AS sj_mktestimates_total
            , SUM(sj_mkte_conv_pct_total)*100 AS sj_mkte_conv_pct_total
            , SUM(sj_mkte_conv_usd_total) AS sj_mkte_conv_usd_total
            , SUM(airflow_prj_mix_pct_total)*100 AS airflow_prj_mix_pct_total
            , SUM(af_prj_avg_usd_total) AS af_prj_avg_usd_total
            , SUM(equip_mix_pct_total)*100 AS equip_mix_pct_total
            , SUM(equip_avg_usd_total) AS equip_avg_usd_total
            , SUM(svc_prj_pct_total)*100 AS svc_prj_pct_total
            , SUM(svc_prj_avg_usd_total) AS svc_prj_avg_usd_total
'''

select_parts_externa = []

for field, alias in ltm_fields_array:
    select_parts_externa.append(f"LTM.{field} AS {field}")

final_sql_externo = f"""
SELECT LTM.company_new_name
     , C.company_join_date AS middle_point
     , LTM.year AS year
     , LTM.month_num AS month
    {'\n, '.join(select_parts_externa)}
"""

with open('lista_field_vista_externa.txt', 'w', encoding='utf-8') as file:
    file.write(f"{final_sql_externo}")


select_parts_interna = []

for field, alias in ltm_fields_array:
    if "pct" in field:
        select_part = f"(SUM({field})*100) AS {field}"
    elif "usd" in field:
        select_part = f"ROUND(SUM({field}),0) AS {field}"
    else:
        select_part = f"SUM({field}) AS {field}"
    select_parts_interna.append(select_part)

final_sql_interno = f"""
       SELECT company_new_name
            , year
            , month_num
            {'\n, '.join(select_parts_interna)}            
"""    

with open('lista_field_vista_interna.txt', 'w', encoding='utf-8') as file:
    file.write(f"{final_sql_interno}")


