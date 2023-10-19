from flask import Blueprint, jsonify, request
import requests
from config import Config
from bs4 import BeautifulSoup
from flasgger import swag_from
from app.docs.swagger import swagger_login_spec

bp = Blueprint("login", __name__, url_prefix="/api")
session = requests.Session()


@bp.route("/login", methods=["POST"])
@swag_from(swagger_login_spec)
def login():
    body = request.get_json()
    username = body.get("username")
    password = body.get("password")

    if not username or not password:
        return jsonify({"message": "Username and password is required"}), 401

    payload = {
        "LoginForm[username]": username,
        "LoginForm[password]": password,
        "yt0": "",
    }

    headers = {
        "User-Agent": Config.USER_AGENT,
        "Content-Type": "application/x-www-form-urlencoded",
    }

    response = session.post(
        f"{Config.BASE_URL}/user/login", data=payload, headers=headers
    )
    soup = BeautifulSoup(response.text, "html.parser")
    title = soup.find("title").text
    if "login" in title.lower():
        return jsonify({"message": "Invalid username or password"}), 401
    cookie = session.cookies.get_dict()["RITSESSIONID"]

    return jsonify({"message": "Login successful", "cookie": cookie}), 200
