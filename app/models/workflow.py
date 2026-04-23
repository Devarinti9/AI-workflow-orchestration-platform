from sqlalchemy import Column, DateTime, Integer, String, Text
from sqlalchemy.sql import func

from app.services.db import Base


class WorkflowRecord(Base):
    __tablename__ = "workflow_records"

    id = Column(Integer, primary_key=True, index=True)
    source_name = Column(String(100), nullable=False)
    title = Column(String(255), nullable=True)
    raw_payload = Column(Text, nullable=False)
    processed_output = Column(Text, nullable=True)
    status = Column(String(50), default="processed")
    created_at = Column(DateTime(timezone=True), server_default=func.now())
