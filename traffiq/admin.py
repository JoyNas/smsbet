from django.contrib import admin
from traffiq.models import TrafficReport


class TrafficAdmin(admin.ModelAdmin):
    list_display = (
        'latitude',
        'longitude',
        'last_latitude',
        'last_longitude',
        'response',
        'when')


admin.site.register(TrafficReport, TrafficAdmin)
