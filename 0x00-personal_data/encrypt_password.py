#!/usr/bin/env python3
"""`encrypt_password.py` contains a hash_password function."""

import bcrypt


def hash_password(password: str) -> bytes:
    """returns a salted, hashed password, which is a byte string."""
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())


if __name__ == "__main__":
    password = "MyAmazingPassw0rd"
    print(hash_password(password))
    print(hash_password(password))
