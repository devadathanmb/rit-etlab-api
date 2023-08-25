from functools import wraps
from flask import request, jsonify


def require_cookie_auth(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if "Cookie" in request.headers:
            return func(*args, **kwargs)

        return jsonify({"message": "Cookie is required"}), 401

    return wrapper
