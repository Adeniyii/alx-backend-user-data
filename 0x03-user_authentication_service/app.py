#!/usr/bin/env python3
"""Module `app.py` sets up a Flask application.
"""
from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    """Basic home route
    """
    return jsonify({"message": "Wagwan monsieur"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
