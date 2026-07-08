FROM python:3.13-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

# COPY all files from current dir in host
# current dir in container
COPY . .

ENTRYPOINT ["sh", "entrypoint.sh"]