from django.db import models


class Purchase(models.Model):
    gameId = models.CharField(max_length=200)
    customerId = models.CharField(max_length=200)
    timestamp = models.DateTimeField()
    price = models.FloatField(blank=True)
