from fastapi import APIRouter, Request, status
from typing import List
from src.models.product import Product

import src.rules.product as product_rule

router = APIRouter(prefix="/api/products",tags=["Products"])


#To list all products
@router.get("/", response_description="List all product", response_model=List[Product])
def list_product(request:Request):
    return product_rule.list_products(request)


#To get the product by Id
@router.get("/{id}", response_description="Get by id", response_model=Product)
def get_product_by_id(request:Request,id:int):
    product = product_rule.get_product_by_id(request,id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

#To update the product
@router.patch("/{id}", response_description="Update Product", response_model=Product)
def update_product(request:Request,id: int, updated_product: Product):
    product = product_rule.get_product_by_id(request,id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    
    product["available_quantity"] = updated_product.available_quantity
    update_product = product_rule.update_product_quantity(request,product,id)
    return updated_product

