import requests
from bs4 import BeautifulSoup
from flasgger import swag_from
from flask import Blueprint, jsonify, request

from app.utils.token_required import require_token_auth
from config import Config

bp = Blueprint("absent", __name__, url_prefix="/api")


@bp.route("/absent", methods=["GET"])
@require_token_auth
def absent():
    try:
        month = int(request.args.get("month"))
        semester = int(request.args.get("semester"))
        year = int(request.args.get("year"))
    except (ValueError, TypeError):
        return jsonify({"message": "Invalid parameters"}), 400

    if not (month >= 1 and month <= 12):
        return jsonify({"message": "Invalid month"}), 400

    if not (semester >= 1 and semester <= 8):
        return jsonify({"message": "Invalid semester"}), 400

    headers = {
        "User-Agent": Config.USER_AGENT,
    }

    cookie = {Config.COOKIE_KEY: request.headers["Authorization"]}
    payload = {
        "month": month,
        "semester": (8 + semester),
        "year": year,
    }
    response = requests.post(
        f"{Config.BASE_URL}/ktuacademics/student/attendance",
        headers=headers,
        cookies=cookie,
        data=payload,
    )
    if response.status_code != 200:
        return jsonify({"message": "Failed to fetch data"}), 500

    soup = BeautifulSoup(response.text, "html.parser")
    if "login" in soup.title.string.lower():
        return jsonify({"message": "Token expired. Please login again."}), 401

    try:
        semester_element = soup.find("select", {"name": "semester"}).find(
            "option", {"selected": "selected"}
        )
        semester = semester_element.get_text(strip=True).lower()
        semester_num = semester_element["value"]

        month_element = soup.find("select", {"name": "month"}).find(
            "option", {"selected": "selected"}
        )
        month = month_element.get_text(strip=True).lower()
        month_num = month_element["value"]
        year = (
            soup.find("select", {"name": "year"})
            .find("option", {"selected": "selected"})
            .text
        ).strip()

        absent_hours_data = []

        table = soup.find("table", {"id": "itsthetable"})

        rows = table.select("tbody tr")
        for row in rows:
            day = row.find("th").text.strip()
            cols = row.find_all("td")

            if len(cols) == 1:
                continue

            for hour, col in enumerate(cols, start=1):
                if "absent" in col.get("class"):
                    absent_hour_data = {}
                    suffixes = ["st", "nd", "rd", "th"]
                    if day.endswith(tuple(suffixes)):
                        day = day[:-2]
                    absent_hour_data["day"] = int(day)
                    absent_hour_data["hour"] = hour
                    absent_hour_data["subject_code"] = col.text.split("-")[0].strip()
                    absent_hour_data["subject_name"] = (
                        col.text.split("-")[1].strip().split("\n")[0].strip()
                    )
                    absent_hours_data.append(absent_hour_data)

        respone_dict = {
            "month": month,
            "month_num": month_num,
            "semester": semester,
            "semester_num": semester_num,
            "year": year,
            "absent_hours": absent_hours_data,
        }
        return (
            jsonify({"message": "Successfully fetched data", "data": respone_dict}),
            200,
        )
    except Exception as e:
        print(e)
        return jsonify({"message": "Failed to parse data"}), 500
