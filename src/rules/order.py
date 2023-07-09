from fastapi import Request, HTTPException, status
from fastapi.encoders import jsonable_encoder
from bson import ObjectId
from src.models.product import Product
from src.models.order import Order
from datetime import datetime
import src.rules.product as product_rule

def get_collection_orders(request):
    return request.app.database['orders']

def get_order_by_id(request:Request,id:str):
    order = get_collection_orders(request).find_one({"_id":ObjectId(id)}) 
    return order

def get_all_orders(request:Request,):
    orders = list(get_collection_orders(request).find())
    return orders

def create_order_in_db(request:Request,order:Order,total_amount:float):
    order = jsonable_encoder(order)
    order["totalAmount"] = total_amount
    new_order = get_collection_orders(request).insert_one(order)
    created_new_order = get_collection_orders(request).find_one({"_id":new_order.inserted_id})
    return created_new_order
   
def create_order(request:Request,order:Order):
    order.timestamp = datetime.now()
    total_order_amount = 0.0
    for item in order.items:
        product = product_rule.get_product_by_id(request,item.productId)
        print(product)
        if product is None:
            return {"message":f"product not found: {item.productId}"}
        total_order_amount += product["price"] * item.boughtQuantity
        product["available_quantity"] -= item.boughtQuantity

    created_order = create_order_in_db(request,order,total_order_amount)
    return created_order

        
