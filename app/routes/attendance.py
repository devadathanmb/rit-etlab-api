import re

import requests
from bs4 import BeautifulSoup
from flasgger import swag_from
from flask import Blueprint, jsonify, request

from app.docs.swagger import swagger_attendance_spec
from app.utils.token_required import require_token_auth
from config import Config

bp = Blueprint("attendance", __name__, url_prefix="/api")


@bp.route("/attendance", methods=["GET"])
@swag_from(swagger_attendance_spec)
@require_token_auth
def attendance():
    semester = request.args.get("semester")
    if not semester:
        return jsonify({"message": "Semester required"}), 400

    try:
        semester = int(semester)
    except ValueError:
        return jsonify({"message": "Semester should be a valid integer"}), 400

    if not (semester >= 1 and semester <= 8):
        return (
            jsonify(
                {"message": "Invalid semester. Semester has to be between 1 and 8"}
            ),
            400,
        )

    headers = {
        "User-Agent": Config.USER_AGENT,
    }
    cookie = {Config.COOKIE_KEY: request.headers["Authorization"]}
    response = requests.get(
        f"{Config.BASE_URL}/ktuacademics/student/viewattendancesubject/{semester}",
        headers=headers,
        cookies=cookie,
    )
    soup = BeautifulSoup(response.text, "html.parser")
    if "login" in soup.title.string.lower():
        return jsonify({"message": "Token expired. Please login again."}), 401

    response_body = {}
    table = soup.find("table", class_="items")
    table_headers = table.find_all("th")
    table_data = table.find_all("td")

    response_body["university_reg_no"] = table_data[0].text
    response_body["roll_no"] = table_data[1].text
    response_body["name"] = table_data[2].text

    for i in range(3, len(table_data) - 2):
        subject_code = table_headers[i].text.strip()
        attendance_str = table_data[i].text.strip()
        present_hours = attendance_str.split("/")[0].strip()
        total_hours = attendance_str.split("/")[1].split("(")[0].strip()
        attendance_percentage = re.search(r"\((.*?)\)", attendance_str).group(1).strip()

        subject_attendance = {}
        subject_attendance["present_hours"] = present_hours
        subject_attendance["total_hours"] = total_hours
        subject_attendance["attendance_percentage"] = attendance_percentage

        response_body[subject_code] = subject_attendance

    response_body["total_present_hours"] = (
        table_data[len(table_data) - 2].text.split("/")[0].strip()
    )
    response_body["total_hours"] = (
        table_data[len(table_data) - 2].text.split("/")[0].strip()
    )
    response_body["total_perecentage"] = table_data[len(table_data) - 1].text

    return jsonify(response_body), 200
