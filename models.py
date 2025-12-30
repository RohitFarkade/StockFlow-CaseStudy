from pydantic import BaseModel
from decimal import Decimal

class ProductCreate(BaseModel):
    name: str
    sku: str
    price: Decimal
    company_id: int
    warehouse_id: int
    initial_quantity: int
