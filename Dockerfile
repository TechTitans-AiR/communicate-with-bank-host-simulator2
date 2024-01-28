FROM --platform=linux/amd64 python:3.11-slim-buster as build

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends libssl-dev libffi-dev

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

ARG MONGO_URI
RUN echo "MONGO_URI=${MONGO_URI}" > .env

COPY . /app

CMD ["python", "bankCommunication.py"]
