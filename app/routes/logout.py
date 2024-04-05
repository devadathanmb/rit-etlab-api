import requests
from bs4 import BeautifulSoup
from flasgger import swag_from
from flask import Blueprint, jsonify, request

from app.docs.swagger import swagger_logout_spec
from app.utils.token_required import require_token_auth
from config import Config

bp = Blueprint("logout", __name__, url_prefix="/api")


@bp.route("/logout", methods=["GET"])
@require_token_auth
@swag_from(swagger_logout_spec)
def logout():
    headers = {
        "User-Agent": Config.USER_AGENT,
    }
    cookie = {Config.COOKIE_KEY: request.headers["Authorization"]}
    response = requests.get(
        f"{Config.BASE_URL}/user/logout",
        headers=headers,
        cookies=cookie,
    )
    soup = BeautifulSoup(response.text, "html.parser")
    if "login" in soup.title.string.lower():
        return (
            jsonify({"message": "Logged out successfully"}),
            200,
        )
    return (
        jsonify({"message": "Error logging out"}),
        500,
    )
