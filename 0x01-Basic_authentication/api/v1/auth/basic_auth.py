#!/usr/bin/env python3
"""Basic auth module for the app
"""
from base64 import b64decode
from typing import List, TypeVar


class BasicAuth():
    """Implements basic authentication
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Return False True if path requires authentication
        """
        if path and excluded_paths:
            if not path.endswith("/"):
                path += "/"
            return path not in excluded_paths
        return True

    def authorization_header(self, request=None) -> str:
        """Returns the authorization headers
        """
        if request is not None:
            return request.headers.get('Authorization', None)
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Returns the current User
        """
        return None

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
