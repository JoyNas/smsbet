from django import forms
from emmob.models import Entry


class EntryForm(forms.ModelForm):

    class Meta:
        model = Entry
        exclude = ('curr_date',)
