from flask import Blueprint, jsonify

bp = Blueprint("status", __name__, url_prefix="/api")


@bp.route("/status", methods=["GET"])
def get_status():
    return jsonify({"message": "I am alive"})
