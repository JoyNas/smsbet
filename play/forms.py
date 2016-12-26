import decimal
from datetime import datetime

from django import forms

from pins.models import Pin
from game.models import Game
from play.models import Message, Entry


class WebPlayForm(forms.Form):
    text = forms.CharField(max_length=200)

    def clean_text(self):
        current_time = datetime.now()

        if 'text' in self.cleaned_data:
            parts = self.cleaned_data['text'][1:-1].split('*')
            if not len(parts) == 4:
                raise forms.ValidationError(
                    'The format for playing is *PIN*GAME*RESULT*AMOUNT#')
            _pin = parts[0].strip()
            _game = parts[1].strip()
            _result = parts[2].strip()
            _amount = parts[3].strip()

            msg = Message.objects.create(sender='TEST', sms=self.cleaned_data['text'])

            try:
                pin = Pin.objects.get(pin=_pin)
            except Pin.DoesNotExist:
                raise forms.ValidationError('The Pin you sent is invalid')

            try:
                game = Game.objects.get(code=_game)
            except Game.DoesNotExist:
                raise forms.ValidationError('The Game you sent is invalid')

            # Check for expiry
            if game.bet_expiry < current_time:
                raise forms.ValidationError('Too late to bet on this game')

            if _result not in ('HW', 'AW', 'D'):
                raise forms.ValidationError('The result you sent is invalid')

            try:
                amt = decimal.Decimal(_amount)
            except ValueError:
                raise forms.ValidationError('The amount you sent is invalid')

            entry = Entry.objects.create(
                message=msg, pin=pin, game=game, amount=amt)
            return entry
