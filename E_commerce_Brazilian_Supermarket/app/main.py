#importing the necessary libraries
from fastapi import FastAPI, status, HTTPException,Depends

# Both used for BaseModel
from pydantic import BaseModel
from typing import Optional,List

# You need this to be able to turn classes into JSONs and return
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

# Importing sqlalchemy and its dependencies
from sqlalchemy import create_engine,Column, String,Integer,Float,DateTime,ForeignKey
from sqlalchemy.orm import sessionmaker,declarative_base, Session

import json
from os import times
import datetime

#connecting to my dataase
conn = create_engine("mysql+pymysql://{user}:{pw}@localhost:{host}/{db}"
                       .format(user = "user",
                               pw = "password",
                               host = 42333,
                               db = "Brazilian_Supermarket_Sales"))

SessionLocal = sessionmaker(bind=conn, autoflush=False, autocommit=False)
Base = declarative_base()



# -------------------------
# Database Models
# -------------------------
class Customer(Base):
    __tablename__ = "CUSTOMER"

    customer_id = Column(String(50), primary_key=True)
    zip_code = Column(String(20))
    city = Column(String(100))
    state = Column(String(100))

class Product(Base):
    __tablename__ = "PRODUCT"

    product_id = Column(String(50), primary_key=True)
    product_category_name = Column(String(255))
    product_weight_g = Column(Float)
    product_length_cm = Column(Float)
    product_height_cm = Column(Float)
    product_width_cm = Column(Float)

class Order(Base):
    __tablename__ = "ORDER"

    order_id = Column(String(50), primary_key=True)
    order_purchase_timestamp = Column(DateTime)
    order_approved_at = Column(DateTime)
    order_delivered_timestamp = Column(DateTime)
    payment_sequential = Column(Integer)
    payment_type = Column(String(100))
    payment_installments = Column(Integer)
    payment_value = Column(Float)
    shipping_charges = Column(Float)
    price = Column(Float)
    order_status = Column(String(100))
    customer_id = Column(String(50), ForeignKey("CUSTOMER.customer_id"))
    product_id = Column(String(50))
    seller_id = Column(String(50))

# -------------------------
# Pydantic Schemas
# -------------------------
class CustomerCreate(BaseModel):
    customer_id: str
    zip_code: str
    city: str
    state: str

class ProductCreate(BaseModel):
    product_id: str
    product_category_name: str
    product_weight_g: float
    product_length_cm: float
    product_height_cm: float
    product_width_cm: float

class OrderCreate(BaseModel):
    order_id: str
    order_purchase_timestamp: datetime.datetime
    order_approved_at: datetime.datetime
    order_delivered_timestamp: datetime.datetime
    payment_sequential: int
    payment_type: str
    payment_installments: int
    payment_value: float
    shipping_charges: float
    price: float
    order_status: str
    customer_id: str
    product_id: str
    seller_id: str

# -------------------------
# Dependency
# -------------------------
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# -------------------------
# FastAPI App
# -------------------------
app = FastAPI()

# -------------------------
# Routes
# -------------------------

@app.get("/")
def root():
    return {"message": "Welcome to the Brazilian Supermarket Sales API"}

@app.get("/customers/{customer_id}", response_model=List[CustomerCreate])
async def read_customer(customer_id: str, db: Session = Depends(get_db)):
    # Query the database
    customer = db.query(Customer).filter(Customer.customer_id == customer_id).first()

    # Handle result
    if customer:
        return JSONResponse(content=jsonable_encoder(customer))
    else:
        raise HTTPException(status_code=404, detail="Customer not found")

@app.post("/customers", status_code=201)
def create_customer(customer: CustomerCreate, db: Session = Depends(get_db)):
    db_customer = db.query(Customer).filter(Customer.customer_id == customer.customer_id).first()
    if db_customer:
        raise HTTPException(status_code=400, detail="Customer already exists")
    db.add(Customer(**customer.dict()))
    db.commit()
    return {"message": "Customer added successfully"}

@app.get("/products/{product_id}", response_model=List[ProductCreate])
def read_product(product_id:str , db:Session=Depends(get_db())):
    # query the database
    product = db.query(Product).filter(Product.product_id == product_id).first()

    if product:
        return JSONResponse(content=jsonable_encoder(product))
    else:
        raise HTTPException(status_code=404, detail="Product not found")


@app.post("/products", status_code=201)
def create_product(product: ProductCreate, db: Session=Depends(get_db)):
    db_product = db.query(Product).filter(Product.product_id == product.product_id).first()
    if db_product:
        raise HTTPException(status_code=400, detail="Product already exists")
    db.add(Product(**product.dict()))
    db.commit()
    return {"message": "Product added successfully"}

@app.get("/orders/{order_id}", response_model=List[OrderCreate])
def read_orders(order_id:str , db: Session = Depends(get_db)):

    order = db.query(Order).filter(Order.order_id == order_id).first()

    if order:
        return JSONResponse(content=jsonable_encoder(order))
    else:
        raise HTTPException(status_code=404, detail="Order not found")

@app.post("/orders", status_code=201)
def create_order(order: OrderCreate, db: Session = Depends(get_db)):
    if db.query(Order).filter(Order.order_id == order.order_id).first():
        raise HTTPException(status_code=400, detail="Order already exists")
    db.add(Order(**order.dict()))
    db.commit()
    return {"message": "Order added successfully"}

@app.put("/orders/{order_id}")
def update_order(order_id: str, update: OrderCreate, db: Session = Depends(get_db)):
    order = db.query(Order).filter(Order.order_id == order_id).first()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    for field, value in update.dict().items():
        setattr(order, field, value)
    db.commit()
    return {"message": f"Order {order_id} updated"}