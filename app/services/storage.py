import json
from sqlalchemy.orm import Session
from app.models.workflow import WorkflowRecord

def save_record(db: Session, source_name: str, title: str, raw_payload: dict, processed_output: dict | None = None, status: str = "stored"):
    record = WorkflowRecord(
        source_name=source_name,
        title=title,
        raw_payload=json.dumps(raw_payload),
        processed_output=json.dumps(processed_output) if processed_output else None,
        status=status,
    )
    db.add(record)
    db.commit()
    db.refresh(record)
    return record

def get_records(db: Session):
    return db.query(WorkflowRecord).order_by(WorkflowRecord.id.desc()).all()