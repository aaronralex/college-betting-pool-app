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

    class Meta:
        unique_together = ("userID", "gameID")

    def __str__(self):
        return "Bet for User: " + str(self.userID) + "; Game: " + str(self.gameID)


class Setting(models.Model):
    setting = models.CharField(max_length=500, unique=True)
    value = models.CharField(max_length=500)

    def __str__(self):
        return self.setting + ": " + self.value
