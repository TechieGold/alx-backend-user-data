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
        if path is None or excluded_paths is None or len(excluded_paths) == 0:
            return True

        if path[-1] != '/':
            path += '/'

        for paths in excluded_paths:
            if paths.endswith('*'):
                if path.startswith(paths[:-1]):
                    return False
            elif path == paths:
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """
        Extract the authorization header from the request.

        Args:
            request (flask.Request): The Flask request object.

        Returns:
            str: The authorization header value, or None if not present.
        """
        if request is None or 'Authorization' not in request.headers:
            return None
        return request.headers['Authorization']

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
