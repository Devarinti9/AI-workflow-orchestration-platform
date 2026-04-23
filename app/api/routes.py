import json

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.services.db import get_db
from app.services.ingestion import IngestionError, fetch_external_data
from app.services.orchestrator import run_workflow
from app.services.storage import get_records, save_record

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
            processed = run_workflow(title)

            record = save_record(
                db=db,
                source_name="jsonplaceholder",
                title=title,
                raw_payload=item,
                processed_output=processed,
                status="processed",
            )

            saved.append({"id": record.id, "title": record.title, "status": record.status})

        return {
            "status": "success",
            "message": f"Ingested {len(saved)} records",
            "records": saved,
        }
    except IngestionError as exc:
        raise HTTPException(status_code=502, detail=str(exc)) from exc
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc)) from exc


@router.get("/records")
def records(db: Session = Depends(get_db)):
    rows = get_records(db)
    formatted = []

    for row in rows:
        processed_output = None
        if row.processed_output:
            try:
                processed_output = json.loads(row.processed_output)
            except json.JSONDecodeError:
                processed_output = row.processed_output

        formatted.append(
            {
                "id": row.id,
                "source_name": row.source_name,
                "title": row.title,
                "status": row.status,
                "processed_output": processed_output,
                "created_at": row.created_at,
            }
        )

    return {"status": "success", "count": len(formatted), "records": formatted}


@router.post("/orchestrate")
def orchestrate(db: Session = Depends(get_db)):
    rows = get_records(db)
    if not rows:
        return {"status": "success", "message": "No records found to orchestrate yet"}

    latest = rows[0]
    result = run_workflow(latest.title or "")

    return {
        "status": "success",
        "message": "Workflow orchestration executed successfully",
        "latest_record": {
            "id": latest.id,
            "title": latest.title,
            "status": latest.status,
        },
        "workflow_result": result,
    }
