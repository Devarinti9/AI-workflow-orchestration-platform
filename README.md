# AI Workflow Orchestration Platform

## Overview
AI-driven workflow orchestration platform for automated external data ingestion, backend processing, intelligent workflow execution, and structured data storage.

## Tech Stack
Python, FastAPI, LangGraph, SQLAlchemy, SQLite, Docker, Airflow

## Features
- External API ingestion using Python and Requests
- FastAPI backend with REST endpoints
- LangGraph-based workflow orchestration
- Structured record storage with SQLAlchemy
- Processed output including summary, word count, and classification
- Test coverage for key API endpoints
- Airflow DAG for scheduled ingestion example

## Workflow
External API -> Ingestion Service -> LangGraph Workflow -> Database Storage -> API Response

## API Endpoints
- `GET /health` - Health check endpoint
- `POST /ingest` - Fetches and stores external data with workflow processing
- `GET /records` - Returns stored records and processed workflow output
- `POST /orchestrate` - Executes orchestration on the latest stored record

## Example Processing
Each ingested record is processed through a workflow that:
- generates a short summary
- calculates word count
- classifies the record into a category

## Run in Codespaces or local terminal
```bash
python -m pip install -r requirements.txt
python -m uvicorn app.main:app --host 0.0.0.0 --port 8000
```

## Run tests
```bash
python -m pytest
```

## Docker
```bash
docker compose up --build
```

## Future Enhancements
- PostgreSQL integration
- GCP deployment
- Authentication and monitoring
- CI/CD pipeline
