import requests
import os
from dotenv import load_dotenv
import pandas as pd

load_dotenv()

SITE_URL = os.getenv("SITE_URL")
LIST_NAME = os.getenv("LIST_NAME")
TENANT_ID = os.getenv("TENANT_ID")
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")

TOKEN = f"https://login.microsoftonline.com/{TENANT_ID}/oauth2/v2.0/token"

payload = {
        "grant_type": "client_credentials",
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "scope": "https://graph.microsoft.com/.default"
    }

response = requests.post(TOKEN, data=payload)
response.raise_for_status()
accessToken = response.json()["access_token"]

acesso_site = url = f"https://graph.microsoft.com/v1.0/sites/ditalcombr.sharepoint.com:/sites/Dital-ApontamentoProducao:/lists/{LIST_NAME}/items?$expand=fields"

headers = {
        "Authorization": f"Bearer {accessToken}",
       "Accept": "application/json"
}

response = requests.get(url,headers=headers)

dados =(response.json())

df = pd.DataFrame([item["fields"] for item in dados["value"]])


print(df.head())