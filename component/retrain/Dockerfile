FROM python:3.6-slim

ENV PYTHONUNBUFFERED 1

COPY ./src /src/
WORKDIR /src
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
