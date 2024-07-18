from django.db import models
from django.contrib.auth.models import User


class SearchHistory(models.Model):
    city = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.city} - {self.timestamp}"


class CitySearchCount(models.Model):
    city = models.CharField(max_length=100, unique=True)
    count = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.city} - {self.count}"
