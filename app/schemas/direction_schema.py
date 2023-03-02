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




class DirectionCreate(DirectionBase):
    pass

class DirectionUserUpdate(DirectionBase):
    pass


class DirectionUser(DirectionBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True

class DirectionStore(DirectionBase):
    id: int
    store_id: int

    class Config:
        orm_mode = True

