import os
from typing import Dict

from flask import Flask
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
csrf = CSRFProtect()
csrf.init_app(app)


@app.route("/", methods=["GET"])
def home() -> str:
    return "App is running!"


@app.route("/health/ready", methods=["GET"])
def liveness_probe() -> Dict[str, str]:
    return {"status": "ok"}


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 3000))  # Explicitly cast to int
    app.run(port=port, host="0.0.0.0")
