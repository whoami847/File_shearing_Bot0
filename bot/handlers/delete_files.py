import os
import schedule
import time
from pathlib import Path
from config import Config

def cleanup_files():
    path = Path(Config.STORAGE_PATH)
    for file in path.glob("*"):
        # Delete files older than 24 hours
        if time.time() - file.stat().st_mtime > 24 * 3600:
            os.remove(file)
            print(f"Deleted: {file.name}")

def start_cleanup_scheduler():
    schedule.every().hour.do(cleanup_files)
    while True:
        schedule.run_pending()
        time.sleep(1)
