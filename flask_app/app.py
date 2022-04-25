import logging
import random
import time

from flask import Flask, Response

app = Flask(__name__)


@app.route("/")
def hello_world():
    app.logger.error("Hello, World!")
    return "Hello, World!"


@app.route("/io_task")
def io_task():
    time.sleep(2)
    return "IO bound task finish!"


@app.route("/cpu_task")
def cpu_task():
    for i in range(10000):
        n = i*i*i
    return "CPU bound task finish!"


@app.route("/random_sleep")
def random_sleep():
    time.sleep(random.randint(0, 5))
    return "random sleep"


@app.route("/random_status")
def random_status():
    status_code = random.choice([200] * 6 + [300, 400, 400, 500])
    return Response("random status", status=status_code)


if __name__ != '__main__':
    # Use gunicorn's logger to replace flask's default logger
    gunicorn_logger = logging.getLogger('gunicorn.error')
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)
