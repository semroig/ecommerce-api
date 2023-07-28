from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship

from .database import Base

class User(Base):
    __tablename__ = "Users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

class Brand(Base):
    __tablename__ = "Brands"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

    products = relationship("Product", back_populates="brand")

class Category(Base):
    __tablename__ = "Categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

    products = relationship("Product", back_populates="category")

class Product(Base):
    __tablename__ = "Products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    price = Column(Float, index=True)
    is_active = Column(Boolean, default=True)
    brand_id = Column(Integer, ForeignKey("Brands.id"))
    category_id = Column(Integer, ForeignKey("Categories.id"))

    brand = relationship("Brand", back_populates="products")
    category = relationship("Category", back_populates="products")