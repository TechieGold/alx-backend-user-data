#!/usr/bin/env python3
""" This module contains a class SessionAuth that inherits from Auth.
"""
from api.v1.auth.auth import Auth
import uuid


class SessionAuth(Auth):
    """
    This class Provides basic authentication-related functionality for the API.
    It inherits from Auth.
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """ Create a Session ID for a user. """
        if user_id is None or not isinstance(user_id, str):
            return

        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id

        return (session_id)
