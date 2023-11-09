#!/usr/bin/env python3
"""
Route module for the API
"""
from os import getenv
from typing import List
from api.v1.views import app_views
from flask import Flask, jsonify, abort, request
from flask_cors import (CORS, cross_origin)


app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})
auth = None
auth_type = getenv("AUTH_TYPE", "")


if auth_type == "auth":
    from api.v1.auth.auth import Auth
    auth = Auth()
elif auth_type == "basic_auth":
    from api.v1.auth.basic_auth import BasicAuth
    auth = BasicAuth()
elif auth_type == "session_auth":
    from api.v1.auth.session_auth import SessionAuth
    auth = SessionAuth()
elif auth_type == "session_exp_auth":
    from api.v1.auth.session_exp_auth import SessionExpAuth
    auth = SessionExpAuth()


@app.errorhandler(404)
def not_found(error) -> str:
    """ Not found handler
    """
    return jsonify({"error": "Not found"}), 404


@app.errorhandler(401)
def not_authed(error) -> str:
    """Not authenticated handler
    """
    return jsonify({"error": "Unauthorized"}), 401


@app.errorhandler(403)
def forbidden(error) -> str:
    """Not authorized handler
    """
    return jsonify({"error": "Forbidden"}), 403


@app.before_request
def middleware() -> None:
    """Middleware to run before every request
    """
    excluded_paths: List[str] = ['/api/v1/status/',
                                 "/api/v1/auth_session/login/",
                                 '/api/v1/unauthorized/', '/api/v1/forbidden/']

    if auth is None:
        return None
    if not auth.require_auth(request.path, excluded_paths):
        return None
    if not auth.authorization_header(request)\
            and not auth.session_cookie(request):
        return abort(401)
    u = auth.current_user(request)
    if not u:
        return abort(403)
    request.current_user = u
    return None


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)
