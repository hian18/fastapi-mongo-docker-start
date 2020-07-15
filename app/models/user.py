from pydantic import BaseModel
from typing import Optional, Any
from bson import ObjectId
import uuid
import datetime


class Item(BaseModel):
    id: uuid.UUID
    name: str


class ItemCreate(BaseModel):
    name: str


class UserBase(BaseModel):
    name: str
    email: str


class UserInDb(UserBase):
    ID: uuid.UUID
    created_at: datetime.datetime
    password: str


class UserCreate(UserBase):
    password: str


class UserOut(UserBase):
    ID: uuid.UUID
