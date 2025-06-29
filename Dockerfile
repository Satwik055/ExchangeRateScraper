FROM python:3.9-slim

WORKDIR /app

COPY app/ /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "./main.py"]