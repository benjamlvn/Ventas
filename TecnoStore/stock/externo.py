import requests
from django.conf import settings

def obtener_token():
    url = settings.TOKEN_URL
    data = {
        'grant_type': 'client_credentials',
        'client_id': settings.CLIENT_ID,
        'client_secret': settings.CLIENT_SECRET,
        'scope': settings.TOKEN_SCOPE,
    }
    r = requests.post(url, data=data)
    r.raise_for_status()
    return r.json()['access_token']

def obtener_stock_externo():
    token = obtener_token()
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json',
    }
    
    url = f"{settings.API_BASE_URL}/api/stock/"  # Ajusta si cambia
    r = requests.get(url)# headers=headers)
    r.raise_for_status()
    return r.json()

def enviar_stock_externo(data):
    token = obtener_token()
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json',
    }
    url = f"{settings.API_BASE_URL}/api/stock/"
    r = requests.post(url, json=data) #headers=headers)
    r.raise_for_status()
    return r.json()
