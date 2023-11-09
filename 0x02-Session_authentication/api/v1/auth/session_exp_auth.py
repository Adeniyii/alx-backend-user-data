#!/usr/bin/env python3
"""Session auth module for the app
"""
import os
import datetime
from api.v1.auth.session_auth import SessionAuth


class SessionExpAuth(SessionAuth):
    """Implements expiring session authentication
    """
    def __init__(self) -> None:
        super().__init__()
        self.session_duration = int(os.getenv("SESSION_DURATION", 0))

    def create_session(self, user_id: str = None) -> str:
        """Creates a Session ID for a user_id
        """
        session_id = super().create_session(user_id)
        if session_id is None:
            return None
        self.user_id_by_session_id[session_id] = {
            "user_id": user_id,
            "created_at": datetime.datetime.now()
        }
        return session_id

    def user_id_for_session_id(self, session_id=None):
        """Returns a User ID based on a Session ID
        """
        if session_id is None:
            return None

        seshObj = self.user_id_by_session_id.get(session_id)
        if seshObj is None:
            return None

        createdAt = seshObj.get("created_at")
        if createdAt is None:
            return None

        exp = datetime.timedelta(seconds=self.session_duration) + createdAt
        if exp < datetime.datetime.now():
            return None

        return seshObj.get("user_id")
