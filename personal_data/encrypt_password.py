#!/usr/bin/env python3
"""encrypt_password.py"""

import bcrypt


def hash_password(password: str) -> bytes:
    """Hashes a password using bcrypt and returns the hashed password."""
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed


def is_valid(hashed_password: bytes, password: str) -> bool:
    """Validates a password against a given hashed password."""
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
