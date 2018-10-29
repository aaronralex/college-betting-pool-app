from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)


class Game(models.Model):
    favorite = models.CharField(max_length=200)
    underdog = models.CharField(max_length=200)
    line = models.DecimalField(decimal_places=1, max_digits=3)
    tv = models.CharField(max_length=20)
    datetime = models.DateTimeField(default=0)
    week = models.IntegerField(default=0)

    def __str__(self):
        return self.favorite + ' vs ' + self.underdog


class BettingSheet(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    game_of_the_week = models.CharField(max_length=200)
    total_points_scored = models.IntegerField(default=0)
    high_risk_game = models.CharField(max_length=200)
    week = models.IntegerField(default=0)

    def __str__(self):
        return self.week


class Participant(models.Model):
    betting_sheet = models.ForeignKey(BettingSheet, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    total_points = models.IntegerField(default=0)

    def __str__(self):
        return self.name


