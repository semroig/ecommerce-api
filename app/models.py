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

class Adress(Base):
    __tablename__ = "Adresses"

    id = Column(Integer, primary_key=True, index=True)
    adress_line = Column(String, index=True)
    city = Column(String, index=True)
    state = Column(String, index=True)
    postal_code = Column(Integer, index=True)
    user_id = Column(Integer, ForeignKey("Users.id"))

    user = relationship("User", back_populates="adresses")

class Order(Base):
    __tablename__ = "Orders"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(String, index=True)
    user_id = Column(Integer, ForeignKey("Users.id"))

    user = relationship("User", back_populates="adresses")

class OrderItem(Base):
    __tablename__ = "OrderItems"

    id = Column(Integer, primary_key=True, index=True)
    quantity = Column(Integer, index=True)
    unit_price = Column(Float, index=True)
    order_id = Column(Integer, ForeignKey("Orders.id"))
    product_id = Column(Integer, ForeignKey("Products.id"))

    order = relationship("Order", back_populates="order_items")
    product = relationship("Product", back_populates="order_items")

class Shipment(Base):
    __tablename__ = "Shipments"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(String, index=True)
    order_id = Column(Integer, ForeignKey("Orders.id"))
    adress_id = Column(Integer, ForeignKey("Adresses.id"))

    order = relationship("Order", back_populates="shipments")
    adress = relationship("Adress", back_populates="shipments")