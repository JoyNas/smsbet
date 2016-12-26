from django.shortcuts import render

from play.forms import WebPlayForm


def webplay(request):
    if request.method == 'POST':
        form = WebPlayForm(request.POST)
        if form.is_valid():
            pass
            # entry = form.cleaned_data['text']
            # return render(request, 'play/play.html', {'form': form})
    else:
        form = WebPlayForm()
    return render(request, 'play/play.html', {'form': form})
