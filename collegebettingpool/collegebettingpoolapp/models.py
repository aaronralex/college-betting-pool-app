from django.db import models
from django.contrib.auth.models import User


class Game(models.Model):
    favorite = models.CharField(max_length=200)
    underdog = models.CharField(max_length=200)
    line = models.DecimalField(decimal_places=1, max_digits=3)
    tv = models.CharField(max_length=20)
    datetime = models.DateTimeField(default=0)
    week = models.IntegerField(default=0)

    def __str__(self):
        return self.favorite + ' vs ' + self.underdog


class Bet(models.Model):
    userID = models.IntegerField(default=0)
    gameID = models.IntegerField(default=0)
    week = models.IntegerField(default=0)
    winner = models.BooleanField()
    bet_selection = models.CharField(max_length=200)

    def __str__(self):
        return self.gameID + ', ' + self.userID
