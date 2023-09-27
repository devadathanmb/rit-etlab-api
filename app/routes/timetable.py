from flask import Blueprint, jsonify, request
import requests
from config import Config
from app.utils.cookie_required import require_cookie_auth
import csv

bp = Blueprint("timetable", __name__, url_prefix="/api")


@bp.route("/timetable", methods=["GET"])
@require_cookie_auth
def timetable():
    headers = {
        "User-Agent": Config.USER_AGENT,
    }

    cookie = {"RITSESSIONID": request.headers["Cookie"]}
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
