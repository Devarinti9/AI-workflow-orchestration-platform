# API Reference

## `GET /health`
### Purpose
Simple service health check.

### Response
```json
{
  "status": "ok",
  "message": "AI Workflow Orchestration Platform is running"
}
```

## `POST /ingest`
### Purpose
Fetch external records, process them through the workflow, and persist them.

### Behavior
- calls the external API configured in `API_BASE_URL`
- reads up to five items
- extracts each item's `title`
- runs LangGraph processing
- stores raw and processed payloads

### Success response shape
```json
{
  "status": "success",
  "message": "Ingested 5 records",
  "records": [
    {
      "id": 1,
      "title": "...",
      "status": "processed"
    }
  ]
}
```

### Error behavior
- returns `502` for ingestion-specific fetch failures
- returns `500` for unexpected server errors

## `GET /records`
### Purpose
Return all stored workflow records in descending order.

### Returned fields per record
- `id`
- `source_name`
- `title`
- `status`
- `processed_output`
- `created_at`

## `POST /orchestrate`
### Purpose
Run the orchestration logic on the latest stored record.

### Success response shape
```json
{
  "status": "success",
  "message": "Workflow orchestration executed successfully",
  "latest_record": {
    "id": 1,
    "title": "...",
    "status": "processed"
  },
  "workflow_result": {
    "title": "...",
    "summary": "...",
    "word_count": 3,
    "classification": "general"
  }
}
```
