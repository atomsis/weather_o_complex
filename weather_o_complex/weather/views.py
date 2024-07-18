import requests
from django.shortcuts import render, redirect
from .forms import CityForm
from django.utils.encoding import smart_str


def get_coordinates(city):
    url = f"https://nominatim.openstreetmap.org/search?q={city}&format=json&limit=1"
    headers = {"User-Agent": "YourAppName/1.0 (test@example.com)"}
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        if data:
            return data[0]["lat"], data[0]["lon"]
        else:
            return None, None
    except requests.exceptions.RequestException as e:
        print(f"Error fetching coordinates: {e}")
        return None, None


def get_weather(lat, lon):
    lat, lon = float(lat), float(lon)

    if lat > 90 or lat < -90 or lon > 180 or lon < -180:
        return None

    url = "https://api.open-meteo.com/v1/forecast"
    headers = {"Content-Type": "application/json"}
    params = {
        "latitude": lat,
        "longitude": lon,
        "current": [
            "temperature_2m",
            "relative_humidity_2m",
            "apparent_temperature",
            "is_day",
            "precipitation",
            "rain",
            "showers",
            "snowfall",
            "weather_code",
            "cloud_cover",
            "pressure_msl",
            "surface_pressure",
            "wind_speed_10m",
            "wind_direction_10m",
            "wind_gusts_10m",
        ],
        "timezone": "Europe/Moscow",
    }
    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return None


def input_city(request):
    last_searched_city = request.COOKIES.get("last_city", None)
    if request.method == "POST":
        form = CityForm(request.POST)
        if form.is_valid():
            city = form.cleaned_data["city"]
            # Set last city in cookie
            response = redirect("weather:weather", city=city)
            response.set_cookie(
                "last_city", city.encode("utf-8"), max_age=30 * 24 * 60 * 60
            )
            return response
    else:
        form = CityForm()
    return render(
        request,
        "weather/input_city.html",
        {"form": form, "last_city": last_searched_city},
    )


def weather(request, city):
    lat, lon = get_coordinates(city)
    if lat is not None and lon is not None:
        weather_data = get_weather(lat, lon)
        if weather_data:
            context = {"weather_data": weather_data, "city": city}
            return render(request, "weather/weather.html", context)
    context = {
        "message": "Не удалось получить данные о погоде. Пожалуйста, попробуйте позже."
    }
    return render(request, "weather/error.html", context)
