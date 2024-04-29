#!/usr/bin/env python3
"""
This module defines a private method that hashes the
input password string using bcrypt
"""
from user import User
from db import DB

import bcrypt
from sqlalchemy.orm.exc import NoResultFound
import uuid


def _hash_password(password: str) -> bytes:
    """ Hashes the input password string using bcrypt"""
    salt = bcrypt.gensalt()
    hashed_pwd = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_pwd


def _generate_uuid() -> str:
    """ Generate a new UUID and return its string repesentation """
    new_uuid = uuid.uuid4()
    return str(new_uuid)


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """ Register a new user"""

        try:
            self._db.find_user_by(email=email)
        except NoResultFound:
            hashed_pwd = _hash_password(password)
            user = self._db.add_user(email, hashed_pwd)
            return user

        raise ValueError(f"User {email} already exists")

    def valid_login(self, email: str, password: str) -> bool:
        """ Check if the provided email and password form a valid login"""
        try:
            user = self._db.find_user_by(email=email)
            hashed_pwd = user.hashed_password
            input_pwd = password.encode('utf-8')

            return bcrypt.checkpw(input_pwd, hashed_pwd)

        except NoResultFound:
            return False

    def create_session(self, email: str) -> str:
        """ Create a new session for the user and return the session ID. """
        try:
            user = self._db.find_user_by(email=email)
            session_id = _generate_uuid()
            self._db.update_user(user.id, session_id=session_id)
            return session_id
        except NoResultFound:
            return None

    def get_user_from_session_id(self, session_id: str):
        """ Retrive the user corresponding to the session ID"""

        if session_id is None:
            return None

        try:
            user = self._db.find_user_by(session_id=session_id)
            return user
        except NoResultFound:
            return None
