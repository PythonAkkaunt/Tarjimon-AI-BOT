from playhouse.shortcuts import model_to_dict

from data.config import ADMINS
from handlers.users import users
from .models import *


async def add_user(user_id: int, username: str):
    with db:
        if not Users.select().where(Users.user_id == user_id).exists():
            Users.create(user_id=user_id, username=username)


async def count_users():
    with db:
        return Users.select().count()


async def get_users_id():
    with db:
        users = [model_to_dict(item) for item in Users.select(Users.user_id)]
        return users
