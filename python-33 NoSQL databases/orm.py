from flask import session

from models import session, Product, CartItems, Order, OrderItem


#

def view_cart():
    cartitems = session.query(CartItems).all()

    for cartitem in cartitems:
        print(cartitem.id, cartitem.product_id, cartitem.quantity)


view_cart()


def add_product( name, price, quantity):

    product = Product(name, price, quantity)

    session.add(product)
    session.commit()


# add_product("mouse", 4, 1)
# print("added product successfully")


def delete_product(id):

    product = session.query(Product).filter_by(id=id).first()

    session.delete(product)
    session.commit()


# delete_product(1)
# print("deleted product successfully")


def order(order_date, total_amount):

    order = Order(order_date, total_amount)

    session.add(order)
    session.commit()
#
# order(2023-10-12 15-10,  3)


def view_order():

    orders = session.query(OrderItem).all()
    for order in orders:
        print(order.order_id, order.quantity)


view_order()