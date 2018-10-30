from django.contrib import admin

# Register your models here.
from .models import Game
admin.site.register(Game)
from .models import Bet
admin.site.register(Bet)