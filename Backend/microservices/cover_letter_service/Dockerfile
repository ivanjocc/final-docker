FROM python:3.9-slim

WORKDIR /app

COPY microservices/cover_letter_service/requirements.txt /app/requirements.txt

COPY microservices/cover_letter_service /app

RUN pip install --no-cache-dir -r requirements.txt

CMD ["uvicorn", "cover_letter:app", "--host", "127.0.0.1", "--port", "8002"]
