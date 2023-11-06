#!/usr/bin/env python3
""" Auth module for the API
"""


class Auth:
    """Authentication class
    """

    def __init__(self):
        pass

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """"""
        if path and excluded_paths:
            if not path.endswith("/"):
                path += "/"
            return path in excluded_paths
        return True

    def authorization_header(self, request=None) -> str:
        """"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """"""
        return None