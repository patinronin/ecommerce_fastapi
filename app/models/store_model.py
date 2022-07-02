from sqlalchemy import Column, Integer, String
from db import Base

class Store(Base):
    __tablename__ = "stores"

    id = Column(Integer, primary_key=True, index=True)
    description = Column(String)
    warehouse_location = Column(String)
    store_name = Column(String)
