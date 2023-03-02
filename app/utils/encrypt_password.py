from passlib.handlers.bcrypt import bcrypt


def encrypt_password(pasword: str):
    return bcrypt.hash(pasword)
