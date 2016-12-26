from django.contrib import admin
from game.models import League, Club, Game


class LeagueAdmin(admin.ModelAdmin):
    list_detail = ('name', 'description')


class ClubAdmin(admin.ModelAdmin):
    list_detail = ('name', 'league')


class GameAdmin(admin.ModelAdmin):
    list_detail = ('home_side', 'away_side', 'code', 'game_date',
                   'odds', 'bet_expiry', 'result')

admin.site.register(League, LeagueAdmin)
admin.site.register(Club, ClubAdmin)
admin.site.register(Game, GameAdmin)
