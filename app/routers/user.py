from fastapi import APIRouter, Depends
from ..models.user import UserCreate, UserOut, UserInDb
from ..crud import Crud
from ..database import get_db

router = APIRouter()

crud = Crud(UserCreate, UserInDb, UserOut, "users")


@router.post("/")
async def create_user(obj: UserCreate, db=Depends(get_db)):
    obj_created = await crud.create(db, obj)
    return obj_created


@router.put("/{id}")
async def update_user(id, obj: UserCreate, db=Depends(get_db)):
    obj_created = await crud.update(db, id, obj)
    return obj_created


@router.get("/{id}")
async def list_users(id, db=Depends(get_db)):
    result = await crud.get_one(db, id)
    return result


@router.delete("/{id}")
async def delete_user(id, db=Depends(get_db)):
    result = await crud.delete(db, id)
    return result


@router.get("/")
async def get_all_users(db=Depends(get_db)):
    result = await crud.get_all(db)
    return result
