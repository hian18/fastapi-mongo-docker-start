from pydantic import BaseModel, Field
from typing import Optional, Any
from bson import ObjectId
import uuid
import datetime


class UserBase(BaseModel):
    name: str
    email: str


class UserInDb(UserBase):
    ID: uuid.UUID = Field(default_factory=uuid.uuid4)
    created_at: datetime.datetime = Field(default_factory=datetime.datetime.now)
    hashed_password: str = ""


class UserCreate(UserBase):
    password: str


class UserOut(UserBase):
    ID: uuid.UUID
