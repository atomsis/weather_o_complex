from django.urls import path
from . import views

app_name = "weather"

urlpatterns = [
    path("", views.input_city, name="input_city"),
    # path('autocomplete/', views.city_autocomplete, name='city_autocomplete'),
    path("weather/<str:city>/", views.weather, name="weather"),
]
