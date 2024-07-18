import requests


def get_weather_data(city):
    cities_coordinates = {
        "New York": (40.7128, -74.0060),
        "London": (51.5074, -0.1278),
        "Paris": (48.8566, 2.3522),
        "Tokyo": (35.6895, 139.6917),
        "Moscow": (55.7558, 37.6176),
    }
    latitude, longitude = cities_coordinates.get(city, (0, 0))
    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=temperature_2m"
    response = requests.get(url)
    return response.json()
