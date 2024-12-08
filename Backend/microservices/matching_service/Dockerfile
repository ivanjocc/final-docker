FROM python:3.9-slim

WORKDIR /app

COPY microservices/matching_service/requirements.txt /app/requirements.txt

COPY microservices/matching_service /app

RUN pip install --no-cache-dir -r requirements.txt

CMD ["uvicorn", "matching:app", "--host", "127.0.0.1", "--port", "8003"]
