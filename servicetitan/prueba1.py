import requests
from requests.auth import HTTPBasicAuth
import json

auth_url = f"https://auth-integration.servicetitan.io/connect/token"

def get_service_titan_token(app_id, client_id, client_secret, tenant_id):
    
    # 1. Configuración de la solicitud
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'ST-App-Id': app_id
    }
    
    data = {
        'grant_type': 'client_credentials',
        'client_id' : client_id,
        'client_secret' : client_secret
    }
    
    # 2. Configurar autenticación básica
    auth = HTTPBasicAuth(client_id, client_secret)
    
    try:
        # 3. Realizar la solicitud POST con diagnóstico completo
        response = requests.post(
            auth_url,
            auth=auth,
            headers=headers,
            data=data,
            timeout=30
        )
        
        # 4. Mostrar información detallada del request (para diagnóstico)
        print("\n=== DIAGNÓSTICO DE LA SOLICITUD ===")
        print(f"URL: {auth_url}")
        print(f"Headers: {json.dumps(dict(headers), indent=2)}")
        print(f"Body: {data}")
        print(f"Response Status: {response.status_code}")
        print(f"Response Body: {response.text}\n")
       
        # 5. Manejar la respuesta
        if response.status_code == 200:
            return response.json()['access_token']
        else:
            # Analizar el error específico
            error_data = response.json()
            if 'error' in error_data:
                if error_data['error'] == 'invalid_scope':
                    raise Exception("Error de scope: Verifica que tu aplicación tenga los permisos necesarios en el portal de ServiceTitan")
                elif error_data['error'] == 'invalid_client':
                    raise Exception("Error de cliente: Verifica client_id y client_secret")
                else:
                    raise Exception(f"Error de autenticación: {error_data}")
            else:
                response.raise_for_status()
                
    except requests.exceptions.RequestException as e:
        raise Exception(f"Error en la solicitud HTTP: {str(e)}")

# Ejemplo de uso con manejo mejorado de errores
try:
    # Configura tus credenciales (en producción usa Secret Manager)
    CREDENTIALS = {
        "app_id":"9jxbbcf06a42i",
        "client_id":"cid.dtq2ekk9l23mnp70y3sowky89",
        "client_secret":"cs2.yk71kq7hj0xyi3x5bd1syl0xazjxm344crle3mkxvripg0m80g",
        "tenant_id":"1270943139"
    }
    
    print("Intentando autenticación con ServiceTitan API...")
    token = get_service_titan_token(**CREDENTIALS)
    print(f"\n¡Autenticación exitosa! Token obtenido: {token[:50]}... (truncado por seguridad)")
    
except Exception as e:
    print(f"\nERROR: {str(e)}")
    print("\nPasos para solucionar:")
    print("1. Verifica que todas las credenciales sean exactamente iguales a las del portal de ServiceTitan")
    print("2. Confirma que tu aplicación tenga asignado el scope 'api'")
    print("3. Prueba las credenciales directamente con cURL:")
    print(f"   curl -X POST {auth_url} \\")
    print(f"   -H 'Content-Type: application/x-www-form-urlencoded' \\")
    print(f"   -H 'ST-App-Id: {CREDENTIALS['app_id']}' \\")
    print(f"   -u '{CREDENTIALS['client_id']}:{CREDENTIALS['client_secret']}' \\")
    print("   -d 'grant_type=client_credentials&scope=api'")