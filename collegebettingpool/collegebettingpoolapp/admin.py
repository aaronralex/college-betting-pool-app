from django.contrib import admin
from .models import Game, Bet, Setting

# def close_out_week(modeladmin, request, queryset):
# 	for week in queryset:
# 		for game in week.games.all():
# 			bet_list = bet.objects.filter(game=game)
# 			for bet in bet_list:
# 				if bet.choice==bet.game.result:
# 					if bet.is_high_risk_game:
# 						bet.user.total_points+=5
# 					else if bet.is_game_of_the_week:
# 						bet.user.total_points+=2
# 					else:
# 						bet.user.total_points+=1
# 				else:
# 					if bet.is_high_risk_game:
# 						bet.user.total_points-=5
# 					else if bet.is_game_of_the_week:
# 						bet.user.total_points-=2
# 					else:
# 						bet.user.total_points-=1

# class GameAdmin(admin.ModelAdmin):
# 	list_display = ['favorite', 'week']
#     ordering = ['week']
#     actions = [close_out_week]


# Register your models here.
admin.site.register(Game)
admin.site.register(Bet)
admin.site.register(Setting)
# admin.site.register(game, GameAdmin)