#!/usr/bin/env python3
""" Module of Users views
"""
from os import getenv
from typing import List
from api.v1.views import app_views
from flask import jsonify, request
from models.user import User


@app_views.route("/auth_session/login", methods=["POST"], strict_slashes=False)
def login():
    """Logs a user into the application
    """
    email = request.form.get("email")
    pwd = request.form.get("password")

    if not email:
        return jsonify({"error": "email missing"}), 400
    if not pwd:
        return jsonify({"error": "password missing"}), 400

    users: List[User] = User.search({"email": email})
    if not users or len(users) == 0:
        return jsonify({"error": "no user found for this email"}), 404

    res = list(filter(lambda u: u.is_valid_password(pwd), users))
    if len(res) == 0:
        return jsonify({"error": "wrong password"}), 401

    from api.v1.app import auth
    sesh_id = auth.create_session(res[0].id)
    out = jsonify(res[0].to_json())
    out.set_cookie(getenv("SESSION_NAME"), sesh_id)
    return out
