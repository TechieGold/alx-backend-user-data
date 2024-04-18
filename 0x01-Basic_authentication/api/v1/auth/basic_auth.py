#!/usr/bin/env python3
""" This module contains a class BasicAuth that inherits from Auth.
"""
from api.v1.auth.auth import Auth
import base64


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
