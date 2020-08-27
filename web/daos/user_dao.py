import logging


def user_exists(username: str, db: any) -> bool:
    user = find_user_by_username(username, db)
    if user.count() == 0:
        return False
    else:
        logging.info("user data {0}".format(user[0]))
        return True


def find_user_by_username(username: str, db: any) -> object:
    users = db['Users']
    return users.find({"Username": username})


def user_update(username: str, db: any, refill_amount: int) -> None:
    users = db['Users']
    users.update({
        "Username": username
    }, {
        "$set": {
            "Tokens": refill_amount
        }
    })


def count_tokens(username: str, db: any):
    return db['Users'].find({
        "Username": username
    })[0]['Tokens']


def create_user(username: str, hash_password: bytes, tokens: int, db: any) -> any:
    inserted = db['Users'].insert({"Username": username, "Password": hash_password, "Tokens": tokens})
    logging.info("inserted with id {0} ".format(inserted))
    return inserted
