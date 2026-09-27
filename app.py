import os
from flask import Flask, jsonify

app = Flask(__name__)

@app.get("/")
def index ():
    return jsonify(service="devops-practice", version="1.0.0")


@app.get("/health")
def health():
    return jsonify(status="alive"), 200


@app.get("/ready")
def ready():
    #LAb Simulation only: no Real dependency check it
    is_ready = os.getenv("APP_READY", "true").lower() == "true"
    status = "ready" if is_ready else "no_ready"
    return jsonify(status=status), 200 if is_ready else 503
