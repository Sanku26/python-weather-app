import requests

API_KEY = "YOUR_API_KEY"

city = input("Enter city name: ")

url = "https://api.openweathermap.org/data/2.5/weather"

params = {
    "q": city,
    "appid": API_KEY,
    "units": "metric"
}

response = requests.get(url, params=params)
data = response.json()

if data.get("cod") == 200:
    temperature = data["main"]["temp"]
    weather = data["weather"][0]["description"]

    print("\nWeather Information")
    print("City:", city)
    print("Temperature:", temperature, "°C")
    print("Condition:", weather)

else:
    print("Error:", data.get("message"))