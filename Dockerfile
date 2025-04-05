FROM python:3.10-slim

RUN apt-get update && \
    apt-get install -y \
    build-essential \
    libssl-dev \
    ffmpeg \
    bash

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all files including scripts
COPY . .

# Make scripts executable
RUN chmod +x /app/scripts/start.sh

CMD ["/app/scripts/start.sh"]  # Full path to script
