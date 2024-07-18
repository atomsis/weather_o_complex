import pytest
from weather.views import get_coordinates, get_weather, input_city, weather
from django.urls import reverse


def test_get_coordinates():
    lat, lon = get_coordinates("London")
    assert lat is not None
    assert lon is not None

    lat, lon = get_coordinates("InvalidCityName")
    assert lat is None
    assert lon is None


def test_get_weather():
    lat, lon = 51.5074, -0.1278  # London

    weather_data_valid = get_weather(lat, lon)
    assert weather_data_valid is not None

    weather_data_invalid = get_weather(1000, 1000)
    assert weather_data_invalid is None


@pytest.fixture
def client():
    from django.test import Client

    return Client(HTTP_HOST="testserver")


@pytest.mark.django_db
def test_input_city_view(client):
    url = reverse("weather:input_city")
    response = client.get(url)
    assert response.status_code == 200

    data = {"city": "London"}
    response = client.post(url, data)
    assert response.status_code == 302
    assert response.url == reverse("weather:weather", kwargs={"city": "London"})


@pytest.mark.django_db
def test_weather_view(client):
    url = reverse("weather:weather", kwargs={"city": "London"})
    response = client.get(url)
    assert response.status_code == 200
    assert "Погода в London" in response.content.decode()

    url = reverse("weather:weather", kwargs={"city": "InvalidCityName"})
    response = client.get(url)
    assert response.status_code == 200
