from .extensions import db
from datetime import datetime,timezone

class BaseModel(db.Model):
    __abstract__=True
    id=db.Column(db.Integer,primary_key=True)
    created_at=db.Column(db.DateTime(timezone=True),default=lambda:datetime.now(timezone.utc))
    updated_at=db.Column(db.DateTime(timezone=True),default=lambda:datetime.now(timezone.utc),onupdate=lambda:datetime.now(timezone.utc))

class User(BaseModel):
    name=db.Column(db.String,nullable=True)
    email=db.Column(db.String,required=True,unique=True)
    password=db.Column(db.String,required=True)
    requests=db.relationship("Request",back_populates="user")

class Requests(BaseModel):
    data=db.Column(db.JSON())
    status=db.Column(db.Enum("approved","rejected","created"))
    type=db.Column(db.String(20))
    #who created the request
    user_id=db.Column(db.Integer,db.ForeignKey("user.id"))
    #relation
    user=db.relationship("User",back_populates="requests")


class Section(BaseModel):
    name=db.Column(db.String(20),nullable=True)

    products=db.relationship("Product",back_populates="section")

class Product(BaseModel):
    name=db.Column(db.String,required=True)
    price=db.Column(db.Numeric(10,2),nullable=True)
    stock=db.COlumn(db.Numeric(10,2))
    expiry=db.COlumn(db.DateTime(timezone=True))
    unit_of_sale=db.Column(db.Enum("kg","litre","item"))

    section_id=db.Column(db.Integer,db.ForeignKey("section.id"))
    section=db.relationship("Section",back_populates="requests")
    sale_items=db.relationship("SaleItem",back_populates="product")
    
class SaleItem(BaseModel):
    quantity=db.Column(db.Numeric(10,2))
    price_at_sale=db.Column(db.Numeric(10,2),nullable=False)
    product_id=db.Column(db.Integer(),db.ForeignKey)
    sale_id=db.Column(db.Integer,db.ForeignKey("sale.id"))
    sale=db.relationship("Sale",back_populates="sale_items")
    product=db.relationship("Product",back_populates="sale_items")

class Sale(BaseModel):
    total_amount=db.Column(db.Numeric(10,2))
    customer_id=db.Column(db.Integer,db.ForeignKey("user.id"))    
    sale_items=db.relationship("SaleItem",back_populates="sale")

