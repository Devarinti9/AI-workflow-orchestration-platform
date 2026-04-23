# Troubleshooting

## `ModuleNotFoundError`
### Cause
A required file is missing or package directories are not structured correctly.

### Fix
Make sure these files exist:
- `app/__init__.py`
- `app/api/__init__.py`
- `app/services/__init__.py`
- `app/models/__init__.py`

## `address already in use`
### Cause
The server is already running on the selected port.

### Fix
Use a different port or stop the previous process.

## External API fetch failure
### Cause
`API_BASE_URL` is wrong, unavailable, or rate-limited.

### Fix
- verify `.env`
- test the URL manually
- confirm the source returns a list payload

## Database file or connection issue
### Cause
`DATABASE_URL` is invalid.

### Fix
Use the default SQLite value for the current starter implementation:
```env
DATABASE_URL=sqlite:///./workflow.db
```

## Airflow expectation mismatch
### Clarification
The Airflow DAG is included as a starter example. The main FastAPI application does not require Airflow to be running.
