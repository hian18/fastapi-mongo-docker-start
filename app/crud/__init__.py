import uuid
from typing import TypeVar, Generic, List
from pydantic import BaseModel

T = TypeVar("T")
X = TypeVar("X")


class Crud(Generic[T]):
    def __init__(self, model_create: X, model_in_db, model_out: T, collection: str):

        self.model_create = model_create
        self.model_in_db = model_in_db
        self.model_out = model_out
        self.collection = collection

    async def create(self, db, documento, id=None) -> T:
        value = documento.dict()
        if id:
            value["ID"] = uuid.UUID(id)
        else:
            value["ID"] = uuid.uuid4()
        result = await db[self.collection].insert_one(value)
        return self.model_out(**value)

    async def get_all(self, db) -> List[T]:
        values = []
        async for x in db[self.collection].find():
            values.append(self.model_out(**x))
        return values

    async def get_one(self, db, item_id) -> T:
        result = await db[self.collection].find_one({"ID": uuid.UUID(item_id)})
        return self.model_out(**result)

    async def delete(self, db, item_id):
        await db[self.collection].find_one_and_delete({"ID": uuid.UUID(item_id)})

    async def update(self, db, item_id: str, documento) -> T:
        result = await self.delete(db, item_id)
        return await self.create(db, documento, id)
