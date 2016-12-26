from emmob.forms import EntryForm

from django.http import HttpResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def report(request):
    if request.method == 'POST':
        form = EntryForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Ok')
        else:
            errors = '\n'.join(form.errors)
            return HttpResponseBadRequest(errors)
    else:
        return HttpResponseBadRequest('Only POST request allowed')
