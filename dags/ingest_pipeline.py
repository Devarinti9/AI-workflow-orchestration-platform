from datetime import datetime

from airflow import DAG
from airflow.operators.bash import BashOperator

with DAG(
    dag_id="ai_workflow_ingest_pipeline",
    start_date=datetime(2025, 1, 1),
    schedule="@daily",
    catchup=False,
    tags=["ai", "workflow", "ingestion"],
) as dag:
    run_ingestion = BashOperator(
        task_id="run_ingestion_api",
        bash_command="curl -X POST http://host.docker.internal:8000/ingest",
    )

    run_ingestion
