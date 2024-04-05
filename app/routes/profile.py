import requests
from bs4 import BeautifulSoup
from flasgger import swag_from
from flask import Blueprint, jsonify, request

from app.docs.swagger import swagger_profile_spec
from app.utils.token_required import require_token_auth
from config import Config

bp = Blueprint("profile", __name__, url_prefix="/api")


@bp.route("/profile", methods=["GET"])
@require_token_auth
@swag_from(swagger_profile_spec)
def profile():
    headers = {
        "User-Agent": Config.USER_AGENT,
    }
    cookie = {Config.COOKIE_KEY: request.headers["Authorization"]}
    response = requests.get(
        f"{Config.BASE_URL}/student/profile",
        headers=headers,
        cookies=cookie,
    )
    soup = BeautifulSoup(response.text, "html.parser")
    if "login" in soup.title.string.lower():
        return jsonify({"message": "Token expired. Please login again."}), 401

    name = soup.find("th", string="Name").find_next("td").get_text(strip=True)
    dob = soup.find("th", string="Date of Birth").find_next("td").get_text(strip=True)
    admission_no = (
        soup.find("th", string="Admission No").find_next("td").get_text(strip=True)
    )
    university_roll_no = (
        soup.find("th", string="University Reg No").find_next("td").get_text(strip=True)
    )

    json_repsonse = {
        "name": name,
        "dob": dob,
        "admission_no": admission_no,
        "university_roll_no": university_roll_no,
    }
    return (
        jsonify(
            {"message": "Successfully fetched data", "profile_details": json_repsonse}
        ),
        200,
    )
