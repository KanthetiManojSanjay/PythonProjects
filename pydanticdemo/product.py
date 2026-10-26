from pydantic import BaseModel
from typing import Optional


class Product(BaseModel):
    id: int
    name: str
    price: float
    description: Optional[str] = "No description provided"


p1 = Product(id=101, name="Laptop", price=2000)
print(p1)
print(p1.model_dump()) # dict representation
print(p1.model_dump_json(indent=2)) # json representation
