from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.template import loader

from .models import Game, BettingSheet, Participant, Bet


def index(request):
    current_week_game_list = Game.objects.filter(week=1).order_by('id')[:15]
    context = {'current_week_game_list': current_week_game_list}

    if request.method == "POST":
        userID = request.POST["userID"]

        for game in current_week_game_list:
            selection = request.POST["g"+str(game.id)]
            if selection == game.favorite:
                winner = True
            else:
                winner = False

            bet = Bet.objects.update_or_create(userID=userID, gameID=game.id, week=1, winner=winner,
                                               bet_selection=selection)

    return render(request, 'collegebettingpoolapp/home.html', context)


def about(request):
    return render(request, 'collegebettingpoolapp/about.html')
