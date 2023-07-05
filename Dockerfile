FROM python:latest
RUN apk update
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY client.py ping.py
