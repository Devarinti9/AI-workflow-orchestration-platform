import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./workflow.db")
API_BASE_URL = os.getenv("API_BASE_URL", "https://jsonplaceholder.typicode.com/posts")
