import csv

import requests
from flasgger import swag_from
from flask import Blueprint, jsonify, request

from app.docs.swagger import swagger_timetable_spec
from app.utils.token_required import require_token_auth
from config import Config

bp = Blueprint("timetable", __name__, url_prefix="/api")


@bp.route("/timetable", methods=["GET"])
@require_token_auth
@swag_from(swagger_timetable_spec)
def timetable():
    headers = {
        "User-Agent": Config.USER_AGENT,
    }

    cookie = {Config.COOKIE_KEY: request.headers["Authorization"]}
    response = requests.get(
        f"{Config.BASE_URL}/student/timetable?format=csv&yt0=",
        headers=headers,
        cookies=cookie,
    )
    if response.status_code == 200:
        csv_data = response.text

        timetable = {}

        csv_reader = csv.reader(csv_data.splitlines(), delimiter=",", quotechar='"')
        headers = next(csv_reader)
        next(csv_reader)

        for row in csv_reader:
            day = row[0]
            timetable[day.lower()] = {}

            for i, period in enumerate(row[1:], start=1):
                period_name = f"period-{i}"
                period_data = {"name": period.strip()}

                if "<br/>[ Theory ]<br/>" in period:
                    parts = period.split("<br/>[ Theory ]<br/>")
                    period_data["name"] = parts[0].strip()
                    period_data["teacher"] = parts[1].strip()

                timetable[day.lower()][period_name] = period_data

        return jsonify(timetable), 200
    else:
        return jsonify({"message": "Time table data not found"}), 404
