from flask import jsonify, request, Blueprint
from app.auth import generate_token
from .auth import token_required
from .services import get_all_products, add_product, get_product_by_id, authenticate_user

routes = Blueprint('routes', __name__)


@routes.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if authenticate_user(username, password):
        token = generate_token(username)
        return jsonify({'token': token}), 200
    else:
        return jsonify({'message': 'Invalid username or password.'}), 401


@routes.route('/get-products')
@token_required(['privileged'])
def get_products():
    products = get_all_products()
    return jsonify(products)


@routes.route('/add-product', methods=['POST'])
@token_required(['admin'])
def create_product():
    data = request.get_json()
    try:
        product = add_product(data['name'], data['price'])
        return jsonify({'message': 'Product added successfully.', 'product': product}), 201
    except ValueError as e:
        return jsonify({'message': str(e)}), 400


@routes.route('/get-product/<int:product_id>')
@token_required(['privileged'])
def get_product(product_id):
    product = get_product_by_id(product_id)
    if product:
        return jsonify(product)
    else:
        return jsonify({'message': 'Product not found.'}), 404
