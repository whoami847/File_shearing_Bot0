import os
from pydantic import BaseSettings

class Config(BaseSettings):
    API_ID: int = 28774737
    API_HASH: str = "851190ab85bb0b6dd547fff8e3c35b73"
    BOT_TOKEN: str = "7671316803:AAFiG_mhL1wy7T1cTB-aL_ktjVAO0vwKvhU"
    # Add other config values...

    class Config:
        env_file = ".env"

config = Config()
