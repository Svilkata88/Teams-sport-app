from django.shortcuts import render
from teams.models import Team


def index(request):
    print(request.template)
    return render(request, 'common/index.html')
