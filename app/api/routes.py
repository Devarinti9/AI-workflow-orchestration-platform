from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.services.db import get_db
from app.services.ingestion import fetch_external_data
from app.services.storage import save_record, get_records

router = APIRouter()

@router.get("/health")
def health():
    return {"status": "ok", "message": "AI Workflow Orchestration Platform is running"}

@router.post("/ingest")
def ingest(db: Session = Depends(get_db)):
    try:
        items = fetch_external_data(limit=5)
        saved = []

        for item in items:
            title = item.get("title", "Untitled")
            processed = {
                "summary": title[:80],
                "word_count": len(title.split()),
                "source_type": "external_api"
            }

            record = save_record(
                db=db,
                source_name="jsonplaceholder",
                title=title,
                raw_payload=item,
                processed_output=processed,
                status="stored"
            )

            saved.append({
                "id": record.id,
                "title": record.title,
                "status": record.status
            })

        return {
            "status": "success",
            "message": f"Ingested {len(saved)} records",
            "records": saved
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/records")
def records(db: Session = Depends(get_db)):
    rows = get_records(db)

    return {
        "status": "success",
        "count": len(rows),
        "records": [
            {
                "id": r.id,
                "source_name": r.source_name,
                "title": r.title,
                "status": r.status,
                "created_at": r.created_at
            }
            for r in rows
        ]
    }

@router.post("/orchestrate")
def orchestrate(db: Session = Depends(get_db)):
    rows = get_records(db)

    if not rows:
        return {
            "status": "success",
            "message": "No records found to orchestrate yet"
        }

    latest = rows[0]
    return {
        "status": "success",
        "message": "Sample orchestration flow executed",
        "latest_record": {
            "id": latest.id,
            "title": latest.title,
            "status": latest.status
        }
    }