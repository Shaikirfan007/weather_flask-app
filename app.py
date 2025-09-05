from flask import Flask, render_template_string, request
import requests

app = Flask(__name__)

OPENWEATHER_API_KEY = "334d51fa072f8e8c53b613649db905f6"

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
        <html>
        <head><title>Weather App</title></head>
        <body>
            <h2>🌤️ Weather App</h2>
            <form method="post">
                <input type="text" name="city" placeholder="Enter city name">
                <button type="submit">Get Weather</button>
            </form>
            {% if weather %}
                {% if weather.error %}
                    <p>❌ {{ weather.error }}</p>
                {% else %}
                    <p>✅ Weather in {{ weather.city }}: {{ weather.temperature }}°C, {{ weather.description }}</p>
                {% endif %}
            {% endif %}
        </body>
        </html>
    """, weather=weather)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
