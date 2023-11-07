#!/usr/bin/env python3
"""Basic auth module for the app
"""
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
