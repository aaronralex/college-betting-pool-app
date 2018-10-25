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
    line = models.DecimalField(null=true)
    tv = models.CharField(max_length=20, null=true)
    datetime = models.DateTimeField(null=true)
    week = models.IntegerField(default=0)


