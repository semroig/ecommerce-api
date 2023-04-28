from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel, Field, condecimal

# Start the app
app = FastAPI()

### I declare all the models ###

class Brand(BaseModel):
    id: int
    name: str = Field(
        title="The name of the brand",
        description="The name has a maximum length of 50 characters",
        max_length=50
    )

class Category(BaseModel):
    id: int
    name: str = Field(
        title="The name of the category",
        description="The name has a maximum length of 30 characters",
        max_length=30
    )

class Product(BaseModel):
    id: int
    name: str = Field(
        title="The name of the product",
        description="The name has a maximum length of 50 characters",
        max_length=50
    )
    price: condecimal(
        # title="The price of the product",
        # description="The price has to be greater than 0, and has a maximum number of 2 digits within the decimal",
        gt = 0,
        max_digits = 2
    )
    brand: Brand
    category: Category

#### I declare all the endpoints ###

@app.get("/")
def read_root():
    return {"Hello": "World"}

# This route receives query params to filter search
@app.get("/products")
def read_products(
    brand: Union[str, None] = None,
    category: Union[str, None] = None,
    name: Union[str, None] = None
):
    return {"Hello": "World"}

@app.post("/products")
def create_product(product: Product):
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