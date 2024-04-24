import jwt
from . import SECRET_KEY
from flask import jsonify, request
from jwt import DecodeError, ExpiredSignatureError
from functools import wraps
from datetime import datetime, timedelta
from app.models import User


def generate_token(username):
    expiration_time = datetime.utcnow() + timedelta(hours=1)
    payload = {'username': username, 'exp': expiration_time}
    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
    return token


def token_required(roles):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            token = request.headers.get('Authorization')
            if not token:
                return jsonify({'message': 'Authentication is required.'}), 401
            try:
                token = token.replace('Bearer ', '')
                data = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
                username = data['username']
                user = User.query.filter_by(username=username).first()
                if not user or user.role not in roles:
                    return jsonify({'message': 'Unauthorized access.'}), 403
            except (DecodeError, ExpiredSignatureError):
                return jsonify({'message': 'Authentication unsuccessful.'}), 401
            return func(*args, **kwargs)
        return wrapper
    return decorator
