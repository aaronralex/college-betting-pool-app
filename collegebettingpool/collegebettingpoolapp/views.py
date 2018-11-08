from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.template import loader

from .models import Game, Bet, Setting


def index(request):
    current_week = Setting.objects.get(setting="CurrentWeek")
    current_week_game_list = Game.objects.filter(week=current_week.value).order_by('id')[:15]
    context = {'current_week_game_list': current_week_game_list}

    if request.method == "POST":
        user_id = request.POST["userID"]
        game_of_the_week_points = request.POST["game_of_the_week_points"]

        for game in current_week_game_list:
            selection = request.POST["g" + str(game.id)]
            if selection == game.favorite:
                winner = True
            else:
                winner = False
            try:
                select_object = Bet.objects.get(userID=user_id, gameID=game.id)
                b = Bet(id=select_object.id, userID=user_id, gameID=game.id, week=current_week.value,
                        winner=winner)
                b.save()
            except Bet.DoesNotExist:
                b = Bet(userID=user_id, gameID=game.id, week=current_week.value, winner=winner)
                b.save()

    return render(request, 'collegebettingpoolapp/home.html', context)


def scores(request):
    return render(request, 'collegebettingpoolapp/scores.html')


def about(request):
    return render(request, 'collegebettingpoolapp/about.html')
