from ast import TypeVar
from flask import request

class Auth:
    """Authentication class
    """

    def require_auth(self, path: str, excluded_paths: list[str]) -> bool:
        """ Determine if a path requires authentication"""
        return False


    def authorization_header(self, request=None) -> str:
        """ Return the Authorization header from the request"""
        return None


    def current_user(self, request=None) -> TypeVar('User'):
        """ Return the current user"""
        return None
