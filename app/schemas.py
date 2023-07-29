from pydantic import BaseModel, Field, condecimal

# Brand schemas
class BrandBase(BaseModel):
    name: str = Field(
        title="The name of the brand",
        description="The name has a maximum length of 50 characters",
        max_length=50,
        example = "Xiaomi"
    )

class BrandCreate(BrandBase):
    pass

class Brand(BrandBase):
    id: int

# Category schemas
class CategoryBase(BaseModel):
    name: str = Field(
        title="The name of the category",
        description="The name has a maximum length of 30 characters",
        max_length=30,
        example = "Mobile phone"
    )

class CategoryCreate(CategoryBase):
    pass

class Category(CategoryBase):
    id: int

# Product schemas
class ProductBase(BaseModel):
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

class ProductCreate(ProductBase):
    pass

class Product(ProductBase):
    id: int

# Adress schemas
class AdressBase(BaseModel):
    userId: int = Field(
        title="The id of the user record",
        description="The user record needs to be already created"
    )
    adressLine: str = Field(
        title="The adress",
        description="Street adress + department number + ... It has a maximum length of 100 characters",
        max_length=100,
        example = "The Oaks 540, department B"
    )
    city: str = Field(
        title="The name of the city",
        description="The city name has a maximum length of 30 characters",
        max_length=30,
        example = "Palo Alto"
    )
    state: str = Field(
        title = "The name of the State",
        description = "The State name has a maximum length of 30 characters",
        max_length = 30,
        example = "California"
    )
    postalCode: int = Field(
        title = "The number of the postal code",
        description = "The postal code number has a maximum length of 6 digits"

        ## TO DO: max of 6 digits

        # max_length = 50,
        # example = "POCO M3"
    )

class AdressCreate(AdressBase):
    pass

class Adress(AdressBase):
    id: int

# Order schemas
class OrderBase(BaseModel):
    userId: int = Field(
        title="The id of the user record",
        description="The user record needs to be already created"
    )
    ## TO DO: hacerlo tipo date
    date: str = Field(
        title="The date when shipment was placed",
        description="The date when shipment record was created"
    )

class OrderCreate(OrderBase):
    pass

class Order(OrderBase):
    id: int

# OrderItem schemas
class OrderItemBase(BaseModel):
    orderId: int = Field(
        title="The id of the order record",
        description="The order record needs to be already created"
    )
    productId: int = Field(
        title="The id of the product record",
        description="The product record needs to be already created"
    )
    quantity: int = Field(
        title="The quantity ordered for this item"
    )
    unitPrice: condecimal(
        gt = 0,
        max_digits = 2
    )

class OrderItemCreate(OrderItemBase):
    pass

class Order(OrderItemBase):
    id: int

# Shipment schemas
class ShipmentBase(BaseModel):
    adressId: int = Field(
        title="The id of the adress record",
        description="The shipment record needs to be already created"
    )
    orderId: int = Field(
        title="The id of the order record",
        description="The order record needs to be already created"
    )
    ## TO DO: hacerlo tipo date
    date: str = Field(
        title="The date when shipment was placed",
        description="The date when shipment record was created"
    )

class ShipmentCreate(ShipmentBase):
    pass

class Shipment(ShipmentBase):
    id: int

# User schemas
class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True