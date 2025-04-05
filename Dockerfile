FROM python:3.10-slim

# Install system dependencies
RUN apt-get update && \
    apt-get install -y \
    build-essential \
    libssl-dev \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY . .

# Install TgCrypto for performance
RUN pip install --no-cache-dir TgCrypto

# Run the application
CMD ["python3", "-m", "bot.main_handler"]
