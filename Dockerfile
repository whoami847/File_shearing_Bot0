FROM python:3.10-slim

RUN apt-get update && \
    apt-get install -y \
    build-essential \
    libssl-dev \
    ffmpeg \
    bash

WORKDIR /app

# First copy requirements to cache dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all files including scripts
COPY . .

# Make script executable and fix line endings
RUN sed -i 's/\r$//' /app/scripts/start.sh && \
    chmod +x /app/scripts/start.sh

CMD ["/bin/bash", "/app/scripts/start.sh"]
