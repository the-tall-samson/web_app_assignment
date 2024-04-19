from . import db
from .models import User, Product
from werkzeug.security import check_password_hash


def authenticate_user(username, password):
    user = User.query.filter_by(username=username).first()
    if user and check_password_hash(user.password_hash, password):
        return True
    return False


def get_all_products():
    products = Product.query.all()
    products_data = [{'id': product.id, 'name': product.name, 'price': product.price} for product in products]
    return products_data


def add_product(name, price):
    existing_product = Product.query.filter_by(name=name).first()
    if existing_product:
        raise ValueError('Product already exists.')
    new_product = Product(name=name, price=price)
    db.session.add(new_product)
    db.session.commit()
    return {'id': new_product.id, 'name': new_product.name, 'price': new_product.price}


def get_product_by_id(product_id):
    product = Product.query.get(product_id)
    if product:
        return {'id': product.id, 'name': product.name, 'price': product.price}
    else:
        return None
