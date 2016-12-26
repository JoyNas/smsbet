from random import choice

from django.contrib import admin

from pins.models import Batch, Pin
from pins.forms import BatchForm


def gen_randomdigits(size=10):
    return ''.join([choice('1234567890') for i in range(size)])


class BatchAdmin(admin.ModelAdmin):
    list_display = ('count', 'used', 'created_on', 'download_pins')
    form = BatchForm
    date_heirarchy = 'created_on'

    def save_model(self, request, obj, form, change):
        obj.save()
        num_pins = form.cleaned_data['number_of_pins']
        count = 0
        if change:
            return
        while count < num_pins:
            try:
                Pin.objects.create(pin=gen_randomdigits(), batch=obj)
            except:
                pass
            else:
                count += 1


class PinAdmin(admin.ModelAdmin):
    list_display = ('pin', 'batch', 'used')


admin.site.register(Batch, BatchAdmin)
admin.site.register(Pin, PinAdmin)
