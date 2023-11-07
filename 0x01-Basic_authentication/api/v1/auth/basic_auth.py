#!/usr/bin/env python3
"""Basic auth module for the app
"""
from typing import List, Optional, TypeVar
from flask import Request


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

    def authorization_header(
            self, request: Optional[Request] = None) -> Optional[str]:
        """Returns the authorization headers
        """
        if request is None:
            return None
        return request.headers.get("Authorization")

    def current_user(self, request=None) -> TypeVar('User'):
        """Returns the current User
        """
        return None
