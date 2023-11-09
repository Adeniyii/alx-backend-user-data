#!/usr/bin/env python3
""" Auth module for the API
"""
from typing import List, TypeVar


class Auth:
    """Authentication class
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Return False True if path requires authentication
        """
        if not path or not excluded_paths:
            return True
        for p in excluded_paths:
            if path == p:
                return False
            if path + "/" == p:
                return False
            if p.endswith("*") and path.startswith(p.rstrip("*")):
                return False
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
