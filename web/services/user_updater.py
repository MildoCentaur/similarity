from bcrypt import hashpw, gensalt

from daos.user_dao import user_update, count_tokens, create_user
from services.database import DataBase


def update_tokens(username: str, refil_amount: int) -> None:
    return user_update(username, DataBase.get_instance(), refil_amount)


def decrease_tokens(username: str) -> None:
    refill_amount = count_tokens(username, DataBase.get_instance()) - 1
    return update_tokens(username, refill_amount)


def new_user(username: str, password: str, tokens: int = 6):
    hashed_password = hashpw(password.encode("utf8"), gensalt())
    return create_user(username, hashed_password, tokens, DataBase.get_instance())
