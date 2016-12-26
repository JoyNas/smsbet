from django.db import models


class League(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)

    def __unicode__(self):
        return self.name


class Club(models.Model):
    name = models.CharField(max_length=200)
    league = models.ForeignKey(League)

    def __unicode__(self):
        return self.name


class Game(models.Model):
    HW = 'HW'
    AW = 'AW'
    DR = 'D'
    RESULT = (('HW', 'Home Win'), ('AW', 'Away Win'), ('D', 'Draw'))

    home_side = models.ForeignKey(Club, related_name='home_game')
    away_side = models.ForeignKey(Club, related_name='away_game')
    code = models.CharField(max_length=10)
    game_date = models.DateTimeField()
    odds = models.DecimalField(max_digits=10, decimal_places=2)
    bet_expiry = models.DateTimeField()
    result = models.CharField(max_length=4, choices=RESULT, blank=True)

    def __unicode__(self):
        return self.code
