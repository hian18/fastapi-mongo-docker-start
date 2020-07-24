from fastapi import APIRouter, Depends
from ..models.user import UserCreate, UserOut, UserInDb
from ..crud.user_crud import UserCrud
from ..crud.oder_crud import OrderCrud
from ..database import get_db
from .. import auth
from passlib.context import CryptContext
from enum import Enum

router = APIRouter()

crud = UserCrud()
order_crud = OrderCrud()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class PathsEnum(str, Enum):
    orders = "orders"
    me = "me"


@router.get("/{path}/")
async def get_me(
    path: PathsEnum, db=Depends(get_db), user=Depends(auth.get_current_user)
):
    if path == PathsEnum.me:
        return UserOut(**user.dict())
    if path == PathsEnum.orders:
        result = await order_crud.get_orders_by_user(db, user.ID)
        return result
    raise Exception("notFoud")


@router.get("/orders/")
async def get_my_orders(user=Depends(auth.get_current_user)):
    order_crud.get_orders_by_user(user.ID)
    return UserOut(**user.dict())


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
async def list_users(id: str, db=Depends(get_db)):
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

