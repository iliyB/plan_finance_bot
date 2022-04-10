import os

API_TOKEN = os.environ.get("TELEGRAM_API_TOKEN")
REDIS_HOST = os.environ.get("REDIS_CONTAINER_NAME")
REDIS_PORT = os.environ.get("REDIS_PORT")
REDIS_DB_FSM = os.environ.get("REDIS_DB_FSM")

POSTGRES_USER = os.environ.get("POSTGRES_USER")
POSTGRES_PASSWORD = os.environ.get("POSTGRES_PASSWORD")
POSTGRES_HOST = os.environ.get("POSTGRES_HOST")
POSTGRES_PORT = os.environ.get("POSTGRES_PORT")
POSTGRES_DB = os.environ.get("POSTGRES_DB")
