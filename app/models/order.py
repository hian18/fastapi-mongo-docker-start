from pydantic import BaseModel
from .item import ItemInDb
from typing import List
import uuid
from datetime import datetime


class ItemAmout(BaseModel):
    amount: int
    item_id: uuid.UUID


class OrderCreate(BaseModel):
    items: List[ItemAmout]


class ItemOrder(ItemInDb):
    amount: int


class OrderInDb(BaseModel):
    ID: uuid.UUID
    user_id: uuid.UUID
    state: str
    items: List[ItemOrder]
    create_at: datetime


class OrderOut(OrderInDb):

    total: int = 0

    def dict(self, *args, **kwargs):
        if self.total:
            return super().dict(*args, **kwargs)
        else:
            self.total = self.get_total()
            return super().dict(*args, **kwargs)

    def get_total(self):
        return sum([x.price_cents * x.amount for x in self.items])
