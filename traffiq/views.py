from traffiq.forms import TrafficForm
from traffiq.models import TrafficReport

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from django.utils.timesince import timesince
from django.utils import timezone

import json
from math import atan2, degrees, pi


@csrf_exempt
def report(request):
    if request.method == 'POST':
        form = TrafficForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Ok')
        else:
            errors = '\n'.join(form.errors)
            return HttpResponseBadRequest(errors)
    else:
        return HttpResponseBadRequest("only POST requests")


def map(request):
    markers = [','.join(
        (rep.latitude, rep.longitude, rep.response)
        )for rep in TrafficReport.objects.all()]
    markers = [
        {
            'latitude': rep.latitude,
            'longitude': rep.longitude,
            'response': rep.response
        }
        for rep in TrafficReport.objects.all()
    ]
    markers = json.dumps(markers)
    #markers = TrafficReport.objects.all()
    return render(request, 'map.html', {'markers': markers})


def get_markers(request):
    #six_hrs_ago = timezone.now() - timezone.timedelta(hours=2)
    six_hrs_ago = timezone.now() - timezone.timedelta(hours=168)
    markers = []
    for rep in TrafficReport.objects.filter(when__gte=six_hrs_ago):
        try:
            angle = str(get_degrees(rep))
        except:
            continue
        else:
            # If in same spot, ignore
            if (rep.latitude == rep.last_latitude) and\
               (rep.longitude == rep.last_longitude):
                continue
            markers.append(
                {
                    'latitude': rep.latitude,
                    'longitude': rep.longitude,
                    'last_latitude': rep.last_latitude,
                    'last_longitude': rep.last_longitude,
                    'angle': angle,
                    'response': rep.response,
                    'since': timesince(rep.when)
                })

    return HttpResponse(json.dumps(markers), content_type="application/json")


def get_degrees(rep):
    dx = float(rep.latitude) - float(rep.last_latitude)
    dy = float(rep.longitude) - float(rep.last_longitude)
    rads = atan2(dy, dx)
    deg = degrees(rads)
    if dy >= 0 and dx >= 0:
        return deg
    elif dy >= 0 and dx < 0:
        return deg
    elif dy < 0 and dx < 0:
        return 360.0 + deg
    else:  # dy < 0 and dx >= 0
        return 360 + deg

    #rads %= 2*pi
