import requests
from requests.auth import HTTPBasicAuth
import json
from datetime import datetime, timedelta

class ServiceTitanAuth:
    """
    Clase completa para autenticación y obtención de jobs
    """
    
    AUTH_URL = "https://auth-integration.servicetitan.io/connect/token"
#    BASE_API_URL = "https://api.servicetitan.io"
#    BASE_API_URL = "https://public-api-gateway.st.dev"
    BASE_API_URL = "https://api-integration.servicetitan.io"

#                   https://public-api-gateway.st.dev/jpm/v2/tenant/{tenant}/jobs
#           url = f"https://api-integration.servicetitan.io/jpm/v2/tenant/{self.credentials['tenant_id']}/jobs"

    
    def __init__(self, app_id: str, client_id: str, client_secret: str, tenant_id: str, app_key: str):
        self.credentials = {
            'app_id': app_id,
            'client_id': client_id,
            'client_secret': client_secret,
            'tenant_id': tenant_id,
            'app_key': app_key
        }
    
    def get_access_token(self) -> str:
        """Getting access token"""
        response = requests.post(
            self.AUTH_URL,
            auth=HTTPBasicAuth(self.credentials['client_id'], self.credentials['client_secret']),
            headers={
                'Content-Type': 'application/x-www-form-urlencoded',
                'ST-App-Key': self.credentials['app_key']
            },
            data={
                'grant_type': 'client_credentials',
                'client_id': self.credentials['client_id'],
                'client_secret': self.credentials['client_secret']
            }
        )
        response.raise_for_status()
        print(f"Token (truncado): {response.json()['access_token'][128]}...")
        return response.json()['access_token']
    
    def get_jobs(self) -> list:
        """Getting Jobs"""
        token = self.get_access_token()
        #url = f"{self.BASE_API_URL}/jpm/v2/tenant/{self.credentials['tenant_id']}/jobs"
        tenant_id = self.credentials['tenant_id']
        url = f"{self.BASE_API_URL}/jpm/v2/tenant/{tenant_id}/jobs"
        
        response = requests.get(
            url,
            headers={
                'Authorization': f'Bearer {token}',
                'ST-App-Id': self.credentials['app_id'],
                'ST-App-Key': self.credentials['app_key']
            }
        )
        response.raise_for_status()
        return response.json().get('data', [])
    
    def export_jobs_to_file(self, filename: str = None) -> str:
        """
        Exporta todos los jobs a un archivo JSON
        Args:
            filename: Nombre del archivo (opcional)
        Returns:
            str: Ruta del archivo generado
        """
        jobs = self.get_jobs()  # Obtenemos los jobs
        
        if not filename:
            # Generar nombre automático si no se especifica
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"servicetitan_jobs_{timestamp}.json"
        
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(jobs, f, ensure_ascii=False, indent=2)
            
            return f"Jobs exportados correctamente a: {filename}"
            
        except Exception as e:
            return f"Error al exportar: {str(e)}"

# Ejemplo de uso
if __name__ == "__main__":
    client = ServiceTitanAuth(
        app_id="9jxbbcf06a42i",
        client_id="cid.dtq2ekk9l23mnp70y3sowky89",
        client_secret="cs2.yk71kq7hj0xyi3x5bd1syl0xazjxm344crle3mkxvripg0m80g",
        tenant_id="1270943139",
        app_key="ak1.8a2vhmlnvi1vzi17py5haw03w"
    )
    
    try:
        print("Obteniendo todos los jobs...")
        jobs = client.get_jobs()
        print(f"Se obtuvieron {len(jobs)} jobs")
        if jobs:
            print("\n Job #1:")
            #print(json.dumps(jobs, indent=2))

            print("\n2. Exportando a archivo...")
            result = client.export_jobs_to_file()
            print(f"✅ {result}")
        
            # Opcional: Mostrar ruta absoluta del archivo
            import os
            print(f"📁 Ruta completa: {os.path.abspath(result.split(': ')[1])}")

    except Exception as e:
        print(f"Error: {str(e)}")