#!/usr/bin/env python3
"""Module `app.py` sets up a Flask application.
"""
from flask import Flask, abort, jsonify, redirect, request
from auth import Auth


AUTH = Auth()
app = Flask(__name__)

SESH_ID = "session_id"


@app.route("/", methods=["GET"], strict_slashes=False)
def home() -> str:
    """ GET /
    Return:
      - a simple json message
    """
    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=["POST"], strict_slashes=False)
def users() -> str:
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
        AUTH.register_user(email=email, password=password)
    except ValueError:
        return jsonify({"message": "email already registered"}), 400

    return jsonify({"email": email, "message": "user created"}), 200


@app.route("/sessions", methods=["POST"], strict_slashes=False)
def login() -> str:
    """ POST /sessions
    Form data:
      - email
      - password
    Return:
      - The account login payload
      - 401 if login credentials are invalid
    """
    email = request.form.get("email")
    password = request.form.get("password")
    is_valid_login = AUTH.valid_login(email, password)

    if not is_valid_login:
        abort(401)

    sesh = AUTH.create_session(email)
    res = jsonify({"email": email, "message": "logged in"})
    res.set_cookie(SESH_ID, sesh)

    return res


@app.route("/sessions", methods=["DELETE"], strict_slashes=False)
def logout():
    """ DELETE /sessions
    Cookie data:
      - session_id
    Return:
      - 403 if session_id matches no user
    Redirect:
      - GET /
    """
    sesh_id = request.cookies.get(SESH_ID)
    user = AUTH.get_user_from_session_id(sesh_id)
    if user is None:
        abort(403)
    AUTH.destroy_session(user.id)
    redirect("/")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
