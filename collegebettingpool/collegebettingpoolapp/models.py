from django.db import models


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
    game_of_the_week = models.CharField(default=0, max_length=200) #yes or no

class Game_of_the_Week(models.Model):
    team_1 = models.CharField(max_length=200)
    team_2 = models.CharField(max_length=200)
    total_points_scored = models.IntegerField(default=0)

class BettingSheet(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    game_of_the_week = models.ForeignKey(Game_of_the_Week, on_delete=models.CASCADE)
    high_risk_game = models.CharField(max_length=200)
    participant_username = models.CharField(max_length=200)
    week = models.IntegerField(default=0)




