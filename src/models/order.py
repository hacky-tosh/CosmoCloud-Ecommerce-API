import uuid
from typing import Optional
from pydantic import BaseModel,Field,validator
from typing import List
from .product import Product
from datetime import datetime


class Item(BaseModel):
    productId: int = Field(gt=0)
    boughtQuantity: int = Field(gt=0)

class UserAddress(BaseModel):
    city: str
    country: str
    zipCode: str

class Order(BaseModel):
    timestamp: str
    items: List[Item]
    totalAmount: float 
    userAddress: UserAddress
    class Config:
        orm_mode = True
        allow_population_by_field_name = True