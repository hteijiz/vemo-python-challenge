FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY app ./app
COPY logs ./logs

CMD ["uvicorn", "app:main", "--host", "127.0.0.1", "--port", "8080"]

# docker build -t vemo .
# docker run -p 8080:8080 vemo
