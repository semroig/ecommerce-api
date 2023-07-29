from typing import Union
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

### Initial setup ###

# Create the database tables
models.Base.metadata.create_all(bind=engine)
# Start the app
app = FastAPI()
# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#### I declare all the endpoints ###

# Root route
@app.get("/", response_model = dict)
def read_root() -> dict:
    return {"Hello": "World"}

# Product routes
# This route receives query params to filter search
@app.get("/products", response_model = list[schemas.Product])
def read_products(
    brand: Union[str, None] = None,
    category: Union[str, None] = None,
    name: Union[str, None] = None
):
    return {"Hello": "World"}

@app.post("/products", response_model = schemas.Product)
def create_product(product: schemas.Product):
    return {"Hello": "World"}

@app.get("/products/{item_id}", response_model = schemas.Product)
def read_product(item_id: int):
    return {"Hello": "World"}

# Brand routes
@app.get("/brands", response_model = list[schemas.Brand])
def read_brands():
    return {"Hello": "World"}

# Category routes
@app.get("/categories", response_model = list[schemas.Category])
def read_categories():
    return {"Hello": "World"}

# User routes
@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)

@app.get("/users/", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users

@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user