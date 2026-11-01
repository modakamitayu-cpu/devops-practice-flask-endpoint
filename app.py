import json
import logging
import os
import time
import uuid
from datetime import datetime, timezone

import psycopg
from flask import Flask, g, jsonify, request


class JsonFormatter(logging.Formatter):
    """Format application logs as one JSON object per line."""

    def format(self, record):
        log_entry = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "level": record.levelname,
            "logger": record.name,
            "message": record.getMessage(),
        }

        optional_fields = (
            "event",
            "request_id",
            "method",
            "path",
            "status_code",
            "duration_ms",
            "remote_addr",
            "error_type",
        )

        for field in optional_fields:
            value = getattr(record, field, None)
            if value is not None:
                log_entry[field] = value

        return json.dumps(log_entry, separators=(",", ":"))


app = Flask(__name__)

log_handler = logging.StreamHandler()
log_handler.setFormatter(JsonFormatter())

app.logger.handlers.clear()
app.logger.addHandler(log_handler)
app.logger.setLevel(os.getenv("LOG_LEVEL", "INFO").upper())
app.logger.propagate = False


@app.before_request
def start_request():
    supplied_request_id = request.headers.get("X-Request-ID", "").strip()

    g.request_id = supplied_request_id[:128] or uuid.uuid4().hex
    g.request_start_time = time.perf_counter()


@app.after_request
def log_request(response):
    duration_ms = round(
        (time.perf_counter() - g.request_start_time) * 1000,
        2,
    )

    response.headers["X-Request-ID"] = g.request_id

    app.logger.info(
        "request_completed",
        extra={
            "event": "http_request",
            "request_id": g.request_id,
            "method": request.method,
            "path": request.path,
            "status_code": response.status_code,
            "duration_ms": duration_ms,
            "remote_addr": request.remote_addr,
        },
    )

    return response


@app.get("/")
def index():
    return jsonify(service="devops-practice", version="1.0.0")


@app.get("/health")
def health():
    return jsonify(status="alive"), 200


@app.get("/ready")
def ready():
    if os.getenv("APP_READY", "true").lower() != "true":
        return jsonify(status="not_ready", reason="disabled"), 503

    if not os.getenv("DB_HOST"):
        return jsonify(status="ready", database="not_configured"), 200

    try:
        with psycopg.connect(
            host=os.environ["DB_HOST"],
            port=os.getenv("DB_PORT", "5432"),
            dbname=os.environ["DB_NAME"],
            user=os.environ["DB_USER"],
            password=os.environ["DB_PASSWORD"],
            connect_timeout=3,
            options="-c statement_timeout=3000",
        ) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT 1")
                cur.fetchone()

        return jsonify(status="ready", database="connected"), 200

    except psycopg.Error as exc:
        app.logger.warning(
            "Database readiness failed: %s",
            type(exc).__name__,
        )
        return jsonify(status="not_ready", database="unavailable"), 503