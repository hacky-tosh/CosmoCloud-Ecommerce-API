import uuid
from typing import Optional
from pydantic import BaseModel,Field,validator

class Product(BaseModel):
    id:int
    name: str
    price: float
    available_quantity: int
    category: str