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

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """Reetrive user connected to a given session
        """
        if not isinstance(session_id, str):
            return None
        return type(self).user_id_by_session_id.get(session_id)