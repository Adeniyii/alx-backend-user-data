#!/usr/bin/env python3
""" Session authentication
"""
from api.v1.auth.session_exp_auth import SessionExpAuth
import datetime


class SessionDBAuth(SessionExpAuth):
    """SessionDBAuth class"""

    def create_session(self, user_id=None):
        """Create a session"""
        session_id = super().create_session(user_id)
        if session_id is None:
            return None
        from models.user_session import UserSession

        UserSession(user_id=user_id, session_id=session_id).save()
        return session_id

    def user_id_for_session_id(self, session_id=None):
        """Returns a User ID based on a Session ID
        """
        if session_id is None:
            return None

        from models.user_session import UserSession

        sesh_obj_list = UserSession.search({"session_id": session_id})
        if len(sesh_obj_list) == 0:
            return None
        seshObj = sesh_obj_list[0]

        if self.session_duration <= 0 or self.session_duration is None:
            return seshObj.get("user_id")

        createdAt = seshObj.get("created_at")
        if createdAt is None:
            return None

        exp = datetime.timedelta(seconds=self.session_duration) + createdAt
        if exp < datetime.datetime.now():
            return None

        return seshObj.get("user_id")

    def destroy_session(self, request=None):
        """Delete the user session / log out.
        """
        if request is None:
            return False

        sesh_id = self.session_cookie(request)
        if not sesh_id:
            return False

        from models.user_session import UserSession

        sesh_obj_list = UserSession.search({"session_id": sesh_id})
        if len(sesh_obj_list) == 0:
            return False

        seshObj = sesh_obj_list[0]
        seshObj.remove()
        return True
