import requests

from app.config import API_BASE_URL


class IngestionError(Exception):
    pass


def fetch_external_data(limit: int = 5) -> list[dict]:
    try:
        response = requests.get(API_BASE_URL, timeout=20)
        response.raise_for_status()
        data = response.json()
        if not isinstance(data, list):
            raise IngestionError("External API did not return a list payload")
        return data[:limit]
    except requests.RequestException as exc:
        raise IngestionError(f"Failed to fetch external data: {exc}") from exc
