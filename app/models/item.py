from pydantic import BaseModel
import typing
import uuid
import ujson


class ItemCreate(BaseModel):
    name: str
    price_cents: int
    description: str

    class Config:
        json_loads = ujson.loads


class ItemInDb(ItemCreate):
    ID: uuid.UUID
    name: str


class ItemOut(ItemInDb):
    ...
