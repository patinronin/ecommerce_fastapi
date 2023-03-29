from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from db import Base



class Product(Base):
    __tablename__ = "products"
    print("creating products table")

    id = Column(Integer, primary_key=True, index=True)
    description = Column(String)
    quantity = Column(Integer)
    product_name = Column(String)
    price = Column(Float)

    store_id = Column(Integer, ForeignKey("stores.id"))
    owner_store = relationship("Store", back_populates="products")
