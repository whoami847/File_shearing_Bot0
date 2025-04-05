FROM python:3.10-slim

# Add MongoDB dependencies
RUN apt-get update && apt-get install -y libssl-dev ca-certificates

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python3", "-m", "bot.main_handler"]
