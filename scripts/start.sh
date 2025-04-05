#!/bin/bash
python3 -m bot.main_handler &
python3 -m bot.handlers.delete_files &
echo "Bot started on port 8080!"
