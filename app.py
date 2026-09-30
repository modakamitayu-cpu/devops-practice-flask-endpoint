import os
from flask import Flask, jsonify

import psycopg

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

    # is_ready = os.getenv("APP_READY", "true").lower() == "true"
    # status = "ready" if is_ready else "no_ready"
    # return jsonify(status=status), 200 if is_ready else 503

    if os.getenv("APP_READY", "true").lower() != "true":
        return jsonify(status="not_ready", reason="disabled"), 503

    # Preserve standalone operation for labs without a database.
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
            "Database readiness failed: %s", type(exc).__name__
        )
        return jsonify(status="not_ready", database="unavailable"), 503