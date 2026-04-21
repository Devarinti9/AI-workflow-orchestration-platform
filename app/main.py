from fastapi import FastAPI
from app.api.routes import router
from app.services.db import Base, engine
from app.models.workflow import WorkflowRecord

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="AI Workflow Orchestration Platform",
    description="API for ingestion, workflow orchestration, and record retrieval",
    version="1.0.0",
)

app.include_router(router)