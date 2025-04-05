FROM python:3.10-slim

RUN apt-get update && \
    apt-get install -y \
    build-essential \
    libssl-dev \
    ffmpeg

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["bash", "scripts/start.sh"]
