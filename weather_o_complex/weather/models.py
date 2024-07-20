from django.db import models
from django.contrib.auth.models import User


class SearchHistory(models.Model):
    ip_address = models.GenericIPAddressField(default='0.0.0.0')
    city = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.city} searched at {self.timestamp} from IP {self.ip_address}"


class CitySearchCount(models.Model):
    city = models.CharField(max_length=100, unique=True)
    count = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.city} - {self.count}"
