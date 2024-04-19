from app import create_app, db
from app.models import User, Product


def create_tables():
    app = create_app()
    with app.app_context():
        db.create_all()
        print('Database tables created successfully')


def populate_users():
    users = [
        {'username': 'admin', 'password': 'admin123', 'role': 'admin'},
        {'username': 'privileged', 'password': 'priv123', 'role': 'privileged'}
    ]
    app = create_app()
    with app.app_context():
        for user_data in users:
            user = User(username=user_data['username'], role=user_data['role'])
            user.set_password(user_data['password'])
            db.session.add(user)
        db.session.commit()


def populate_products():
    app = create_app()
    with app.app_context():
        products = [
            {'name': 'Product 1', 'price': 10.0},
            {'name': 'Product 2', 'price': 20.0}
        ]
        for product_data in products:
            product_name = product_data['name']
            product_price = product_data['price']
            if not Product.query.filter_by(name=product_name, price=product_price).first():
                product = Product(name=product_name, price=product_price)
                db.session.add(product)

        db.session.commit()
        print('Products populated successfully')


if __name__ == '__main__':
    create_tables()
    populate_users()
    populate_products()
