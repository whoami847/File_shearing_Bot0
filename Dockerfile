FROM python:3.10-slim

RUN apt-get update && \
    apt-get install -y \
    build-essential \
    libssl-dev \
    ffmpeg \
    curl \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Set Python path
ENV PYTHONPATH=/app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

HEALTHCHECK --interval=30s --timeout=3s \
    CMD curl -f http://localhost:8080/health || exit 1

CMD ["sh", "-c", "cd /app && uvicorn web.routes:app --host 0.0.0.0 --port 8080 & python3 -m bot.main_handler"]
