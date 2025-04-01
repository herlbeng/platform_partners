import os
import re
import pandas as pd

# Definir la carpeta de entrada y salida
input_folder = 'csv_raw'
output_folder = 'csv_clean'
os.makedirs(output_folder, exist_ok=True)

# Definir el encabezado correcto
valid_columns = ['key','month','region','rev_build_pc','payroll_pc','month_name','month_num','year','company_id','company_name','company_new_name','created_by','update_by','revenue_new_cust','revenue_ncust__trend','revenue_repeat_cust','revenue_rcust__trend','revenue_demand','revenue_maint','revenue_estimates','revenue_projects','revenue_total','revenue_pace','revenue_rev_trend','recurring_rev_pct_ncust_pct','recurring_rev_pct_reptd_cust_pct','field6_','field7_','single_jobs_new_cust','single_jobs_ncust__trend','single_jobs_new_cust_ib','single_jobs_new_cust_ob','single_jobs_r_cust_ob','single_jobs_r_cust_ib','single_jobs_r_cust_ib_pace','single_jobs_r_ib_trend','single_jobs_repeat_cust','single_jobs_demand','single_jobs_maint','single_jobs_total','single_jobs_pace','single_jobs_sj_trend','gba_new_cust','gba_r_cust','gba_demand','gba_maint','gba_actual','gba_pace','gba_trend','sold_estimates_actual','sold_estimates_pace','sold_estimates_trend','manpower_sj_qty','manpower_svc_avg','manpower_svc_pj_qty','manpower_svc_prj_avg','manpower_repl_pj_qty','manpower_installer_avg','sold_hours_sj_svc_sold_hours','sold_hours_sj_svc_rev_sold_hrs','sold_hours_sj_svc_worked_hrs','sold_hours_sj_svc_rev_worked_hrs','sold_hours_pj_svc_sold_hours','sold_hours_pj_svc_rev_sold_hrs','sold_hours_pj_svc_worked_hrs','sold_hours_pj_svc_rev_worked_hrs','sold_hours_repl_sold_hours','sold_hours_repl_rev_sold_hrs','sold_hours_repl_worked_hours','sold_hours_repl_rev_worked_hrs','sold_hours_total_sold_hrs','field8_','field9_','sj__usd_100_new_cust','sj__usd_100_repeat_cust','field10_','sj__usd_100_demand','sj__usd_100_maint','field11_','sj__usd_100_total','recalls_new_cust','recalls_repeat_cust','recalls_total_hide_','recalls_demand','field12_','field13_','recalls_total','sj_repair_pct_new_cust','sj_repair_pct_repeat_cust','sj_repair_pct_total_hide_','sj_repair_pct_demand','sj_repair_pct_maint','field14_','sj_repair_pct_total','sj_repair_avg_usd_new_cust','sj_repair_avg_usd_repeat_cust','sj_repair_avg_usd_total_hide_','sj_repair_avg_usd_demand','sj_repair_avg_usd_maint','field15_','sj_repair_avg_usd_total','opportunity_to_pct_new_cust','opportunity_to_pct_repeat_cust','opportunity_to_pct_total_hide_','opportunity_to_pct_demand','opportunity_to_pct_maint','opportunity_to_pct_est','opportunity_to_pct_total','to_conversion_pct_new_cust','to_conversion_pct_repeat_cust','to_conversion_pct_total_hide_','to_conversion_pct_demand','to_conversion_pct_maint','field16_','to_conversion_pct_total','conversion_usd_avg_new_cust','conversion_usd_avg_repeat_cust','conversion_usd_avg_total_hide_','conversion_usd_avg_demand','conversion_usd_avg_maint','field17_','conversion_usd_avg_total','sj_mktestimates_new_cust','sj_mktestimates_repeat_cust','sj_mktestimates_estimates','sj_mktestimates_total','sj_mktestimates_pace','sj_mktestimates_est_trend','sj_mkte_conv_pct_new_cust','sj_mkte_conv_pct_repeat_cust','sj_mkte_conv_pct_total_hide_','sj_mkte_conv_pct_demand','sj_mkte_conv_pct_maint','sj_mkte_conv_pct_estimates','sj_mkte_conv_pct_total','sj_mkte_conv_usd_new_cust','sj_mkte_conv_usd_repeat_cust','field18_','field19_','field20_','sj_mkte_conv_usd_estimates','sj_mkte_conv_usd_total','airflow_prj_mix_pct_new_cust','airflow_prj_mix_pct_repeat_cust','airflow_prj_mix_pct_total','airflow_prj_mix_pct_demand','airflow_prj_mix_pct_maintenance','airflow_prj_mix_pct_estimates','airflow_prj_mix_pct_total_hide_','af_prj_avg_usd_new_cust','af_prj_avg_usd_repeat_cust','af_prj_avg_usd_total','af_prj_avg_usd_count_prj_new','af_prj_avg_usd_count_prj_repeat','af_prj_avg_usd_total_prj','equip_mix_pct_new_cust','equip_mix_pct_repeat_cust','equip_mix_pct_total','equip_mix_pct_demand','equip_mix_pct_maint','equip_mix_pct_estimates','equip_mix_pct_total_hide_','equip_avg_usd_new_cust','equip_avg_usd_repeat_cust','equip_avg_usd_total','equip_avg_usd_demand','equip_avg_usd_maint','equip_avg_usd_estimates','equip_avg_usd_total_hide_','svc_prj_pct_new_cust','svc_prj_pct_repeat_cust','svc_prj_pct_total_hide_','svc_prj_pct_demand','svc_prj_pct_maint','svc_prj_pct_estimates','svc_prj_pct_total','svc_prj_avg_usd_new_cust','svc_prj_avg_usd_repeat_cust','svc_prj_avg_usd_total_hide_','svc_prj_avg_usd_demand','svc_prj_avg_usd_maint','svc_prj_avg_usd_estimates','svc_prj_avg_usd_total','tab_title','last_field_hide_']
#valid_columns = 'key,month,region,rev_build_pc,payroll_pc,month_name,month_num,year,company_id,company_name,company_new_name,created_by,update_by,revenue_new_cust,revenue_ncust__trend,revenue_repeat_cust,revenue_rcust__trend,revenue_demand,revenue_maint,revenue_estimates,revenue_projects,revenue_total,revenue_pace,revenue_rev_trend,recurring_rev_pct_ncust_pct,recurring_rev_pct_reptd_cust_pct,field6_,field7_,single_jobs_new_cust,single_jobs_ncust__trend,single_jobs_new_cust_ib,single_jobs_new_cust_ob,single_jobs_r_cust_ob,single_jobs_r_cust_ib,single_jobs_r_cust_ib_pace,single_jobs_r_ib_trend,single_jobs_repeat_cust,single_jobs_demand,single_jobs_maint,single_jobs_total,single_jobs_pace,single_jobs_sj_trend,gba_new_cust,gba_r_cust,gba_demand,gba_maint,gba_actual,gba_pace,gba_trend,sold_estimates_actual,sold_estimates_pace,sold_estimates_trend,manpower_sj_qty,manpower_svc_avg,manpower_svc_pj_qty,manpower_svc_prj_avg,manpower_repl_pj_qty,manpower_installer_avg,sold_hours_sj_svc_sold_hours,sold_hours_sj_svc_rev_sold_hrs,sold_hours_sj_svc_worked_hrs,sold_hours_sj_svc_rev_worked_hrs,sold_hours_pj_svc_sold_hours,sold_hours_pj_svc_rev_sold_hrs,sold_hours_pj_svc_worked_hrs,sold_hours_pj_svc_rev_worked_hrs,sold_hours_repl_sold_hours,sold_hours_repl_rev_sold_hrs,sold_hours_repl_worked_hours,sold_hours_repl_rev_worked_hrs,sold_hours_total_sold_hrs,field8_,field9_,sj__usd_100_new_cust,sj__usd_100_repeat_cust,field10_,sj__usd_100_demand,sj__usd_100_maint,field11_,sj__usd_100_total,recalls_new_cust,recalls_repeat_cust,recalls_total_hide_,recalls_demand,field12_,field13_,recalls_total,sj_repair_pct_new_cust,sj_repair_pct_repeat_cust,sj_repair_pct_total_hide_,sj_repair_pct_demand,sj_repair_pct_maint,field14_,sj_repair_pct_total,sj_repair_avg_usd_new_cust,sj_repair_avg_usd_repeat_cust,sj_repair_avg_usd_total_hide_,sj_repair_avg_usd_demand,sj_repair_avg_usd_maint,field15_,sj_repair_avg_usd_total,opportunity_to_pct_new_cust,opportunity_to_pct_repeat_cust,opportunity_to_pct_total_hide_,opportunity_to_pct_demand,opportunity_to_pct_maint,opportunity_to_pct_est,opportunity_to_pct_total,to_conversion_pct_new_cust,to_conversion_pct_repeat_cust,to_conversion_pct_total_hide_,to_conversion_pct_demand,to_conversion_pct_maint,field16_,to_conversion_pct_total,conversion_usd_avg_new_cust,conversion_usd_avg_repeat_cust,conversion_usd_avg_total_hide_,conversion_usd_avg_demand,conversion_usd_avg_maint,field17_,conversion_usd_avg_total,sj_mktestimates_new_cust,sj_mktestimates_repeat_cust,sj_mktestimates_estimates,sj_mktestimates_total,sj_mktestimates_pace,sj_mktestimates_est_trend,sj_mkte_conv_pct_new_cust,sj_mkte_conv_pct_repeat_cust,sj_mkte_conv_pct_total_hide_,sj_mkte_conv_pct_demand,sj_mkte_conv_pct_maint,sj_mkte_conv_pct_estimates,sj_mkte_conv_pct_total,sj_mkte_conv_usd_new_cust,sj_mkte_conv_usd_repeat_cust,field18_,field19_,field20_,sj_mkte_conv_usd_estimates,sj_mkte_conv_usd_total,airflow_prj_mix_pct_new_cust,airflow_prj_mix_pct_repeat_cust,airflow_prj_mix_pct_total,airflow_prj_mix_pct_demand,airflow_prj_mix_pct_maintenance,airflow_prj_mix_pct_estimates,airflow_prj_mix_pct_total_hide_,af_prj_avg_usd_new_cust,af_prj_avg_usd_repeat_cust,af_prj_avg_usd_total,af_prj_avg_usd_count_prj_new,af_prj_avg_usd_count_prj_repeat,af_prj_avg_usd_total_prj,equip_mix_pct_new_cust,equip_mix_pct_repeat_cust,equip_mix_pct_total,equip_mix_pct_demand,equip_mix_pct_maint,equip_mix_pct_estimates,equip_mix_pct_total_hide_,equip_avg_usd_new_cust,equip_avg_usd_repeat_cust,equip_avg_usd_total,equip_avg_usd_demand,equip_avg_usd_maint,equip_avg_usd_estimates,equip_avg_usd_total_hide_,svc_prj_pct_new_cust,svc_prj_pct_repeat_cust,svc_prj_pct_total_hide_,svc_prj_pct_demand,svc_prj_pct_maint,svc_prj_pct_estimates,svc_prj_pct_total,svc_prj_avg_usd_new_cust,svc_prj_avg_usd_repeat_cust,svc_prj_avg_usd_total_hide_,svc_prj_avg_usd_demand,svc_prj_avg_usd_maint,svc_prj_avg_usd_estimates,svc_prj_avg_usd_total,tab_title,last_field_hide_'
#new_header = valid_columns.split()

