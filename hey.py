from flask import Flask
import blinker as _

from ddtrace import tracer
from ddtrace.contrib.flask import TraceMiddleware

app = Flask(__name__)

traced_app = TraceMiddleware(app, tracer, service="my-flask-app", distributed_tracing=False)

@app.route("/")
def home():
    return "hello world"

