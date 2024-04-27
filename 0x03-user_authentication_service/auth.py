#!/usr/bin/env python3
"""
This module defines a private method that hashes the
input password string using bcrypt
"""
from user import User
from db import DB

import bcrypt
from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str) -> bytes:
    """ Hashes the input password string using bcrypt"""
    salt = bcrypt.gensalt()
    hashed_pwd = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_pwd


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
