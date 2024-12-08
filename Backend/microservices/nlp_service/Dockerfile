FROM python:3.9-slim

WORKDIR /app

COPY microservices/nlp_service/requirements.txt /app/requirements.txt

COPY microservices/nlp_service /app

RUN pip install --no-cache-dir -r requirements.txt

CMD ["uvicorn", "nlp:app", "--host", "0.0.0.0", "--port", "8001"]
