import os
import schedule
import time
from pathlib import Path

def cleanup_files(directory: str = "uploads", age: int = 24):
    path = Path(directory)
    for file in path.glob("*"):
        if time.time() - file.stat().st_mtime > age * 3600:
            os.remove(file)

def start_cleanup_scheduler():
    schedule.every().day.at("00:00").do(cleanup_files)
    while True:
        schedule.run_pending()
        time.sleep(1)
