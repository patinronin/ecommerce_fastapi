from pydantic import BaseModel


class ProductBase(BaseModel):
    description: str
    quantity: int
    product_name: str
    price: float



class ProductCreate(ProductBase):
    pass


class Product(ProductBase):
    id: int
    store_id: int

    class Config:
        orm_mode = True
