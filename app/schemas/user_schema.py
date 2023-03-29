from pydantic import BaseModel
from schemas.direction_schema import DirectionUser
class UserBase(BaseModel):
    user_name: str
    email: str

class UserCreate(UserBase):
    age: int
    password: str

class UserLogin(UserBase):
    pass

class User(UserBase):
    id: int
    password: str
    age: int
    directions: list[DirectionUser] = []


    class Config:
        orm_mode = True