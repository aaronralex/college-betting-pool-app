from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.template import loader

from .models import Game, Bet


def index(request):
    current_week_game_list = Game.objects.order_by('id')[:15]
    context = {'current_week_game_list': current_week_game_list}

    if request.method == "POST":
        

        for game in current_week_game_list:
            bet_selection = request.POST[game.id]
            bet_selection.save()

    return render(request, 'collegebettingpoolapp/home.html', context)


def about(request):
    return render(request, 'collegebettingpoolapp/about.html')
