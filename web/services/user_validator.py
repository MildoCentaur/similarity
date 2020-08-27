from bcrypt import hashpw

from daos.user_dao import user_exists, find_user_by_username
from services.database import DataBase

SECRET = "abc123"


def is_valid_user(username: str) -> bool:
    return user_exists(username, DataBase.get_instance())


def is_valid_admin(password: str) -> bool:
    if password != SECRET:
        return False
    else:
        return True


def authenticate(username: str, password: str) -> bool:
    if not is_valid_user(username):
        return False

    hashed_password = find_user_by_username(username, DataBase.get_instance())[0]["Password"]

    if hashed_password == hashpw(password.encode("utf8"), hashed_password):
        return True
    else:
        return False


def has_tokens(username: str) -> bool:
    return find_user_by_username(username, DataBase.get_instance())[0]["Tokens"] > 0
