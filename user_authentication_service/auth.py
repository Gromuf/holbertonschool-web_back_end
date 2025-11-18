#!/usr/bin/env python3
"""Auth module"""

import bcrypt
from db import DB
from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str) -> str:
    """Hash a password using bcrypt"""
    hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    return hashed.decode('utf-8')


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str):
        """Register a new user with email and password"""
        try:
            self._db.find_user_by(email=email)
            raise ValueError("User {} already exists".format(email))
        except NoResultFound:
            hashed_password = _hash_password(password)
            user = self._db.add_user(email, hashed_password)
            return user
