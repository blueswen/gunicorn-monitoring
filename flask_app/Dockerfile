FROM python:3.9.10-slim

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

EXPOSE 8000

CMD gunicorn --bind=0.0.0.0:8000 --statsd-host=${STATSD_HOST}:${STATSD_PORT} --statsd-prefix=${APP_NAME} app:app
