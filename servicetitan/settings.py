import requests
from requests.auth import HTTPBasicAuth
import json
from datetime import datetime, timedelta

class ServiceTitanAuth:
    """
    Clase completa para Servicetitan
    """
    
    AUTH_URL = "https://auth-integration.servicetitan.io/connect/token"
#    BASE_API_URL = "https://api.servicetitan.io"
#    BASE_API_URL = "https://public-api-gateway.st.dev"
    BASE_API_URL = "https://api-integration.servicetitan.io"

#                   https://public-api-gateway.st.dev/jpm/v2/tenant/{tenant}/business-units
#           url = f"https://api-integration.servicetitan.io/jpm/v2/tenant/{self.credentials['tenant_id']}/business-units"

    
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
    
    def get_business_units(self) -> list:
        """Getting business-units"""
        token = self.get_access_token()
        #url = f"{self.BASE_API_URL}/jpm/v2/tenant/{self.credentials['tenant_id']}/business-units"
        tenant_id = self.credentials['tenant_id']
        url = f"{self.BASE_API_URL}/settings/v2/tenant/{tenant_id}/business-units"
        
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
    
    def export_results_to_file(self, filename: str = None) -> str:
        """
        Exporta el Result a un archivo JSON
        Args:
            filename: Nombre del archivo (opcional)
        Returns:
            str: Ruta del archivo generado
        """
        business_units = self.get_business_units()  # Obtenemos los business-units
        
        if not filename:
            # Generar nombre automático si no se especifica
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"servicetitan_business_units_{timestamp}.json"
        
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(business_units, f, ensure_ascii=False, indent=2)
            
            return f"business_units exportados correctamente a: {filename}"
            
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
        print("Obteniendo todos los business-units...")
        business_units = client.get_business_units()
        print(f"Se obtuvieron {len(business_units)} business-units")
        if business_units:
            print("\n BU:")
            #print(json.dumps(business_units, indent=2))

            print("\n2. Exportando a archivo...")
            result = client.export_results_to_file()
            print(f"✅ {result}")
        
            # Opcional: Mostrar ruta absoluta del archivo
            import os
            print(f"📁 Ruta completa: {os.path.abspath(result.split(': ')[1])}")

    except Exception as e:
        print(f"Error: {str(e)}")