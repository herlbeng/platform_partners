import os
import pickle
import pandas as pd
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
import gspread
import time 

# Alcances requeridos
SCOPES = ["https://www.googleapis.com/auth/spreadsheets.readonly"]

# Autenticación con OAuth2
def authenticate():
    creds = None
    # Si ya existe un token guardado, lo usamos
    if os.path.exists("token.pickle"):
        with open("token.pickle", "rb") as token:
            creds = pickle.load(token)

    # Si no hay credenciales válidas, iniciamos sesión manualmente
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials_oauth2.json", SCOPES)
            creds = flow.run_local_server(port=0)

        # Guardamos las credenciales para futuros usos
        with open("token.pickle", "wb") as token:
            pickle.dump(creds, token)

    return creds

# Conectar con Google Sheets y descargar la hoja
def download_sheet(spreadsheet_ids, sheet_name):
    creds = authenticate()
    client = gspread.authorize(creds)

    for spreadsheet_id in spreadsheet_ids:
        try:
            # Abre la hoja de cálculo
            spreadsheet = client.open_by_key(spreadsheet_id)
            #spreadsheet_name = spreadsheet.title.replace(" ", "")  # Reemplaza espacios con guiones bajos
            spreadsheet_name = spreadsheet.title  # Original, para cambiarlo en clean_csv

            # Obtiene los datos de la hoja especificada
            worksheet = spreadsheet.worksheet(sheet_name)
            data = worksheet.get_all_values()  # Obtiene todos los valores de la hoja
            
            if not data:
                print(f"❌ No hay datos en la hoja '{sheet_name}' del documento '{spreadsheet_name}'.")
                continue  # Si no hay datos, pasa al siguiente documento

            # Convertir a DataFrame
            df = pd.DataFrame(data)

            # Generar el nombre del archivo CSV
            file_name = f"{spreadsheet_name}_{sheet_name}.csv"
            df.to_csv(file_name, index=False, header=False)  # Exporta como CSV

            print(f"✅ Hoja '{spreadsheet_name}' descargada como {file_name}")
            time.sleep(3)

        except Exception as e:
            print(f"❌ Error con {spreadsheet_id}: {e}")

# Configuración: Cambia esto por los valores de tu Google Sheets
SHEET_NAME = "LTM_KPIS"
SPREADSHEET_IDS = [
   "1Y-r29mP-2GDI1QSUnqR40dmQHg2FiVJb6_I72fLUZjA",
    "1uYlSfRLgWJbvbCpDL9IHspk8RtW8IQ_oxOra1lqH6lI",
    "1kr3HITbMlV-UJobolw_u-U6WQD36WapieGmCdOwsUac",
    "1iipay4K9b0Hyr-MU_xM4ooO7WQlpgRbtJOX0DlJTa10",
    "1I1-JCPktjbRD3CKdGE6b0_Afg5L3LNwIjVMhuhjgJWg",
    "1IB6gI3zkxK04TvO1XNhqtW9OuR4Z9lU3_rduwjICPgs",
    "1xvVYFL13_CxYILX67ZqXskNw14DM9-7VQNrYmg86nNs",
    "1uiN721yVRDP5ZQc1Gbgbsqf5PKcJNmZgtcUSAhRAn88",
    "1ZSBrIrc_RxMx4VVhuBnUADZF3bFidEKrrUrGQ7V5_dU",
    "1WArD825AgoAfgDW2Y4luTC21ljZYM1sWetd3mMnz_gk",
    "1uuFuvx1lsJs07fH8cKfvCPasE3ZCElh69CgAwktiBSI",
    "19zPAJSDity3pGHRDITzDs5yc8um4bnRE-LNJMlUKeRI",
    "1DLfaZ2MIwiEj9AMEVUa7d4X-99r30BIqVqeowXPkDeg",
    "1wIkcQkjblBIU6lTdVls92Dg3M3GBYrvrkPxEjVzeeK0",
    "1fqA3ihNaueJIumEZO9kMRSyTQpz-GusA5eiEzhY5548",
    "1ORV4j00omq3QlRVwJRJYFjD8tcgxJSfcneY4WYhoFh0",
    "15-bv1W6slerJs9V88EGCYt8hPvu65NuNWY-spNz7cqQ",
    "1woNM7ZRSz4sFdhJYqKZQfspXBzhslOswCxzTCxU1VRg",
    "18QK8mz1E7fCBiNFeveM4AmV3Oz8ufoH-1-mpmTJGYI0",
    "1-lBtmbXLNXsouAx-ZzuGXRmFHw23CkA0WPQSTXJVtDw",
    "1FRhsbKnWLcWRoRFkIBWdaW6vlybS3pyT_qDj8rl40Ug",
    "10qbr-E5JK2BtcKmcxXlFW8NHq4BEOzw3OzIzOxoNl7A",
    "11qJyeA0AubWKK6rpzwBXwECTBLHcienLfUvg9AVGnyg",
    "11s4sG7unM0QAeG6GTw3PL2xB_1BPpIAuoVYtfdKjTXs",
    "1QQLnTQvOkuH86G4TIpwlKG4DGvw0uRszRV7afIDchYE",
    "1t7OpjMZWatVfSkifm-I2hzFMsq6ZlALiOaL1WzLDA0g",
    "1cJz8a_9-T16mhQrSXADzYpBoNeys_C_ERh0oyHKTmkM",
    "1tq8SsYVB20bLZwY-lJ8VTJyBtpJBOqWV7OyYxXdpwt4",
    "1cmGYJZzsH_n3uL7UYxLoOryHERgFRasxVCu8bt59oWI"
]

download_sheet(SPREADSHEET_IDS, SHEET_NAME)  # Este es el ciclo con el nombre de la hoja
