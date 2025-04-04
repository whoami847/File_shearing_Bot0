#!/bin/bash
source venv/bin/activate
uvicorn start:app --reload --host 0.0.0.0 --port 8080
