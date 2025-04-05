FROM python:3.10-slim

# Install system dependencies
RUN apt-get update && \
    apt-get install -y \
    build-essential \
    libssl-dev \
    ffmpeg \
    curl \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Set Python path
ENV PYTHONPATH="${PYTHONPATH}:/app"

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application
COPY . .

# Health check
HEALTHCHECK --interval=30s --timeout=3s \
    CMD curl -f http://localhost:8080/health || exit 1

# Run both services with proper path
CMD ["sh", "-c", "uvicorn web.routes:app --host 0.0.0.0 --port 8080 --app-dir ./web & python3 -m bot.main_handler"]
