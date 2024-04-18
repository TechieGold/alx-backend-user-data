#!/usr/bin/env python3
""" This module contains a class to manage the API authentication."""

from flask import request
from typing import TypeVar, List


class Auth():
    """ Auth class encapsulating authentication-related functionality."""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Determine whether authentication is required for a given path.

        Args:
            path (str): The path to check.
            excluded_paths (List[str]): List of paths excluded
            from authentication.

        Returns:
            bool: True if authentication is required, False otherwise.
        """
        return False

    def authorization_header(self, request=None) -> str:
        """
        Extract the authorization header from the request.

        Args:
            request (flask.Request): The Flask request object.

        Returns:
            str: The authorization header value, or None if not present.
        """
        if request is None:
            request = request
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Retrieve the current user from the request.

        Args:
            request (flask.Request): The Flask request object.

        Returns:
            TypeVar('User'): The current user, or None if not authenticated.
        """
        if request is None:
            request = request
        return None
