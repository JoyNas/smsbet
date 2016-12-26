from django.contrib import admin
from play.models import Message, Entry


class MessageAdmin(admin.ModelAdmin):
    list_display = ('sender', 'sms', 'when')


class EntryAdmin(admin.ModelAdmin):
    list_display = ('message', 'pin', 'game', 'amount', 'wins')


admin.site.register(Message, MessageAdmin)
admin.site.register(Entry, EntryAdmin)
