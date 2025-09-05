import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")

def get_weather(city):
    if not OPENWEATHER_API_KEY:
        return {"error": "API key not found. Please set it in .env file."}

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

if __name__ == "__main__":
    print("🌤️  Welcome to Python Weather App 🌤️")
    city = input("Enter city name: ")
    weather = get_weather(city)

    if "error" in weather:
        print("❌", weather["error"])
    else:
        print(f"✅ Weather in {weather['city']}: {weather['temperature']}°C, {weather['description']}")
