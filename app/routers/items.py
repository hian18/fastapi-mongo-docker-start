from fastapi import APIRouter, Depends
from ..models.item import ItemCreate, ItemOut, ItemInDb
from ..crud import Crud
from ..database import get_db

router = APIRouter()

crud = Crud(ItemCreate, ItemInDb, ItemOut, "items")


@router.post("/")
async def create_item(item: ItemCreate, db=Depends(get_db)):
    item = await crud.create(db, item)
    return item


@router.put("/{id}")
async def update_item(id, item: ItemCreate, db=Depends(get_db)):
    created_item = await crud.update(db, id, item)
    return item


@router.get("/{id}")
async def list_items(id, db=Depends(get_db)):
    result = await crud.get_one(db, id)
    return result


@router.delete("/{id}")
async def delete_item(id, db=Depends(get_db)):
    result = await crud.delete(db, id)
    return result


@router.get("/")
async def get_all_items(db=Depends(get_db)):
    result = await crud.get_all(db)
    return result
