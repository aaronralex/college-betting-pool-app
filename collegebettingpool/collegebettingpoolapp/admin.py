from django.contrib import admin

# Register your models here.
from .models import Game, Bet
admin.site.register(Game)
<<<<<<< HEAD
from .models import BettingSheet
admin.site.register(BettingSheet)
from .models import Bet
admin.site.register(Bet)
=======
admin.site.register(Bet)
>>>>>>> 736fe240627c2539a63759ecc8e57d082bba2f2c
