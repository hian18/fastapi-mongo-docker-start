from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordBearer
from .routers import user, items, orders, auth
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"]
)
app.include_router(
    auth.router, prefix="/login", tags=["auth"],
)
app.include_router(
    user.router, prefix="/users", tags=["users"],
)

app.include_router(
    items.router, prefix="/items", tags=["items"],
)
app.include_router(
    orders.router, prefix="/orders", tags=["orders"],
)
