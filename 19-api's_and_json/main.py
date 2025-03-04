import os
import requests
from dotenv import load_dotenv


# Sending HTTP Requests
response = requests.get("https://api.github.com/users/TalhaJamal02")
print("Status Code:", response.status_code)  # Check status code
print(response.json())  # Convert Response to JSON

# Parsing JSON Data
data = response.json()
print("Name:", data["name"])  # Access specific key
print("Repositories:", data["public_repos"])  # Access specific key

# Practice Tasks:
# 1. Fetch Random Joke API: URL: https://official-joke-api.appspot.com/random_joke

# Make a GET request
# Parse the JSON response
# Print the joke setup and punchline

# Sending HTTP Requests
res = requests.get("https://official-joke-api.appspot.com/random_joke")
print("Status Code:", res.status_code)

# Parsing JSON Data
jokes = res.json()
print("Type:", jokes["type"])
print("Setup:", jokes["setup"])
print("Punchline:", jokes["punchline"])


# Weather API:
# Use https://api.openweathermap.org
# Send request
# Extract temperature, weather and humidity condition

load_dotenv(".env.local")
api_key = os.getenv("WEATHER_API_KEY")
print(api_key)

url = f"https://api.openweathermap.org/data/2.5/weather?q=Karachi&appid={api_key}&units=metric"

response = requests.get(url)
print("Status Code:", response.status_code)

if response.status_code == 200:
    data = response.json()

    # Parsing Data
    print("City:", data["name"])
    print("Temperature:", data["main"]["temp"], "°C")
    print("Weather:", data["weather"][0]["description"])
    print("Humidity:", data["main"]["humidity"], "%")
else:
    print("Failed to fetch data")