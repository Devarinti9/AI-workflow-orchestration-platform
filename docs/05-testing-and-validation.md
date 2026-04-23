# Testing and Validation

## Included tests
The repository includes a small API test file in `tests/test_routes.py`.

## Run tests
```bash
python -m pytest
```

## Recommended manual checks
### Health endpoint
Expected result: HTTP 200 with `status: ok`

### Ingest endpoint
Expected result:
- new rows inserted into `workflow_records`
- response shows record count and status values

### Records endpoint
Expected result:
- response contains `count`
- response contains previously ingested records
- `processed_output` is visible

### Orchestrate endpoint
Expected result:
- latest record is returned
- workflow result includes summary, word count, and classification

## Functional acceptance checklist
- application starts without import errors
- API docs page loads
- ingestion succeeds against the configured external API
- records are persisted and retrievable
- orchestration returns structured output
