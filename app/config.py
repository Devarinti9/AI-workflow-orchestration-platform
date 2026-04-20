from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "AI Workflow Orchestration Platform"
    environment: str = "development"
    database_url: str = "postgresql+psycopg://postgres:postgres@postgres:5432/workflow_db"
    external_api_url: str = "https://jsonplaceholder.typicode.com/posts"
    airflow_api_url: str = "http://airflow:8080"
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


settings = Settings()
