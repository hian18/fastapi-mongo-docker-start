from fastapi import APIRouter, Depends
from ..models.user import UserCreate, UserOut, UserInDb
from ..crud.user_crud import UserCrud
from ..database import get_db
from .. import auth
from passlib.context import CryptContext

router = APIRouter()

crud = UserCrud(UserCreate, UserInDb, UserOut, "users")

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


@router.post("/")
async def create_user(obj: UserCreate, db=Depends(get_db)):
    obj_created = await crud.create(db, obj)
    return obj_created


@router.put("/{id}")
async def update_user(
    id, obj: UserCreate, db=Depends(get_db), user=Depends(auth.get_current_user)
):
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


@router.get("-me/")
async def get_me(user=Depends(auth.get_current_user)):
    return UserOut(**user.dict())

