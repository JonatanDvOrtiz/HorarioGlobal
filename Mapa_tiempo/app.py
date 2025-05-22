from flask import Flask, render_template, jsonify, request
from datetime import datetime
import pytz

app = Flask(__name__)

all_cities = {
    "Nueva York": "America/New_York",
    "Londres": "Europe/London",
    "Tokio": "Asia/Tokyo",
    "Sídney": "Australia/Sydney",
    "Buenos Aires": "America/Argentina/Buenos_Aires",
    "Madrid": "Europe/Madrid",
    "París": "Europe/Paris",
    "Los Ángeles": "America/Los_Angeles",
    "Ciudad de México": "America/Mexico_City",
    "Johannesburgo": "Africa/Johannesburg",
    "Dubai": "Asia/Dubai",
    "Pekín": "Asia/Shanghai",
    "Moscú": "Europe/Moscow"
}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/time", methods=["POST"])
def get_selected_times():
    selected = request.json.get("cities", [])
    response = {}
    for city in selected:
        if city in all_cities:
            tz = pytz.timezone(all_cities[city])
            now = datetime.now(tz)
            response[city] = now.strftime("%A, %Y-%m-%d %H:%M:%S")
    return jsonify(response)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)