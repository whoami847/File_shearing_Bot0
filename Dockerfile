FROM python:3.10-slim

# Install dependencies
RUN apt-get update && \
    apt-get install -y \
    build-essential \
    libssl-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Install Python packages
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application
COPY . .

CMD ["python3", "-m", "bot.main_handler"]
