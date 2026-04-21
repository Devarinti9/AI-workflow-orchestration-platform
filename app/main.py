from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(
    title="AI Workflow Orchestration Platform",
    description="API for ingestion, workflow orchestration, and record retrieval",
    version="1.0.0",
)

app.include_router(router)
