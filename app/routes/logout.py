from flask import Blueprint, jsonify, request
import requests
from config import Config
from bs4 import BeautifulSoup
from app.utils.cookie_required import require_cookie_auth

bp = Blueprint("logout", __name__, url_prefix="/api")


@bp.route("/logout", methods=["GET"])
@require_cookie_auth
def logout():
    headers = {
        "User-Agent": Config.USER_AGENT,
    }
    cookie = {"RITSESSIONID": request.headers["Cookie"]}
    response = requests.get(
        f"{Config.BASE_URL}/user/logout",
        headers=headers,
        cookies=cookie,
    )
    print(response.status_code)
    soup = BeautifulSoup(response.text, "html.parser")
    if "login" in soup.title.string.lower():
        return (
            jsonify({"message": "Logged out successfully"}),
            200,
        )
