#!/usr/bin/env python3
"""
This module defines a private method that hashes the
input password string using bcrypt
"""
import bcrypt


def _hash_password(password: str) -> bytes:
    """ Hashes the input password string using bcrypt"""
    salt = bcrypt.gensalt()
    hashed_pwd = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_pwd
