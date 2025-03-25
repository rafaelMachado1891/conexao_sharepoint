import requests
import os
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()

TENANT_ID = os.getenv("TENANT_ID")
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
SITE_URL = os.getenv("SITE_URL")
LIST_NAME = os.getenv("LIST_NAME")

TOKEN_URL = f"https://login.microsoftonline.com/{TENANT_ID}/oauth2/v2.0/token"

def obter_token():
    """Obtém o token de acesso do SharePoint."""
    payload = {
        "grant_type": "client_credentials",
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "scope": "https://graph.microsoft.com/.default"
    }
    response = requests.post(TOKEN_URL, data=payload)
    response.raise_for_status()
    return response.json()["access_token"]

def obter_lista_itens(access_token):
    """Obtém os dados da API do SharePoint."""
    url = f"https://graph.microsoft.com/v1.0/sites/ditalcombr.sharepoint.com:/sites/Dital-ApontamentoProducao:/lists/{LIST_NAME}/items?$expand=fields"

    headers = {"Authorization": f"Bearer {access_token}", "Accept": "application/json"}
    
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    
    return response.json()  # Retorna os dados brutos

if __name__ == "__main__":
    token = obter_token()
    dados = obter_lista_itens(token)
    
    print(dados)  # Exibe os dados diretamente