from ..database import db
from ..models import Item
from uuid import uuid4
import uuid


class ItemCrud:
    @staticmethod
    async def create(db, documento: Item, id=None) -> Item:
        value = documento.dict()
        if id:
            value["id"] = id
        else:
            value["id"] = uuid4()
        result = await db.items.insert_one(value)
        return Item(**value)

    @staticmethod
    async def get_all(db):
        values = []
        async for x in db.items.find():
            values.append(Item(**x))
        return values

    @staticmethod
    async def get_one(db, item_id) -> Item:
        result = await db.items.find_one({"id": uuid.UUID(item_id)})
        return Item(**result)

    @staticmethod
    async def delete(db, item_id):
        await db.items.find_one_and_delete({"id": uuid.UUID(item_id)})

    @staticmethod
    async def update(db, item_id, documento):
        result = await ItemCrud.delete(db, item_id)
        return await ItemCrud.create(db, documento, id)
