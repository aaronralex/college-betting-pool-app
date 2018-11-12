from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.template import loader
from django.db import connection

from .models import Game, Bet, Setting, Participant


def index(request):
    current_week = Setting.objects.get(setting="CurrentWeek")
    user_id = request.user.id
    current_week_game_list = Game.objects.filter(week=current_week.value).order_by('id')[:15]
    current_user_bets = Bet.objects.filter(userID=user_id, week=current_week.value)

    if request.method == "POST":
        user_id = request.POST["userID"]
        game_of_the_week_points = request.POST["game_of_the_week_points"]

        for game in current_week_game_list:
            if "g" + str(game.id) in request.POST:
                selection = request.POST["g" + str(game.id)]
                if selection == game.favorite:
                    winner = True
                else:
                    winner = False
                try:
                    select_object = Bet.objects.get(userID=user_id, gameID=game.id)
                    b = Bet(id=select_object.id, userID=user_id, gameID=game.id, week=current_week.value,
                            winner=winner, game=game)
                    b.save()
                except Bet.DoesNotExist:
                    b = Bet(userID=user_id, gameID=game.id, week=current_week.value, winner=winner, game=game)
                    b.save()

    cursor = connection.cursor()
    cursor.execute("""
                    SELECT g.*, b.winner
                    FROM collegebettingpoolapp_game g 
                    LEFT JOIN collegebettingpoolapp_bet b
                        ON b.gameID = g.id
                    WHERE g.week = %s
                        AND (b.userID = %s
                                OR b.userID IS NULL)""", [current_week.value, user_id])

    query = cursor.fetchall()

    context = {'current_week_game_list': current_week_game_list,
               'current_user_bets': current_user_bets,
               'query': query}

    return render(request, 'collegebettingpoolapp/home.html', context)


def scores(request):
    try:
        participants = Participant.objects.all().order_by('total_points')
    except (KeyError, Participant.DoesNotExist):
        participants = ['null msg', 'null msg']

    context = {'participants': participants}

    return render(request, 'collegebettingpoolapp/scores.html', context)


def history(request):
    current_week = Setting.objects.get(setting="CurrentWeek")
    user_id = request.user.id

    current_week_game_list = Game.objects.all().filter(week=current_week.value).order_by('id')[:15]

    current_user_bets = Bet.objects.all().filter(week=current_week.value, userID=user_id)

    context = {'current_week_game_list': current_week_game_list,
               'current_user_bets': current_user_bets}

    return render(request, 'collegebettingpoolapp/history.html', context)


def about(request):
    return render(request, 'collegebettingpoolapp/about.html')


def elements(request):
    return render(request, 'collegebettingpoolapp/generics/elements.html')


def generic(request):
    return render(request, 'collegebettingpoolapp/generics/generic.html')
