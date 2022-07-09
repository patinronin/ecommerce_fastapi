from pydantic import BaseModel

from schemas.product_schema import Product

class StoreBase(BaseModel):
    description: str
    warehouse_location: str
    store_name: str


class Store(StoreBase):
    id: int
    products: list[Product] = []


    class Config:
        orm_mode = True