float_start_col = 13  # Índice de la primera columna a convertir
float_end_col = 182  # Índice de la última columna a convertir

# Función para limpiar y convertir valores
def clean_and_convert(value):
    if isinstance(value, str):
        # Eliminar símbolos de moneda y separadores de miles
        if "$" in value:
            value = value.replace("$", "").replace(",", "")
        # Convertir porcentajes a decimales
        if "%" in value:
            value = value.replace("%", "")
            return float(value) / 100
        # Convertir a float si es un número
        try:
            return float(value)
        except ValueError:
            return pd.NA  # Si no se puede convertir, devolver NaN
    return value  # Si no es una cadena, devolver el valor original

# Recorrer archivos CSV en la carpeta de entrada
for filename in os.listdir(input_folder):
    if filename.endswith('.csv'):
        input_path = os.path.join(input_folder, filename)
        clean_filename = filename.replace('_', '').replace('LTM', '').replace('KPIS', '').replace('2023', '').replace('2024', '').replace('2025', '').replace('&', ' AND ')
        final_filename = re.sub(r"\s", "_", clean_filename).upper()
        output_path = os.path.join(output_folder, final_filename)
        
        # Cargar archivo CSV
        df = pd.read_csv(input_path, header=None)
        
        # Asignar el encabezado correcto solo a las primeras 185 columnas
        #df.columns = valid_columns #list(df.columns[len(new_header):])

        # Si el archivo tiene más columnas que valid_columns, truncar o rellenar
        if len(df.columns) > len(valid_columns):
            # Truncar las columnas adicionales
            df = df.iloc[:, :len(valid_columns)]
        elif len(df.columns) < len(valid_columns):
            # Rellenar con columnas adicionales (por ejemplo, con NaN)
            for i in range(len(df.columns), len(valid_columns)):
                df[i] = None

        # Asignar los nombres de las columnas válidas
        df.columns = valid_columns
        
        # Buscar la primera fila que contenga 'KEY'
        first_line = df[df.apply(lambda row: row.astype(str).str.contains('KEY', case=False, na=False).any(), axis=1)].index
        if not first_line.empty:
            df = df.loc[first_line[0] + 1:]  # Esto elimina también la fila donde aparece 'KEY'
        else:
            continue  # Si no se encuentra 'KEY', pasar al siguiente archivo

        # Convertir el rango de columnas a numérico (float)    ESTO NO FUNCIONO PARA $ Y %
        #for col in df.columns[float_start_col:float_end_col + 1]:  # +1 para incluir la última columna
        #    df[col] = pd.to_numeric(df[col], errors="coerce")     

        # Limpiar y convertir el rango de columnas a numérico
        for col in df.columns[float_start_col:float_end_col]:  # +1 para incluir la última columna
            df[col] = df[col].apply(clean_and_convert)                   

        # Eliminar columnas después de la 185
        df = df.iloc[:, :185]

        # Guardar archivo limpio
        df.to_csv(output_path, index=False, encoding='utf-8')
        print(f"✅ Archivo '{input_path}' procesado en {output_path}")


print('Procesamiento completado. Archivos guardados en:', output_folder)

