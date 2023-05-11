from pydantic import BaseModel, Field, condecimal

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
class UserBase(BaseModel):
    username: str
    email: str
    full_name: str | None = None
    is_active: bool

class UserIn(UserBase):
    password: str

class UserOut(UserBase):
    pass

class UserInDB(UserBase):
    hashed_password: str