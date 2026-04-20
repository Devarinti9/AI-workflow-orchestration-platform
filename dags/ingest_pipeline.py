from datetime import datetime
import requests
from airflow import DAG
from airflow.operators.python import PythonOperator


def call_api():
    response = requests.post("http://api:8000/ingest?limit=5", timeout=30)
    response.raise_for_status()
    return response.json()


with DAG(
    dag_id="external_data_ingestion",
    start_date=datetime(2025, 1, 1),
    schedule="@daily",
    catchup=False,
    tags=["ingestion", "api", "workflow"],
) as dag:
    PythonOperator(
        task_id="trigger_ingestion_api",
        python_callable=call_api,
    )
