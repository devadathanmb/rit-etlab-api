from functools import wraps
from flask import request, jsonify


def require_token_auth(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if "Authorization" in request.headers:
            return func(*args, **kwargs)

        return jsonify({"message": "Token is required"}), 401

    return wrapper
