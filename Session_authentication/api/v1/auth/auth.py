#!/usr/bin/env python3
""" Module of Auth class
"""
from typing import TypeVar
from flask import request


class Auth:
    """Authentication class
    """

    def require_auth(self, path: str, excluded_paths: list[str]) -> bool:
        """ Determine if a path requires authentication"""
        if path is None:
            return True
        if excluded_paths is None or excluded_paths == []:
            return True
        if not path.endswith('/'):
            path += '/'
        for excluded in excluded_paths:
            if excluded.endswith('*'):
                if path.startswith(excluded[:-1]):
                    return False
            else:
                if not excluded.endswith('/'):
                    excluded += '/'
                if path == excluded:
                    return False
        return True

    def authorization_header(self, request=None) -> str:
        """ Return the Authorization header from the request"""
        if request is None:
            return None
        if request.headers.get('Authorization') is None:
            return None
        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """ Return the current user"""
        return None
