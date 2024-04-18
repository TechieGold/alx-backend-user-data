#!/usr/bin/env python3
""" This module contains a class BasicAuth that inherits from Auth.
"""
from api.v1.auth.auth import Auth
from models.user import User
import base64
from typing import TypeVar


class BasicAuth(Auth):
    """
    This class Provides basic authentication-related functionality for the API.
    It inherits from Auth.
    """

    def extract_base64_authorization_header(self, authorization_header:
                                            str) -> str:
        """ Extract the Base64 part of the Authorization header
        for Basic Authentication

        Args:
            authorization_header: The Authorization header value.
        Returns:
            str: The Base64 part of the Authorization header,
            or None if not valid.

        """
        if authorization_header is None or not isinstance(authorization_header,
                                                          str):
            return None

        if not authorization_header.startswith("Basic "):
            return None

        token = authorization_header.split(" ")[1]
        return token

    def decode_base64_authorization_header(self, base64_authorization_header:
                                           str) -> str:
        """ Decode the Base64 authorization header to UTF-8 string.

        Args:
            base64_authorization_header (str): The Base64 encoded
            authorization header.

        Returns:
            str: The decoded value as UTF-8 string, or None if not valid.
        """
        if base64_authorization_header is None and not isinstance(
                base64_authorization_header, str):
            return None

        try:
            decoded_bytes = base64.b64decode(base64_authorization_header)
            decoded_str = decoded_bytes.decode('utf-8')

            return decoded_str

        except Exception:
            return None

    def extract_user_credentials(self, decoded_base64_authorization_header:
                                 str) -> (str, str):
        """
        Extract the user email and password from the Base64 decoded
        authorization header.

        Args:
            decoded_base64_authorization_header (str): The Base64 decoded
            authorization header.

        Returns:
            tuple: A tuple containing the user email and password,
            or (None, None) if not valid.
        """

        if decoded_base64_authorization_header is None or not isinstance(
                decoded_base64_authorization_header, str):
            return None, None

        if ':' not in decoded_base64_authorization_header:
            return None, None

        user_email, user_passwd = decoded_base64_authorization_header.split(
            ':', 1)
        return user_email, user_passwd

    def user_object_from_credentials(self, user_email: str, user_pwd:
                                     str) -> TypeVar('User'):
        """
        Get the User instance based on email and password.

        Args:
            user_email (str): The email of the user.
            user_pwd (str): The password of the user.

        Returns:
            TypeVar('User'): The User instance,
            or None if not found or invalid credentials.
        """
        if user_email is None or not isinstance(user_email, str):
            return None
        if user_pwd is None or not isinstance(user_pwd, str):
            return None

        try:
            users = User.search({"email": user_email})
            if not users or users == []:
                return None

            for user in users:
                if user.is_valid_password(user_pwd):
                    return user
            return None

        except Exception:
            return None
