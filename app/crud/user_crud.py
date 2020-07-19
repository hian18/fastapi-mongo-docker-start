from .base import Crud
from ..models.user import UserCreate, UserOut, UserInDb
import uuid
from ..enumerator import StateEnum
import datetime
from typing import Optional
from passlib.context import CryptContext


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class UserCrud(Crud):
    async def create(self, db, user_data: UserCreate, user_id: str = None):

        hash_pwd = pwd_context.hash(user_data.password)
        new_user = UserInDb(**user_data.dict())
        new_user.hashed_password = hash_pwd
        if user_id:
            new_user.ID = uuid.UUID(user_id)

        result = await db.users.insert_one(new_user.dict())
        return UserOut(**new_user.dict())
