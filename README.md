# AI Workflow Orchestration Platform

A FastAPI-based backend platform that automates external data ingestion, scheduled workflows, AI-driven orchestration, and structured storage.

## Tech Stack
- Python
- FastAPI
- Airflow
- LangGraph
- PostgreSQL
- Supabase-ready architecture
- Docker

## Features
- External API ingestion
- Scheduled Airflow DAG
- AI workflow orchestration using LangGraph
- Structured PostgreSQL storage
- Docker-based local setup

## Project Structure
- `app/` FastAPI application
- `dags/` Airflow pipelines
- `tests/` basic tests

## Run Locally

### 1. Clone and enter the project
```bash
git clone <your-repo-url>
cd ai-workflow-orchestration-platform
```

### 2. Start the stack
```bash
docker compose up --build
```

### 3. Open the services
- FastAPI docs: `http://localhost:8001/docs`
- Airflow: `http://localhost:8080`

## Useful Endpoints
- `GET /health`
- `POST /ingest?limit=5`
- `GET /records`
- `POST /orchestrate`
efficiency and reducing manual intervention across cloud-based environments.
