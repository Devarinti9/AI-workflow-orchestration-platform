import requests
from app.config import API_BASE_URL

def fetch_external_data(limit: int = 5):
    response = requests.get(API_BASE_URL, timeout=20)
    response.raise_for_status()
    data = response.json()
    return data[:limit]