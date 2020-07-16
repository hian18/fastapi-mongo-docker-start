import uuid
from typing import TypeVar, Generic, List
from pydantic import BaseModel
from fastapi.exceptions import HTTPException
from http import HTTPStatus

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

    async def get_one(self, db, id_) -> T:
        result = await db[self.collection].find_one({"ID": uuid.UUID(id_)})
        if result is None:
            raise HTTPException(
                status_code=HTTPStatus.NOT_FOUND, detail="Item not found"
            )
        return self.model_out(**result)

    async def delete(self, db, id_):
        await db[self.collection].find_one_and_delete({"ID": uuid.UUID(id_)})

    async def update(self, db, id_: str, documento) -> T:
        result = await self.delete(db, id_)
        return await self.create(db, documento, id_)
