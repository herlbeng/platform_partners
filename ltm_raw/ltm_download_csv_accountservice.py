import gspread
from google.oauth2.service_account import Credentials

# Autenticación con el archivo de credenciales
scopes = ["https://www.googleapis.com/auth/spreadsheets.readonly"]
creds = Credentials.from_service_account_file("sigma-night-454217-c9-e7a051b348be.json", scopes=scopes)
client = gspread.authorize(creds)

# ID de la hoja de cálculo (desde la URL)
spreadsheet_id = "1Jgv0d-nH1CqRvwAKW3tQ-PanONhXpNP_1URemkEN8zc"

# Nombre de la hoja específica que quieres descargar
sheet_name = "LTM_KPIS"

# Abrir la hoja y obtener datos
spreadsheet = client.open_by_key(spreadsheet_id)
worksheet = spreadsheet.worksheet(sheet_name)

# Obtener datos como lista de listas (cada fila es una lista)
data = worksheet.get_all_values()

# Guardar como CSV
import pandas as pd
df = pd.DataFrame(data)
df.to_csv("hoja.csv", index=False, header=False)
print("Hoja descargada como hoja.csv")