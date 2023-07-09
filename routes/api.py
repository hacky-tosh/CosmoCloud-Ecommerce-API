from fastapi import APIRouter
from src.endpoints import product,orders

router = APIRouter()

router.include_router(product.router)
router.include_router(orders.router)
