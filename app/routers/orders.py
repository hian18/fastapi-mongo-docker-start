from fastapi import APIRouter, Depends
from ..models.order import OrderCreate, OrderInDb, OrderOut
from ..crud.oder_crud import OrderCrud
from ..database import get_db
from typing import List

router = APIRouter()

crud = OrderCrud(OrderCreate, OrderInDb, OrderOut, "orders")


@router.post("/", response_model=OrderOut)
async def create_order(item: OrderCreate, db=Depends(get_db)):
    item = await crud.create(db, item)
    return item


@router.put("/{id}", response_model=OrderOut)
async def update_order(id, item: OrderCreate, db=Depends(get_db)):
    created_order = await crud.update(db, id, item)
    return item


@router.get("/{id}", response_model=OrderOut)
async def get_one_order(id, db=Depends(get_db)):
    result = await crud.get_one(db, id)
    return result


@router.delete("/{id}")
async def delete_order(id, db=Depends(get_db)):
    result = await crud.delete(db, id)
    return result


@router.get("/", response_model=List[OrderOut])
async def list_orders(db=Depends(get_db)):
    result = await crud.get_all(db)
    return result
