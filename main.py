from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


# class Item(BaseModel):
#     name: str
#     price: float
#     is_offer: Union[bool, None] = None

# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}

# @app.put("/items/{item_id}")
# def update_item(item_id: int, item: Item):
#     return {"item_name": item.name, "item_id": item_id}


### A partir de aca API posta ###

# I declare all the models

class Brand(BaseModel):
    id: int
    name: str

class Category(BaseModel):
    id: int
    name: str

class Product(BaseModel):
    id: int
    name: str
    price: int
    brand: Brand
    category: Category

# I declare all the endpoints

@app.get("/")
def read_root():
    return {"Hello": "World"}

# This route receives query params to filter search
@app.get("/products")
def read_products(q: Union[str, None] = None):
    return {"Hello": "World"}

@app.get("/products/{item_id}")
def read_product(item_id: int):
    return {"Hello": "World"}

@app.get("/brands")
def read_brands():
    return {"Hello": "World"}

@app.get("/categories")
def read_categories():
    return {"Hello": "World"}