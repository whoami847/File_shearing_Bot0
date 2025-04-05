from pydantic_settings import BaseSettings, SettingsConfigDict

class Config(BaseSettings):
    # Required Fields (Telegram)
    API_ID: int
    API_HASH: str
    BOT_TOKEN: str
    
    # Optional Fields with Default Values
    OWNER_ID: int = 7282066033
    ADMINS: list[int] = [7282066033, 6564441490]
    CHANNEL_ID: int = -1002644513465
    FSUB_CHANNELS: list[int] = [-1002644513465, -1002656647177]
    DATABASE_URL: str = "mongodb+srv://Anime1:Anime1@cluster0.030ybld.mongodb.net/Cluster0?retryWrites=true&w=majority&appName=Cluster0"
    DATABASE_NAME: str = "Cluster0"
    AUTO_DELETE_TIME: int = 1200  # Minutes
    PROTECT_CONTENT: bool = False
    PORT: int = 8080

    # Pydantic v2 Configuration
    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"  # Allow extra fields in .env
    )

config = Config()
