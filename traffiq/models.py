from django.db import models
from datetime import datetime


class TrafficReport(models.Model):
    latitude = models.CharField(max_length=20)
    longitude = models.CharField(max_length=50)
    last_latitude = models.CharField(max_length=20, blank=True)
    last_longitude = models.CharField(max_length=50, blank=True)
    speed = models.CharField(max_length=50, blank=True)
    response = models.CharField(max_length=10)
    when = models.DateTimeField(default=datetime.now)

    def __unicode__(self):
        return self.response
