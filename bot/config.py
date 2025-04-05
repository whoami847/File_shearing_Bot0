from pydantic import BaseSettings
from typing import List

class Config(BaseSettings):
    API_ID: int = 28774737
    API_HASH: str = "851190ab85bb0b6dd547fff8e3c35b73"
    BOT_TOKEN: str = "7671316803:AAFiG_mhL1wy7T1cTB-aL_ktjVAO0vwKvhU"
    OWNER_ID: int = 7282066033
    ADMINS: List[int] = [7282066033, 6564441490]
    CHANNEL_ID: List[int] = [-1002644513465]
    FSUB_CHANNELS: List[int] = [-1002644513465, -1002656647177]
    DATABASE_URL: str = "mongodb+srv://Anime1:Anime1@cluster0.030ybld.mongodb.net/Cluster0?retryWrites=true&w=majority&appName=Cluster0"
    DATABASE_NAME: str = "Cluster0"
    AUTO_DELETE_TIME: int = 1200
    PROTECT_CONTENT: bool = False
    PORT: int = 8080

    class Config:
        env_file = ".env"

config = Config()
