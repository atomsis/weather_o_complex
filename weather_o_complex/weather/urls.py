from django.urls import path
from . import views

app_name = "weather"

urlpatterns = [
    path("", views.input_city, name="input_city"),
    path("weather/<str:city>/", views.weather, name="weather"),
    path('city-statistics/', views.city_statistics, name='city_statistics'),

]
