from typing import Union
from fastapi import FastAPI

# Start the app
app = FastAPI()


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