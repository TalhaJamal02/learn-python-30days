import os
import requests
from dotenv import load_dotenv

load_dotenv()


api_key = os.getenv("WEATHER_API_KEY")


def fetch_weather(city="New York"):
    url = f"https://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        if "error" in data:
            return None, None
        return data["current"]["temp_c"], data["location"]["name"]
    except (requests.RequestException, KeyError, ValueError):
        return None, None
