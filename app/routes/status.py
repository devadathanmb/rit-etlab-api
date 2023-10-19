from flask import Blueprint, jsonify
from flasgger import swag_from
from app.docs.swagger import swagger_status_spec

bp = Blueprint("status", __name__, url_prefix="/api")


@bp.route("/status", methods=["GET"])
@swag_from(swagger_status_spec)
def get_status():
    return jsonify({"message": "I am alive"})
