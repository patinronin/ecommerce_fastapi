from pydantic import BaseModel

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


    class Config:
        orm_mode = True