from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import List
import json

class Config(BaseSettings):
    # Required Fields (Telegram)
    API_ID: int
    API_HASH: str
    BOT_TOKEN: str
    
    # List Fields with Custom Parsing
    ADMINS: List[int] = [7282066033, 6564441490]
    FSUB_CHANNELS: List[int] = [-1002644513465, -1002656647177]
    
    # Other Fields
    OWNER_ID: int = 7282066033
    CHANNEL_ID: int = -1002644513465
    DATABASE_URL: str = "mongodb+srv://Anime1:Anime1@cluster0.030ybld.mongodb.net/Cluster0?retryWrites=true&w=majority&appName=Cluster0"
    DATABASE_NAME: str = "Cluster0"
    AUTO_DELETE_TIME: int = 1200
    PROTECT_CONTENT: bool = False
    PORT: int = 8080

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
        json_loads=lambda s: json.loads(s) if s.startswith('[') else [int(x) for x in s.split(',')]
    )

config = Config()
