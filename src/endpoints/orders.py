from fastapi import APIRouter, Request, status,Query
from typing import List
from src.models.product import Product
from src.models.order import Order
import src.rules.product as product
import src.rules.order as order_rule
from datetime import datetime
from pydantic import BaseModel

router = APIRouter(prefix="/api/orders",tags=["Orders"])

#To create an order
@router.post("/", response_description="Create a Order", status_code=status.HTTP_201_CREATED, response_model=Order)
async def create_book(request: Request, order:Order):
     return order_rule.create_order(request,order)
     
#To get order details by orderId     
@router.get("/{id}",response_description="Get order by order Id",response_model=Order)
def get_order_by_id(request:Request,id:str):
    return order_rule.get_order_by_id(request,id)

# To Get all orders Details
@router.get("/",response_description="Get all Orders",response_model=List[Order])
def get_orders(request:Request,limit: int = Query(10, ge=1), offset: int = Query(0, ge=0)):
     orders = order_rule.get_all_orders(request)
     paginated_orders = orders[offset:offset+limit]   
     return orders 


