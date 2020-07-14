from .database import get_db
from .crud.item import ItemCrud
from .models import ItemCreate, Item
from fastapi import FastAPI, Depends
from typing import List
import uuid

app = FastAPI()


@app.post("/item")
async def create_item(item: ItemCreate, db=Depends(get_db)):
    item = await ItemCrud.create(db, item)
    return item


@app.put("/item/{id}")
async def update_item(item_id, item: ItemCreate, db=Depends(get_db)):
    created_item = await ItemCrud.update(db, item)
    return item


@app.get("/item/{id}")
async def list_items(item_id, db=Depends(get_db)):
    result = await ItemCrud.get_one(db, item_id)
    return result


@app.delete("/item/{id}")
async def delete_item(item_id, db=Depends(get_db)):
    result = await ItemCrud.delete(db, item_id)
    return result


@app.get("/item")
async def get_all_items(db=Depends(get_db)):
    result = await ItemCrud.get_all(db)
    return result
