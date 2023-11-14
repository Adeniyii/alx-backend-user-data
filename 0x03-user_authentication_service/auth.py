#!/usr/bin/env python3
"""Auth module defines authentication utilities.
"""
import bcrypt


def _hash_password(password: str) -> bytes:
    """Hash a password
    """
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
