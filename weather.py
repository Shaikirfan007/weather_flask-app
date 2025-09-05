import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get API key from .env
API_KEY = os.getenv("OPENWEATHER_API_KEY")

def get_weather(city):
    if not API_KEY:
        return None, "❌ API key not found. Please check your .env file."

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data, None
    else:
        return None, f"❌ Error: {response.json().get('message', 'City not found or API request failed')}"

def main():
    print("🌤️  Welcome to Python Weather App 🌤️")
    city = input("Enter city name: ").strip()

    data, error = get_weather(city)

    if error:
        print(error)
    else:
        print(f"\n🌍 City: {data['name']}, {data['sys']['country']}")
        print(f"🌡️ Temperature: {data['main']['temp']}°C")
        print(f"💧 Humidity: {data['main']['humidity']}%")
        print(f"🌤️ Weather: {data['weather'][0]['description'].title()}")
        print(f"💨 Wind Speed: {data['wind']['speed']} m/s")

if __name__ == "__main__":
    main()
