from django.db import models


class Game(models.Model):
    gameId = models.CharField(max_length=200)
    category = models.CharField(max_length=1)
    subCategory = models.IntegerField()
    price = models.FloatField()
