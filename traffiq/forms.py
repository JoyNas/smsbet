from django import forms
from traffiq.models import TrafficReport


class TrafficForm(forms.ModelForm):

    class Meta:
        model = TrafficReport
        exclude = ('when',)
