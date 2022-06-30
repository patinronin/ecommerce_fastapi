from pydantic import BaseModel

class Store(BaseModel):
    description: str
    warehouse_location: str
    store_name: str


    class Config:
        orm_mode = True