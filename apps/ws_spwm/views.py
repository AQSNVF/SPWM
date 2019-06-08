from django.shortcuts import render


def home(request):
    return render(request, 'ws_spwm/index.html')
