# აღწერეთ შემდეგი კლასები sqlalchemy გამოყენებით(თეიბლები არ შექმნათ ხელით მონაცემთა ბაზაში)
#
#
# Product:
# •	id
# •	name
# •	price
# •	quantity_in_stock
#
# CartItems:
# •	id
# •	product_id
# •	quantity
#
# Order:
# •	id
# •	order_date
# •	total_amount
#
# OrderItem:
# •	id
# •	order_id
# •	product_id
# •	quantity
# •	price_per_item
#
#
# შეიყვანეთ გარკვეული ინფორმაცია პროდუქტების ცხრილში
#
# ააწყვეთ მომხმარებელზე ორიენტირებული ინტერფეისი რათა შეძლოს აირჩიოს თუ რა მოქმედების გახორციელება უნდა, მოქმედებები კი უნდა იყოს შემდეგი:
#
# •	კალათის ნახვა
# •	პროდუქტების დამატება კალათაში
# •	პროდუქტების ამოშლა კალათიდან
# •	ორდერის გახორციელება
# •	ორდერების ნახვა


from sqlalchemy import create_engine, Column, Float, Integer, ForeignKey, String, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime

# Database configuration
host = 'localhost'
port = 5433
database = 'postgres'
user = 'postgres'
password = '99Youaremighty'

# Set up the engine and base
engine = create_engine(f'postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}')
Base = declarative_base()

# Define models
class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Float)
    quantity_in_stock = Column(Integer)

    def __init__(self, name, price, quantity_in_stock):
        self.name = name
        self.price = price
        self.quantity_in_stock = quantity_in_stock

class CartItems(Base):
    __tablename__ = 'cart_items'
    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey('products.id'))
    quantity = Column(Integer)

    def __init__(self, product_id, quantity):
        self.product_id = product_id
        self.quantity = quantity

class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True)
    order_date = Column(DateTime)
    total_amount = Column(Float)

    def __init__(self, order_date, total_amount):
        self.order_date = order_date
        self.total_amount = total_amount

class OrderItem(Base):
    __tablename__ = 'order_items'
    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey('orders.id'))
    product_id = Column(Integer, ForeignKey('products.id'))
    quantity = Column(Integer)
    price_per_item = Column(Float)

    def __init__(self, order_id, product_id, quantity, price_per_item):
        self.order_id = order_id
        self.product_id = product_id
        self.quantity = quantity
        self.price_per_item = price_per_item


Base.metadata.create_all(engine)

# Set up session
Session = sessionmaker(bind=engine)
session = Session()





