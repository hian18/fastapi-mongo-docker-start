from pydantic import BaseModel
import uuid


class ItemCreate(BaseModel):
    name: str


class ItemInDb(ItemCreate):
    ID: uuid.UUID
    name: str


class ItemOut(ItemInDb):
    ...

