import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # Removed crypto-related API keys
    DATABASE_URL = os.getenv("DATABASE_URL")
    MAX_FILE_SIZE = int(os.getenv("MAX_FILE_SIZE", 500 * 1024 * 1024))  # 500MB default
    ALLOWED_EXTENSIONS = {'mp4', 'mkv', 'avi', 'mov', 'pdf', 'docx'}
    STORAGE_PATH = os.getenv("STORAGE_PATH", "uploads")
    BASE_URL = os.getenv("BASE_URL", "http://localhost:8000")
