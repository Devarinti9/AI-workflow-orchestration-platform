from typing import Any
import requests
from sqlalchemy.orm import Session
from app.config import settings
from app.models.workflow import WorkflowRecord
from app.services.orchestrator import build_summary


def fetch_external_data(limit: int = 5) -> list[dict[str, Any]]:
    response = requests.get(settings.external_api_url, timeout=15)
    response.raise_for_status()
    return response.json()[:limit]


def ingest_records(db: Session, limit: int = 5) -> int:
    items = fetch_external_data(limit=limit)
    created = 0

    for item in items:
        summary = build_summary(item.get("title", ""), item.get("body", ""))
        record = WorkflowRecord(
            source_name="jsonplaceholder",
            title=item.get("title", "untitled"),
            raw_payload=item,
            processed_output=summary,
            status="processed",
        )
        db.add(record)
        created += 1

    db.commit()
    return created
