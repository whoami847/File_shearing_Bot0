#!/bin/bash

# Start web server
uvicorn bot.web.routes:router --host 0.0.0.0 --port 8080 &

# Start Telegram bot
python3 -m bot.main_handler &

# Keep container running
wait
