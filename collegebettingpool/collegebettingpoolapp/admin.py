from django.contrib import admin

# Register your models here.
from .models import Game
admin.site.register(Game)
from .models import Game_of_the_Week
admin.site.register(Game_of_the_Week)
from .models import BettingSheet
admin.site.register(BettingSheet)