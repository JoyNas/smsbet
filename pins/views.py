from django.http import HttpResponse

from pins.models import Pin


def download_pins(request):
    batch = request.GET.get('batch')
    _pins = '\n'.join([pin.pin for pin in Pin.objects.filter(batch=batch)])
    response = HttpResponse(mimetype='text/plain')
    response['Content-disposition'] = 'attachment;filename=pins_%s.txt' % batch
    response.write(_pins)
    return response
