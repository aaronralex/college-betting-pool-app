from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.template import loader

from .models import Game, Bet


def index(request):
    current_week_game_list = Game.objects.order_by('id')[:15]
    context = {'current_week_game_list': current_week_game_list}

<<<<<<< HEAD
	if request.method == "POST":
		userID = request.POST["username"]

		for game in current_week_game_list:
			bet_selection = request.POST["favorite"]
			bet = Bet(1, 2, 1, 0, bet_selection)
			bet.save()
=======
    if request.method == "POST":
        

        for game in current_week_game_list:
            bet_selection = request.POST[game.id]
            bet_selection.save()

    return render(request, 'collegebettingpoolapp/home.html', context)
>>>>>>> 736fe240627c2539a63759ecc8e57d082bba2f2c


def about(request):
    return render(request, 'collegebettingpoolapp/about.html')
