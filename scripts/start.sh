#!/bin/bash
uvicorn bot.main_handler:app --host 0.0.0.0 --port 8080 &
python3 -m bot.handlers.delete_files &
