#!/usr/bin/env python3
"""Module `app.py` sets up a Flask application.
"""
from flask import Flask, jsonify, request
from auth import Auth


AUTH = Auth()
app = Flask(__name__)


@app.route("/", methods=["GET"], strict_slashes=False)
def home() -> str:
    """ GET /
    Return:
      - a simple json message
    """
    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=["POST"], strict_slashes=False)
def users():
    """ POST /users
    Form data:
      - email
      - password
    Return:
      - 200 if created successfully
      - 400 if can't create the new User
    """
    email = request.form.get("email")
    password = request.form.get("password")

    try:
        Auth.register_user(email=email, password=password)
    except ValueError:
        return jsonify({"message": "email already registered"}), 400

    return jsonify({"email": email, "message": "user created"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
