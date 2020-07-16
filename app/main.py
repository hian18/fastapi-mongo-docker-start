from fastapi import FastAPI
from .routers import user, items, orders

app = FastAPI()


app.include_router(
    user.router, prefix="/users", tags=["users"],
)

app.include_router(
    items.router, prefix="/items", tags=["items"],
)
app.include_router(
    orders.router, prefix="/orders", tags=["orders"],
)
