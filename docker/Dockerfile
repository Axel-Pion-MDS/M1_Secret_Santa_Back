FROM python:latest

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /src

COPY requirements.txt /src/

RUN pip install -r requirements.txt
RUN pip install psycopg2
RUN pip install django-cors-headers

COPY . /src/