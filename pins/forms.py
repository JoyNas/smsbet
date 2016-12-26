from django import forms
from pins.models import Batch


class BatchForm(forms.ModelForm):
    number_of_pins = forms.IntegerField()

    class Meta:
        model = Batch
