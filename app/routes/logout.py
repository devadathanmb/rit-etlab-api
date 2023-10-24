from flask import Blueprint, jsonify, request
import requests
from config import Config
from bs4 import BeautifulSoup
from app.utils.token_required import require_token_auth
from flasgger import swag_from
from app.docs.swagger import swagger_logout_spec

bp = Blueprint("logout", __name__, url_prefix="/api")


@bp.route("/logout", methods=["GET"])
@require_token_auth
@swag_from(swagger_logout_spec)
def logout():
    headers = {
        "User-Agent": Config.USER_AGENT,
    }
    cookie = {"RITSESSIONID": request.headers["Authorization"]}
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
