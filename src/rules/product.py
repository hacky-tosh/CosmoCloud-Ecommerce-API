from fastapi import Request, HTTPException, status
from fastapi.encoders import jsonable_encoder
from bson import ObjectId
from src.models.product import Product


def get_collection_product(request: Request):
  return request.app.database["products"]


def list_products(request:Request):
    product = list(get_collection_product(request).find())
    return product


def get_product_by_id(request:Request,id:int):
   product = get_collection_product(request).find_one({"id":id})
   if product is None:
     return {"message":f"product not found: {item.productId}"}
   return product

def update_product_quantity(request:Request,product:Product,id:int):
    get_collection_product(request).update_one({"id": id},{'$set': product})
    return product

