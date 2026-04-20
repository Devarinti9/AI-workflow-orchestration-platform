from sqlalchemy import DateTime, Integer, String, func
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column
from app.db import Base


class WorkflowRecord(Base):
    __tablename__ = "workflow_records"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    source_name: Mapped[str] = mapped_column(String(100), index=True)
    title: Mapped[str] = mapped_column(String(255))
    raw_payload: Mapped[dict] = mapped_column(JSONB)
    processed_output: Mapped[dict] = mapped_column(JSONB)
    status: Mapped[str] = mapped_column(String(50), default="processed")
    created_at: Mapped[str] = mapped_column(DateTime(timezone=True), server_default=func.now())
