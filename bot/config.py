import os
from pydantic_settings import BaseSettings

class Config(BaseSettings):
    API_ID: int = os.getenv("API_ID")  # ENV variable থেকে পড়বে
    API_HASH: str = os.getenv("API_HASH")
    BOT_TOKEN: str = os.getenv("BOT_TOKEN")

    class Config:
        env_file = ".env"

config = Config()
