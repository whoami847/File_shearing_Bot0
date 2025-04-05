from pydantic_settings import BaseSettings

class Config(BaseSettings):
    API_ID: int = 18662358  # Your new API ID
    API_HASH: str = "6ee14b1c055ba7466d6bf293852d3765"  # Your new API hash
    BOT_TOKEN: str = "7671316803:AAFiG_mhL1wy7T1cTB-aL_ktjVAO0vwKvhU"  # From @BotFather
    
    class Config:
        env_file = ".env"

config = Config()
