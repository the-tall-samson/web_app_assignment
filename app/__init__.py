from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()
SECRET_KEY = ''  # update to proper 16-character randomly generated secret


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = SECRET_KEY
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'db', 'users.db'))
    app.config['SQLALCHEMY_BINDS'] = {
        'products': 'sqlite:///' + os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'db', 'products.db'))
    }
    db.init_app(app)
    from app.routes import routes
    app.register_blueprint(routes)

    return app
