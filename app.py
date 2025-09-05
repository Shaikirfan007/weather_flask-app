from flask import Flask, render_template_string, request
import requests, os
from dotenv import load_dotenv

load_dotenv()  # Load variables from .env

app = Flask(__name__)

OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")

def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER_API_KEY}&units=metric"
    response = requests.get(url)
    if response.status_code != 200:
        return {"error": "City not found or API request failed"}
    data = response.json()
    return {
        "city": data["name"],
        "temperature": data["main"]["temp"],
        "description": data["weather"][0]["description"]
    }

@app.route("/", methods=["GET", "POST"])
def home():
    weather = None
    if request.method == "POST":
        city = request.form["city"]
        weather = get_weather(city)
    return render_template_string("""
        <form method="post">
            <input type="text" name="city" placeholder="Enter city">
            <button type="submit">Get Weather</button>
        </form>
        {% if weather %}
            <h2>{{ weather.city }}</h2>
            <p>Temperature: {{ weather.temperature }}°C</p>
            <p>Description: {{ weather.description }}</p>
        {% endif %}
    """, weather=weather)

if __name__ == "__main__":
    app.run(debug=True)
