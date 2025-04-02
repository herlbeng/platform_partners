from google.cloud import storage
from google.cloud import bigquery
import json
import os

# Configura las credenciales (solo necesario si ejecutas localmente)
# Descarga el archivo JSON de credenciales desde Google Cloud Console
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "tu-archivo-credenciales.json"

def load_json_to_bigquery(bucket_name, blob_name, dataset_id, table_id):
    """Transforma y carga el JSON a BigQuery"""
    
    try:
        # Inicializar clientes
        storage_client = storage.Client()
        bq_client = bigquery.Client()
        
        # 1. Obtener el archivo de Cloud Storage
        bucket = storage_client.bucket(bucket_name)
        blob = bucket.blob(blob_name)
        json_data = json.loads(blob.download_as_string())
        
        # 2. Convertir a formato newline-delimited JSON
        ndjson = '\n'.join([json.dumps(item) for item in json_data])
        
        # 3. Configurar el job de carga
        table_ref = bq_client.dataset(dataset_id).table(table_id)
        
        job_config = bigquery.LoadJobConfig(
            source_format=bigquery.SourceFormat.NEWLINE_DELIMITED_JSON,
            autodetect=True  # BigQuery detectará el esquema automáticamente
        )
        
        # 4. Cargar los datos
        load_job = bq_client.load_table_from_string(
            ndjson, table_ref, job_config=job_config
        )
        
        load_job.result()  # Espera a que complete
        
        # Verificar resultados
        table = bq_client.get_table(table_ref)
        return f"✅ Datos cargados en {dataset_id}.{table_id} - {table.num_rows} filas"
        
    except Exception as e:
        return f"❌ Error: {str(e)}"

# Ejemplo de uso
if __name__ == "__main__":
    result = load_json_to_bigquery(
        bucket_name="servicetitan_tests",
        blob_name="servicetitan_business_units_20250401_142840.json",
        dataset_id="servicetitan",
        table_id="business_units"
    )
    print(result)