import requests
from requests.auth import HTTPBasicAuth
import json

auth_url = f"https://auth-integration.servicetitan.io/connect/token"

def get_service_titan_token(app_id, client_id, client_secret):
    """
    Obtiene token de acceso de ServiceTitan API
    Basado en la conexión exitosa que lograste con cURL
    """
    #auth_url = "https://auth.servicetitan.io/connect/token"
    
    # Configuración que funciona (basada en tu cURL exitoso)
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'ST-App-Id': app_id
    }
    
    # Parámetros que funcionan en tu cURL
    data = {
        'grant_type': 'client_credentials',
        'scope': 'api'  # Scope que funciona en tu cURL
    }
    
    # Autenticación Basic Auth
    auth = HTTPBasicAuth(client_id, client_secret)
    
    try:
        response = requests.post(
            auth_url,
            auth=auth,
            headers=headers,
            data=data,
            timeout=30
        )
        
        # Mostrar detalles para diagnóstico
        print("\n=== Detalles de la Solicitud ===")
        print(f"URL: {auth_url}")
        print(f"Headers: {json.dumps(dict(headers), indent=2)}")
        print(f"Body: {data}")
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.text}")
        
        if response.status_code == 200:
            return response.json()['access_token']
        else:
            response.raise_for_status()
            
    except Exception as e:
        print(f"\nError completo: {str(e)}")
        raise

# Ejemplo de uso
try:
    # Reemplaza con tus credenciales reales
    token = get_service_titan_token(
        app_id="9jxbbcf06a42i",
        client_id="cid.dtq2ekk9l23mnp70y3sowky89",
        client_secret="cs2.yk71kq7hj0xyi3x5bd1syl0xazjxm344crle3mkxvripg0m80g"
    )
    
    print(f"\n¡Token obtenido con éxito!: {token[:50]}...")  # Muestra parte del token por seguridad
    
    # Ahora puedes usar este token para otras peticiones API
    # Ejemplo:
    # headers = {'Authorization': f'Bearer {token}', 'ST-App-Id': 'TU_APP_ID_EXACTO'}
    # response = requests.get('https://api.servicetitan.io/...', headers=headers)
    
except Exception as e:
    print(f"\nFallo en la autenticación: {str(e)}")
    print("\nPosibles soluciones:")
    print("1. Verifica que todas las credenciales sean IDÉNTICAS a las usadas en cURL")
    print("2. Asegúrate de no tener espacios antes/después de los valores")
    print("3. Compara el output de este script con tu comando cURL exitoso")