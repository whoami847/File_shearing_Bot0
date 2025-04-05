#!/bin/bash

# Start web server
uvicorn web.routes:app --host 0.0.0.0 --port 8080 &

# Start bot
python3 -m bot.main_handler &

# Keep container alive
wait
