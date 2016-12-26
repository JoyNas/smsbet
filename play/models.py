from django.db import models
from datetime import datetime

from pins.models import Pin
from game.models import Game


class Message(models.Model):
    sender = models.CharField(max_length=20)
    sms = models.CharField(max_length=200, blank=True)
    when = models.DateTimeField(default=datetime.now)

    def __unicode__(self):
        return self.sender


class Entry(models.Model):
    message = models.ForeignKey(Message)
    pin = models.ForeignKey(Pin, null=True)
    game = models.ForeignKey(Game, null=True)
    amount = models.PositiveIntegerField()
    wins = models.DecimalField(max_digits=15, decimal_places=2, default=0)

    class Meta:
        verbose_name_plural = 'Entries'

    def __unicode__(self):
        return self.message

    @property
    def is_valid(self):
        if not self.game or not self.pin:
            return False
        if self.when < self.game.game_date:
            return True
        return False
