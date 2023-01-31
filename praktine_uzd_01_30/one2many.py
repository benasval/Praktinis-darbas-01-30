from sqlalchemy import Column, Integer, String, ForeignKey, Float, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

engine = create_engine('sqlite:///data/sales_o2m.db')
Base = declarative_base()

class OrderLine(Base):
    __tablename__ = "orderline"
    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey("order.id"))
    item_id = Column(Integer, ForeignKey("item.id"))
    amount = Column(Integer)
    price = Column(Float)
    total_price = Column(Float)
    order = relationship("Order", back_populates="orderlines")
    item = relationship("Item", back_populates="orderlines")


class Order(Base):
    __tablename__ = "order"
    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey("customer.id"))
    date = Column(String)
    orderlines = relationship("OrderLine", back_populates="order")
    customer = relationship("Customer", back_populates="orders")


class Item(Base):
    __tablename__ = "item"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Float) 
    weight = Column(Float)
    orderlines = relationship("OrderLine", back_populates="item")


class Customer(Base):
    __tablename__ = "customer"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    surname= Column(String)
    email = Column(String)
    address = Column(String)
    orders = relationship("Order", back_populates="customer")

if __name__ == "__main__":
    Base.metadata.create_all(engine)

