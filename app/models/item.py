from pydantic import BaseModel
from typing import Optional, Any
from bson import ObjectId
import uuid
import datetime


class ItemCreate(BaseModel):
    name: str


class ItemInDb(ItemCreate):
    id: uuid.UUID
    name: str


class ItemOut(ItemInDb):
    ...

