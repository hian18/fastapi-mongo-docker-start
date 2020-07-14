from pydantic import BaseModel
from typing import Optional, Any
from bson import ObjectId
import uuid


class Item(BaseModel):
    id: uuid.UUID
    name: str
    

class ItemCreate(BaseModel):
    name: str

