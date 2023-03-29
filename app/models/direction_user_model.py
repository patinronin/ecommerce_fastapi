from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from db import Base


class DirectionUser(Base):
    __tablename__ = "directionuser"

    id = Column(Integer, primary_key=True, index=True)
    indications = Column(String)
    exterior_number = Column(String)
    interior_number = Column(String)
    postal_code = Column(String)
    street = Column(String)
    colony = Column(String)
    city = Column(String)
    federal_entity = Column(String)
    country = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))
    owner_user = relationship("User", back_populates="directions")
