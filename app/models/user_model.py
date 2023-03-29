from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from db import Base


class User(Base):
    __tablename__ = "users"
    print("creating User table")

    id = Column(Integer, primary_key=True, index=True)
    user_name = Column(String)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    age = Column(Integer)
    directions = relationship("DirectionUser", back_populates="owner_user")




