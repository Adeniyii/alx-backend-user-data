#!/usr/bin/env python3
"""Basic auth module for the app
"""
from base64 import b64decode
from typing import List, TypeVar

from api.v1.auth.auth import Auth
from models.user import User


class BasicAuth(Auth):
    """Implements basic authentication
    """

    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """Return encoded authorization header value
        """
        if not isinstance(authorization_header, str):
            return None
        basic, hash, *_ = authorization_header.split(" ") + [" ", "meh"]
        if basic != "Basic":
            return None
        return hash

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """Decode base64 encoded auth credentials
        """
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            decoded = b64decode(base64_authorization_header)
        except Exception:
            return None
        else:
            return decoded.decode("utf-8")

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        """Return username and password from auth header
        """
        if not isinstance(decoded_base64_authorization_header, str):
            return None, None
        cred = decoded_base64_authorization_header.split(":")
        if len(cred) != 2:
            return None, None
        return cred[0], cred[1]

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """Returns a matching user.
        """
        if not isinstance(user_email, str) or not isinstance(user_pwd, str):
            return None
        user = User(email=user_email, password=user_pwd)
        found = user.search({"email": user_email})
        if len(found) < 1:
            return None
        if not found[0].is_valid_password(user_pwd):
            return None
        return found[0]
