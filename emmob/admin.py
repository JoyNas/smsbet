from django.contrib import admin
from emmob.models import Entry


class EntryAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone1', 'phone2', 'email', 'device_id', 'curr_date')
    date_heirarchy = 'curr_date'
    search_fields = ('name', 'device_id')


admin.site.register(Entry, EntryAdmin)
