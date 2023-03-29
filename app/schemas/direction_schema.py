from pydantic import BaseModel


class DirectionBase(BaseModel):
    indications: str
    exterior_number: str
    interior_number: str
    postal_code: str
    street: str
    colony: str
    city: str
    federal_entity: str
    country: str
    user_id: int




class DirectionCreate(DirectionBase):
    pass




class DirectionUser(DirectionBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True

class DirectionUserUpdate(DirectionBase):
    user_id: int
    pass
class DirectionStore(DirectionBase):
    id: int
    store_id: int

    class Config:
        orm_mode = True

