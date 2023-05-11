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


# Revisar los siguientes models
class UserIn(BaseModel):
    username: str
    password: str
    email: str
    full_name: str | None = None


class UserOut(BaseModel):
    username: str
    email: str
    full_name: str | None = None


class UserInDB(BaseModel):
    username: str
    hashed_password: str
    email: str
    full_name: str | None = None

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


# Reemplazar las siguientes funciones por lógica correcta
def fake_password_hasher(raw_password: str):
    return "supersecret" + raw_password

def fake_save_user(user_in: UserIn):
    hashed_password = fake_password_hasher(user_in.password)
    # Next line "unwraps" the dict and add the hashed_password pair
    user_in_db = UserInDB(**user_in.dict(), hashed_password=hashed_password)
    print("User saved! ..not really")
    return user_in_db

@app.post("/user", response_model = UserOut)
def create_user(user_in: UserIn):
    user_saved = fake_save_user(user_in)
    return user_saved