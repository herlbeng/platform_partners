import requests
from requests.auth import HTTPBasicAuth
import json
from datetime import datetime, timedelta  # Importación corregida
from typing import Dict, List, Optional  # Asegúrate de importar List

class ServiceTitanAuth:
    """
    Clase para manejar la autenticación con ServiceTitan API
    Versión: 2.0 (Optimizada basada en solución confirmada)
    """
    
    AUTH_URL = "https://auth-integration.servicetitan.io/connect/token"
    
    def __init__(self, app_id: str, client_id: str, client_secret: str, tenant_id: str):
        """
        Inicializa con credenciales de ServiceTitan
        
        Args:
            app_id: ID de la aplicación
            client_id: Client ID para OAuth
            client_secret: Client Secret para OAuth
            tenant_id: ID del inquilino (tenant)
        """
        print(f"tenant_id: {tenant_id}")

        self.credentials = {
            'app_id': app_id,
            'client_id': client_id,
            'client_secret': client_secret,
            'tenant_id': tenant_id
        }
        self._last_response = None

    def get_access_token(self, verbose: bool = False) -> str:
        """
        Obtiene token de acceso de ServiceTitan API
        
        Args:
            verbose: Si True, muestra detalles de la solicitud
            
        Returns:
            str: Token de acceso
        """
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'ST-App-Id': self.credentials['app_id']
        }
        
        data = {
            'grant_type': 'client_credentials',
            'client_id': self.credentials['client_id'],
            'client_secret': self.credentials['client_secret']
        }
        
        auth = HTTPBasicAuth(
            self.credentials['client_id'], 
            self.credentials['client_secret']
        )
        
        try:
            response = requests.post(
                self.AUTH_URL,
                auth=auth,
                headers=headers,
                data=data,
                timeout=30
            )
            
            self._last_response = response
            
            if verbose:
                self._print_request_details(response)
            
            response.raise_for_status()
            
            return response.json()['access_token']
            
        except requests.exceptions.RequestException as e:
            error_msg = self._handle_error(e)
            raise Exception(error_msg) from e
    
    def _print_request_details(self, response: requests.Response) -> None:
        """Muestra detalles de la solicitud/respuesta"""
        print("\n=== SERVICE TITAN AUTH DEBUG ===")
        print(f"Endpoint: {self.AUTH_URL}")
        print("Headers:", json.dumps(dict(response.request.headers), indent=2))
        print("Body:", response.request.body)
        print(f"Status: {response.status_code}")
#        print("Response:", response.text)
        print(f"Token: {response.text[:50]}...")
        print("="*30 + "\n")
    
    def _handle_error(self, error: Exception) -> str:
        """Procesa errores y devuelve mensaje descriptivo"""
        if hasattr(self._last_response, 'json'):
            error_data = self._last_response.json()
            if 'error' in error_data:
                return (f"Error {self._last_response.status_code}: {error_data['error']}\n"
                       f"Description: {error_data.get('error_description', 'No details')}")
        
        return f"Error en la conexión: {str(error)}"
    
    #def get_jobs(self, verbose: bool = False) -> str:
    def get_jobs(self, verbose: bool = False) -> list:

        """Obtiene jobs de ServiceTitan API"""
        token = self.get_access_token()
        
        # URL corregida (nota el cambio en la estructura del path)
        endpoint = "jobs/v2/jobs"
        #url = f"https://api-integration.servicetitan.io/{endpoint}"
        url = f"https://api-integration.servicetitan.io/jpm/v2/tenant/{self.credentials['tenant_id']}/jobs"
            
        headers = {
            'Authorization': f'Bearer {token}',
            'ST-App-Id': self.credentials['app_id'],
            'Content-Type': 'application/json'
        }
        #        headers = {
#            'Content-Type': 'application/x-www-form-urlencoded',
#            'ST-App-Id': self.credentials['app_id']
#        }

        try:
            response = requests.get(
                url,
                headers=headers,
                timeout=30
            )
            
            self._last_response = response
            
            if verbose:
                print("\n=== REQUEST DETAILS ===")
                print(f"URL: {response.url}")
                print(f"Headers: {headers}")
                print(f"Status Code: {response.status_code}")
                print(f"Response: {response.text[:200]}...")  # Muestra solo parte de la respuesta
            
            response.raise_for_status()
            
            return response.json().get('data', [])
            
        except requests.exceptions.HTTPError as http_err:
            if response.status_code == 401:
                error_msg = "Error 401: Acceso denegado. Verifica:\n"
                error_msg += "1. Que el token sea válido\n"
                error_msg += "2. Que tu aplicación tenga los scopes necesarios para acceder a jobs\n"
                error_msg += "3. Que el tenant_id sea correcto\n"
                error_msg += f"Respuesta completa: {response.text}"
            else:
                error_msg = f"HTTP Error: {str(http_err)}"
            raise Exception(error_msg)
        except Exception as err:
            raise Exception(f"Error al obtener jobs: {str(err)}")
       
       
# Ejemplo de uso
if __name__ == "__main__":
    try:
        # Configuración (en producción usa variables de entorno o Secret Manager)
        config = {
            "app_id": "9jxbbcf06a42i",
            "client_id": "cid.dtq2ekk9l23mnp70y3sowky89",
            "client_secret": "cs2.yk71kq7hj0xyi3x5bd1syl0xazjxm344crle3mkxvripg0m80g",
            "tenant_id": "1270943139"
        }
        
        # Crear cliente de autenticación
        auth_client = ServiceTitanAuth(**config)
        
        # Obtener token (modo verbose=True para diagnóstico)
        #print("Obteniendo token de acceso...")
        #token = auth_client.get_access_token(verbose=True)
        #jobs = auth_client.get_jobs(verbose=True)

        # Ejemplo de uso del nuevo método get_jobs:
        print("\nObteniendo jobs modificados en los últimos 7 días...")
        seven_days_ago = (datetime.now() - timedelta(days=7)).strftime('%Y-%m-%d')
        jobs = auth_client.get_jobs(verbose=True)
        
        print(f"\n✅ Se obtuvieron {len(jobs)} jobs")
        if jobs:
            print("Primer job obtenido:")
            print(json.dumps(jobs[0], indent=2))
       
        print("\n✅ Autenticación exitosa")
        print(f"Token (truncado): {token[:50]}...")
        print(f"Longitud del token: {len(token)} caracteres")
        #print(f"Jobs:{jobs}")
        
    except Exception as e:
        print("\n❌ Error en la autenticación:")
        print(str(e))
        print("\nSolución:")
        print("1. Verifica que las credenciales sean correctas")
        print("2. Confirma que el tenant_id sea el adecuado")
        print("3. Verifica la conectividad a internet y firewalls")
        print("4. Revisa que la aplicación esté activa en ServiceTitan")