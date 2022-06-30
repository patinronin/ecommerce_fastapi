from pydantic import BaseModel

class User(BaseModel):
    user_name: str
    email: str
    password: str
    age: int

    class Config:
        orm_mode = True