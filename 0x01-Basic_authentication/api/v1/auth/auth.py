#!/usr/bin/env python3
""" Auth module for the API
"""
from flask import Request


from typing import List, Optional, TypeVar


class Auth:
    """Authentication class
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Return False True if path requires authentication
        """
        if path and excluded_paths:
            if not path.endswith("/"):
                path += "/"
            return path not in excluded_paths
        return True

    def current_user(self, request=None) -> TypeVar('User'):
        """Returns the current User
        """
        return None
