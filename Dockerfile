FROM python:3.13-slim

WORKDIR /app

COPY requirements.txt .

RUN apt-get update && \
    apt-get install netcat-traditional && \
    pip install -r requirements.txt && \
    rm -rf /var/lib/apt/list

# COPY all files from current dir in host
# current dir in container
COPY . .

ENTRYPOINT ["sh", "entrypoint.sh"]