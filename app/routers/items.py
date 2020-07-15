from fastapi import APIRouter, Depends
from ..models.item import ItemCreate, Item
from ..crud import Crud
from ..database import get_db

router = APIRouter()

crud = Crud(ItemCreate, Item, Item, "items")


@router.post("/")
async def create_item(item: ItemCreate, db=Depends(get_db)):
    item = await crud.create(db, item)
    return item


@router.put("/{id}")
async def update_item(item_id, item: ItemCreate, db=Depends(get_db)):
    created_item = await crud.update(db, item)
    return item


@router.get("/{id}")
async def list_items(item_id, db=Depends(get_db)):
    result = await crud.get_one(db, item_id)
    return result


@router.delete("/{id}")
async def delete_item(item_id, db=Depends(get_db)):
    result = await crud.delete(db, item_id)
    return result


@router.get("/")
async def get_all_items(db=Depends(get_db)):
    result = await crud.get_all(db)
    return result
