from sqlalchemy import Column, Integer, String

from db import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    user_name: Column(String)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    age: Column(Integer)




