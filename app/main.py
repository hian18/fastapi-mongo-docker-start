from fastapi import FastAPI
from .routers import user, items

app = FastAPI()


app.include_router(
    user.router, prefix="/users", tags=["users"],
)

app.include_router(
    items.router, prefix="/items", tags=["items"],
)
