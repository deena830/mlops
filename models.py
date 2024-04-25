from django.db import models

class Country(models.Model):
    country = models.CharField(max_length=255)
    confirmed = models.IntegerField()
    deaths = models.IntegerField()
    recovered = models.IntegerField()

    def __str__(self):
        return self.country
