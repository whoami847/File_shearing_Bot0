#!/bin/bash

# Start FastAPI server
uvicorn web.routes:router --host 0.0.0.0 --port 8080 &

# Start Telegram bot
python3 -m bot.main_handler &

# Start cleanup scheduler
python3 -m bot.handlers.delete_files &

# Keep container running
wait
