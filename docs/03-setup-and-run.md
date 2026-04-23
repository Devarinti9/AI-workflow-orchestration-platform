# Setup and Run Guide

## Prerequisites
- Python 3.10+
- `pip`
- Optional: Docker / Docker Compose

## Recommended quick-start
### 1. Install dependencies
```bash
python -m pip install -r requirements.txt
```

### 2. Create environment file
Create `.env` from `.env.example`.

Example:
```env
DATABASE_URL=sqlite:///./workflow.db
API_BASE_URL=https://jsonplaceholder.typicode.com/posts
```

### 3. Start the API
```bash
python -m uvicorn app.main:app --host 0.0.0.0 --port 8000
```

### 4. Open the API docs
- `/docs`
- `/health`

## Docker run
```bash
docker compose up --build
```

## Expected startup behavior
On startup the application:
1. reads the environment configuration
2. creates the SQLAlchemy engine
3. creates database tables if they do not exist
4. starts the FastAPI application

## Recommended validation sequence
1. `GET /health`
2. `POST /ingest`
3. `GET /records`
4. `POST /orchestrate`

## Output expectations
### `POST /ingest`
Should ingest five records from the configured external API and store them in the database.

### `GET /records`
Should return stored records with parsed `processed_output`.

### `POST /orchestrate`
Should run the orchestration flow against the latest stored record.
