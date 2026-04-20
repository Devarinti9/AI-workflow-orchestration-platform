from datetime import datetime
from pydantic import BaseModel


class IngestResponse(BaseModel):
    ingested_count: int
    message: str


class OrchestrateRequest(BaseModel):
    text: str


class WorkflowRecordOut(BaseModel):
    id: int
    source_name: str
    title: str
    raw_payload: dict
    processed_output: dict
    status: str
    created_at: datetime

    class Config:
        from_attributes = True
