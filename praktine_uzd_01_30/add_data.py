from sqlalchemy.orm import sessionmaker
from one2many import Customer, Item, Order, OrderLine, engine

session = sessionmaker(bind=engine)()

# cus1 = Customer(name="Nick", surname="Mercs", email="e@mail.com", address="g")
# cus2 = Customer(name="Dwight", surname="Howard", email="mail@mail.com", address="g")
# cus3 = Customer(name="Jim", surname="Scott", email="email@mail.com", address="g")
# cus4 = Customer(name="Daniel", surname="Dwight", email="emai@l.com", address="g")
# cus5 = Customer(name="Gary", surname="Paul", email="ema@il.com", address="g")
# cus6 = Customer(name="Antony", surname="James", email="em@ail.com", address="g")


# order1 = Order(customer=cus1, date="2020-01-15")
# order2 = Order(customer=cus4, date="2018-01-25")
# order3 = Order(customer=cus2, date="2016-12-16")
# order4 = Order(customer=cus3, date="2008-09-10")
# order5 = Order(customer=cus6, date="2020-11-8")
# order6 = Order(customer=cus4, date="2022-10-13")
# order7 = Order(customer=cus5, date="2019-05-22")
# order8 = Order(customer=cus1, date="2021-02-28")



# session.add(order1)
# session.add(order2)
# session.add(order3)
# session.add(order4)
# session.add(order5)
# session.add(order6)
# session.add(order7)
# session.add(order8)


# item1 = Item(name="Sand", price="20", weight="1")
# item2 = Item(name="Car", price="25000", weight="1500")
# item3 = Item(name="Mousepad", price="30", weight="0.5")
# item4 = Item(name="PC", price="1500", weight="2.5")
# item5 = Item(name="Plate", price="5", weight="0.3")
# item6 = Item(name="House", price="350000", weight="0")


# orderline1 = OrderLine(order_id=1, item_id=1, amount=100, price=20, total_price=2000)
# orderline2 = OrderLine(order_id=2, item_id=2, amount=1, price=25000, total_price=25000)
# orderline3 = OrderLine(order_id=3, item_id=3, amount=10, price=30, total_price=3000)
# orderline4 = OrderLine(order_id=4, item_id=4, amount=2, price=1500, total_price=3000)
# orderline5 = OrderLine(order_id=5, item_id=5, amount=150, price=5, total_price=750)
# orderline6 = OrderLine(order_id=6, item_id=6, amount=1, price=350000, total_price=350000)
# orderline7 = OrderLine(order_id=7, item_id=3, amount=150, price=30, total_price=4500)
# orderline8 = OrderLine(order_id=8, item_id=4, amount=4, price=1500, total_price=6000)


# session.add(orderline1)
# session.add(orderline2)
# session.add(orderline3)
# session.add(orderline4)
# session.add(orderline5)
# session.add(orderline6)
# session.add(orderline7)
# session.add(orderline8)

# session.add(item1)
# session.add(item2)
# session.add(item3)
# session.add(item4)
# session.add(item5)
# session.add(item6)

# session.add(cus1)
# session.add(cus2)
# session.add(cus3)
# session.add(cus4)
# session.add(cus5)
# session.add(cus6)


# session.commit()