#!/usr/bin/env python3
""" Session authentication
"""
from api.v1.auth.session_exp_auth import SessionExpAuth


class SessionDBAuth(SessionExpAuth):
		"""SessionDBAuth class
		"""
		def create_session(self, user_id=None):
			"""Create a session
			"""
			session_id = super().create_session(user_id)
			if session_id is None:
				return None
			from models.user_session import UserSession
			UserSession(user_id=user_id, session_id=session_id).save()
			return session_id
