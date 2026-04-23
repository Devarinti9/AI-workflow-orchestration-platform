# Architecture

## High-level flow
External API -> Ingestion Service -> LangGraph Workflow -> Database Storage -> API Response

## Application structure
- `app/main.py` — FastAPI application startup and database table creation
- `app/api/routes.py` — REST endpoints
- `app/config.py` — environment-driven configuration
- `app/services/db.py` — database engine, session factory, and dependency
- `app/services/ingestion.py` — external HTTP fetch logic
- `app/services/orchestrator.py` — LangGraph workflow definition and execution
- `app/services/storage.py` — record persistence and retrieval helpers
- `app/models/workflow.py` — SQLAlchemy model definition
- `tests/test_routes.py` — basic API tests
- `dags/ingest_pipeline.py` — starter Airflow DAG example

## Runtime responsibilities
### FastAPI layer
Handles external requests and maps them to service functions.

### Ingestion layer
Fetches a list payload from the configured external API source.

### Orchestration layer
Runs a deterministic processing graph with these nodes:
- summarize
- count_words
- classify

### Storage layer
Stores:
- source name
- record title
- raw payload JSON
- processed output JSON
- current status
- creation timestamp

## Current data model
`workflow_records`
- `id`
- `source_name`
- `title`
- `raw_payload`
- `processed_output`
- `status`
- `created_at`

## Configuration model
The project reads configuration from environment variables via `.env`.

### Current variables
- `DATABASE_URL`
- `API_BASE_URL`

## Notes on the Airflow DAG
The repository includes an Airflow DAG file as a documentation and extension artifact. The FastAPI app itself does not require Airflow to run.
