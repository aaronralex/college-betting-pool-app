from django.shortcuts import render
from django.template import loader


posts = [
	{
		'author': 'Garrett',
		'title': 'Gameweek',
		'team': 'randomteam1'
	},

	{
		'author': 'Admin',
		'title': 'Gameweeks',
		'team': 'randomteam2'
	}

]

def index(request):
	context = {
		'posts': posts
	}
	return render(request, 'collegebettingpoolapp/home.html', context)

def about(request):
	return render(request, 'collegebettingpoolapp/about.html')