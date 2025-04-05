from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import List

class Config(BaseSettings):
    # Required Fields (Telegram)
    API_ID: int
    API_HASH: str
    BOT_TOKEN: str
    
    # Optional Fields with Default Values
    OWNER_ID: int = 7282066033
    ADMINS: List[int] = [7282066033, 6564441490]
    CHANNEL_ID: int = -1002644513465
    FSUB_CHANNELS: List[int] = [-1002644513465, -1002656647177]
    DATABASE_URL: str = "mongodb+srv://Anime1:Anime1@cluster0.030ybld.mongodb.net/Cluster0?retryWrites=true&w=majority&appName=Cluster0"
    DATABASE_NAME: str = "Cluster0"
    AUTO_DELETE_TIME: int = 1200  # Minutes
    PROTECT_CONTENT: bool = False
    PORT: int = 8080

    # Pydantic Configuration
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )

config = Config()
