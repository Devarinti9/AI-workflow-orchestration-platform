from fastapi import APIRouter

router = APIRouter()

@router.get("/health")
def health():
    return {"status": "ok", "message": "AI Workflow Orchestration Platform is running"}

@router.post("/ingest")
def ingest():
    return {"status": "success", "message": "Sample ingestion endpoint ready"}

@router.get("/records")
def records():
    return {
        "status": "success",
        "records": [
            {"id": 1, "source": "demo-api", "status": "stored"}
        ],
    }

@router.post("/orchestrate")
def orchestrate():
    return {"status": "success", "message": "Sample orchestration flow executed"}