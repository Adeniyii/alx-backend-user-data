#!/usr/bin/env python3
"""Session auth module for the app
"""
from flask.json import uuid
from api.v1.auth.auth import Auth


class SessionAuth(Auth):
    """Implements session authentication
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """Create a session for the user.
        """
        if not isinstance(user_id, str):
            return None
        sesh_id = str(uuid.uuid4())
        type(self).user_id_by_session_id[sesh_id] = user_id
        return sesh_id
