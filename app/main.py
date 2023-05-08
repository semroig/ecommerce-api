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
        max_length=50,
        example = "Xiaomi"
    )

class Category(BaseModel):
    id: int
    name: str = Field(
        title="The name of the category",
        description="The name has a maximum length of 30 characters",
        max_length=30,
        example = "Mobile phone"
    )

class Product(BaseModel):
    id: int
    name: str = Field(
        title="The name of the product",
        description="The name has a maximum length of 50 characters",
        max_length=50,
        example = "POCO M3"
    )
    price: condecimal(
        gt = 0,
        max_digits = 2
    )
    brandId: int = Field(
        title="The id of the brand record",
        description="The brand record needs to be already created"
    )
    categoryId: int = Field(
        title="The id of the category record",
        description="The category record needs to be already created"
    )

#### I declare all the endpoints ###

@app.get("/", response_model = dict)
def read_root() -> dict:
    return {"Hello": "World"}

# This route receives query params to filter search
@app.get("/products", response_model = list[Product])
def read_products(
    brand: Union[str, None] = None,
    category: Union[str, None] = None,
    name: Union[str, None] = None
):
    return {"Hello": "World"}

@app.post("/products", response_model = Product)
def create_product(product: Product):
    return {"Hello": "World"}

@app.get("/products/{item_id}", response_model = Product)
def read_product(item_id: int):
    return {"Hello": "World"}

@app.get("/brands", response_model = list[Brand])
def read_brands():
    return {"Hello": "World"}

@app.get("/categories", response_model = list[Category])
def read_categories():
    return {"Hello": "World"}