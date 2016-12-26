from django.db import models
from datetime import datetime


class Entry(models.Model):
    name = models.CharField(max_length=200, blank=True)
    phone1 = models.CharField(max_length=50, blank=True)
    phone2 = models.CharField(max_length=50, blank=True)
    email = models.CharField(max_length=100, blank=True)
    curr_date = models.DateTimeField(default=datetime.now)
    device_id = models.CharField(max_length=200, blank=True)

    class Meta:
        verbose_name_plural = 'Entries'

    def __unicode__(self):
        return self.name
