from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app.db import Base, engine, get_db
from app.models.workflow import WorkflowRecord
from app.schemas import IngestResponse, OrchestrateRequest, WorkflowRecordOut
from app.services.ingestion import ingest_records
from app.services.orchestrator import build_summary

router = APIRouter()
Base.metadata.create_all(bind=engine)


@router.get("/health")
def health() -> dict:
    return {"status": "ok", "service": "ai-workflow-orchestration-platform"}


@router.post("/ingest", response_model=IngestResponse)
def ingest(limit: int = Query(default=5, ge=1, le=20), db: Session = Depends(get_db)):
    created = ingest_records(db, limit=limit)
    return {"ingested_count": created, "message": "Records ingested successfully"}


@router.get("/records", response_model=list[WorkflowRecordOut])
def list_records(db: Session = Depends(get_db)):
    return db.query(WorkflowRecord).order_by(WorkflowRecord.id.desc()).all()


@router.post("/orchestrate")
def orchestrate(request: OrchestrateRequest):
    if not request.text.strip():
        raise HTTPException(status_code=400, detail="Text cannot be empty")

    result = build_summary(title=request.text, body=request.text)
    return {"result": result}
